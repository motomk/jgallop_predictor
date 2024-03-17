import os
from struct.record_format import record_type_id_map, H1_csv_header


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

    def extract_csv_values(line, format):
        csv_values = []
        for field in format:
            start_pos, repeat, length = field[0] - 1, field[1], get_field_length(field)
            for _ in range(repeat):
                value = line[start_pos : start_pos + length].strip()
                csv_values.append(value)
                start_pos += length
        return csv_values

    def get_field_length(field):
        return field[3] if isinstance(field[2], int) else sum(field[2])

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
            csv_file.write(csv_line + "\n")

    for file in files:
        if file.endswith(".jvd"):
            file_path = os.path.join(data_folder_path, file)
            process_jvd_file(file_path)


def main():
    process_files_in_data_folder()


if __name__ == "__main__":
    main()
