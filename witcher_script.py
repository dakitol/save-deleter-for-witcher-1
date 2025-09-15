import os
from pathlib import Path
import time

def clean_folder(folder_path, keep_count=5):
    """Очищает папку, оставляя только keep_count последних файлов"""
    
    # Преобразуем путь в объект Path
    folder = Path(folder_path)
    
    # Проверяем существование папки
    if not folder.exists():
        print(f"❌ Папка '{folder_path}' не существует!")
        return
    
    if not folder.is_dir():
        print(f"❌ '{folder_path}' не является папкой!")
        return
    
    # Получаем все файлы (исключая папки и симлинки)
    files = []
    for item in folder.iterdir():
        if item.is_file():
            files.append(item)
        else:
            print(f"ℹ️  Пропускаем '{item.name}' (это не файл)")
    
    print(f"📁 Найдено файлов: {len(files)}")
    
    # Выводим список найденных файлов для отладки
    if files:
        print("📋 Список файлов:")
        for file in files:
            print(f"   - {file.name}")
    else:
        print("ℹ️  Файлов не найдено")
        return
    
    if len(files) <= keep_count:
        print(f"✅ Нечего удалять (файлов: {len(files)}, оставляем: {keep_count})")
        return
    
    # Сортируем файлы по времени изменения (от старых к новым)
    files.sort(key=lambda x: x.stat().st_mtime)
    
    # Файлы для удаления (все кроме последних keep_count)
    files_to_delete = files[:-keep_count]
    
    print(f"🗑️  Будет удалено файлов: {len(files_to_delete)}")
    
    # Удаляем старые файлы
    deleted_count = 0
    for old_file in files_to_delete:
        try:
            old_file.unlink()
            print(f"✅ Удален: {old_file.name}")
            deleted_count += 1
        except Exception as e:
            print(f"❌ Ошибка удаления {old_file.name}: {e}")
    
    print(f"🎯 Удалено {deleted_count} файлов, оставлено {keep_count}")



if __name__ == "__main__":
    print("Скрипт включён")
    try:
        while True:
            clean_folder("C:/Users/user/Documents/The Witcher/saves", 5)
            time.sleep(30)
    except KeyboardInterrupt:
        print("Скрипт выключен")
