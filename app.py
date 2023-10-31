from queue import Queue
import threading
import streamlit as st
import time
import autogen
from typing import Any, Dict, List, Optional, Union

import random

def ai():
    return "🤖"
def user():
    return "😊"

st.sidebar.write("# Streamlit Autogen")
st.sidebar.write("# "+ai()+"   : Assistant")
st.sidebar.write("# "+user()+" : UserProxy")

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    #file_location="./",
    filter_dict={
        "model":{
            "gpt-3.5-turbo",
        }
    }
)

st.text(config_list)

@st.cache_resource
def iniHis():
    history=[]
    return history

his=iniHis()
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
if 'input_msg' not in st.session_state:
    st.session_state.input_msg = None


class StreamlitUserAgent(UserProxyAgent):
    def setSt(self,st):
        self.st=st

    def setQueue(self,g):
        self.input_queue=q

    def get_human_input(self, prompt: str) -> str:
        print("get_human input")

        time.sleep(5)
        print("AI handle input automatically...")
        user_input=None
        return user_input

class CC:
    def setAgent(self,agent):
        self.Agent=agent

    def _generate_board_reply(
        self,
        recipient:autogen.AssistantAgent,
        messages,#: Optional[List[Dict]] = None,
        sender: Optional[autogen.Agent] = None,
        config: Optional[Any] = None,
    ):
        message = messages[-1]
        print(sender.name)
        first_prompt=message['content']
        if first_prompt!=None:
            #prinqmessages)
            his.append({'role':'assistant','content':message['content']})

            self.Agent.st.chat_message(message["role"],avatar=ai()).write(message['content'])

        return (
            False,
            None
        )


@st.cache_resource
def initialAgents():
    print('initialAgents')
    assistant = AssistantAgent(
                name="assistant",
                llm_config={
                    "seed":42,# seed for caching and reproducibility
                    "config_list": config_list, # a list of OpenAI API configurations
                    "temperature": 0,# temperature for sampling
                },# configuration for flaml.oa, an enhanced inference API compatible with OpenAI API
            )
        # create a UserProxyAgent instance named "user_proxy!
    user_proxy = StreamlitUserAgent(
        name="user",
        human_input_mode="ALWAYS", #"NEVER",#
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content",).rstrip().endswith("TERMINATE"),
        code_execution_config={
            "work_dir":"coding",
            "use_docker": "python:3",
        },
    )

    c=CC()
    c.setAgent(user_proxy)
    user_proxy.register_reply( [AssistantAgent, None],c._generate_board_reply)
    #assistant.register_reply([UserProxyAgent，None]，c_generate_board_reply)

    return user_proxy,assistant


user_proxy,assistant = initialAgents()


if 'count' not in st.session_state:
    st.session_state.count = 0

user_input = st.chat_input('Enter input')
#his=getHis()

if st.session_state.count == 0:
    if user_input is None:
        st.chat_message('assistant',avatar=ai()).write('please input something!')
    else:
        st.session_state.count += 1
        user_proxy.setSt(st)
        st.chat_message('user',avatar=user()).write(user_input)
        his.append({'role':'user','content':user_input})
        user_proxy.initiate_chat(
            assistant,
            message=user_input,
        )

    #def aa():
        # initialAgents(user input)

        #x = threading.Thread(target=aa)
        #x.start()

else:
    #print(user input is None)
    if user_input is None:
        st.chat_message('assistant',avatar=ai()).write('please input something!')
    else:
        print(his)
        for h in his:
            avater=ai()
            if h["role"]=="user":
                avater=user()
            st.chat_message(h["role"],avatar=avater).write(h['content'])

        his.append({'role':'user','content':user_input})

        st.chat_message('user',avatar=user()).write(user_input)
        #st.session_state.input_msg=user_input
        user_proxy.setSt(st)
        user_proxy.send({'content':user_input},assistant)


