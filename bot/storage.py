from typing import *

import json
from threading import Lock


class StarredMessage(object):
    """A class used to store information of starred messages

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

    def __eq__(self, o: object) -> bool:
        return isinstance(o, StarredMessage) and self.message_id == o.message_id


class StarredUser(object):
    """A class used to store information of starred messages

    Attributes
    ----------
    user_id : int
        the id of the user
    messages : List[StarredMessage]
        the list of starred messages sent by the user

    Methods
    -------
    """

    def __init__(self, user_id: int) -> None:
        """Creates a new StarredUser object

        Parameters
        ----------
        user_id : int
            the id of the user

        Returns
        -------
        None"""
        self.user_id: int = user_id
        self.messages: List[StarredMessage] = []

    def to_json(self):
        """Returns a json representation of the user

        Returns
        -------
        str
            the json representation of the user"""
        pass

    def __str__(self) -> str:
        return self.to_json()

    def __eq__(self, o: object) -> bool:
        return isinstance(o, StarredUser) and self.user_id == o.user_id


class Store(object):
    """A thread-safe class used to store the information of users, their stars, and their
    starred messages

    Attributes
    ----------
    users : Dict[int,StarredUser]
        the dictionary of all users and their associated starred messages stored in this storage
        object
    messages: Dict[int,StarredMessage]
        the dictionary of all starred messages with key as id and value as
        StarredMessage object
    lock : threading.Lock
        the lock that protects methods from threads

    Methods
    -------
    contains_message(message_id : int) : bool
        Returns if the id of a message is already in the list of messages
    contains_user(user_id : int) : bool
        Returns if the id of a user is already in the list of users

    to_json() : str
        Returns a json representation of the message"""

    def __init__(self) -> None:
        """Creates a new Store object with an empty users and messages dicts

        Returns
        -------
        None"""
        self.users: Dict[int, StarredUser] = {}
        self.messages: Dict[int, StarredMessage] = {}
        self.lock: Lock = Lock()

    def contains_message(self, message_id: int) -> bool:
        """Returns if the id of a message is already in the list of messages

        Parameters
        ----------
        message_id : int
            the id of the message

        Returns
        -------
        bool
            True if the message is already in the list of messages in storage,
            False otherwise"""
        self.lock.acquire()
        result = message_id in self.messages
        self.lock.release()
        return result

    def contains_user(self, user_id: int) -> bool:
        """Returns if the id of a user is already in the list of users

        Parameters
        ----------
        user_id : int
            the id of the user

        Returns
        -------
        bool
            True if the user is already in the list of users in storage,
            False otherwise"""
        self.lock.acquire()
        result = user_id in self.users
        self.lock.release()
        return result

    def new_message(
        self,
        message_id: int,
        author_id: int,
        author_nick: str,
        message_content: str,
        stars: int,
    ) -> bool:
        """Creates a new starred message in the system

        Parameters
        ----------
        message_id : int
            the id of the message to add
        author_id : int
            the id of the author
        author_nick : str
            the nickname of the author as it appears in the server the message
            is taken from
        message_content : str
            the content of the message
        stars : int
            the number of stars given to the message

        Returns
        -------
        bool
            True if the message is not already in the system, False otherwise"""
        self.lock.acquire()
        if message_id in self.messages:
            self.lock.release()
            return False
        self.messages[message_id] = StarredMessage(message_id, author_id, author_nick, message_content, stars)
        self.lock.release()
        return True

    def new_user(self, user_id: int) -> bool:
        """Creates a new user in the system

        Parameters
        ----------
        user_id : int
            the id of the user to add

        Returns
        -------
        bool
            True if the user is not already in the system, False otherwise"""
        self.lock.acquire()
        if user_id in self.users:
            self.lock.release()
            return False
        self.users[user_id] = StarredUser(user_id)
        self.lock.release()
        return True

    def change_star(self, message_id: int, stars: int) -> bool:
        """Changes the star value of a message

        Parameters
        ----------
        message_id : int
            the id of the message to change
        stars : int
            the number of stars to change to
            Precondition: must be nonzero

        Returns
        -------
        bool
            True if the message exists and stars are nonzero, False otherwise
        """
        self.lock.acquire()
        if not self.contains_message(message_id) or stars < 0:
            self.lock.release()
            return False
        message = self.messages[message_id]
        message.stars = stars
        self.lock.release()
        return True

    def to_json(self) -> str:
        """Returns a json representation of the message

        Returns
        -------
        str
            the json representation of the message"""
        pass

    def __str__(self) -> str:
        self.lock.acquire()
        result = self.to_json()
        self.lock.release()
        return result
