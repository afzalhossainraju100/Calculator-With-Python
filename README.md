# Simple Python Calculator

This is a small interactive CLI calculator implemented in `Calculator.py`.

Features:

- Safe arithmetic expression evaluation using Python AST
- Supports `+ - * / // % **` and unary plus/minus
- A few math functions: `sqrt`, `sin`, `cos`, `tan`, `log`, `log10`, `exp`, `abs`, `round`
- Constants: `pi`, `e`
- `history` command in interactive mode

Usage:

Evaluate expression from command line:

```bash
python Calculator.py "2 + 3 * 4"
```

Start interactive mode:

```bash
python Calculator.py
```

In interactive mode examples:

> `2+2`

> `sqrt(2)`

> `history` (shows previous expressions)

Type `help` for available functions, or `quit`/`exit` to leave.
