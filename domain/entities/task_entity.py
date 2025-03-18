from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class TaskEntity:
    id: Optional[int]
    title: str
    description: str
    completed: bool
    created_at: Optional[datetime] = None

    def __init__(
        self,
        id: Optional[int],
        title: str,
        description: str,
        completed: bool = False,
        created_at: Optional[datetime] = None,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at
