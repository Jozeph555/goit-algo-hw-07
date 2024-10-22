"""
Модуль для реалізації AVL-дерева.

Цей модуль містить реалізацію AVL-дерева з усіма необхідними 
методами для підтримки балансу, вставки та видалення вузлів.
"""


from typing import Optional, Union


class AVLNode:
    """
    Клас, що представляє вузол AVL-дерева.

    Attributes:
        key: Значення вузла
        height: Висота піддерева з коренем у цьому вузлі
        left: Лівий нащадок
        right: Правий нащадок
    """
    def __init__(self, key: int) -> None:
        """
        Ініціалізація вузла AVL-дерева.

        Args:
            key (int): Значення для збереження у вузлі
        """
        self.key = key
        self.height = 1
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None

    def __str__(self, level: int = 0, prefix: str = "Root: ") -> str:
       """
       Створює рядкове представлення дерева з поточного вузла.
       
       Метод рекурсивно обходить дерево та формує його текстове представлення,
       використовуючи відступи для показу ієрархії вузлів.

       Args:
           level (int, optional): Рівень вкладеності для відступів. За замовчуванням 0.
           prefix (str, optional): Префікс для позначення типу вузла. За замовчуванням "Root: ".

       Returns:
           str: Рядкове представлення дерева.
       
       Example:
           Root: 5
           L--- 3
           R--- 7
               L--- 6
               R--- 8
       """
       # Створюємо рядок для поточного вузла з відповідним відступом
       ret = "\t" * level + prefix + str(self.key) + "\n"
       
       # Рекурсивно додаємо рядкове представлення лівого піддерева
       if self.left:
           ret += self.left.__str__(level + 1, "L--- ")
           
       # Рекурсивно додаємо рядкове представлення правого піддерева
       if self.right:
           ret += self.right.__str__(level + 1, "R--- ")
           
       return ret


def get_height(node: Optional[AVLNode]) -> int:
    """
    Отримує висоту піддерева.

    Args:
        node: Вузол, висоту піддерева якого потрібно отримати

    Returns:
        int: Висота піддерева
    """
    if not node:
        return 0
    return node.height


def get_balance(node: Optional[AVLNode]) -> int:
    """
    Обчислює баланс вузла.

    Args:
        node: Вузол, баланс якого потрібно обчислити

    Returns:
        int: Значення балансу вузла
    """
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z: AVLNode) -> AVLNode:
    """
    Виконує лівий поворот навколо вузла.

    Args:
        z: Вузол, навколо якого виконується поворот

    Returns:
        AVLNode: Новий корінь піддерева після повороту
    """
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y: AVLNode) -> AVLNode:
    """
    Виконує правий поворот навколо вузла.

    Args:
        y: Вузол, навколо якого виконується поворот

    Returns:
        AVLNode: Новий корінь піддерева після повороту
    """
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def min_value_node(node: AVLNode) -> AVLNode:
    """
    Знаходить вузол з мінімальним значенням у піддереві.

    Args:
        node: Корінь піддерева

    Returns:
        AVLNode: Вузол з мінімальним значенням
    """
    current = node
    while current.left:
        current = current.left
    return current


def insert(root: Optional[AVLNode], key: int) -> AVLNode:
    """
    Вставляє новий ключ в AVL-дерево.

    Args:
        root: Корінь дерева
        key: Значення для вставки

    Returns:
        AVLNode: Новий корінь дерева після вставки
    """
    # Стандартна вставка в BST
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    # Оновлення висоти
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Отримання балансу
    balance = get_balance(root)

    # Випадки балансування
    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def delete_node(root: Optional[AVLNode], key: int) -> Optional[AVLNode]:
    """
    Видаляє вузол з заданим ключем з AVL-дерева.

    Args:
        root: Корінь дерева
        key: Значення для видалення

    Returns:
        Optional[AVLNode]: Новий корінь дерева після видалення
    """
    # Стандартне видалення з BST
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    # Оновлення висоти
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Отримання балансу
    balance = get_balance(root)

    # Випадки балансування
    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root
