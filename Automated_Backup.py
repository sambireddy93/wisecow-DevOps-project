import shutil
import os
import logging
from datetime import datetime

# Source directory to backup
SOURCE_DIR = "my_data"

# Backup location (can be a mounted remote path or another folder)
BACKUP_DIR = "backup_folder"

# Configure logging
logging.basicConfig(
    filename="backup_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

try:
    # Create backup folder if it doesn't exist
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # Create timestamp for backup folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_path = os.path.join(BACKUP_DIR, "backup_" + timestamp)

    # Copy files
    shutil.copytree(SOURCE_DIR, backup_path)

    message = "Backup completed successfully"
    print(message)
    logging.info(message)

except Exception as e:
    message = f"Backup failed: {e}"
    print(message)
    logging.error(message)
