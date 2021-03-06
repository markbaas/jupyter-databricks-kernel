class ClusterNotOnlineException(Exception):
    skip_traceback = True

    def __str__(self):
        return "Cluster is not online."


class IncompleteResults(Exception):
    skip_traceback = True

    def __str__(self):
        return "No results found."


class CommandError(Exception):
    skip_traceback = True

    def __init__(self, summary, cause):
        self.summary = summary
        self.cause = cause

    def __str__(self):
        return f"Command Error: {self.cause}"


class CommandCanceled(Exception):
    skip_traceback = True

    def __str__(self):
        return "Command is cancelled."


class NoSuchMagic(Exception):
    skip_traceback = True

    def __init__(self, magic):
        self.magic = magic

    def __str__(self):
        return f"No such magic: {self.magic}"
