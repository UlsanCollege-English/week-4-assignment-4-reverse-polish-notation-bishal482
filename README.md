[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PXVwFAme)
# HW4 — RPN Calculator (Stack)

## Story
You’re wiring a tiny embedded calculator with no parentheses and minimal CPU. Expressions come in **Reverse Polish Notation** (postfix), like `"2 1 + 3 *"` → `(2 + 1) * 3 = 9`.

## Task (Technical)
Implement `eval_rpn(tokens: list[str]) -> int` supporting `+ - * /` (integer division truncates toward zero) and integers (may be negative). Use a **stack**:
- push numbers
- on operator: pop `b`, pop `a`, push `a op b`

## Hints
1) Order matters: for `a - b` and `a / b`, `b` is the **second** pop.
2) Python integer division toward zero: use `int(a / b)` not `a // b`.
3) Minimal validation: assume the input is a valid RPN expression.

## Run tests locally
```bash
python -m pytest -q
```
## Submission

Push to GitHub Classroom

Commit → push → check Actions.

## Common problems
- Reversing a and b.

- Using // (floors negatives) instead of truncating toward zero.