# System Test Plan

## Functional categories

1. Definition and meaning questions
2. Advantages, disadvantages, applications and examples
3. Lists, causes, effects and processes
4. Comparisons and summaries
5. Examination/revision questions
6. Calculations and formula-related queries
7. English/Twi translation and Akan lexical questions
8. Follow-up questions using previous context
9. Unknown-topic fallback behaviour
10. Flask `/ask` and `/health` API contracts

## Quality measurements for the final report

- Retrieval hit rate / top-k recall
- Answer accuracy on a labelled test set
- Intent classification accuracy
- Akan translation accuracy on a manually verified sample
- Confidence calibration (high-confidence answers should have higher measured correctness)
- Response latency
- API success rate
- Failure/fallback rate

## Reproducible commands

```powershell
python scripts/runtime_validation.py
python -m unittest discover -s tests -p "test*.py" -v
```
