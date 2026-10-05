# sourcemap-trace

Offline flat v3 source-map tracing with VLQ validation and unmapped-span handling.

## Install and first useful result

```bash
git clone https://github.com/nripankadas07/sourcemap-trace
cd sourcemap-trace
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/python demo.py
.venv/bin/sourcemap-trace --help
```

Python 3.10 or newer. The example creates synthetic inputs; it needs no account, service, token or downloaded dataset. Runtime uses only the standard library. Building requires setuptools from the package registry. POSIX commands above; Windows/macOS installation has not been tested.

## Useful contract

Resolve generated one-based line/zero-based UTF-16 column to greatest-lower-bound original segment on that line; reject invalid VLQ and references; never fetch source URLs.

Import `sourcemap_trace` for the function used by `demo.py`, or use the installed CLI described by `--help`. JSON reports print to stdout. Exit 0 means the documented success condition, 1 means diagnostic findings or an unmapped source position where applicable, and 2 means invalid input or I/O failure. JSONL indexing uses 0/2 only; LFS returns 2 when no pointers were found.

## Limits

Flat v3 maps only, no indexed sections, map composition, sourceRoot resolution or code snippets. Returned source labels are raw map entries, not fetched/resolved files. No precision interpolation inside a mapping span. Duplicate generated columns rejected. 10 MB JSON / 5 million mapping characters. Linux tested; no telemetry or runtime dependencies.

No performance or superiority claim. Demand is inferred. See [research and acceptance criteria](RESEARCH.md), [validation](VALIDATION.md) and [support and security](SUPPORT.md). MIT license; implementation and synthetic fixtures are original. Comparables inform scope; no competitor code or prose is incorporated.

## Development

```bash
python -m unittest -v
python -m compileall -q sourcemap_trace.py
python demo.py
```

## CLI input

`sourcemap-trace bundle.js.map 1 6` traces generated line 1, UTF-16 column 6. Lines are one based and columns zero based, matching the documented Mozilla consumer convention. The raw source label and original segment position are returned; sourceRoot is not resolved and URLs are never fetched. Flat map example: `{"version":3,"sources":["demo.js"],"names":[],"mappings":"AAAA,KACE"}`.
