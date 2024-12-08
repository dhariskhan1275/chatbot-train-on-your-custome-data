import gradio as gr
from example import chain

def chat(question,history):
    if question=="":
        return"please ask a quesion"
    
    else:
        return chain.invoke(question)
    
gr.ChatInterface(
    fn=chat,
    type="messages"
).launch()
