# authgen
A random string gen for Python.

# Install

`pip install git+https://github.com/DemonEclipSe/authgen/`

# Usage.

`amount` is now optional. If you don't qadd an amount, It will set to 15.

```python
from authgen import Generator

authg = Generator

print(authg.random_simple(length=8))
print(authg.multiple_simple(length=8, amount=15))
```

You can change `authg` to anything you want, I just used it for simplicity reasons.

# All types for strings.

| Methods       | What they do  |
| ------------- |:-------------:|
| `authg.random_simple`      | Simple Generation |
| `authg.random_medium`      | Medium Generation     |
| `authg.random_strong` | Strong Generation      |
| `authg.multiple_simple`| Same as simple but does more |
| `authg.multiple_medium`| Same as medium but does more |
| `authg.multiple_strong`| Same as strong but does more |
