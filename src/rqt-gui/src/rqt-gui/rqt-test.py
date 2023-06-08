# coding: UTF-8

from qt_gui.plugin import Plugin
from python_qt_binding.QtCore import QTimer

from rqt-gui.RQtWidget import Widget


# クラス名は参照されるので書き間違えないこと
# Tusrai とか書くとつらいです
class RQtTest(Plugin):

    def __init__(self, context):
        super(guiTest, self).__init__(context)
        # オブジェクト名は間違えても動く？未調査
        self.setObjectName('RQtTestWidget')

        self._context = context

        # ここでTsuraiWdigetをセットしてつらくなろう
        self._widget = RQtTestWidget()
        if context.serial_number() > 1:
            self._widget.setWindowTitle(
                self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        context.add_widget(self._widget)

        # TsuraiWidgetは一定周期で更新したいのでQTimerを使う
        self._timer = QTimer()
        self._timer.timeout.connect(self._widget.update)
        # 16 msec 周期で更新させる
        self._timer.start(16)


    def shutdown_plugin(self):
        # 終了時はタイマーを止める
        self._timer.stop()
        pass


    def save_settings(self, plugin_settings, instance_settings):
        # セーブ機能は何もしない
        # つらい気持ちをファイルに保存する機能　いる？
        pass


    def restore_settings(self, plugin_settings, instance_settings):
        # リストア機能は何もしない
        # つらい気持ちを復元してどうするの？
        pass
