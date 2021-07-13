from typing import *

import json


class StarredMessage(object):
    """A thread-safe class used to store information of starred messages

    Attributes
    ----------
    message_id : int
        the id of the message
    author_id : int
        the id of the author of the message
    author_nick : str
        the nickname of the author as it appears in the server the message
        is taken from
    message_content : str
        the content of the message
    stars : int
        the number of stars given to the message

    Methods
    -------
    to_json() : str
        Returns a json representation of the message"""

    def __init__(
        self,
        message_id: int,
        author_id: int,
        author_nick: str,
        message_content: str,
        stars: int,
    ) -> None:
        """Creates a new StarredMessage object

        Parameters
        ----------
        message_id : int
            the id of the message
        author_id : int
            the id of the author of the message
        author_nick : str
            the nickname of the author as it appears in the server the message
            is taken from
        message_content : str
            the content of the message
        stars : int
            the number of stars given to the message

        Returns
        -------
        None"""
        self.message_id: int = message_id
        self.author_id: int = author_id
        self.author_nick: str = author_nick
        self.message_content: str = message_content
        self.stars: int = stars

    def to_json(self) -> str:
        """Returns a json representation of the message

        Returns
        -------
        str
            the json representation of the message"""
        dic = {}
        dic["message_id"] = self.message_id
        dic["author_id"] = self.author_id
        dic["author_nick"] = self.author_nick
        dic["message_content"] = self.message_content
        dic["stars"] = self.stars
        return json.dumps(dic)

    def __str__(self) -> str:
        return self.to_json()


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
    -------
    to_json() : str
        Returns a json representation of the message"""

    def __init__(self) -> None:
        """Creates a new Store object with an empty users dict and messages
        list

        Returns
        -------
        None"""
        self.users: Dict[int, StarredMessage] = {}
        self.messages: List[StarredMessage] = []

    def to_json(self) -> str:
        """Returns a json representation of the message

        Returns
        -------
        str
            the json representation of the message"""
        dic = {}
        dic["users"] = self.users
        dic["messages"] = self.messages
        return json.dumps(dic)

    def __str__(self) -> str:
        return self.to_json()
