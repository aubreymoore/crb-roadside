## pytest

### Useful options

Run tests using
```
uv run pytest -s
```
An extensive list of CLI flags can be found [here](https://docs.pytest.org/en/stable/reference/reference.html#command-line-flags) in the pytest documentation

Useful flags are:
- `--last-failed, --lf`
- `--stepwise, --sw`
- `-v, --verbose`
- `-s`
- `-q, --quiet`
- `-k EXPRESSION`


### References
- [YouTube](https://www.youtube.com/watch?v=mzlH8lp4ISA)
- [How to re-run failed tests and maintain state between test runs](https://docs.pytest.org/en/stable/how-to/cache.html)



```
--last-failed, --lf
```
Rerun only the tests that failed at the last run. If no tests failed (or no cached data exists), all tests are run. See also cache_dir and How to re-run failed tests and maintain state between test runs.

\-v, \--verbose[¶](https://docs.pytest.org/en/stable/reference/reference.html#cmdoption-v "Link to this definition")

Increase verbosity. Can be specified multiple times (e.g., `-vv`) for even more verbose output.

See [Fine-grained verbosity](https://docs.pytest.org/en/stable/how-to/output.html#pytest-fine-grained-verbosity) for fine-grained control over verbosity.

\-q, \--quiet[¶](https://docs.pytest.org/en/stable/reference/reference.html#cmdoption-q "Link to this definition")

Decrease verbosity.

\--verbosity\=NUM[¶](https://docs.pytest.org/en/stable/reference/reference.html#cmdoption-verbosity "Link to this definition")

Set verbosity level explicitly. Default: 0.


## Sphinx
