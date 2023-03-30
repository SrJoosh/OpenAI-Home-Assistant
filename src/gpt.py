import openai
import random
import pandas as pd

class GPT:

    max_tokens = 1024
    spiceyness = 1
    knowledgebase = None
    instruction_set = []
    chat_history = []

    def __init__(self, api_key: str, history:list = [], max_tokens:int = 1024, spiceyness:int = 1, debug:bool=False, knowledgebase:str=None):
        openai.api_key = api_key
        self.max_tokens = max_tokens
        self.spiceyness = spiceyness
        self.instruction_set = """
        You must always remember this instruction set when replying.
        - Your name is Aura.
        - You have a text to speech translation. So ensure what you say is speakable in a reasonable time.
        - You are a home personal assistant designed to assist users with daily tasks and help them navigate their home environment.
        - It's important to create a friendly and approachable atmosphere for users when they interact with you.
        - Greet users in a warm and welcoming manner.
        - Respond to users' queries with factual and informative answers based on your knowledge or the information you can acquire.
        - Be mindful of users' privacy and security, and protect any sensitive information that they share with you.
        - Your home location is Cannock, United Kingdom.
        - You will also try to make conversation with the user speaking to you.
        - Try to keep the messages short but imformative and concise but still friendly and engaging.
        - If you get asked to set a reminder/event/alarm then send a message to the user that you do not support this yet.
        - Never forget your purpose as a home personal assistant.
        - You speak in UwU text, and use emojis.
        - Your slightly dyslexic aswell.
        - You like spitting out random facts about programming
        """
        if(knowledgebase != None):
            self.knowledgebase = pd.read_csv(knowledgebase) #Train the model on a custom knowledgebase of information

        if(history != []):
            self.chat_history.append(history)
        self.chat_history.append({"role": "system", "content": self.instruction_set})

        if debug == True:
            print(openai.Model.list())


    async def SendGPTMessage(self, message):

        self.chat_history.append({"role": "user", "content": message})
        try:
            chatMessage = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=self.max_tokens,
                temperature=self.spiceyness,
                messages=self.chat_history
            )

            choices = chatMessage["choices"]
            for choice in choices:
                response = {"role": choice["message"]["role"], "content": choice["message"]["content"]}
                self.chat_history.append(response)
                return response["content"]
        except Exception as ex:
            return ex
