"""Download optional Ghanaian-language QA datasets.

The full Ghana-QA files are large. This script downloads the Twi CSV from the
GhanaNLP Ghana-QA project when internet access is available. The project uses
these files as optional retrieval data rather than requiring them at import.
"""

import os
import sys
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, "data", "datasets")
TWI_URL = "https://huggingface.co/datasets/ghananlpcommunity/ghana-qa/resolve/main/twi.csv?download=true"
OUT = os.path.join(DATA_DIR, "ghana_qa.csv")


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Ghana-QA source:", TWI_URL)
    print("Destination:", OUT)
    print("This is a large download and requires internet access.")
    try:
        urllib.request.urlretrieve(TWI_URL, OUT)
    except Exception as exc:
        print("Download failed:", exc)
        print("Download the Twi CSV manually and save it as:", OUT)
        return 1
    print("Ghana-QA Twi dataset downloaded successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
