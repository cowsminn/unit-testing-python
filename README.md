# Unit-testing-py

## Overview

## Core Technologies

| Category | Technology | Package/Module | Purpose |
|---|---|---|---|
| **Testing Framework** | Pytest | `pytest` | For writing and running tests. |
| **Code Coverage** | Pytest-Cov | `pytest-cov` | To measure code coverage during tests. |
| **Mutation Testing** | Mut-mut | `mutmut` | To test the quality of tests by introducing mutations. |
| **Mutation Testing** | Mutpy | `mutpy-pynguin` | Automated test generation and mutation testing. |

### Python Dependencies

```bash
pip install -r requirements.txt
```

### Usage

To run the tests, use `pytest`:

```bash
pytest
```

To run mutation testing with `mutmut`:

```bash
mutmut run
```

To see the results of the mutation testing:

```bash
mutmut results
```

You can also run `mut.py` which is a wrapper around `mutmut`:
```bash
mut.py --target src --unit-test tests --runner pytest
```

## Execution Screenshots

![1](img/2.png)
![2](img/3.png)
![3](img/4.png)

## Execution Flow
![exec](img/execution.png)


## Video Demonstration

[![demo](https://img.youtube.com/vi/eUc5V2GvTuY/0.jpg)](https://youtu.be/eUc5V2GvTuY)

## Limitations

1. **Database Support**: Currently limited to SQLite (Spider2-Lite subset)
2. **Query Complexity**: Performance degrades on highly complex nested queries
3. **Schema Size**: Large schemas may exceed context window limits
4. **API Dependencies**: Cloud models require stable internet and API keys

## Resources

- [BDNSV](https://github.com/iuliabanu/BDNSV)
- [Spider2](https://github.com/xlang-ai/Spider2)
- [Netflix_db](https://github.com/lerocha/netflixdb)
- [Pandas vs Polars](https://blog.jetbrains.com/pycharm/2024/07/polars-vs-pandas/)
- [Diagrams](https://www.plantuml.com)