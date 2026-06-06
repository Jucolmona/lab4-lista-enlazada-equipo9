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

def test_delete_preserva_restantes():
    """Eliminar un nodo del medio no altera los demás nodos."""
    ll = LinkedList()
    for val in [10, 20, 30, 40]:
        ll.append(val)
    ll.delete(20)
    assert str(ll) == "10 -> 30 -> 40"
    assert len(ll) == 3