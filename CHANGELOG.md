# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.6](https://github.com/99stealth/aws-profile-switcher/tree/v0.0.6) - 2020-05-12
### Fixed
- Floating default. Now the default profile is statically in the first place
### Removed
- Lazy function `check_default_exists`

## [0.0.5](https://github.com/99stealth/aws-profile-switcher/tree/v0.0.5) - 2020-05-09
### Added
- Static types for those functions where it was possible
### Removed
- Lazy function `new_profile_name_is_among_all_proiles`

## [0.0.4](https://github.com/99stealth/aws-profile-switcher/tree/v0.0.4) - 2020-04-04
### Fixed
- https://github.com/99stealth/aws-profile-switcher/issues/1

## [0.0.3](https://github.com/99stealth/aws-profile-switcher/tree/v0.0.3) - 2020-03-31
### Added
- Function that sets up the logging
- Output that shows current default if it is duplicated in `~/.aws/credentials`


## [0.0.2](https://github.com/99stealth/aws-profile-switcher/tree/v0.0.2) - 2020-03-30
### Fixed
- Issue that appears when backup for `default` is present in `~/.aws/credentials`

## [0.0.1](https://github.com/99stealth/aws-profile-switcher/tree/v0.0.1) - 2020-03-30
### Added
- Function that allows to find users home and credentials file into it
- Find default profile and backup it if there is no duplication
- Write changes to `~/.aws/credentials` file