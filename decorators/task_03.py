import os
import json
from datetime import datetime
from modules.client import get_name


def logger(old_function):
    log_info = {}

    log_info.update({
        "name": old_function.__name__,
        "timestamp": datetime.now()
    })

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)

        log_info.update({
            "args": args,
            "kwargs": kwargs,
            "result": result
        })

        json_object = json.dumps(log_info, indent=4, default=str)

        with open('log_task_03_1.log', "a+") as outfile:
            outfile.writelines(json_object + ",\n")

        return result

    return new_function


def main():
    path = 'log_task_03_1.log'

    if os.path.exists(path):
        os.remove(path)

    @logger
    def new_function(name):
        result = get_name(name)

        return result

    print(new_function("10006"))


if __name__ == '__main__':
    main()
