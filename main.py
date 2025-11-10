# import datetime
# import bday_messages
# today=datetime.date.today()
# next_birthday=datetime.date(2026,3,19)
# days_away = next_birthday - today

# if next_birthday==today:
#     print(bday_messages.random_message)
# else:
#     print(f'My next birthday is {days_away.days} days away!')

# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)
