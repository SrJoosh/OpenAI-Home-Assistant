import os
import asyncio
import gpt
from dotenv import load_dotenv

#Main Code
async def Main():

    load_dotenv()
    GPT = gpt.GPT(os.getenv('API_KEY') , 
                  history=[], #Any pre-existing history to load
                  max_tokens=int(os.getenv('MAX_TOKENS')), #Maximum tokens per conversation
                  spiceyness=int(os.getenv('SPICEYNESS')), #How Spicy/Creative the AI is
                  debug=os.getenv('DEBUG'), #Enable Debug Logs
                  knowledgebase="resources/knowledgebase.csv") #Specified Training CSV File

    print("\nWhat would you like to ask?: ")
    while True:
        query = input("\n  : ")
        if(len(query) > 5):
            print(f"\n {await GPT.SendGPTMessage(query)}")

asyncio.run(Main())