# Clean Metadata

A plugin for [MusicBrainz Picard](https://picard.musicbrainz.org) to explicitly delete all unset metadata (else tagging script sees old values from file).

## What it Does

The plugin runs as a track metadata processor and explicitly deletes all metadata not present in the new metadata.

This addresses the issue reported in https://tickets.metabrainz.org/browse/PICARD-1993 related to $copymerge.

A tag is only deleted if:
* The setting to clear existing tags is enabled.
* The value is actually stored as a tag.
* The tag is not calculated.
* The tag is not configured as a preserved tag.
* The tag is not from a plugin.
* The tag is not configured as preserved in the options of this plugin.

## License

The code is released under the Apache License Version 2.0. Please see [LICENSE](LICENSE) for details and [NOTICE](NOTICE) for the required information when using picard-plugin-clean-metadata in your own work.
