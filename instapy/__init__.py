# flake8: noqa

from .instapy import InstaPy
from .util import smart_run
from .util import click_element
from .util import web_address_navigator
from .time_util import sleep
from .settings import Settings
from .file_manager import set_workspace
from .file_manager import get_workspace


# __variables__ with double-quoted values will be available in setup.py
__version__ = "0.4.3"

