"""Canonical date-partitioned NSE archive placement.

Deployment-specific archive locations are supplied through environment configuration. Optional
mount/share attestation remains fail-closed when configured so a missing network archive cannot
silently turn into an unintended local capture directory.
"""

from __future__ import annotations

import os
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Self

from shaurya.contracts.timing import IST

NSE_ARCHIVE_ROOT_ENV = "SHAURYA_NSE_ARCHIVE_ROOT"
NSE_ARCHIVE_MOUNT_ENV = "SHAURYA_NSE_ARCHIVE_MOUNT"
NSE_ARCHIVE_EXPECTED_SHARE_ENV = "SHAURYA_NSE_ARCHIVE_EXPECTED_SHARE"

# Portable, non-operational defaults. Production deployments should set
# SHAURYA_NSE_ARCHIVE_ROOT explicitly. The default path still requires archive validation
# before use and therefore cannot be created silently by capture code.
DEFAULT_NSE_ARCHIVE_ROOT = Path.home() / ".local" / "share" / "shaurya" / "nse"
DEFAULT_NSE_ARCHIVE_MOUNT = DEFAULT_NSE_ARCHIVE_ROOT.parent
EXPECTED_NSE_ARCHIVE_SHARE = ""


class NSEArchiveUnavailableError(RuntimeError):
    """The configured production archive is not the expected writable SMB target."""


def _configured_root() -> Path:
    value = os.environ.get(NSE_ARCHIVE_ROOT_ENV)
    root = Path(value).expanduser() if value else DEFAULT_NSE_ARCHIVE_ROOT
    if not root.is_absolute():
        raise NSEArchiveUnavailableError(
            f"{NSE_ARCHIVE_ROOT_ENV} must be an absolute path, got {root}"
        )
    return root.resolve()


def _verify_default_smb_mount() -> None:
    mount_value = os.environ.get(NSE_ARCHIVE_MOUNT_ENV)
    share_value = os.environ.get(NSE_ARCHIVE_EXPECTED_SHARE_ENV, "").strip()
    mount = (
        Path(mount_value).expanduser().resolve()
        if mount_value
        else DEFAULT_NSE_ARCHIVE_MOUNT
    )
    if not mount.is_mount():
        raise NSEArchiveUnavailableError(f"{mount} is not mounted; refusing local fallback")
    if not share_value or sys.platform != "darwin":
        return
    observed = subprocess.run(
        ["/sbin/mount"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    expected = f"{share_value} on {mount} (smbfs,"
    if expected not in observed:
        raise NSEArchiveUnavailableError(
            f"{mount} is mounted, but not from the configured archive share"
        )


@dataclass(frozen=True, slots=True)
class NSEArchiveLayout:
    """One NSE trading-date partition and its four stable storage lanes."""

    root: Path
    trading_date: date

    @classmethod
    def configured(cls, trading_date: date | None = None) -> Self:
        return cls(
            root=_configured_root(),
            trading_date=trading_date or datetime.now(IST).date(),
        )

    @property
    def day_root(self) -> Path:
        return self.root / self.trading_date.isoformat()

    @property
    def raw(self) -> Path:
        return self.day_root / "raw"

    @property
    def metadata(self) -> Path:
        return self.day_root / "metadata"

    @property
    def indexes(self) -> Path:
        return self.day_root / "indexes"

    @property
    def derived(self) -> Path:
        return self.day_root / "derived"

    def prepare(self) -> Self:
        if self.root == DEFAULT_NSE_ARCHIVE_ROOT or os.environ.get(NSE_ARCHIVE_MOUNT_ENV):
            _verify_default_smb_mount()
        if not self.root.is_dir():
            raise NSEArchiveUnavailableError(
                f"configured NSE archive root does not exist: {self.root}"
            )
        if self.root == DEFAULT_NSE_ARCHIVE_ROOT and not (self.root / "README.md").is_file():
            raise NSEArchiveUnavailableError(
                f"configured NSE archive sentinel is missing: {self.root / 'README.md'}"
            )
        for lane in (self.raw, self.metadata, self.indexes, self.derived):
            lane.mkdir(mode=0o700, parents=True, exist_ok=True)
        return self


def resolve_raw_capture_root(
    explicit: Path | None,
    *,
    trading_date: date | None = None,
    allow_nonarchive: bool = False,
) -> Path:
    """Resolve a capture root, defaulting normal DAT calls to the NSE daily raw lane.

    An explicit path inside the configured archive remains fail-closed and verified. A path
    outside it is rejected unless the caller separately opts into a controlled non-archive run.
    Normal live calls omit both and therefore receive the server default.
    """

    layout = NSEArchiveLayout.configured(trading_date)
    if explicit is None:
        return layout.prepare().raw
    resolved_explicit = explicit.expanduser().resolve() if explicit.is_absolute() else explicit
    if resolved_explicit.is_absolute() and resolved_explicit.is_relative_to(layout.root):
        layout.prepare()
        return resolved_explicit
    if not allow_nonarchive:
        raise NSEArchiveUnavailableError(
            f"non-archive capture root rejected: {explicit}; normal DAT storage is under "
            f"{layout.root}. Use the controlled-test override only for an intentional "
            "isolated run."
        )
    return explicit


def resolve_data_catalog(
    explicit: Path | None,
    *,
    trading_date: date | None = None,
    allow_nonarchive: bool = False,
    nonarchive_capture_root: Path | None = None,
) -> Path:
    """Resolve the shared lifecycle catalogue into the daily metadata lane.

    Controlled isolated captures keep their catalogue beside, but outside, the raw run root so
    repeated test captures still share one claim. Production never falls back off the verified
    archive merely because the metadata file does not exist yet.
    """

    layout = NSEArchiveLayout.configured(trading_date)
    if explicit is None:
        if allow_nonarchive and nonarchive_capture_root is not None:
            return nonarchive_capture_root.resolve().parent / "datasets"
        return layout.prepare().metadata / "datasets"
    resolved_explicit = explicit.expanduser().resolve() if explicit.is_absolute() else explicit
    if resolved_explicit.is_absolute() and resolved_explicit.is_relative_to(layout.root):
        layout.prepare()
        return resolved_explicit
    if not allow_nonarchive:
        raise NSEArchiveUnavailableError(
            f"non-archive data catalogue rejected: {explicit}; production metadata is under "
            f"{layout.root}. Use the controlled-test override only for an intentional "
            "isolated run."
        )
    return explicit
