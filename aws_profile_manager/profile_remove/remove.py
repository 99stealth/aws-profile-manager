import sys
from typing import Dict
import logging

class Remove:
    def choose_profile_to_remove(self, profiles: Dict) -> str:
        i = 1
        counter = {}
        for profile in profiles:
            counter[i] = profile
            i += 1
        for c in counter:
            print("{}: {}".format(c, counter[c]))
        while True:
            try:
                answer = input("\nChoose a number of the profile which you want to remove: ")
            except (KeyboardInterrupt, EOFError):
                logging.error("\nProcess has been stopped. Interrupted by user")
                sys.exit(1)
            try:
                return counter[int(answer)]
            except ValueError as e:
                logging.error("Answer \"{}\" is not valid. Please provide number from 1 to {}".format(answer, len(counter)))