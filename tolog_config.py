import os
import sys
import tolog_to_dropbox_exeptions as t_exeptions


class TologConfig:
    """
    Tologの設定を扱うクラス

    Attributes
    ----------
    Token : str
        Dropboxのtoken
    LogDir : str
        Dropbox上のlogディレクトリのパス
    FileType : str
        tologファイルの拡張子
    DateFormat : str
        tologファイルのファイル名に使う日付のフォーマット
    """

    def __init__(self):
        TOKEN="TOLOG_DB_TOKEN"
        LOG_DIR="TOLOG_DB_LOG_DIR"
        FILE_TYPE="TOLOG_FILETYPE"
        DATE_FORMATR="TOLOG_DATE_FORMAT"
        LOG_FORMAT="TOLOG_LOG_FORMAT"

        D_FILE_TYPE = ".md"
        D_DATE_FORMAT = "%y%m%d"
        D_LOG_FORMAT = "[%H:%M]"


        self.Token = os.getenv(TOKEN)
        self.LogDir = os.getenv(LOG_DIR)
        self.FileType = os.getenv(FILE_TYPE, D_FILE_TYPE)
        self.DateFormat = os.getenv(DATE_FORMATR, D_DATE_FORMAT)
        self.LogFormat = os.getenv(LOG_FORMAT, D_LOG_FORMAT)

        if self.Token is None:
            raise t_exeptions.TologConfigError
        if self.LogDir is None:
            raise t_exeptions.TologConfigError
