---
title: Расшифровать PDF-файл
linktitle: Расшифровать PDF-файл
type: docs
weight: 20
url: /python-net/decrypt-pdf-file/
description: Это руководство объясняет, как удалить ограничения, такие как печать, копирование и редактирование, чтобы получить полный доступ к вашему PDF‑документу.
lastmod: "2026-03-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить защиту паролем из PDF
Abstract: В этой статье демонстрируется, как расшифровать PDF‑файл с помощью пароля владельца. Описывается процесс удаления ограничений безопасности, которые ограничивают такие действия, как печать, редактирование или копирование содержимого. При вводе правильного пароля владельца пользователи могут разблокировать документ и восстановить полный контроль над его функциями.
---

## Расшифровать PDF с паролем владельца

Расшифровать защищённый паролем PDF‑документ, используя пароль владельца с Aspose.PDF for Python via .NET. Эта операция удаляет шифрование и обеспечивает неограниченный доступ к документу.

1. Создайте объект 'PdfFileSecurity'.
1. Загрузите зашифрованный PDF, используя метод 'bind_pdf()'.
1. Расшифруйте Document.
1. Сохраните расшифрованный PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## Попробуйте расшифровать PDF без исключения

PDF‑документы часто защищаются паролями, чтобы ограничить доступ и использование. Чтобы полностью получить доступ к таким документам или изменить их, может потребоваться удалить шифрование. Расшифруйте защищённый PDF‑документ, используя пароль владельца, чтобы удалить шифрование и ограничения доступа, с помощью Aspose.PDF for Python via .NET.

1. Создайте объект 'PdfFileSecurity'.
1. Привяжите входной PDF.
1. Расшифровать PDF.
1. Сохранить выходной PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```
