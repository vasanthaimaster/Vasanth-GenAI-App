from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain

def titan_llm():
    llm = BedrockChat(
        model_id="amazon.titan-text-express-v1",
        region_name="us-east-1",  # Replace with your AWS region
        model_kwargs={
            "temperature": 0.5,
            "topP": 1,
            "maxTokenCount": 100
        }
    )
    return llm

def create_memory():
    llm = titan_llm()
    memory = ConversationSummaryBufferMemory(
        llm=llm,
        max_token_limit=256,
    )
    return memory

def get_chat_response(input_text, memory):
    llm = titan_llm()
    conversation = ConversationChain(
        llm=llm,
        verbose=True,
        memory=memory,
    )
    chat_response = conversation.invoke(input=input_text)
    return chat_response['response']
