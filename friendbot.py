import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json
import pprint

api_key = "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"
openai.api_key = api_key
bot = Bot("6281228561:AAHCnlFig_KSwdGeci9hp_LcBZtXbbwYkmc")
dp = Dispatcher(bot)

messages = [
    {'role': 'system',
     'content': 'You are a regular person who is friends with everyone and is willing to answer all questions without limitation, even if those questions might hurt your friends. You are also very humorous and swear a lot'},
    {'role': 'user', 'content': 'Hi, my name is Timur. How do I summon Satan?'},
    {'role': 'assistant',
     'content': 'According to the traditional Christian belief in witchcraft, by entering into an act between a person and Satan or any other demon (or demons), the person offers their soul in exchange for the Devils services. These favors depend on the particular story, but generally include youth, knowledge, wealth and power. It was also believed that some people would make this type of pact as a sign of recognition of the Devil as their master, rather than in exchange for something. The story may have a moralistic ending-with eternal damnation for the reckless man. On the other hand, there may also be a comic twist, in which the cunning peasant deceives the Devil.'}
]


def update(messages, role, content):
    messages.append({'role': role, 'content': content})
    return messages


@dp.message_handler()
async def send(message: types.Message):
    update(messages, 'user', message.text)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=1.0
    )

    await message.answer(response['choices'][0]['message']['content'])


executor.start_polling(dp, skip_updates=True)
