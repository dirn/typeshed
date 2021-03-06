from typing import Any, Optional

def release_local(local): ...

class Local:
    def __init__(self): ...
    def __iter__(self): ...
    def __call__(self, proxy): ...
    def __release_local__(self): ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def __delattr__(self, name): ...

class LocalStack:
    def __init__(self): ...
    def __release_local__(self): ...
    def _get__ident_func__(self): ...
    def _set__ident_func__(self, value): ...
    __ident_func__ = ...  # type: Any
    def __call__(self): ...
    def push(self, obj): ...
    def pop(self): ...
    @property
    def top(self): ...

class LocalManager:
    locals = ...  # type: Any
    ident_func = ...  # type: Any
    def __init__(self, locals: Optional[Any] = ..., ident_func: Optional[Any] = ...): ...
    def get_ident(self): ...
    def cleanup(self): ...
    def make_middleware(self, app): ...
    def middleware(self, func): ...

class LocalProxy:
    def __init__(self, local, name: Optional[Any] = ...): ...
    @property
    def __dict__(self): ...
    def __bool__(self): ...
    def __unicode__(self): ...
    def __dir__(self): ...
    def __getattr__(self, name): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    __getslice__ = ...  # type: Any
    def __setslice__(self, i, j, seq): ...
    def __delslice__(self, i, j): ...
    __setattr__ = ...  # type: Any
    __delattr__ = ...  # type: Any
    __lt__ = ...  # type: Any
    __le__ = ...  # type: Any
    __eq__ = ...  # type: Any
    __ne__ = ...  # type: Any
    __gt__ = ...  # type: Any
    __ge__ = ...  # type: Any
    __cmp__ = ...  # type: Any
    __hash__ = ...  # type: Any
    __call__ = ...  # type: Any
    __len__ = ...  # type: Any
    __getitem__ = ...  # type: Any
    __iter__ = ...  # type: Any
    __contains__ = ...  # type: Any
    __add__ = ...  # type: Any
    __sub__ = ...  # type: Any
    __mul__ = ...  # type: Any
    __floordiv__ = ...  # type: Any
    __mod__ = ...  # type: Any
    __divmod__ = ...  # type: Any
    __pow__ = ...  # type: Any
    __lshift__ = ...  # type: Any
    __rshift__ = ...  # type: Any
    __and__ = ...  # type: Any
    __xor__ = ...  # type: Any
    __or__ = ...  # type: Any
    __div__ = ...  # type: Any
    __truediv__ = ...  # type: Any
    __neg__ = ...  # type: Any
    __pos__ = ...  # type: Any
    __abs__ = ...  # type: Any
    __invert__ = ...  # type: Any
    __complex__ = ...  # type: Any
    __int__ = ...  # type: Any
    __long__ = ...  # type: Any
    __float__ = ...  # type: Any
    __oct__ = ...  # type: Any
    __hex__ = ...  # type: Any
    __index__ = ...  # type: Any
    __coerce__ = ...  # type: Any
    __enter__ = ...  # type: Any
    __exit__ = ...  # type: Any
    __radd__ = ...  # type: Any
    __rsub__ = ...  # type: Any
    __rmul__ = ...  # type: Any
    __rdiv__ = ...  # type: Any
    __rtruediv__ = ...  # type: Any
    __rfloordiv__ = ...  # type: Any
    __rmod__ = ...  # type: Any
    __rdivmod__ = ...  # type: Any
    __copy__ = ...  # type: Any
    __deepcopy__ = ...  # type: Any
