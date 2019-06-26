import dropbox
import os
import sys
import datetime as dt
import tolog_to_dropbox_exeptions as t_exeptions

TOKEN="TOLOG_DB_TOKEN"
LOG_DIR="TOLOG_DB_LOG_DIR"


token = os.getenv(TOKEN)
log_dir = os.getenv(LOG_DIR)

if token is None:
    print("ERROR:", TOKEN , " is not set", file=sys.stderr)
    sys.exit(1)


class TologDropbox:
    """
    Dropbox上のTologファイルを扱うクラス

    Attributes
    ----------
    dbx : dropbox.dropbox.Dropbox
        ドロップボックスのクラス
    log_dir : str
        ドロップボックス上でのlogディレクトリのパス
    """

    def __init__(self, token, log_dir):
        """
        Parameters
        ----------
        token : str
            dropboxのトークン
        log_dir : str
            ドロップボックス上でのlogディレクトリのパス
        """
        self.dbx = dropbox.Dropbox(token)
        # TODO この辺を設定するファイルを別に用意する
        self.log_dir = log_dir
        self.FileType = ".md"
        self.DateFormat = "%y%m%d"

    def validateTologDate(self, date):
        """
        tologの日付かどうか確認するやつ

        Parameters
        ----------
        date : str
            確認する日付

        Returns
        -------
        ok : bool
            okならTrue
        """
        if len(date) is not 6:
            return False
        try:
            dt.datetime.strptime(date, self.DateFormat)
        except:
            return False
        return True

    def _makeTologPath(self, date):
        """
        tologファイルのパスを作るやつ

        Parameters
        ----------
        date : str
            目的の日付
        """

        return self.log_dir + "/" + date + self.FileType


    def getTologFileInfo(self, date):
        """
        日付文字列から該当するTologファイルの情報をとってくる

        Parameters
        ----------
        date : str
            目的の日付

        Returns
        -------
        metadata : dropbox.files.FileMetadata
            ファイルの情報
            ファイルが存在しない場合はNone

        Raises
        ---------
        tolog_to_dropbox_exeptions.OverflowError
            ファイルが重複していたとき
        """
        search_ret = self.dbx.files_search(self.log_dir, date).matches
        if len(search_ret) is 0:
            return None
        if len(search_ret) > 2:
            raise t_exeptions.OverlapError
        return search_ret[0].metadata

    def getTologText(self, metadata):
        """
        Tologファイルのテキストをとってくる

        Parameters
        ----------
        metadata : dropbox.files.FileMetadata
            ファイルの情報

        Returns
        -------
        text : str
            Tologファイルの中身
        """

        file_response = self.dbx.files_download(metadata.id)
        return file_response[1].text

    def uploadTologFile(self, date, text):
        """
        Tologファイルをuploadする
        既に存在している場合は更新
        存在していない場合は新規作成

        Parameters
        ----------
        date : str
            目的の日付
        text : str
            uploadするテキスト

        Returns
        -------
        metadata : dropbox.files.FileMetadata
            更新したファイルのメタデータ
        """

        if not self.validateTologDate(date):
            raise t_exeptions.TologFileNameError
        meta = self.getTologFileInfo(date)

        if meta is None:
            tolog_path = self._makeTologPath(date)
            ret_meta = self.dbx.files_upload(text.encode(), tolog_path, mode=dropbox.files.WriteMode.add)
        else:
            tolog_path = meta.path_lower
            rev = meta.rev
            ret_meta = self.dbx.files_upload(text.encode(), tolog_path, mode=dropbox.files.WriteMode.update(rev))

        return ret_meta

    def appendTologFile(self, date, text, pretext="\n"):
        """
        Tologファイルに追記する
        ファイルが存在しない場合は何もしない

        Parameters
        ----------
        date : str
            目的の日付
        text : str
            追記するテキスト
        pretext : str
            追記するときに最初に挿入される文字列
            デフォルトは"\n"

        Returns
        -------
        metadata : dropbox.files.FileMetadata
            更新したファイルのメタデータ
            ファイルが存在しなかった場合はNone
        """

        if not self.validateTologDate(date):
            raise t_exeptions.TologFileNameError
        meta = self.getTologFileInfo(date)
        if meta is None:
            return meta
        base_text = self.getTologText(meta)

        new_text = base_text + pretext + text

        tolog_path = meta.path_lower
        rev = meta.rev
        ret_meta = self.dbx.files_upload(text.encode(), tolog_path, mode=dropbox.files.WriteMode.update(rev))
        return ret_meta

    def newTologFile(self, date, text):
        """
        Tologファイルを新規作成する
        ファイルが存在する場合は何もしない

        Parameters
        ----------
        date : str
            目的の日付
        text : str
            ファイルに書き込むテキスト

        Returns
        -------
        metadata : dropbox.files.FileMetadata
            作成したファイルのメタデータ

        Raises
        ----------
        t_exeptions.OverlapError
            ファイルが存在してた場合
        """

        if not self.validateTologDate(date):
            raise t_exeptions.TologFileNameError

        meta = self.getTologFileInfo(date)
        if meta is not None:
            raise t_exeptions.OverlapError

        tolog_path = self._makeTologPath(date)
        ret_meta = self.dbx.files_upload(text.encode(), tolog_path, mode=dropbox.files.WriteMode.add)

        return ret_meta




td = TologDropbox(token, log_dir)
#print(td.getTologText(td.getTologFile("19062")))
#td.uploadTologFile("190626", "hoge")
#print(td.uploadTologFile("991231", "huga"))
print(td.appendTologFile("991231", "append"))
#try:
#    print(td.newTologFile("991231", "hogehoge"))
#except:
#    print("exist")
#print(td.newTologFile("991230", "hogehoge"))
