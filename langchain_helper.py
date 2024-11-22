from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from secret_key import openapi_key
from langchain.chains import SequentialChain

import os

os.environ['OPENAI_API_KEY']=openapi_key

llm=OpenAI(temperature=0.6)

def cuisine_function(cuisine):

    prompt_template_name=PromptTemplate(
    input_variables = ['cuisine'],
    template="I want to open a resturent for {cuisine} food.suggest some fancy name for this."
    )
    name_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key="reasturent_name")
    prompt_template_name=PromptTemplate(
        input_variables = ['reasturent_name'],
        template="""Suggest some menu items for {reasturent_name} food.return it as a comma separated list."""
    )
    food_item_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key="menu_items")
    chain = SequentialChain(
    chains=[name_chain, food_item_chain],
    input_variables=["cuisine"],
    output_variables=["reasturent_name", "menu_items"],
    )   
    response=chain({'cuisine':cuisine})
    return response

if __name__=="__main__":
    print(cuisine_function("Italian"))