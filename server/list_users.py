#!/usr/bin/env python3
import argparse
import pathlib
import shutil

from mini_event.mini_event import MiniEventApp
from mini_event.models import User


parser = argparse.ArgumentParser(description="Lists registered users")
args = parser.parse_args()

app = MiniEventApp.from_settings()


with app.connect():
    app.init_database()

    print("    Telegram ID | Admin | Name")
    for user in User.select():
        print("%15s | %5s | %s" % (user.telegram_id, user.is_admin, user.name))