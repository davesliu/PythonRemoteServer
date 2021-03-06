import os


class BasicCommunication(object):
    """Testing basic communication and keyword documentation using a class.

    Module.py has same stuff but using a module, not a class, as a library.
    """

    def passing(self):
        """This keyword passes.

        See `Failing`, `Logging`, and `Returning` for other basic keywords.
        """
        pass

    def get_pid(self):
        """Return process id of the server that is serving this library."""
        return os.getpid()

    def failing(self, message):
        """This keyword fails with provided `message`"""
        raise AssertionError(message)

    def logging(self, message, level='INFO'):
        """This keywords logs given `message` with given `level`

        Example:
        | Logging | Hello, world! |      |
        | Logging | Warning!!!    | WARN |
        """
        print('*%s* %s' % (level, message))

    def returning(self, value):
        """This keyword returns the given `value`."""
        return value

    def _private_method(self):
        """This is not a keyword. Nor is the next one."""
        pass

    def __private_method(self):
        pass

    attribute = 'Not a keyword'


if __name__ == '__main__':
    import sys
    from robotremoteserver import RobotRemoteServer

    if sys.argv[-1] == 'no_stop':
        conf = {'allow_remote_stop': False}
        sys.argv.pop()
    else:
        conf = {}
    RobotRemoteServer(BasicCommunication(), '127.0.0.1', *sys.argv[1:], **conf)
