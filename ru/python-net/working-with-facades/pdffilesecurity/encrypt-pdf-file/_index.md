---
title: Зашифровать PDF-файл
linktitle: Зашифровать PDF-файл
type: docs
weight: 30
url: /ru/python-net/encrypt-pdf-file/
description: Зашифровать PDF-документ и настроить разрешения, чтобы контролировать, что пользователи могут делать с файлом.
lastmod: "2026-03-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Зашифровать PDF и управлять действиями пользователей
Abstract: Узнайте, как зашифровать PDF, определяя конкретные разрешения пользователей с помощью Aspose.PDF for Python via .NET. Это руководство показывает, как разрешать или ограничивать действия, такие как печать и копирование, при сохранении безопасности документа.
---

## Зашифровать PDF с паролем пользователя и паролем владельца

Защита PDF‑документов важна при обмене конфиденциальным или ограниченным содержимым. Шифрование позволяет защитить документ паролями и определить, какие действия разрешено выполнять пользователям. Этот фрагмент кода показывает, как применить пароли пользователя и владельца вместе с правами доступа для защиты PDF‑файла.

1. Создайте объект PdfFileSecurity.
1. Привяжите входной PDF.
1. Определите привилегии документа.
1. Зашифруйте PDF.
1. Сохраните зашифрованный PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Зашифровать PDF с разрешениями

Следующий фрагмент кода объясняет, как разрешить выбранные действия, такие как печать и копирование, ограничивая остальные.

1. Инициализировать [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) класс.
1. Привязать входной PDF.
1. Настройте привилегии документа.
1. Вызовите метод 'encrypt_file()'.
1. Сохранить зашифрованный PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Зашифровать PDF с помощью алгоритма шифрования

Шифрование PDF не только защищает документы паролями, но и позволяет выбирать алгоритм шифрования и его стойкость. Выбор подходящего алгоритма обеспечивает более высокий уровень безопасности конфиденциальных документов.

1. Создать объект PdfFileSecurity.
1. Привязать входной PDF.
1. Определить привилегии документа.
1. Зашифровать PDF с помощью алгоритма.
1. Сохранить зашифрованный PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

