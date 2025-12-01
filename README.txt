# PseudoRandom

PseudoRandom is a lightweight, dependency-free pseudo-random generator built using Python object allocations, memory addresses (`id()`), and simple mixing logic.  
While not a cryptographic RNG, in practice it produces output that is sufficiently unpredictable for casual, non-security tasks.

This implementation exists as a small experiment showing how randomness can be constructed from Python internals without relying on `random` or any external libraries.

## Features
- Callable generator returning float values
- Integer generation (`randint`, `randrange`)
- Sequence utilities (`choice`, `shuffle`)
- Uses object allocations + hashed memory addresses as entropy
- Behavior appears random enough for everyday non-critical use

## Notes
- **Not cryptographically secure**; do not use for security-critical systems
- Output depends on Python’s runtime and memory layout
- `stored_objects` grows intentionally to accumulate entropy
- Non-deterministic across program runs

## Example Usage

```python
from pseudorandom import PseudoRandom

rng = PseudoRandom()

print(rng())                   # float random-ish number
print(rng.randint(1, 100))     # bounded integer
print(rng.choice(["apple", "banana", "cherry"]))

shuffled = rng.shuffle("abcde")
print("".join(shuffled))
```

## Purpose

PseudoRandom is meant as a practical demonstration of how to construct a basic pseudo-random generator from scratch.  
It provides “random enough” output for lightweight use cases while remaining simple, transparent, and easy to experiment with.

## License

MIT License with attribution requirement.  
Please credit **charitables** when modifying or redistributing this code.
