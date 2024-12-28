from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain


def get_chat_response(prompt,memory,api_key):
    model = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key, openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm = model,memory = memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

#memory = ConversationBufferMemory(return_messages=True)
#print(get_chat_response("牛顿提出过哪些知名定律",memory,"sk-pLkOYU89UNvEOs2oLmkqwulkweRE4TC3jCAfxLB6ER1JFo5u"))
#print(get_chat_response("我上一个问题问的是什么?",memory,"sk-pLkOYU89UNvEOs2oLmkqwulkweRE4TC3jCAfxLB6ER1JFo5u"))