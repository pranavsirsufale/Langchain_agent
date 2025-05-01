from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
# from langchain_community.chat_model import ChatTogether
from langchain_groq import ChatGroq

load_dotenv()

# print(load_dotenv())
# llm = ChatOpenAI(model = 'gpt-3.5-turbo')
llm = ChatGroq(model = 'llama-3.1-8b-instant')

result = llm.invoke('what is the square toot of 49')

print(result.content)