import gradio as gr
from rag.core import answer_query


def chat_fn(user_message, chat_history):
    result = answer_query(user_message)

    bot_reply = f"{result['answer']}\n\n**Source:** {result['source'].upper()}"
    chat_history.append({"role": "user", "content": user_message})
    chat_history.append({"role": "assistant", "content": bot_reply})

    return chat_history


with gr.Blocks(title="Pakistan History QA Bot") as demo:
    gr.Markdown("<h1>Pakistan History Question-Answering Bot</h1>")
    gr.Markdown("Ask anything about Pakistan's history. The bot uses RAG + Web Search + LLaMA.")

    chatbot = gr.Chatbot(height=450)

    msg = gr.Textbox(
        placeholder="Ask a question about Pakistan history...",
        label="Your Question"
    )

    clear = gr.Button("Clear Chat")

    msg.submit(chat_fn, [msg, chatbot], [chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
