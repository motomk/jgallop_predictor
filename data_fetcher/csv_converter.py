import os
from struct.record_format import record_type_id_map, H1_csv_header, H6_csv_header


def process_files_in_data_folder():
    """dataフォルダ内のファイルを1ファイルずつ処理する"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder_path = os.path.join(script_dir, "data")

    # dataフォルダ内の全ファイルを取得
    files = os.listdir(data_folder_path)

    def process_jvd_file(file_path):
        print(f"Processing {file_path}...")
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                process_line(line, file_path)

    def process_line(line, file_path):
        record_id = line[:2]
        if record_id == "H1":
            format = record_type_id_map[record_id]
            csv_values = extract_csv_values(line, format)
            write_csv_line(file_path, csv_values, record_id)
        elif record_id == "H6":
            format = record_type_id_map[record_id]
            csv_values = extract_csv_values(line, format)
            write_csv_line(file_path, csv_values, record_id)

    def extract_csv_values(line, format):
        """指定されたフォーマットに従って、行からCSV値を抽出する"""
        csv_values = []
        for field in format:
            start_pos = field[0] - 1  # フィールドの開始位置（0ベースインデックス）
            if isinstance(field[2], tuple):
                # データ構造がタプルの場合、繰り返し処理
                repeat_count = field[1]
                field_length = sum(field[2])
                for i in range(repeat_count):
                    field_value = line[start_pos : start_pos + field_length]
                    # タプル内の各フィールドに対して処理
                    sub_field_values = []
                    sub_field_start = 0
                    for sub_field_length in field[2]:
                        sub_field_values.append(
                            field_value[
                                sub_field_start : sub_field_start + sub_field_length
                            ]
                        )
                        sub_field_start += sub_field_length
                    csv_values.extend(sub_field_values)
                    start_pos += field_length
            else:
                # データ構造が単一の場合
                field_length = field[3]
                field_value = line[start_pos : start_pos + field_length]
                csv_values.append(field_value)
        return csv_values

    def write_csv_line(file_path, csv_values, record_id):
        csv_line = ",".join(csv_values)
        csv_file_name = file_path.replace(".jvd", ".csv")
        csv_folder_path = os.path.join(script_dir, "csv")
        os.makedirs(csv_folder_path, exist_ok=True)
        csv_file_path = os.path.join(csv_folder_path, os.path.basename(csv_file_name))
        with open(csv_file_path, "a", encoding="utf-8") as csv_file:
            # Check if the file is empty to write the header
            if csv_file.tell() == 0:
                if record_id == "H1":
                    csv_header = ",".join(H1_csv_header)
                    csv_file.write(csv_header + "\n")
                elif record_id == "H6":
                    csv_header = ",".join(H6_csv_header)
                    csv_file.write(csv_header + "\n")
            csv_file.write(csv_line + "\n")

    for file in files:
        if file.endswith(".jvd"):
            file_path = os.path.join(data_folder_path, file)
            process_jvd_file(file_path)


def main():
    process_files_in_data_folder()


if __name__ == "__main__":
    main()
