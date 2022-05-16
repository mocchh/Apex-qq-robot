from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg,Arg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, escape, Bot, Event
from nonebot.adapters import Message
import nonebot
import requests
import re
import json


ND = on_command("apex",aliases={"APEX"}, priority=2,block=True)
@ND.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  
    if plain_text:
        matcher.set_arg("Name", args)  


@ND.got("Name", prompt="你想查询谁的战绩呢?")
async def handle_city(Name: Message = Arg(), sname: str = ArgPlainText("Name")):
        await ND.send('查询中', at_sender=True)

        URL = f"https://api.mozambiquehe.re/bridge?auth=979d0a73104cc447ebf3cd264030a319&player={sname}&platform=PC"
        res = requests.get(URL)
        jsonobj = json.loads(res.text)

        pname = jsonobj['global']['name'] #昵称
        plevel = jsonobj['global']['level'] #等级
        prankscore = jsonobj['global']['rank']['rankScore'] #排名分
        prankname = jsonobj['global']['rank']['rankName'] #段位

        name = "昵称：" + pname
        level = "等级：" + str(plevel)
        rankscore = "排名分：" + str(prankscore)
        rankname = "段位：" + str(prankname)

        info=(name,level,rankscore,rankname)

        await ND.send('\n'.join(info))  
 