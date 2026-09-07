import importlib
import unittest


class LazyLoadingRegressionTest(unittest.TestCase):
    def test_large_datasets_are_lazy_loaded(self):
        knowledge_engine = importlib.import_module("model.knowledge_engine")
        akan_engine = importlib.import_module("model.akan_engine")

        self.assertTrue(hasattr(knowledge_engine.knowledge_base, "_cache"))
        self.assertTrue(hasattr(akan_engine.dictionary, "_cache"))
        self.assertIsNone(knowledge_engine.knowledge_base._cache)
        self.assertIsNone(akan_engine.dictionary._cache)


if __name__ == "__main__":
    unittest.main()
