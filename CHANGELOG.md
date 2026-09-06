# Intelligent QA Chatbot — Integration Update

## Completed in this package

- Integrated optional Ghana-QA retrieval into the Router Engine.
- Added Ghana-QA candidates to the Ranking Engine without replacing the existing TF-IDF/cosine ranking design.
- Added Ghana-QA source priority and transparent dataset-score contribution.
- Made Ghana-QA retrieval optional so the chatbot still runs when the large CSV is absent.
- Improved dataset loading and validation.
- Added an official Ghana-QA download helper and dataset documentation.
- Prevented common greetings from triggering unnecessary retrieval/web searches.
- Preserved the existing Intent, Conversation, Query, Akan, Knowledge, Web, Ranking and Answer Synthesis architecture.
- Kept the existing public QA APIs (`process_question()` and `get_answer()`).

## Dataset note

The full Ghana-QA Twi dataset is intentionally not bundled because it is very large. Download it separately and place it at:

`data/datasets/ghana_qa.csv`

The application expects `question` and `answer` columns and optionally `lang`.
