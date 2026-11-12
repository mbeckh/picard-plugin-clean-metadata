# REALLY delete all unset metadata (else tagging script sees old values from file).
#
# Copyright 2023-2026 Michael Beckh (mbeckh)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import ClassVar, override

from picard.const.tags import ALL_TAGS
from picard.plugin3.api import (
    Metadata,
    OptionsPage,
    PageOptionConfigs,
    PluginApi,
    Track,
    t_,
)
from picard.tags import TagVar

from .forms.ui_options import Ui_CleanMetadataOptionsPage


def delete_absent_metadata(
    api: PluginApi, track: Track, metadata: Metadata, track_node: dict, release_node: dict | None = None
):
    """REALLY delete all unset metadata (else tagging script sees old values from file)."""

    def tags_to_update(tv: TagVar) -> bool:
        if not tv.is_tag:
            return False
        if tv.name in preserved_tags:
            return False
        if tv.is_calculated:
            return False
        if tv.is_preserved:
            return False
        if tv.plugin_id:
            return False
        if tv.is_hidden and not tv.name.startswith('~id3:'):
            return False
        return True

    setting = api.global_config.setting
    plugin_config = api.plugin_config

    clear_existing_tags = setting['clear_existing_tags']
    if not clear_existing_tags:
        return

    preserved_tags = set(setting['preserved_tags']) | set(plugin_config['preserved_tags'])

    for name in ALL_TAGS.names(tags_to_update):
        if name not in metadata:
            metadata.delete(name)


class CleanMetadataOptionsPage(OptionsPage):
    """Plugin Options."""

    NAME = 'clean_metadata'
    TITLE = t_('ui.clean_metadata.title', "Clean Metadata")
    PARENT = 'plugins'

    OPTIONS: ClassVar[PageOptionConfigs] = {
        'preserved_tags': {'widgets': ['preserved_tags']},
    }

    @override
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CleanMetadataOptionsPage()
        self.ui.setupUi(self)

    @override
    def load(self):
        setting = self.api.global_config.setting
        plugin_config = self.api.plugin_config

        self.ui.preserved_tags.update(plugin_config['preserved_tags'])
        self.ui.preserved_tags.set_user_sortable(False)

        # only enabled if option to clean tags is set
        self.ui.preserved_tags.setEnabled(setting['clear_existing_tags'])

        # react to changes on other options page
        page = self.dialog.get_page('tags')
        page.ui.clear_existing_tags.toggled.connect(self.ui.preserved_tags.setEnabled)

    @override
    def save(self):
        plugin_config = self.api.plugin_config

        plugin_config['preserved_tags'] = list(self.ui.preserved_tags.tags)


def enable(api: PluginApi):
    """Enable plugin."""

    api.plugin_config.register_option(
        'preserved_tags',
        default=['encodingtime', 'taggingtime'],
        title=api.tr('options.preserved_tags', "Preserved tags"),
        in_profile=True,
    )

    # run after all other processors have updated the metadata
    api.register_track_metadata_processor(delete_absent_metadata, -100)
    api.register_options_page(CleanMetadataOptionsPage)


def disable():
    """Disable plugin."""

    pass
