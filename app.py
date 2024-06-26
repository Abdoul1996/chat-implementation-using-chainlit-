import chainlit as cl 
from src.llm import ask_order,  messages

@cl.on_message
async def main(message: cl.Message):
    
    # user role 
    messages.append(
    {
        "role": "user",
        "content": message.content
    }
    )
    
    response = ask_order(messages)
    
    # Assistant role 
    messages.append(
    {
        "role": "assistant",
        "content": response
    }
    )
    
    # sent a response back to the user  
    await cl.Message(
        content= response,
    ).send()
