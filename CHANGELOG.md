# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-09-12

### Added

- Added `evaluate()` for checking conditions against data, returning whether the check passed and, if not, a list of reasons why (e.g. `"Ball completion < 70"`).
- Added `QueryRule` and `QueryGroup` types.
- Added tests.

## [1.0.1] - 2026-09-12

### Changed

- Lowered Python version requirement to >=3.13.

### Removed

- Removed `test.py` file.

## [1.0.0] - 2026-09-12

- Initial release.
