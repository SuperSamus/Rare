from PyQt5.QtCore import QSize, QSettings, pyqtSignal
from PyQt5.QtWidgets import (
    QLineEdit,
    QLabel,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QComboBox,
)

from rare.shared import ApiResultsSingleton
from rare.utils.extra_widgets import SelectViewWidget
from rare.utils.utils import icon


class GameListHeadBar(QWidget):
    filterChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super(GameListHeadBar, self).__init__(parent=parent)
        self.api_results = ApiResultsSingleton()
        # self.installed_only = QCheckBox(self.tr("Installed only"))
        self.settings = QSettings()
        # self.installed_only.setChecked(self.settings.value("installed_only", False, bool))
        # self.layout.addWidget(self.installed_only)

        self.filter = QComboBox()
        self.filter.addItems(
            [
                self.tr("All games"),
                self.tr("Installed only"),
                self.tr("Offline Games"),
            ])

        self.available_filters = [
            "all",
            "installed",
            "offline",
        ]
        if self.api_results.bit32_games:
            self.filter.addItem(self.tr("32 Bit Games"))
            self.available_filters.append("32bit")

        if self.api_results.mac_games:
            self.filter.addItem(self.tr("Mac games"))
            self.available_filters.append("mac")

        if self.api_results.no_asset_games:
            self.filter.addItem(self.tr("Exclude Origin"))
            self.available_filters.append("installable")

        self.filter.addItem(self.tr("Include Unreal Engine"))
        self.available_filters.append("include_ue")

        try:
            self.filter.setCurrentIndex(self.settings.value("filter", 0, int))
        except TypeError:
            self.settings.setValue("filter", 0)
            self.filter.setCurrentIndex(0)

        self.filter.currentIndexChanged.connect(self.filter_changed)

        self.import_game = QPushButton(icon("mdi.import", "fa.arrow-down"), self.tr("Import Game"))
        self.import_clicked = self.import_game.clicked

        self.egl_sync = QPushButton(icon("mdi.sync", "fa.refresh"), self.tr("Sync with EGL"))
        self.egl_sync_clicked = self.egl_sync.clicked
        # FIXME: Until it is ready
        # self.egl_sync.setEnabled(False)

        icon_label = QLabel()
        icon_label.setPixmap(icon("fa.search").pixmap(QSize(20, 20)))
        self.search_bar = QLineEdit()
        self.search_bar.setObjectName("search_bar")
        self.search_bar.setFrame(False)
        self.search_bar.setMinimumWidth(200)
        self.search_bar.setPlaceholderText(self.tr("Search Game"))

        checked = QSettings().value("icon_view", True, bool)

        self.view = SelectViewWidget(checked)

        self.refresh_list = QPushButton()
        self.refresh_list.setIcon(icon("fa.refresh"))  # Reload icon

        layout = QHBoxLayout()
        layout.addWidget(self.filter)
        layout.addStretch(1)
        layout.addWidget(self.import_game)
        layout.addWidget(self.egl_sync)
        layout.addStretch(1)
        layout.addWidget(icon_label)
        layout.addWidget(self.search_bar)
        layout.addStretch(3)
        layout.addWidget(self.view)
        layout.addStretch(1)
        layout.addWidget(self.refresh_list)
        self.setLayout(layout)

    def filter_changed(self, i):
        self.filterChanged.emit(self.available_filters[i])
        self.settings.setValue("filter", i)
