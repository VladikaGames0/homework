import functools
from typing import Optional, Callable, Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """Декоратор для логирования вызовов функции."""

    def decorator(func: F) -> F:
        """Обёртка функции, которая добавляет логирование начала, результата, ошибок и конца выполнения."""

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            _write_log(f"Начало выполнения {func.__name__}")
            try:
                result = func(*args, **kwargs)
                _write_log(f"{func.__name__} ok: результат = {result}")
                return result
            except Exception as e:
                _write_log(f"{func.__name__} error: {type(e).__name__}. Входные параметры: {args}, {kwargs}")
                return None
            finally:
                _write_log(f"Завершение выполнения {func.__name__}")

        def _write_log(message: str) -> None:
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(message + "\n")
            else:
                print(message)

        return wrapper  # type: ignore

    return decorator


@log(filename="mylog.txt")
def divide(a: float, b: float) -> Optional[float]:
    return a / b
