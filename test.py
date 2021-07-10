import discord
import asyncio
import random
import datetime
import os

from discord import client
from discord.colour import Color
from discord.enums import Status

client = discord.Client()

@client.event
async def or_ready():

    print('성곡정으로 봇이 시작됨')
    print(client.User.name)

    game = discord.Game('명령어')
    await client.change_presence(Status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    #기본적인 명령어

    if message.content == "얌마!":
        await message.channel.send("아뭐!!!!")

    if message.content == "어떻하지":
        await message.channel.send("다시해 그럼")

    if message.content == "메이커":
        await message.channel.send("@everyone 잘생김")

    if message.content == "유튜브는?":
        await message.channel.send("@everyone 역시 Y지")

        print('유튜브는?')

    if message.content == "끼어들지마":
        await message.channel.send("싫은뒈")

        print('끼어들지마')

    if message.content == "메이커 끼어들지마":
        await message.channel.send("싫은뒈")

        print('메이커 끼어들지마')

    if message.content == ".":
        await message.channel.send("힘내..")

        print('.')

    if message.content == "너때문이야":
        await message.channel.send("내가왜~")

        print('너때문이야')

    #기본 임베드

    if message.content == "너의 유튜브 소개":
        embed = discord.Embed(title="Y 구독하기", description="영상 좋아요도 누르기", color=0x00ff00)
        embed.add_field(name="찔리면 지금이라도 누르기 ㅇㅋ?", value="싫으면 청까",inline=False)
        embed.add_field(name="찔리면 지금이라도 누르기 ㅇㅋ? (2스택)", value="싫으면 청까 (2스택)",inline=False)
        embed.set_footer(text="구독자 10000명을 원합니다")
        await message.channel.send(embed=embed)
        print('유튜브 소개함')

    if message.content == "너 유튜브 소개":
        embed = discord.Embed(title="Y 구독하기", description="영상 좋아요도 누르기", color=0x00ff00)
        embed.add_field(name="찔리면 지금이라도 누르기 ㅇㅋ?", value="싫으면 청까",inline=False)
        embed.add_field(name="찔리면 지금이라도 누르기 ㅇㅋ? (2스택)", value="싫으면 청까 (2스택)",inline=False)
        embed.set_footer(text="구독자 10000명을 원합니다")
        await message.channel.send(embed=embed)
        print('유튜브 소개함')

    if message.content == "나 어때?":
        embede = discord.Embed(title="거울을 보거라", description="니 면상", color=0x8A0829)
        embede.add_field(name="니 주둥이 냄새나 맡아봐라", value="싫으면 청까",inline=False)
        embede.add_field(name="니 주둥이 냄새나 맡아봐라 (2스택)", value="싫으면 청까 (2스택)",inline=False)
        embede.set_footer(text="암튼 넌 못생김")
        await message.channel.send(embed=embede)

        print('나 어때?')

    if message.content == "나 어때":
        embeda = discord.Embed(title="거울을 보거라", description="니 면상", color=0x8A0829)
        embeda.add_field(name="니 주둥이 냄새나 맡아봐라", value="싫으면 청까",inline=False)
        embeda.add_field(name="니 주둥이 냄새나 맡아봐라 (2스택)", value="싫으면 청까 (2스택)",inline=False)
        embeda.set_footer(text="암튼 넌 못생김")
        await message.channel.send(embed=embeda)

    #렌덤 메시지

    if message.content == "오늘의 운세는?":
        ran = random.randint(0,10)
        if ran == 0:
            d = "가장나쁨"
        if ran == 1:
            d = "조금나쁨"
        if ran == 2:
            d = "약간나쁨"
        if ran == 3:
            d = "그냥나쁨"
        if ran == 4:
            d = "나쁨"
        if ran == 5:
            d = "보통"
        if ran == 6:
            d = "좋음"
        if ran == 7:
            d = "그냥좋음"
        if ran == 8:
            d = "약간좋음"
        if ran == 9:
            d = "조금좋음"
        if ran == 10:
            d = "가장좋음"
        await message.channel.send(d)
        print('오늘의 운세가나옴.')
    
    if message.content == "주사위 굴려줘":
        ran = random.randint(0,6)
        if ran == 0:
            d = "0"
        if ran == 1:
            d = "1"
        if ran == 2:
            d = "2"
        if ran == 3:
            d = "3"
        if ran == 4:
            d = "4"
        if ran == 5:
            d = "5"
        if ran == 6:
            d = "6"
        await message.channel.send(d)
        print('주사위굴림')

    #채팅청소

    if message.content.startswith("청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")

        print('채팅청소함')

    #욕 또는 패드립

    if message.content == "봇 바보":
        await message.channel.send("내가 바보면 너는 뭐냐")
        print('봇 바보')

    if message.content == "천재":
        await message.channel.send("천재같은소리하네")
        print('천재')

    if message.content == "개소리좀 그만해":
        await message.channel.send("월월!(개 짖는소리좀 않나게하라!)")
        print('개소리좀 그만해')

    if message.content == "봇 에미 디진넘이":
        await message.channel.send("(반사)아이고 불쌍해 ㅠㅠ")
        print('봇 에미 디진넘이')

    if message.content == "에미 디진넘이":
        await message.channel.send("(반사)아이고 불쌍해 ㅠㅠ")
        print('에미 디진넘이')

    if message.content == "에미 디진넘":
        await message.channel.send("(반사)아이고 불쌍해 ㅠㅠ")
        print('에미 디진넘')

    if message.content == "야 멍청아":
        await message.channel.send("그건 너가 돌+i겠지")
        print('야 멍청아')

    #서버상태

    if message.content == "서버 상태 알려줘":
        embeds = discord.Embed(title="서버상태", description="주의단계\n――――――――――――――――――――――――――――\n\n지금 서버 상태는 안전하지 않습니다 혹시모르니 조심하시길바랍니다\n\n――――――――――――――――――――――――――――",timestamp=datetime.datetime.now(), color=0x7CEBF3)
        embeds.add_field(name="Chat", value="정상",inline=True)
        embeds.add_field(name="Ping", value="정상",inline=True)
        embeds.add_field(name="Server", value="보통",inline=True)
        embeds.add_field(name="Bot Ping", value="나쁨",inline=True)
        embeds.set_thumbnail(url="https://cdn.discordapp.com/attachments/861877194817404938/861931485358587955/icon.png")
        embeds.set_footer(text="Bot Made by. 메이커 #3446", icon_url="https://cdn.discordapp.com/attachments/861877194817404938/861931485358587955/icon.png")
        await message.channel.send(embed=embeds)

        print('서버상태 알려줌')

    #도움 또는 공지

    if message.content == "도와줘":
        await message.channel.send("명령어: 얌마!, 청소(원하는숫자), 주사위 굴려줘, 오늘의 운세는?, 너의 유튜브 소개, 유튜브는?, 메이커")


        print('기본 명령어 알려줌')

    if message.content.startswith ("!공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(862213535130714123)
            embedr = discord.Embed(title="**공지사항**", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n봇은 오후3시부터 오후4시 40분까지 봇 점검으로 될 예정입니다\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(), color=0x00ff00)
            embedr.set_footer(text="Bot Made by. 메이커#3446 | 담당 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/861877194817404938/861931485358587955/icon.png")
            embedr.set_thumbnail(url="https://cdn.discordapp.com/attachments/861877194817404938/861931485358587955/icon.png")
            await channel.send ("@everyone", embed=embedr)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))


            print('공지를 알려줌')

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
