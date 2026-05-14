---
title: Изменить пароль PDF‑файла
type: docs
weight: 10
url: /python-net/change-password/
description: Изменить пользовательский и владелецский пароли защищённого PDF‑документа с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-03-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обновить пароли PDF
Abstract: Узнайте, как изменить как пользовательский, так и пароль владельца в защищённом PDF‑файле с помощью Aspose.PDF for Python via .NET. Этот пример демонстрирует, как безопасно обновить учётные данные доступа, сохраняя существующее шифрование и разрешения нетронутыми.
---

## Изменить пароль пользователя и владельца

Во многих случаях вам может потребоваться обновить пароли защищённого PDF без изменения текущих настроек безопасности. Это может быть полезно при смене учетных данных, передаче прав собственности или повышении безопасности документа.

Метод 'change_password' класса [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) класс позволяет:

- Обновить пароль пользователя (необходим для открытия документа)
- Обновить пароль владельца (используется для управления правами)
- Сохранить текущие настройки шифрования и прав

1. Создайте объект 'PdfFileSecurity'.
1. Привяжите входной PDF.
1. Измените пароли с помощью метода 'change_password()'.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change User and Owner Password
def change_user_and_owner_password(infile, outfile):
    """Change user and owner passwords while keeping existing security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Change passwords
    file_security.change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save updated PDF
    file_security.save(outfile)
```

## Изменить пароль и сбросить безопасность

При работе с защищёнными PDF‑документами простая смена паролей может быть недостаточной. Возможно, также потребуется изменить разрешения, такие как печать, копирование или права на редактирование.

Узнайте, как обновить пользовательский и владелецкий пароли, одновременно сбрасывая параметры безопасности PDF с помощью Aspose.PDF for Python via .NET. Этот пример показывает, как переопределить разрешения документа и уровень шифрования вместе с новыми учётными данными доступа.

1. Создайте объект 'PdfFileSecurity'.
1. Привяжите входной PDF.
1. Создайте объект 'DocumentPrivilege' и настройте разрешённые действия.
1. Смените пароли и сбросьте безопасность.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change Password and Reset Security
def change_password_and_reset_security(infile, outfile):
    """Change passwords and reset document security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define new privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Change passwords and reset security
    file_security.change_password(
        "owner_password",
        "new_user_password",
        "new_owner_password",
        privilege,
        pdf_facades.KeySize.X128,
    )

    # Save updated PDF
    file_security.save(outfile)
```

## Попробовать изменить пароль без исключения

В некоторых рабочих процессах, особенно при пакетной обработке или в автоматизированных системах, важно избегать исключений, которые могут прервать выполнение. Вместо выбрасывания ошибок вы можете предпочесть безопасную операцию, которая сообщает об успехе или неудаче.

Метод 'try_change_password' [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) класс предоставляет эту функциональность следующим образом:

1. Создайте объект 'PdfFileSecurity'.
1. Загрузите PDF‑документ, используя метод 'bind_pdf()'.
1. Попытка изменить пароли.
1. Проверьте результат.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Change Password Without Exception
def try_change_password_without_exception(infile, outfile):
    """Attempt to change passwords without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to change passwords
    result = file_security.try_change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Password change failed. Check owner password or document security.")
```
