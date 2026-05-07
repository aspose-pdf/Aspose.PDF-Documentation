---
title: Шифрование и расшифровка PDF-файлов на Python
linktitle: Шифрование и расшифровка PDF-файла
type: docs
weight: 70
url: /ru/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Узнайте, как установить привилегии PDF, зашифровать файлы, расшифровать защищённые PDF и изменить пароли в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Установите разрешения PDF и управляйте шифрованием в Python.
Abstract: Эта страница документации объясняет, как задать привилегии документа, применить шифрование и расшифровать PDF‑файлы с помощью Aspose.PDF for Python. Она направляет разработчиков через настройку пользовательских и владельческих паролей, определение ограничений доступа (например, печать, копирование или редактирование). Примеры кода демонстрируют, как защищать конфиденциальный контент и эффективно управлять безопасностью PDF в приложениях Python, обеспечивая контролируемый доступ и конфиденциальность данных.
---

Управление безопасностью документа имеет решающее значение при работе с конфиденциальным или бизнес‑критически важным контентом. Aspose.PDF for Python via .NET предоставляет мощный API для программного применения шифрования, контроля доступа через права и расшифровки защищённых PDF‑файлов.

В этой статье разработчиков Python познакомят с практическими примерами по настройке привилегий, применению и снятию шифрования, изменению паролей и обнаружению состояний защиты — всё в рамках рабочего процесса с PDF.

Aspose.PDF for Python via .NET дает разработчикам полный контроль над безопасностью PDF:

**Установить привилегии** - Тонко настроенный контроль доступа с использованием разрешений.
**Зашифровать файл** - Применить шифрование AES или RC4 с пользовательскими паролями.
**Расшифровать файл** - Удалить защиту, используя пароль владельца.
**Изменить пароли** - Смените или обновите учетные данные без изменения содержимого.
**Проверка безопасности** - Обнаружить статус шифрования или требуемые типы паролей.

Используйте эту страницу, когда вам нужно защищать PDF‑документы паролями, ограничивать печать или копирование, менять учётные данные или проверять, зашифрован ли документ.

## Установить привилегии для существующего PDF‑файла

Вы можете ограничить или разрешить определённые операции (например, печать, копирование, заполнение форм), назначая пользовательские и владелецкие пароли вместе с правами доступа.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## Шифрование PDF-файла с использованием различных типов шифрования и алгоритмов

Шифрование PDF гарантирует, что только пользователи с действительными учетными данными могут открыть или изменить файл.

>Ключевые термины:

- Пароль пользователя. Требуется для открытия документа.

- Пароль владельца. Требуется для изменения разрешений или снятия шифрования.

- KeySize. Используйте AE_SX128 для максимальной безопасности в современных процессах.

Следующий фрагмент кода показывает, как зашифровать PDF‑файлы.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## Расшифровать PDF-файл, используя пароль владельца

Чтобы удалить защиту паролем и восстановить полный доступ:

1. Загружает зашифрованный PDF, используя правильный пароль ('password' — это пароль пользователя или владельца).
1. Удаляет всю защиту паролем и настройки шифрования из документа.
1. Сохраняет теперь незащищённый PDF в указанный файл вывода.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## Шифрование и дешифрование PDF с сертификатами открытого ключа

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## Изменить пароль PDF‑файла

Обновить учетные данные безопасности (пароли пользователя и владельца) PDF‑документа, сохранив его содержимое и структуру.

1. Открывает PDF, используя существующий пароль владельца ('owner'), который предоставляет полный доступ, включая возможность изменять настройки безопасности.
1. Заменяет старые пароли новым паролем пользователя ('newuser') и новым паролем владельца ('newowner').
1. Сохраняет PDF с обновлёнными настройками пароля.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## Как определить, защищён ли исходный PDF паролем

### Определить правильный пароль из массива

В некоторых сценариях вам может потребоваться определить правильный пароль из списка потенциальных вариантов, чтобы получить доступ к защищённому PDF. Приведённый ниже фрагмент кода демонстрирует, как проверить, защищён ли файл PDF паролем, а затем попытаться разблокировать его, перебирая заранее определённый список паролей с помощью Aspose.PDF for Python via .NET.

Процесс включает:

1. Использование PdfFileInfo для определения, зашифрован ли PDF.
1. Пытается открыть PDF с каждым паролем, используя ap.Document().
1. Если успешно, он выводит количество страниц.
1. Если нет, он перехватывает исключение и сообщает о неправильном пароле.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## Связанные темы безопасности

- [Обеспечьте безопасность и подпишите PDF‑файлы с помощью Python](/pdf/ru/python-net/securing-and-signing/)
- [Цифровая подпись PDF файлов в Python](/pdf/ru/python-net/digitally-sign-pdf-file/)
- [Извлечь информацию о подписи из PDF в Python](/pdf/ru/python-net/extract-image-and-signature-information/)
- [Подписать PDF‑документы со смарт‑карты в Python](/pdf/ru/python-net/sign-pdf-document-from-smart-card/)

