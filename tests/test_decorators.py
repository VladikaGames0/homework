import pytest
from src.decorators import *


def test_successful_function_output(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(3, 5)
    captured = capsys.readouterr()

    assert result == 8
    assert "Начало выполнения add" in captured.out
    assert "add ok: результат = 8" in captured.out
    assert "Завершение выполнения add" in captured.out


def test_function_with_exception(capsys):
    @log()
    def div(a, b):
        return a / b

    result = div(10, 0)
    captured = capsys.readouterr()

    assert result is None
    assert "Начало выполнения div" in captured.out
    assert "div error: ZeroDivisionError" in captured.out
    assert "Входные параметры: (10, 0), {}" in captured.out
    assert "Завершение выполнения div" in captured.out
