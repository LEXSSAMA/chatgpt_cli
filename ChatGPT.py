#!/bin/python3

import os
import sys
import openai
import select

from rich.console import Console
from rich.text import Text

prompt = ''

def input_parse(input_text:str):
    global prompt
    if input_text == 'quit' :
        exit(0)
    elif len(input_text) > 0 and  input_text[-1] == '\\':
        prompt += input_text[:-1]
        console.print("...",highlight=True,end=' ')
        return
    prompt += input_text
    if len(prompt) > 0:
        completion = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=2048,
                temperature=1,
                )
        text = Text(completion.choices[0].text)
        text.stylize("bold green")
        console.print(text)
    prompt = ''
    console.print(">>>",highlight=True,end=' ')
    return




console = Console()
openai.api_key = os.getenv("OPENAI_API_KEY")
console.print(">>>",highlight=True,end=' ')
while True :
    read,_,_ = select.select([sys.stdin],[],[],None)
    if read:
        input_text = sys.stdin.readline().strip()
        input_parse(input_text)
