import unittest
import os
import sys
import json

rpath = os.path.abspath('..')

if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader


class TestClass(unittest.TestCase):
    def test_get_users(self):
        data = SlackDataLoader('./tests')
        users = data.get_users()

        expected =['id',
"team_id",
"name",
"deleted",
"color",
"real_name",
"tz",
"tz_label",
"tz_offset",
"profile",
"is_admin",
"is_owner",
"is_primary_owner",
"is_restricted",
"is_ultra_restricted",
"is_bot",
"is_app_user",
"updated",
"is_email_confirmed",
"who_can_share_contact_card"]
        for user in users:
            self.assertListEqual(list(users.keys()), expected)





if __name__ == '__main__':
    unittest.main()
