def scalar_product(v, w):
    """Compute the scalar (dot) product of two vectors."""
    return sum(a * b for a, b in zip(v, w))

n = int(input("Enter the number of components: "))


while True:
    v_input = input(f"Enter {n} components for vector v separated by space: ").split()
    if len(v_input) == n:
        v = tuple(map(float, v_input))
        break
    else:
        print(f"You must enter exactly {n} numbers. Try again.")

while True:
    w_input = input(f"Enter {n} components for vector w separated by space: ").split()
    if len(w_input) == n:
        w = tuple(map(float, w_input))
        break
    else:
        print(f"You must enter exactly {n} numbers. Try again.")

result = scalar_product(v, w)

min_v, max_v = min(v), max(v)
min_w, max_w = min(w), max(w)

print("\nResults:")
print(f"v = {v}")
print(f"w = {w}")
print(f"Scalar product = {result}")
print(f"v: min={min_v} (position {v.index(min_v)}), max={max_v} (position {v.index(max_v)})")
print(f"w: min={min_w} (position {w.index(min_w)}), max={max_w} (position {w.index(max_w)})")
