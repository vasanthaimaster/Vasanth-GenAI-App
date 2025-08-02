# 1. Import langchain functions
from langchain_community.chat_models import BedrockChat
# from langchain.memory import ConversationSummaryBufferMemory
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import transformers
# 2. Create function to invoke model 
def titan_llm():
    llm = ChatBedrock(
        model_id="amazon.titan-text-express-v1",
        model_kwargs={
            "temperature": 0.5,
            "topP": 1, 
            "maxTokenCount": 100  
        },
    )
    return llm  

# create a memory function for the chatbot
def create_memory():
    llm = titan_llm()  
    memory = ConversationBufferMemory(
        llm=llm,
        max_token_limit=256,
    )
    return memory

# create a chat client function to run the chatbot
def get_chat_response(input_text, memory):
    llm = titan_llm() 
    conversation = ConversationChain(
        llm=llm,       
        verbose=True,
        memory=memory,
    )
    chat_response = conversation.invoke(input=input_text)

    return chat_response['response'] 
