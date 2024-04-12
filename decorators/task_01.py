import os
import json
from datetime import datetime


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

        with open('main.log', "a+") as outfile:
            outfile.writelines(json_object + ",\n")

        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    # hello_world
    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"

    # summator
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'

    # div
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    # main.log
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = str(log_file.read())

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
