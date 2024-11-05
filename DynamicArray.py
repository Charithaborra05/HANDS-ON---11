class ResizableArray:
    def __init__(self):
        self.count = 0               # Number of elements currently in the array
        self.capacity = 1            # Starting capacity of the array
        self.storage = self._initialize_array(self.capacity)

    def _initialize_array(self, capacity):
        """Creates a new array with the specified capacity."""
        return [None] * capacity

    def _resize(self, new_capacity):
        """Resizes the internal array to the new capacity (either expanding or shrinking)."""
        new_storage = self._initialize_array(new_capacity)
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage
        self.capacity = new_capacity

    def add(self, element):
        """Appends an element to the end of the array, resizing if necessary."""
        if self.count == self.capacity:
            # Double the array size when it reaches full capacity
            self._resize(2 * self.capacity)
        self.storage[self.count] = element
        self.count += 1

    def get(self, index):
        """Fetches the element at the given index."""
        if 0 <= index < self.count:
            return self.storage[index]
        raise IndexError("Index out of range")

    def update(self, index, element):
        """Updates the element at the specified index."""
        if 0 <= index < self.count:
            self.storage[index] = element
        else:
            raise IndexError("Index out of range")

    def delete_last(self):
        """Removes the last element in the array and shrinks if necessary."""
        if self.count == 0:
            raise IndexError("Cannot delete from an empty array")

        self.count -= 1
        
        # Shrink the array if count is one-fourth of the capacity
        if self.count <= self.capacity // 4 and self.capacity > 1:
            new_capacity = max(self.capacity // 2, 1)
            self._resize(new_capacity)

    def __str__(self):
        """Returns a string representation of the array elements."""
        return f"[{', '.join(map(str, self.storage[:self.count]))}]"

# Test cases
if __name__ == "__main__":
    # Initialize array
    resizable_array = ResizableArray()
    print("Initial array:", resizable_array)

    # Add elements
    resizable_array.add(10)
    resizable_array.add(20)
    resizable_array.add(30)
    print("Array after adding 10, 20, 30:", resizable_array)

    # Access elements
    print("Element at index 0:", resizable_array.get(0))
    print("Element at index 1:", resizable_array.get(1))
    print("Element at index 2:", resizable_array.get(2))

    # Update elements
    resizable_array.update(1, 50)
    print("Array after updating index 1 to 50:", resizable_array)

    # Add more elements to trigger resizing
    resizable_array.add(40)
    resizable_array.add(50)
    print("Array after adding 40, 50:", resizable_array)

    # Delete elements
    resizable_array.delete_last()
    print("Array after deleting the last element:", resizable_array)
    resizable_array.delete_last()
    print("Array after deleting another element:", resizable_array)

    # Final state of the array
    print("Final array:", resizable_array)
