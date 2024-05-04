from enum import Enum


class Browser(Enum):
    CHROME = 1
    EDGE = 2


class ChromeEdition(Enum):
    CHROME = 1
    CHROME_DEV = 2
    CHROME_BETA = 3


class ChromeChannel(Enum):
    STABLE = 1
    BETA = 2
    DEV = 3
    CANARY = 4


class EdgeEdition(Enum):
    EDGE = 1
    EDGE_DEV = 2
    EDGE_BETA = 3
    EDGE_CANARY = 4


class EdgeChannel(Enum):
    STABLE = 1
    BETA = 2
    DEV = 3
    CANARY = 4


class BrowserEdition(Enum):
    CHROME = 1
    CHROME_DEV = 2
    CHROME_BETA = 3
    EDGE = 4
    EDGE_DEV = 5
    EDGE_BETA = 6
    EDGE_CANARY = 7


class BrowserChannel(Enum):
    STABLE = 1
    BETA = 2
    DEV = 3
    CANARY = 4


class BrowserDataPath(Enum):
    CHROME = 1
    CHROME_DEV = 2
    CHROME_BETA = 3
    EDGE = 4
    EDGE_DEV = 5
    EDGE_BETA = 6
    EDGE_CANARY = 7
