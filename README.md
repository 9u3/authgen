# authgen
A random string gen for Python.

# Install

`pip install git+https://github.com/DemonEclipSe/authgen/`

# Usage.

Modules you'll need: `pip install random` and `pip install string`.

For `authg.multiple_simple/medium/strong`, You will need `amount` As it puts it in a table and returns it.

```python
from authgen import Generator

authg = Generator

print(authg.random_simple(length=8))
print(authg.multiple_simple(length=8, amount=15))
```

You can change `authg` to anything you want, I just used it for simplicity reasons.

# All types for strings.

`authg.random_simple`
`authg.random_medium`
`authg.random_strong`
`authg.multiple_simple`
`authg.multiple_medium`
`authg.multiple_strong`
