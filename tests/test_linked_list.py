# tests/test_linked_list.py
# Pruebas base escritas por el docente.
# CADA EQUIPO agregará sus propias pruebas en este archivo
# desde su rama — esto generará merge conflicts intencionales.

import pytest
from src.linked_list import LinkedList, Node


# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                             #
# ------------------------------------------------------------------ #

def test_lista_vacia_str():
    ll = LinkedList()
    assert str(ll) == "Lista vacía"


def test_lista_vacia_len():
    ll = LinkedList()
    assert len(ll) == 0


def test_node_repr():
    n = Node(42)
    assert repr(n) == "Node(42)"
    assert repr(n) == "Node(42)"




# ------------------------------------------------------------------ #
# Pruebas Equipo A — append                                           #
# ------------------------------------------------------------------ #

def test_append_un_elemento():
    ll = LinkedList()
    ll.append(10)
    assert ll.head is not None
    assert ll.head.data == 10
    assert len(ll) == 1


def test_append_varios_elementos():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert str(ll) == "1 -> 2 -> 3"
    assert len(ll) == 3
    
def test_delete_unico_elemento():
    """Eliminar el único nodo deja la lista vacía."""
    ll = LinkedList()
    ll.append(42)
    resultado = ll.delete(42)
    assert resultado is True
    assert ll.head is None

def test_delete_ultimo_elemento():
    """Eliminar el nodo al final ajusta el next del penúltimo a None."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    resultado = ll.delete(3)
    assert resultado is True
    assert str(ll) == "1 -> 2"


def test_append_orden_preservado():
    ll = LinkedList()
    for v in [5, 10, 15]:
        ll.append(v)
    current = ll.head
    for expected in [5, 10, 15]:
        assert current.data == expected
        current = current.next

def test_delete_preserva_restantes():
    """Eliminar un nodo del medio no altera los demás nodos."""
    ll = LinkedList()
    for val in [10, 20, 30, 40]:
        ll.append(val)
    ll.delete(20)
    assert str(ll) == "10 -> 30 -> 40"
    assert len(ll) == 3


# ------------------------------------------------------------------ #
# Pruebas Equipo C — search                                           #
# ------------------------------------------------------------------ #

def test_search_elemento_existente():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    nodo = ll.search(10)
    assert nodo is not None
    assert nodo.data == 10


def test_search_elemento_inexistente():
    ll = LinkedList()
    ll.append(5)
    assert ll.search(99) is None


def test_search_lista_vacia():
    ll = LinkedList()
    assert ll.search(1) is None


def test_search_ultimo_elemento():
    ll = LinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    nodo = ll.search(3)
    assert nodo is not None
    assert nodo.data == 3

