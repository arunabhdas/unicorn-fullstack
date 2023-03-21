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


class Project(Table):
    """
    An example table.
    """

    title = Varchar()
    description = Varchar()
    owner = ForeignKey(references=BaseUser)
    completed = Boolean(default=False)
