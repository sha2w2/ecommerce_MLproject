import os
import urllib.request
import zipfile
import logging

from config import RAW_DATA_DIR

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def download_data(url: str, filename: str):
    """
    Drives to the URL, picks up the ZIP file, 
    and drops it in the raw data folder.
    """
    file_path = RAW_DATA_DIR / filename

    if file_path.exists():
        logging.info(
            f"The file {filename} is already in the loading dock. Skipping download.")
        return file_path

    logging.info(f"Downloading data from {url}...")
    try:
        urllib.request.urlretrieve(url, file_path)
        logging.info("Download complete!")
        return file_path
    except Exception as e:
        logging.error(f"The delivery truck crashed: {e}")
        return None


def extract_data(zip_path):
    """
   Opens the ZIP box and unpacks the CSV files.
    """
    if not zip_path or not zip_path.exists():
        logging.error("No ZIP file found to extract.")
        return

    logging.info(f"Unpacking {zip_path.name}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(RAW_DATA_DIR)

    logging.info("Unpacking complete. Raw data is ready for cleaning.")


if __name__ == "__main__":
    # Placeholder URL for the Bugzilla dataset.
    DATA_URL = "https://example-data-lake.com/mozilla_bugzilla_dataset.zip"
    ZIP_FILENAME = "bugzilla_data.zip"

    logging.info("--- Starting Data Acquisition Pipeline ---")

    # Step 1: Download
    downloaded_file = download_data(DATA_URL, ZIP_FILENAME)

    # Step 2: Extract
    extract_data(downloaded_file)

    logging.info("Pipeline Finished")
