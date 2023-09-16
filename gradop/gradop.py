class Tensor:
    def __init__(self, value, _child=()):
        self.value = value
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_child)

    def __add__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.value + other.value, (self, other))

        def _backward():
            # Gradient calculation for addition
            self.grad += 1 * out.grad  # Gradient with respect to self
            other.grad += 1 * out.grad  # Gradient with respect to other

        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.value * other.value, (self, other))

        def _backward():
            # Gradient calculation for multiplication
            self.grad += other.value * out.grad  # Gradient with respect to self
            other.grad += self.value * out.grad  # Gradient with respect to other

        out._backward = _backward
        return out

    def __truediv__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.value / other.value, (self, other))

        def _backward():
            # Gradient calculation for division
            self.grad += (1 / other.value) * out.grad  # Gradient with respect to self
            other.grad += (-self.value / (other.value ** 2)) * out.grad  # Gradient with respect to other

        out._backward = _backward
        return out

    def __sub__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.value - other.value, (self, other))

        def _backward():
            # Gradient calculation for subtraction
            self.grad += 1 * out.grad  # Gradient with respect to self
            other.grad += -1 * out.grad  # Gradient with respect to other

        out._backward = _backward
        return out

    def backward(self):
        visited = set()
        order_lst = []

        def DFS(node):
            if node not in visited:
                visited.add(node)
                for children in node._prev:
                    DFS(children)
                order_lst.append(node)

        DFS(self)
        self.grad = 1
        for i in reversed(order_lst):
            i._backward()

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        # Handling for right division
        return Tensor(other) / self

    def __rsub__(self, other):
        # Handling for right subtraction
        return (self - other) * (-1)

    def __repr__(self) -> str:
        return f"Tensor(value={self.value}, grad={self.grad})"
