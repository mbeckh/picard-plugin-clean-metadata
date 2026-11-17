# Clean Metadata
![Latest Version](https://img.shields.io/github/v/tag/mbeckh/picard-plugin-clean-metadata?sort=semver&filter=v*&style=flat-square&label=latest)
![Supports](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmbeckh%2Fpicard-plugin-clean-metadata%2Frefs%2Fheads%2Fmain%2F.works_with.yml&query=%24.picard.from&prefix=picard+%3E%3D&style=flat-square&label=supports&color=orange)
![Tested with](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmbeckh%2Fpicard-plugin-clean-metadata%2Frefs%2Fheads%2Fmain%2F.works_with.yml&query=%24.picard.latest&prefix=picard+%3C%3D&style=flat-square&label=tested+with&color=green)

A plugin for [MusicBrainz Picard](https://picard.musicbrainz.org) to explicitly delete all unset metadata (else tagging script sees old values from file).

## What it Does

The plugin runs as a track metadata processor and explicitly deletes all metadata not present in the new metadata.

This addresses the issue reported in [PICARD-1993](https://tickets.metabrainz.org/browse/PICARD-1993) related to $copymerge.

A tag is only deleted if:
* The setting to clear existing tags is enabled.
* The value is actually stored as a tag.
* The tag is not calculated.
* The tag is not configured as a preserved tag.
* The tag is not from a plugin.
* The tag is not configured as preserved in the options of this plugin.

## License

The code is released under the Apache License Version 2.0. Please see [LICENSE](LICENSE) for details and [NOTICE](NOTICE) for the required information when using picard-plugin-clean-metadata in your own work.
