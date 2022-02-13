import discord, datetime
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():

    print(client.user.name)
    print('봇에 로그인이 됬습니다')
    game = discord.Game('채팅이 일')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("와 샌즈!"):
        await message.channel.send("언더테일 아시는구나! 혹시 모르시는분들에 대해 설명해드립니다.\n샌즈랑 언더테일의 세가지 엔딩루트중 몰상엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다.\n 공격은 전부다 회피하고 만피가 92인데 샌즈의 공경력은 1초당 60이 다는데다가 \n독뎀까지 추가로 붙어있습니다.. \n하지만 이러면 절대로 게임을 꺨 수 가없으니 제작진이 치명적인 약점을 만들었죠.\n 샌즈의 치명적인 약점이 바로 지친다는것입니다. \n패턴들을 다 견디고 나면 지쳐서 자신의 턴을 유지한채로 잠에습니다.\n 하지만 잠이 들었을때 창을 옮겨서 공격을 시도하고 샌즈는\n 1차공격은 피하지만 그 후에 바로날라오는 2차 공격을 맞고 죽습니다.")
    elif message.content.startswith("김승우 바보"):
        await message.channel.send("ㄹㅇㅋㅋ")
    elif message.content.startswith("렌지 소환!"):
        OrangeId = "<@900162449511182356>"
        await message.channel.send("%s" % OrangeId)
        await message.channel.send("%s" % OrangeId)
        await message.channel.send("%s" % OrangeId)
        await message.channel.send("%s" % OrangeId)
        await message.channel.send("%s" % OrangeId)
    elif message.content.startswith("노넌 소환!"):
        HononunId = "<@645617675539710002>"
        await message.channel.send("%s" % HononunId)
        await message.channel.send("%s" % HononunId)
        await message.channel.send("%s" % HononunId)
        await message.channel.send("%s" % HononunId)
        await message.channel.send("%s" % HononunId)
    elif message.content.startswith("캐롯 소환!"):
        CarrotId = "<@759727723370250250>"
        await message.channel.send("%s" % CarrotId)
        await message.channel.send("%s" % CarrotId)
        await message.channel.send("%s" % CarrotId)
        await message.channel.send("%s" % CarrotId)
        await message.channel.send("%s" % CarrotId)
    elif message.content.startswith("채팅이 도움말"):
        embed_doumal = discord.Embed(colour=discord.Colour.orange(), title="채팅이_도움말", description= "ㅎㅇ나 채팅이임 도움말보고\n명령어 잘 써봐\n\n\n렌지 소환!: 렌지를 5번 멘션합니다.\n\n노넌 소환!: 노넌을 5번 멘션합니다.\n\n캐롯 소환!: 캐롯을 5번 맨션합니다.\n\n와 샌즈!: 언더테일 드립을 칩니다.\n\n김승우 바보: 사실이기 때문에 ㄹㅇㅋㅋ을 칩니다.")
        await message.channel.send(embed=embed_doumal)

    elif message.content == '내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 100)
        await message.channel.send(f"{message.author.mention}의 가입일: {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임: {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content.startswith("/채널메세지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

access_token = os.environ["BOT_TOKEN"]
client.run(OTE2MzEyOTMxODMzMTEwNTQ4.YaoU6w.uThvC57F_HYkP8XYK3jInTTtkAc)
