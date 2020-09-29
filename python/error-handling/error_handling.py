def handle_error_by_throwing_exception():
    try:
        i = 1/0
    except Exception as error:
        raise Exception(error)


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except Exception:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        return True, int(input_data)
    except Exception:
        return False, None


def filelike_objects_are_closed_on_exception(filelike_object):
    filelike_object.open()
    filelike_object.close()
    filelike_object.do_something()