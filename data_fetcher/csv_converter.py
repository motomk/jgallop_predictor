import os
import sys
from struct.H1Record import H1Record


def process_files_in_data_folder():
    """dataフォルダ内のファイルを1ファイルずつ処理する"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder_path = os.path.join(script_dir, "data")

    # dataフォルダ内の全ファイルを取得
    files = os.listdir(data_folder_path)

    for file in files:
        if file.endswith(".jvd"):
            file_path = os.path.join(data_folder_path, file)
            # ここで各ファイルに対する処理を行う
            print(f"Processing {file_path}...")
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    record_id = line[:2]
                    if record_id == "H1":
                        h1_record = H1Record(line)
                        print(h1_record)
                    sys.exit()  # TODO: ここで処理を終了するのは仮の処理


def main():
    process_files_in_data_folder()


if __name__ == "__main__":
    main()
