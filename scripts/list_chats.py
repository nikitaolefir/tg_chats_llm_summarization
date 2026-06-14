from tg_digest.tg_client import get_client

with get_client() as client:
    for dialog in client.iter_dialogs():
        print(dialog.id, '-', dialog.title)