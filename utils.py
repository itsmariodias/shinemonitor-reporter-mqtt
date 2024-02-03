import config


def log(string: str):
    if config.debug:
        print(string)
