This project demonstrates how to build a RAG Q&A system, which can answer questions based on [the data folder](./data/) containing stock information. Please refer to [this document]([https://github.com/turingplanet/python-mongo-demo/tree/main?tab=readme-ov-file#poetry-setup](https://github.com/turingplanet/python-project-setup-tutorial/blob/main/comprehensive_set_up.md#poetry-project-setup) for poetry setup instructions.

## How to run this project
1. Modify `secret.yml` and paste the OpenAI key.
2. Run `poetry run python3 rag_demo/api_server.py`.
3. Open `index.html`.

## How to test this project
- Run `poetry run pytest tests`.
