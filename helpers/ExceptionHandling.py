import sys

DEBUG_FLAG = True
SIMPLE_EXCEPT = False


def _exception_handler(exception_type, exception, traceback, debug_hook=sys.__excepthook__):
    global DEBUG_FLAG
    global SIMPLE_EXCEPT

    if SIMPLE_EXCEPT:
        SIMPLE_EXCEPT = False
        print("{}".format(exception))
    elif DEBUG_FLAG:
        debug_hook(exception_type, exception, traceback)
    else:
        print("Invoicr has crashed!")
        print("{}: {}".format(exception_type.__name__, exception))


def simple_except(message: str, exception_type=Exception):
    global SIMPLE_EXCEPT
    _simple_except = SIMPLE_EXCEPT
    SIMPLE_EXCEPT = True
    raise exception_type(message)
    SIMPLE_EXCEPT = _simple_except


sys.excepthook = _exception_handler
