class BaseRecord:
    """基底クラス。共通の表現メソッドを提供する。"""

    def __repr__(self):
        attributes = ", ".join(
            [f"{key}={value}" for key, value in self.__dict__.items()]
        )
        return f"{self.__class__.__name__}({attributes})"
