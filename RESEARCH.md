# User brief and comparison

## Intended user and painful task

Python-only build support engineers inspecting saved generated stack positions. A raw flat map is difficult to read; the engineer needs an original label/position without Node, WASM initialization, a browser, or a hosted error service.

Current alternatives: Mozilla source-map consumer, trace-mapping, source-map visualization and source-map-explorer.

Evidence and limits: Mozilla issue 530 reports a WASM build failure; pure-JS trace-mapping is already an alternative. Python-only offline demand is inferred; this is a smaller strict subset, not a replacement. No fabricated customers, requests, adoption, testimonials or growth promise.

## Smallest useful capability and acceptance criteria

Resolve generated one-based line/zero-based UTF-16 column to greatest-lower-bound original segment on that line; reject invalid VLQ and references; never fetch source URLs.

Runnable acceptance fixtures are `test_sourcemap_trace.py` and `demo.py`. Invalid inputs must return an explicit failure, and diagnostics must preserve source files where the contract is read-only. See README for supported subsets and bounds. Plausible discovery path: source-map and debugging topics; original synthetic two-segment map example.

## Live leader research on 5 October 2026

Queries `source map`; `source-map in:name` were requested from live GitHub sorted by stars descending. Search receipts include exact query URLs, observation times and top-ten metadata in [research-evidence.json](research-evidence.json). Irrelevant broad matches were rejected: map fonts/geospatial tools are not JavaScript source-map comparables, browser redirect extensions are not site migration analysis, and unrelated notebook/diffusion matches are not notebook hygiene tools.

Highest-star relevant comparable found among the researched set: [danvk/source-map-explorer](https://github.com/danvk/source-map-explorer) with 3931 stars. Some established comparables were added outside the narrow search query. This is bounded search coverage, not an exhaustive global ranking. Stars are a discovery signal, not a performance/reliability result.

| Comparable | Stars | Last observed push UTC | License metadata | Workflow, install, docs and tradeoff |
| --- | ---: | --- | --- | --- |
| [mozilla/source-map](https://github.com/mozilla/source-map) | 3724 | 2026-09-09T01:00:35Z | unresolved metadata; inspect license before reuse | Node source-map generation/consumption, documented npm install and originalPositionFor examples; some consumer workflows use WASM. Broader functionality; issue 530 is build evidence only. |
| [jridgewell/trace-mapping](https://github.com/jridgewell/trace-mapping) | 110 | 2025-06-28T21:25:07Z | MIT | Pure-JS original/generated position tracing without WASM. README says development moved to jridgewell/sourcemaps; latest monorepo also inspected. This MVP offers Python packaging and a smaller strict subset. |
| [evanw/source-map-visualization](https://github.com/evanw/source-map-visualization) | 597 | 2024-07-09T15:01:37Z | unavailable | Browser map visualization and linked demo. Different UI workflow; repository license metadata is unavailable, so no reuse is made. |
| [danvk/source-map-explorer](https://github.com/danvk/source-map-explorer) | 3931 | 2023-03-14T16:39:24Z | Apache-2.0 | Node source-map bundle composition/size analysis with documented CLI. Last observed push 2023; does not establish abandonment or current support quality. |

Current READMEs and the returned recent issue/PR samples were inspected. Samples may be maintainer PRs, not genuine user requests. Support channels and examples are visible; support responsiveness, actual installation reliability and time to first useful result of comparables were not measured. License metadata marked unresolved/unavailable is not a permission to reuse. No competitor code or prose is incorporated.

## Distinctness and rejected directions

Compared with all 133 owned repository names, descriptions/READMEs for overlapping tools and yesterday's five launch briefs. The five new products handle saved notebook state, planned redirect graphs, exported LFS bytes, content-bound JSONL record references, and generated-code source positions respectively. They share packaging, not one subdivided product.

Existing json-differ/log-parser/traceweave analyze different JSON or agent-trace semantics; urlnorm normalizes URLs; syncplan plans filesystem synchronization; wheel-sentinel validates Python wheel archives; portable-tree audits names. This candidate's user contract is separate. Environment checking was rejected because envdiff/env-vault/dotenv-mini already cover it; another archive checker was rejected as overlapping Wheel Sentinel.

## Fairness and limitations

Flat v3 maps only, no indexed sections, map composition, sourceRoot resolution or code snippets. Returned source labels are raw map entries, not fetched/resolved files. No precision interpolation inside a mapping span. Duplicate generated columns rejected. 10 MB JSON / 5 million mapping characters. Linux tested; no telemetry or runtime dependencies.

There is no measured competitor benchmark or superiority claim. Local examples establish our behavior only. No claim is made that a competitor lacks this capability. Broader established tools can be better choices when their workflow/dependencies fit. Evidence dates, installed behavior and untested limits remain separate.
