import os
import sys
import datetime as dt
import tolog_to_dropbox as t_td


class TologFunctions:
    """
    Textに対してTologの機能を実行するクラス

    Attributes
    ----------
    td : tolog_to_dropbox.TologDropbox
        Dropbox上のファイルを扱うクラス
    """

    def __init__(self, td, config):
        """
        Parameters
        ----------
        td : tolog_to_dropbox.TologDropbox
            Dropbox上のファイルを扱うクラス
        config : tolog_config.TologConfig
        """
        self.td = td
        self.LogFormat = config.LogFormat

    def makeLogText(self, text="", tags=None, pretext="\n"):
        """
        logの形式のテキストを作る関数

        Parameters
        ----------
        text : str, optional
            logのテキスト
        tags : list(str), optional
            タグのリスト
        pretext : str, optional
            textの前につける文字列
            デフォルトは"\n"

        Returns
        -------
        log_text : str
            log形式のテキスト
        """
        log_text = pretext

        # 時間部分
        now = dt.datetime.now()
        time_text = now.strftime(self.LogFormat)

        log_text = log_text + time_text

        # タグ部分
        if tags is not None:
            tags_text = " ".join(tags)
            log_text = log_text + " " + tags_text

        # text部分
        log_text = log_text + "\n\n"
        log_text = log_text + text

        return log_text





    def appendLog(self, date, tags, text):
        """
        Logを追記する関数

        Prameters
        ---------
        date : str
            目的の日付
        tags : list(str)
            つけるタグ
        text : str
            logのテキスト

        Returns
        -------
        metadata : dropbox.files.FileMetadata or None
            追記したファイルのメタデータ
            ファイルが存在しなかったらNone
        """

        text_log = self.makeLogText(text, tags)
        print(text_log)

        metadata = self.td.appendTologFile(date, text_log)

        return metadata

