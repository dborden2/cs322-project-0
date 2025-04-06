"""
Trivial project is just for trying out Git and the
grading mechanisms.
"""

import configparser
config = configparser.ConfigParser()
config.read("credentials-skel.ini")

#message = config["DEFAULT"]["message"]

#print(message)

if not config:
    print("❌ Could not read 'credentials.ini'")
else:
    print("✅ Successfully read:", config)
    print("DEFAULT keys:", dict(config["DEFAULT"]))