import os
import logging
from ollama import query_ollama

def load_documents_from_folder(folder_path):
    docs = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".txt", ".md")):
                try:
                    with open(os.path.join(root, file), encoding="utf-8") as f:
                        docs.append(f.read())
                except Exception as e:
                    logging.warning(f"Failed to read {file}: {e}")
    return docs

class SimpleFileRetriever:
    def __init__(self, folder_path):
        self.documents = load_documents_from_folder(folder_path)
        self.doc_chunks = [p.strip() for doc in self.documents for p in doc.split("\n\n") if p.strip()]

    def get_relevant_documents(self, query, max_chunks=15, max_chars=3000):
        query_lower = query.lower()
        matched = [c for c in self.doc_chunks if query_lower in c.lower()]
        matched = matched or self.doc_chunks[:max_chunks]

        selected, total_len = [], 0
        for chunk in matched:
            if total_len + len(chunk) > max_chars: break
            selected.append(chunk)
            total_len += len(chunk)
            if len(selected) >= max_chunks: break
        return selected

def generate_answer(user_question: str, answer_mode: str) -> str:
    retriever = SimpleFileRetriever("./my_docs")
    relevant_docs = retriever.get_relevant_documents(user_question)
    total_length = sum(len(doc) for doc in relevant_docs)
    context = "\n\n".join(relevant_docs)

    if answer_mode == 'model':
        logging.info("Mode: model-only. Calling large model without context.")
        prompt = f"You are an AI assistant. Answer the question directly:\nQuestion: {user_question}\nAnswer:"
        return query_ollama(prompt)

    elif answer_mode == 'local':
        logging.info("Mode: local-only.")
        if not relevant_docs or total_length < 10:
            return "I don't know. (No sufficient information in local knowledge base)"
        prompt = (
            "You are an AI assistant. Only answer based on the background information below.\n"
            "If the answer is not in the background, reply with 'I don't know.'\n\n"
            f"Background:\n{context}\n\n"
            f"Question: {user_question}\nAnswer:"
        )
        return query_ollama(prompt)