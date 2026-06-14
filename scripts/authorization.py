from tg_digest.tg_client import get_client

with get_client() as client:
    client.loop.run_until_complete(client.send_message('me', 'Authorization success!'))