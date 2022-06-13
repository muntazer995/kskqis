import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQBx1oktC8mc0O1l1y5_UbEhb0BIimZfYbJelhb3WJt3PzlEx2oxaynrakEkCxX-FDnKBBh8JTSlyC0JdaAjkv6vlfJEBWvqP8I3YCman4K4MGYNx1oO--L-Ek3B7XybgHKb2Rsf9vPmDJmY87CWfirTViRNdNmRXdjt6omYppJ88Cddv65jHVnvjV1_aI8mK--oqBAGkHZy3-27Y-H6AR8rGmBOmLevlvOe1Oy5N2njNZIuQ6Xndc1iC5gkMCLZKJpEalUUfFy3mgnJh87M0s7zmkyuQd9yj6eJAYphR3pyUeTwuEoQ0BCBE4QNpe6AFwwDYmnKJ_AenHj7D0Uj_FvcAAAAAHH4i8kA")
