import pytest
from command_factory import CommandObjectFactory

def function_a():
    return "a"

def function_b():
    return "b"

class DummyCommandMakers:
    def handle_a(self, args):
        return function_a

    def handle_b(self, args):
        return function_b
    
    command_list =  {
        "a" : handle_a,
        "b"  : handle_b
    }

def test_factory():
    cof = CommandObjectFactory(DummyCommandMakers().command_list)
    f = cof.command_parser("a")
    assert(f == function_a)
    f = cof.command_parser("")
    assert f is None
    with pytest.raises(KeyError):
        f = cof.command_parser("c")
    f = cof.command_parser("b")
    assert f==function_b