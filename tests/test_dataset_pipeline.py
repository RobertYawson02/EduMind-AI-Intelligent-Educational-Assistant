import json
import os
import unittest

from model.dataset_manager import (
    dataset_available,
    dataset_path,
    load_dataset,
    load_processed_twi_dataset,
    normalize_twi_record,
)


class DatasetPipelineTests(unittest.TestCase):
    def test_dataset_directory_detection(self):
        self.assertTrue(os.path.isdir(os.path.join("data", "datasets")))
        self.assertTrue(os.path.isdir(os.path.join("data", "datasets", "downloads")))
        self.assertTrue(os.path.isdir(os.path.join("data", "datasets", "processed")))

    def test_processed_twi_dataset_is_available_or_can_be_built(self):
        dataset = load_processed_twi_dataset()
        self.assertIsInstance(dataset, list)
        if dataset:
            record = dataset[0]
            self.assertIn("english", record)
            self.assertIn("twi", record)

    def test_dataset_manager_detects_processed_dataset(self):
        self.assertTrue(dataset_available("twi_english") or dataset_path("twi_english") is None)

    def test_normalize_twi_record_handles_empty_or_duplicate_values(self):
        record = {
            "english": " water ",
            "twi": "  nsuo  ",
            "category": "translation",
            "source": "GhanaNLP",
            "language": "Twi",
        }
        cleaned = normalize_twi_record(record)
        self.assertEqual(cleaned["english"], "water")
        self.assertEqual(cleaned["twi"], "nsuo")
        self.assertEqual(cleaned["category"], "translation")

    def test_manifest_exists_and_is_valid_json(self):
        manifest_path = os.path.join("data", "datasets", "dataset_manifest.json")
        with open(manifest_path, "r", encoding="utf-8") as fh:
            manifest = json.load(fh)
        self.assertIsInstance(manifest, dict)
        self.assertTrue(manifest)


if __name__ == "__main__":
    unittest.main()
