async def main():
    global TOKEN
    await client.login(ODIzOTczODcxNjM1MjY3NjE0.YFondw.LEW2Hcb8IjNoOQxnwN8Sg8i7KY4)
    await client.connect()

# Launch the bot
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except:
    loop.run_until_complete(client.logout())
finally:
    loop.close()
