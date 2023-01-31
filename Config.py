import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13429768"))
    API_HASH = os.environ.get("API_HASH", "63b6d07b85e038eae4183c2902c4347b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5405318535:AAHM59nq3X8IuQ8VvTO7Kw1bvdZLNGZv74I")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJoBuzqsYmxThJQKxQAh9wC8m1Y3ZSDl_CDPz8vG5kDZfWnkraAB8r-bNKmXZkNjZ6F5jrD_QD0bMTVkX_L5jDjwMIGj1wevZU5dp1ant8InhlRXrlO_318Qp_q0IwE8mzrYbOD-1ZIeu-_LHsATdgqbvSnUehoDZyQS77LUk7A825m6BPW_hlHqSREtnhO2tAhNRBA-oh6TmeuM7TZFICL-5-X31omEI-6nXp5m8jaCKxzohNqnU8D58xYlDPbtHHu8tSp7Igjm9DCS5wJ4azzddDsblFI66LoAr610UrnRAsVPAgyj9z3R1Pb8vEqgkM8UeThLhPgGciKppiugLUp61V0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", True)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "kang_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5592036777")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
