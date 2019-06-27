import dropbox
import os
import sys


class VirtualTologError(Exception):
    """
    Tolog関連の例外の基底クラス
    """


class OverlapError(VirtualTologError):
    def __init__(self):
        self.message = "ファイルが重複している"

    def __str__(self):
        return self.message

class TologFileNameError(VirtualTologError):
    def __init__(self):
        self.message = "指定されたtologファイルの名前が間違っている"

    def __str__(self):
        return self.message

class TologConfigError(VirtualTologError):
    def __init__(self):
        self.message = "configが不十分。環境変数が指定されていないかも"

    def __str__(self):
        return self.message
