---
title: Установить привилегии для существующего PDF‑файла
linktitle: Установить привилегии для существующего PDF‑файла
type: docs
weight: 40
url: /ru/python-net/set-privileges/
description: Установите и управляйте привилегиями PDF‑документа, чтобы контролировать действия пользователей, такие как печать, копирование и редактирование.
lastmod: "2026-03-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление разрешениями PDF и контролем доступа
Abstract: Узнайте, как контролировать действия пользователей с PDF, устанавливая привилегии документа с помощью Aspose.PDF for Python via .NET. Это руководство охватывает применение разрешений с паролем или без него для ограничения таких действий, как печать, копирование или редактирование.
---

## Установить привилегии PDF без паролей

Посмотрите, как применить привилегии к документу PDF без указания паролей пользователя или владельца, используя Aspose.PDF for Python via .NET. Этот фрагмент кода демонстрирует, как контролировать разрешённые действия, сохраняя документ доступным.

1. Создайте объект 'PdfFileSecurity'.
1. Привяжите входной PDF.
1. Определите привилегии документа.
1. Вызовите метод 'set_privilege()' без передачи паролей.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Установить привилегии PDF с паролями пользователя и владельца

Для полной защиты PDF‑документа часто требуется как контроль доступа (пароли), так и ограничения использования (разрешения). Объединив их, вы можете гарантировать, что только уполномоченные пользователи смогут открыть документ и выполнить определённые действия.

Используя метод set_privilege с параметрами пароля, вы можете:

- Защитите документ пользовательским паролем
- Задайте пароль владельца для полного контроля
- Настройте разрешённые и ограниченные действия
- Применяйте политики безопасности на уровне документа

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Попробуйте установить привилегии PDF без исключений

Этот фрагмент кода объясняет, как контролировать доступ и ограничивать действия, такие как копирование, при этом разрешая другие, например печать.

1. Создайте объект 'PdfFileSecurity'.
1. Загрузите исходный PDF, используя метод 'bind_pdf()'.
1. Определить привилегии документа.
1. Применить привилегии с паролями.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```

