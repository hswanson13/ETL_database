from dataclasses import dataclass
from os import environ
from os.path import dirname, join
root_dir = dirname(__file__)


@dataclass(init=False)
class Config:

    DATABASE_URL: str = 'sqlite:///'+join(root_dir, 'tempdb.sqlite')
    ECHO_SQL: bool = False

    @property
    def keys(self):
        keys = []
        for k in dir(self):
            if k[0].isupper():
                keys.append(k)
        return keys

    def __init__(self):
        for k in self.keys:
            default = getattr(self, k)
            try:
                import env
                val = getattr(env, k)
            except (ImportError, AttributeError):
                val = environ.get(k, default)

            if type(default) == bool:
                if str(val).lower() == "true":
                    val = True
                elif str(val).lower() == "false":
                    val = False
                else:
                    raise ValueError(f"Boolean config \"{k}\" must be True or False, found \"{val}\"")
            else:
                val = type(default)(val)

            if k == 'DATABASE_URL':
                val = val.replace('postgres', 'postgresql+psycopg2', 1)

            setattr(self, k, val)


the_config = Config()
