# Optional Ghanaian QA Data

`ghana_qa_sample.csv` is a small curated offline demonstration set used so the application has Ghanaian-language QA coverage even when the full external dataset is not present.

For the full Ghana-QA resource, place the downloaded CSV at:

`data/datasets/ghana_qa.csv`

The dataset manager automatically prefers `ghana_qa.csv` and falls back to `ghana_qa_sample.csv` when the full file is unavailable.

The Ghana-QA dataset is maintained by the Ghana NLP Community and contains Twi, Ewe and Ga question-answer pairs. The public dataset is described as containing 3,547,660 QA pairs and is licensed CC BY-NC 4.0. Cite the dataset in the project report when the full dataset is used.
