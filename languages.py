from enum import Enum, auto

class Language(Enum):
    PYTHON = auto(), "py"
    C = auto(), "c"
    RUST = auto(), "rs"

    def __init__(self, _, extension):
        self.ext = extension

    @classmethod
    def _missing_(cls, value):
        return language_abbr.get(value, None)

language_abbr = {"py": Language.PYTHON, "python": Language.PYTHON, "c": Language.C, "rust": Language.RUST, "rs": Language.RUST}