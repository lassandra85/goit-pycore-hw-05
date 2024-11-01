import sys
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return None  # Неправильний формат
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3].strip()
    }

def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                log_entry = parse_log_line(line)
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
   
    return [log for log in logs if log["level"].upper() == level.upper()]

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    # Підраховуємо кількість записів для кожного рівня логування
    levels_count = {}
    for log in logs:
        level = log["level"]
        levels_count[level] = levels_count.get(level, 0) + 1
    return levels_count

def display_log_counts(counts: Dict[str, int]):
    # Виводимо таблицю з підрахунком записів за рівнем логування
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def display_logs(logs: List[dict], level: str):
    # Виводимо детальні логи для заданого рівня
    print(f"\n Деталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    # Отримуємо аргументи командного рядка
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [log_level]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    # Завантажуємо логи з файлу
    logs = load_logs(file_path)

    # Підраховуємо кількість логів для кожного рівня
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Якщо вказано рівень логування, виводимо деталі для цього рівня
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            display_logs(filtered_logs, log_level)
        else:
            print(f"No logs found for level '{log_level.upper()}'")

if __name__ == "__main__":
    main()