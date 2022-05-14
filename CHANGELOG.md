# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0](https://github.com/99stealth/aws-profile-manager/tree/v0.4.0) - 2022-05-15
### Added
- Functionality that allows to rotate aws access keys
- `--verson` and `--quiet` root options
- CLI confirmation to `remove-profile` command
### Changed
- Function `choose_profile_to_remove` to `choose_profile` in `profile-remove` command
### Removed
- `profile_remove` module because of moving all its functionality to the `common` module

## [0.3.4](https://github.com/99stealth/aws-profile-manager/tree/v0.3.4) - 2021-01-10
### Added
- Functionality which allows to remove profiles

## [0.3.3](https://github.com/99stealth/aws-profile-manager/tree/v0.3.3) - 2020-11-22
### Fixed
- Commands directory structure

## [0.3.2](https://github.com/99stealth/aws-profile-manager/tree/v0.3.2) - 2020-11-22
### Fixed
- Entrypoint
## [0.3.0](https://github.com/99stealth/aws-profile-manager/tree/v0.3.0) - 2020-11-22
### Added
- Functionality which allows to add profiles
- More unit tests :D
### Changed
- Utilitie's name. Was `aws-profile-switcher` become `aws-profile-manager`

## [0.2.3](https://github.com/99stealth/aws-profile-manager/tree/v0.2.3) - 2020-08-08
### Fixed
- System exit when user press Ctrl+c
- System exit when user press Ctrl+d
- Improved Dockerfile

## [0.2.2](https://github.com/99stealth/aws-profile-manager/tree/v0.2.2) - 2020-08-07
### Fixed
- System exit when user press Ctrl+c

## [0.2.1](https://github.com/99stealth/aws-profile-manager/tree/v0.2.1) - 2020-07-31
### Fixed
- Answer validation for choose_new_default function

## [0.2.0](https://github.com/99stealth/aws-profile-manager/tree/v0.2.0) - 2020-07-29
### Added
- Unittesting base and several simple unittests
- First smoke test
### Changed
- Single module has been split for two different classes Common and Switch

## [0.1.0](https://github.com/99stealth/aws-profile-manager/tree/v0.1.0) - 2020-07-08
### Added
- Initial option that shows version

## [0.0.6](https://github.com/99stealth/aws-profile-manager/tree/v0.0.6) - 2020-05-12
### Fixed
- Floating default. Now the default profile is statically in the first place
### Removed
- Lazy function `check_default_exists`

## [0.0.5](https://github.com/99stealth/aws-profile-manager/tree/v0.0.5) - 2020-05-09
### Added
- Static types for those functions where it was possible
### Removed
- Lazy function `new_profile_name_is_among_all_proiles`

## [0.0.4](https://github.com/99stealth/aws-profile-manager/tree/v0.0.4) - 2020-04-04
### Fixed
- https://github.com/99stealth/aws-profile-manager/issues/1

## [0.0.3](https://github.com/99stealth/aws-profile-manager/tree/v0.0.3) - 2020-03-31
### Added
- Function that sets up the logging
- Output that shows current default if it is duplicated in `~/.aws/credentials`


## [0.0.2](https://github.com/99stealth/aws-profile-manager/tree/v0.0.2) - 2020-03-30
### Fixed
- Issue that appears when backup for `default` is present in `~/.aws/credentials`

## [0.0.1](https://github.com/99stealth/aws-profile-manager/tree/v0.0.1) - 2020-03-30
### Added
- Function that allows to find users home and credentials file into it
- Find default profile and backup it if there is no duplication
- Write changes to `~/.aws/credentials` file