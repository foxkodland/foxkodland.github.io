import os

def rename_files_to_lowercase():
    for dirpath, dirnames, filenames in os.walk("красная упаковка"):
        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            new_filename = filename.lower()
            new_path = os.path.join(dirpath, new_filename)
            # Переименование файла
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Переименовано: {old_path} -> {new_path}")

if __name__ == "__main__":
    # Укажите путь к папке, с которой хотите начать
    rename_files_to_lowercase()