---
title: Защитить PDF‑файлы в Python
linktitle: Шифровать и расшифровать PDF‑файл
type: docs
weight: 70
url: /ru/python-net/protect-pdf-file/
description: Узнайте, как шифровать файлы, расшифровывать защищённые PDF‑файлы и менять пароли в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Устанавливайте разрешения PDF и управляйте шифрованием в Python
Abstract: Эта страница документации объясняет, как установить привилегии документа, применить шифрование и расшифровать PDF‑файлы с использованием Aspose.PDF for Python. Она направляет разработчиков в настройке пользовательских и владельческих паролей, определении ограничений доступа (например, печати, копирования или редактирования). Примеры кода демонстрируют, как защитить конфиденциальный контент и эффективно управлять безопасностью PDF в приложениях Python, обеспечивая контролируемый доступ и конфиденциальность данных.
---

## Зашифровать PDF с паролем и разрешениями

Aspose.PDF for Python показывает, как защитить PDF‑документ с помощью шифрования на основе пароля:

1. Загрузите PDF‑документ.
1. Создайте объект разрешений.
1. Разрешите конкретные разрешения.
1. Установите пароли пользователя и владельца.
1. Выберите алгоритм шифрования.
1. Примените шифрование к документу.
1. Сохраните зашифрованный PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## Зашифровать PDF с полными правами доступа

Зашифровать PDF‑документ, позволяя полные права доступа, с помощью Aspose.PDF for Python. В примере используется шифрование RC4 128-bit, которое обеспечивает базовую безопасность и сохраняет совместимость со старыми PDF‑просмотрщиками.

1. Загрузите PDF‑документ.
1. Определите пароли пользователя и владельца.
1. Установите полные права доступа.
1. Выберите алгоритм шифрования.
1. Вызовите метод encrypt() с паролями, разрешениями и алгоритмом.
1. Сохраните зашифрованный PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## Расшифровать PDF‑файл, используя пароль владельца

Чтобы удалить защиту паролем и восстановить полный доступ:

1. Загрузите зашифрованный PDF, используя правильный пароль ('password' — пароль пользователя или владельца).
1. Удалите всю защиту паролем и настройки шифрования из документа.
1. Сохраните теперь незащищённый PDF в указанный файл вывода.

```python
import aspose.pdf as ap
import sys
from os import path

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## Изменить пароль PDF-файла

Обновить учетные данные безопасности (пароли пользователя и владельца) PDF‑документа, сохраняя его содержимое и структуру.

1. Откройте PDF, используя существующий пароль владельца ('owner'), который дает полный доступ, включая возможность изменять параметры безопасности.
1. Замените старые пароли новым паролем пользователя ('newuser') и новым паролем владельца ('newowner').
1. Сохраните PDF с обновлёнными настройками пароля.

```python
import aspose.pdf as ap
import sys
from os import path

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## Определить правильный пароль из массива

В некоторых сценариях вам может потребоваться определить правильный пароль из списка потенциальных вариантов, чтобы получить доступ к защищённому PDF. Приведённый ниже фрагмент кода демонстрирует, как проверить, защищён ли PDF-файл паролем, а затем попытаться разблокировать его, перебирая заранее определённый список паролей с использованием Aspose.PDF for Python via .NET.

Процесс включает:

1. Использование PdfFileInfo для определения, зашифрован ли PDF.
1. Откройте PDF с каждым паролем, используя ap.Document().
1. Если успешно, он выводит количество страниц.
1. Если нет, он ловит исключение и сообщает о неверном пароле.

```python
import aspose.pdf as ap
import sys
from os import path

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
