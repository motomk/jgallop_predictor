import win32com.client
import time
import re
import sys
import os
import argparse


def initialize_jvlink():
    """JVLinkを初期化する"""
    jvlink = win32com.client.Dispatch("JVDTLab.JVLink")
    ret = jvlink.JVInit("UNKNOWN")
    # jvlink.JVSetUIProperties()
    if ret == 0:
        print("JVInit完了")
    else:
        print("JVInit失敗")
        sys.exit(1)
    return jvlink


def wait_for_download(jvlink, download_count):
    """データのダウンロードが完了するまで待機する"""
    while True:
        current_status = jvlink.JVStatus()
        print("\rDownloading", current_status, "/", download_count, end="\r")
        if current_status < 0:
            print("JVStatus Err=", current_status)
            break
        if download_count == current_status:
            break
        else:
            time.sleep(2)


def read_and_process_data(jvlink, target_recid):
    """データを読み込んで処理する"""
    while True:
        returnval = jvlink.JVRead("", 102890, "")
        # JVReadの戻り値
        # return_code, buff, sise, filename
        if returnval[0] == 0:
            print("JVRead完了")
            break
        elif returnval[0] == -1:
            pass
        elif returnval[0] < -1:
            print("Error\nError Code=", returnval[0])
        else:
            process_data(jvlink, returnval, target_recid)


def process_data(jvlink, returnval, target_recid):
    """データを処理する"""
    # データからレコードID、バッファ、ファイル名を抽出
    rec_id, buff, filename = returnval[1][:2], returnval[1], returnval[3]
    # 改行コードを削除してデータを整形
    formatted_buff = re.sub(r"[\r\n]", "", buff)

    # 対象のレコードIDの場合のみ処理
    if rec_id in target_recid:
        # ファイルにデータを追記
        append_data_to_file(filename, formatted_buff)
    else:
        # 対象外のデータはスキップ
        jvlink.JVSkip()


def append_data_to_file(filename, data):
    """指定されたファイルにデータを追記する"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(script_dir, "data")
    path = os.path.join(raw_data_dir, filename)
    global last_printed_path
    try:
        last_printed_path
    except NameError:
        last_printed_path = None

    if last_printed_path != path:
        print(path)
        last_printed_path = path

    with open(path, "a", encoding="utf-8") as file:
        file.write(data + "\n")  # ファイルにデータを追記


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser()
    parser.add_argument("year", help="データを取得する年を指定")
    parser.add_argument(
        "dataspec",
        help="データ種別を指定",
        choices=[
            "TOKU",
            "RACE",
            "DIFF",
            "DIFN",
            "BLOD",
            "BLDN",
            "MING",
            "SNAP",
            "SNPN",
            "SLOP",
            "YSCH",
            "HOSE",
            "HOSN",
            "HOYU",
            "COMM",
            "WOOD",
            "TCOV",
            "TCVN",
            "RCOV",
            "RCVN",
        ],
    )
    args = parser.parse_args()

    jvlink = initialize_jvlink()
    dataspec = args.dataspec
    fromtime = f"{args.year}0101000000-{args.year}1231235959"
    option = 4
    returnval = jvlink.JVOpen(dataspec, fromtime, option, 0, 0, "")
    # JVOpenの戻り値は以下の通り
    # return_code, readcount, downloadcount, lastfiletimestamp,
    return_code, read_count, download_count, last_file_timestamp = returnval
    if return_code != 0:
        print("JVOpenでエラーが発生しました。エラーコード:", return_code)
        sys.exit(1)

    wait_for_download(jvlink, download_count)

    target_recid = [
        "RA",  # レース番号の詳細情報（中央のみ）
        "SE",  # 出走馬の競争馬毎のレース情報（中央のみ）
        "HR",  # 払戻金情報
        "H1",  # 確定票数（3連単以外）
        "H6",  # 確定票数（3連単）
        "O1",  # 確定オッズ（単複枠）
        "O2",  # 確定オッズ（馬連）
        "O3",  # 確定オッズ（ワイド）
        "O4",  # 確定オッズ（馬単）
        "O5",  # 確定オッズ（3連複）
        "O6",  # 確定オッズ（3連単）
        "WF",  # 重勝式（WINS5）に関する情報
        "JG",  # 競走馬除外情報に関する情報
    ]
    read_and_process_data(jvlink, target_recid)

    return_code = jvlink.JVClose()
    print("JVCloseの戻り値", return_code)


if __name__ == "__main__":
    main()
