VERSION = (0,4)


class Settings:
    TIMEZONE_SUPPORT = False


from humanize.time import *
from humanize.number import *
from humanize.filesize import *
from humanize.i18n import activate, deactivate


__all__ = ['VERSION', 'naturalday', 'naturaltime', 'ordinal', 'intword',
    'naturaldelta', 'intcomma', 'apnumber', 'fractional', 'naturalsize',
    'activate', 'deactivate', 'naturaldate', "Settings"]
