import discord
import config
from discord import Server, Client, ChannelType, Embed

def ex(args, message, client, invoke, config):
    args_out = ""
    author = message.author.nick
    if len(args) > 0:
        args_out = "@everyone \n\n__**Coalition-Ping**__\nFrom: "+ author + "\n\n%s" % args.__str__()[1:-1].replace("'", "").replace(",", "")

    yield from client.send_message(message.channel.server.get_channel(config.CID50), (args_out))
    # 50 SHADES

    yield from client.send_message(client.get_server(config.SIDRMC).get_channel(config.CIDRMC), (args_out))
    # RMC

    yield from client.send_message(client.get_server(config.SIDFRT).get_channel(config.CIDFRT), (args_out))
    # FRT

    yield from client.send_message(client.get_server(config.SIDSAU).get_channel(config.CIDSAU), (args_out))
    #SAU