import os
import sys
from ctypes import windll

sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'ui'))

from PySide6.QtWidgets import QApplication, QMessageBox

from src.ui.MainGUI import MainGUI


if __name__ == '__main__':
    app = QApplication.instance() or QApplication(sys.argv)

    if windll.user32.FindWindowW(None, "哔哩哔哩漫画下载器 v1.0.0") != 0:
        box = QMessageBox.information(None, "提示", "有一个我已经不满足不了你吗？\n\t...(｡•ˇ‸ˇ•｡) ...")
        sys.exit(0)

    window = MainGUI()
    window.show()
    app.exec()

# TODO: 缓存更多资源，减少网络请求
# TODO: 添加二维码登入功能
# TODO: 添加不同的主题
# TODO: 添加一个启动加载进度条
# TODO: 添加我的追漫界面，以及追漫功能
# TODO: 下载任务的暂停和继续功能，断点续传。以及任务的持久化，本地缓存