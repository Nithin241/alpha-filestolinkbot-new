class Translation(object):
    START_TEXT = """
👉 Forward any files to this bot,and bot will generate its directlink.
👉 Do not send multiple files at a time.
👉 If you dont get directlink after 1 hour,forward that file again to the bot
👉 Subscribe our channel for bot updates @filestolink
👉 Direct links are only for personal use,do not share with others.we are not responsible for any content that you generates direct links.

© Source Code : [SpEcHlDe](https://github.com/SpEcHiDe/AnyDLBot)
    """
    HELP_USER = """
👉 Forward any files to this bot,and bot will generate its directlink.
👉 Do not send multiple files at a time.
👉 If you dont get directlink after 1 hour, forward that file again to the bot
👉 Subscribe our channel for bot updates @filestolink
👉 Direct links are only for personal use,do not share with others.we are not responsible for any content that you generates direct links.
    """
    ABS_TEXT = "Please don't be selfish."
    DOWNLOAD_START = "📤 Your request is in the queue. Do not send another request. Please be patient..."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    UPLOAD_START = "Started to upload.."
    AFTER_GET_DL_LINK = """
<b>Direct Link</b> <a href=\"{}\">generated</a>

filename: {}
size: {}
expire_in: {} days

Join our channel @filestolink
    """
    ABUSIVE_USERS = "You got BANNED bro..."