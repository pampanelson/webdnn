from enum import Enum
from typing import Union, Optional, List, Sequence, Set

from webdnn.util import json
from webdnn.util.json import JSONSerializable


class PlaceholderOperator(Enum):
    Add: int
    Mul: int
    Mod: int
    EQ: int
    FloorDiv: int


class Dependency:
    operator: PlaceholderOperator
    operands: List[Union[int, Placeholder]]

    @staticmethod
    def check_deep_equal(d1: Dependency, d2: Dependency) -> bool: ...

    def __init__(self, operator: PlaceholderOperator, operands: Sequence[Union[int, Placeholder]]): ...

    @property
    def is_resolved(self) -> bool: ...

    @property
    def value(self) -> Union[int, Placeholder]: ...

    def __repr__(self) -> str: ...

    def dump(self) -> str: ...

    def generate_js_function(self) -> str: ...


class Placeholder(json.SerializableMixin):
    _value: Optional[int]
    label: Optional[str]
    dependency: Optional[Dependency]

    @staticmethod
    def to_int(x: Union[int, Placeholder]): ...

    @staticmethod
    def force_int(x: Union[int, Placeholder]): ...

    @staticmethod
    def check_resolved(x: Union[int, Placeholder]): ...

    @staticmethod
    def check_deep_equal(p1: Union[int, Placeholder], p2: Union[int, Placeholder]) -> bool: ...

    def __new__(cls, dependency: Optional[Dependency] = None, value: Union[int, Placeholder] = None, label: str = None): ...

    def __init__(self, dependency: Optional[Dependency] = None, value: Union[int, Placeholder] = None, label: Optional[str] = None): ...

    @property
    def value(self) -> Union[int, Placeholder]: ...

    @value.setter
    def value(self, new_v: int): ...

    def unify(self, other: Union[int, Placeholder]): ...

    @property
    def _operator(self) -> Optional[PlaceholderOperator]: ...

    @property
    def _operands(self) -> List[Union[int, Placeholder]]: ...

    def __neg__(self) -> Union[int, Placeholder]: ...

    def __int__(self) -> int: ...

    def __add__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __radd__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __sub__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __rsub__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __mul__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __rmul__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __floordiv__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __rfloordiv__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __mod__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __rmod__(self, other: Union[int, Placeholder]) -> Union[int, Placeholder]: ...

    def __eq__(self, other: Union[int, Placeholder]) -> bool: ...

    def __ne__(self, other: Union[int, Placeholder]) -> bool: ...

    def __gt__(self, other: Union[int, Placeholder]) -> bool: ...

    def __lt__(self, other: Union[int, Placeholder]) -> bool: ...

    def __ge__(self, other: Union[int, Placeholder]) -> bool: ...

    def __le__(self, other: Union[int, Placeholder]) -> bool: ...

    def __repr__(self) -> str: ...

    def __hash__(self) -> str: ...

    def dump(self) -> str: ...

    def _to_serializable_(self) -> JSONSerializable: ...

    def get_depend_placeholders(self) -> Set[Placeholder]: ...

    def generate_js_function(self, flag_semicolon=True) -> str: ...
