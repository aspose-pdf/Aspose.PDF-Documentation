# .codex/skills/ru-step-style/scripts/check_ru_steps.py

import re
import sys
from pathlib import Path

BAD_VERBS = {
    "Создать": "Создайте",
    "Открыть": "Откройте",
    "Добавить": "Добавьте",
    "Установить": "Установите",
    "Настроить": "Настройте",
    "Запустить": "Запустите",
    "Сохранить": "Сохраните",
    "Получить": "Получите",
    "Проверить": "Проверьте",
    "Использовать": "Используйте",
    "Передать": "Передайте",
    "Загрузить": "Загрузите",
    "Извлечь": "Извлеките",
    "Преобразовать": "Преобразуйте",
    "Удалить": "Удалите",
    "Отобразить": "Отобразите",
    "Обновить": "Обновите",
    "Вызвать": "Вызовите",
}

STEP_RE = re.compile(r"^(\s*(?:[-*]|\d+[.)])\s+)([А-ЯЁ][а-яё]+)\b")

def check_file(path: Path) -> int:
    issues = 0

    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = STEP_RE.match(line)
        if not match:
            continue

        verb = match.group(2)
        if verb in BAD_VERBS:
            print(f"{path}:{line_no}: replace '{verb}' with '{BAD_VERBS[verb]}'")
            issues += 1

    return issues

def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    files = list(root.rglob("*.md"))

    total = sum(check_file(file) for file in files)

    if total:
        print(f"\nFound {total} Russian step style issue(s).")
        return 1

    print("No Russian step style issues found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())