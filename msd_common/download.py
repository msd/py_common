from enum import Enum, auto
from pathlib import Path

from requests import Session
import requests

from .url import name_from_url


def _write_response_to_file(response: requests.Response, out_path: Path):
    with out_path.open("wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            # If you have chunk encoded response uncomment if
            # and set chunk_size parameter to None.
            # if chunk:
            f.write(chunk)


class downloading_mode(Enum):
    overwrite_existing = auto()
    skip_existing = auto()
    error_if_exist = auto()


def download_file(
    url: str,
    path: Path,
    session: Session | None = None,
    mode: downloading_mode | None = downloading_mode.error_if_exist,
):
    # global-state session is used if not one is specified
    _session = session or requests

    r = _session.get(url, stream=True)

    r.raise_for_status()

    def get_out_path():
        if not path.exists():
            return path

        if path.is_dir():
            return path / name_from_url(url)

        # not a dir and exists => is a file
        if mode == downloading_mode.overwrite_existing:
            return path
        elif mode == downloading_mode.error_if_exist:
            raise RuntimeError(
                f"Given path is a file and would be overwritten (path={path})"
            )
        return None

    out_path = get_out_path()

    if out_path is not None:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        _write_response_to_file(r, out_path)
    return out_path
