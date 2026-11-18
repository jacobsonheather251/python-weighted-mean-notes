# Calculate a weighted mean: implementation

## What the example does

Values and weights must have equal length. Weights must be nonnegative and their sum positive; otherwise a weighted mean is undefined.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "values": [
    10,
    20
  ],
  "weights": [
    1,
    3
  ]
}
```

Expected result:

```json
17.5
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
