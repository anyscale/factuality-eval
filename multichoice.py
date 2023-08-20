import openai
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatAnyscale
from prompt_mgr import PromptMgr
import os

MODEL = 'meta-llama/Llama-2-70b-chat-hf'

class Multichoice:
    """
    Multichoice is an agent that returns a simple A, B or 
    other given a long textual description. 
    """

    def __init__(self, pm, key):
        self.pm = pm
        self.model = ChatAnyscale(model="meta-llama/Llama-2-70b-chat-hf", 
            anyscale_api_key=key, temperature=0)
       
          
    def extract_choice(self, inp): 
        sys_msg = self.pm.bind('multichoice_system').render()
        multichoice = self.pm.bind('multichoice_query').render(query=inp)  
        messages = [SystemMessage(content=sys_msg),
                HumanMessage(content=multichoice)]
        output = self.model(messages)
        return output.content    

        