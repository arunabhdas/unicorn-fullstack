from piccolo.table import Table
from piccolo.columns import (
    Varchar,
    Integer,
    ForeignKey,
    Boolean,
    Text,
    Timestamp,
    Numeric,
    Real
)
from piccolo.apps.user.tables import BaseUser


#class Task(Table):
#    """
#    An example table.
#    """
#
#    name = Varchar()
#    completed = Boolean(default=False)

class Author(Table):
    """
    Author
    """

    name = Varchar()
    username = Varchar()
    email = Varchar()
    password = Varchar()
    active = Boolean(default=False)


class Post(Table):
    """
    Post
    """

    title = Varchar()
    description = Varchar()
    author = ForeignKey(references=Author)
    completed = Boolean(default=False)




class Todo(Table):
    """
    An example table.
    """

    title = Varchar()
    description = Varchar()
    author = ForeignKey(references=Author)
    completed = Boolean(default=False)


class Idea(Table):
    """
    An example table.
    """

    title = Varchar()
    description = Varchar()
    author = ForeignKey(references=Author)
    completed = Boolean(default=False)


class Project(Table):
    """
    An example table.
    """

    title = Varchar()
    description = Varchar()
    owner = ForeignKey(references=BaseUser)
    completed = Boolean(default=False)
