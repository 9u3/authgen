# authgen
A random string gen for Python.

# Install

`pip install git+https://github.com/9u3/authgen/`

# Update

`pip install -U git+https://github.com/9u3/authgen/`

# Usage.

```python
from authgen import Generator as authg

print(authg.random_simple(length=8))
print(authg.multiple_simple(length=8, amount=15)) # Amount variable is optional, If you don't give it an amount it will return with 15.
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
