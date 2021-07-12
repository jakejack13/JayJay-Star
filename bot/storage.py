from typing import *


class StarredMessage(object):
    """A thread-safe class used to store information of starred messages"""

    pass


class Store(object):
    """A thread-safe class used to store the information of users, their stars, and their
    starred messages

    Attributes
    ----------
    users : Dict[int, List[StarredMessage]]
        the users and their associated starred messages stored in this storage
        object
    messages: List[StarredMessage]
        the list of recently starred messages

    Methods
    -------"""

    def __init__(self):
        self.users: Dict[int, StarredMessage] = {}
        self.messages: List[StarredMessage] = []
