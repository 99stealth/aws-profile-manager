# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.2](https://github.com/99stealth/aws-profile-switcher/tree/v0.0.2) - 2020-03-30
### Fixed
- Issue that appears when backup for `default` is present in `~/.aws/credentials`

## [0.0.1](https://github.com/99stealth/aws-profile-switcher/tree/v0.0.1) - 2020-03-30
### Added
- Function that allows to find users home and credentials file into it
- Find default profile and backup it if there is no duplication
- Write changes to `~/.aws/credentials` file