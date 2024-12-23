# Common Array Methods in Python

1. `append(x)`

   - Adds an item `x` to the end of the array.

   ```python
   arr.append(x)
   ```

2. `extend(iterable)`

   - Extends the array by appending elements from the iterable.

   ```python
   arr.extend([1, 2, 3])
   ```

3. `insert(i, x)`

   - Inserts an item `x` at a given position `i`.

   ```python
   arr.insert(1, x)
   ```

4. `remove(x)`

   - Removes the first occurrence of an item `x`.

   ```python
   arr.remove(x)
   ```

5. `pop([i])`

   - Removes and returns the item at the given position `i`. If no index is specified, removes and returns the last item.

   ```python
   arr.pop()
   arr.pop(1)
   ```

6. `clear()`

   - Removes all items from the array.

   ```python
   arr.clear()
   ```

7. `index(x[, start[, end]])`

   - Returns the index of the first occurrence of an item `x`. Raises a `ValueError` if the item is not found.

   ```python
   arr.index(x)
   ```

8. `count(x)`

   - Returns the number of occurrences of an item `x`.

   ```python
   arr.count(x)
   ```

9. `sort(key=None, reverse=False)`

   - Sorts the items of the array in place.

   ```python
   arr.sort()
   ```

10. `reverse()`

    - Reverses the elements of the array in place.

    ```python
    arr.reverse()
    ```

11. `copy()`
    - Returns a shallow copy of the array.
    ```python
    arr.copy()
    ```
