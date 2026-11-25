import cdsapi
from pathlib import Path
import time

REPO_ROOT = Path(__file__).resolve().parent.parent if "__file__" in globals() else Path.cwd().parent
DOWNLOAD_DIR = REPO_ROOT / "data"
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

DATASET = "reanalysis-era5-single-levels"

base_request = {
    "product_type": ["reanalysis"],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [13, -79, -4, -66]
}

def safe_retrieve(
    client: cdsapi.Client,
    dataset: str,
    request: dict,
    target_path: Path,
    max_retries: int = 3,
    base_delay: int = 15,
) -> bool:
    """Download from CDS to a temporary .part file with retries before renaming."""
    if target_path.is_file():
        print(f"[SKIP] {target_path.name} already exists.")
        return True

    temp_path = target_path.with_suffix(target_path.suffix + ".part")

    for attempt in range(1, max_retries + 1):
        try:
            print(f"[FETCH] Downloading {target_path.name} (Attempt {attempt}/{max_retries})...")
            client.retrieve(dataset, request, str(temp_path))
            temp_path.rename(target_path)
            print(f"[OK] Saved {target_path.name}")
            return True

        except Exception as err:
            # Remove incomplete .part file before retrying or moving on
            if temp_path.exists():
                temp_path.unlink()

            print(f"[WARN] Attempt {attempt} failed for {target_path.name}: {err}")

            if attempt < max_retries:
                wait_time = base_delay * attempt
                print(f"[WAIT] Retrying in {wait_time}s...")
                time.sleep(wait_time)

    print(f"[ERROR] Giving up on {target_path.name} after {max_retries} attempts.")
    return False

def main():
    client = cdsapi.Client()

    # Clean up any leftover partial downloads from interrupted runs
    for part_file in DOWNLOAD_DIR.glob("*.part"):
        print(f"[CLEANUP] Removing incomplete file: {part_file.name}")
        part_file.unlink()

    # --- Step 1: Time-invariant Surface Geopotential ---
    geopotential_path = DOWNLOAD_DIR / "era5_colombia_geopotential.nc"
    geopotential_request = base_request | {
        "variable": ["geopotential"],
        "year": ["2025"],
        "month": ["01"],
        "day": ["01"],
        "time": ["00:00"],
    }
    result = safe_retrieve(client, DATASET, geopotential_request, geopotential_path)
    print(f"File downloading succeessful?: {result}")


    # --- Step 2: Hourly 2m Temperature & Dewpoint (2012–2025) ---
    monthly_base_request = base_request | {
        "variable": [
            "2m_dewpoint_temperature",
            "2m_temperature",
        ],
        "day": [f"{d:02d}" for d in range(1, 32)],
        "time": [f"{h:02d}:00" for h in range(24)],
    }

    for year in range(2012, 2026):
        for month in range(1, 13):
            filename = f"era5_colombia_2m-temp_2m-dew_{year}-{month:02d}.nc"
            file_path = DOWNLOAD_DIR / filename

            request = monthly_base_request | {
                "year": [f"{year}"],
                "month": [f"{month:02d}"],
            }
            result = safe_retrieve(client, DATASET, request, file_path)
            print(f"File downloading succeessful? {result}")


if __name__ == "__main__":
    main()
