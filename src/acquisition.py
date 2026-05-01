import os
import shutil
import logging
import kagglehub
from config import RAW_DATA_DIR

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def fetch_kaggle_data(dataset_slug: str):
    """
    Connects to Kaggle, downloads/unzips the dataset into a cache, 
    and copies the files into our project's raw data directory.
    """
    logging.info(f"Connecting to Kaggle to fetch '{dataset_slug}'...")

    try:
        cache_path = kagglehub.dataset_download(dataset_slug)
        logging.info(f"Dataset cached successfully at: {cache_path}")

        logging.info("Moving files to project loading dock (data/raw/)...")
        # Loop through the unzipped files in the cache and copy them to our RAW_DATA_DIR
        for item in os.listdir(cache_path):
            source_item = os.path.join(cache_path, item)
            destination_item = RAW_DATA_DIR / item

            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item,
                                dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, destination_item)

        logging.info("All files successfully moved to the raw data folder!")

    except Exception as e:
        logging.error(f"The automated pipeline failed: {e}")


if __name__ == "__main__":
    # Thank u monika11
    DATASET_SLUG = "monika11/bug-triagingbug-assignment"

    logging.info("Starting Automated Data Acquisition Pipeline")
    fetch_kaggle_data(DATASET_SLUG)
    logging.info("Pipeline Finished")
