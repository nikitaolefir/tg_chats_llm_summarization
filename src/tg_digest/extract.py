def fetch_messages(client, chat_id, start, end):
    messages = []
    for message in client.iter_messages(chat_id, offset_date=end):
        if message.date < start:
            break
        if not message.text:
            continue
        message_metadata = {}
        message_metadata['chat_id'] = message.chat_id
        message_metadata['message_id'] = message.id
        message_metadata['date'] = int(message.date.timestamp())
        message_metadata['sender_id'] = message.sender_id
        message_metadata['text'] = message.text
        message_metadata['reply_to'] = message.reply_to_msg_id
        messages.append(message_metadata)
    return messages
        




