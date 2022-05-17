import requests
import json
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

pic = on_keyword(['pic'])
@pic.handle()
async def pic_handle(bot: Bot, event: Event):

    await pic.send(MessageSegment.image('file:///E:/qqbot/mobot/testpic.png'))