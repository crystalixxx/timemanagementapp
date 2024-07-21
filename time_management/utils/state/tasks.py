import reflex as rx
from typing import List, Optional
from sqlmodel import select

from .base import State, User
from .auth import AuthState

from time_management.database.models import Task


class TaskState(AuthState):
    tasks: List["Task"] = []

    add_task_modal_open: bool = False
    is_registration: bool = True

    new_task_title: str = ""
    new_task_description: str = ""
    new_task_categories: str = ""
    new_task_date: str = ""
    new_task_urgency: int = 0

    def load_tasks(self):
        self.tasks = []

    def add_task(self):
        print("111")