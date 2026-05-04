---
title: Подписать PDF‑документы со смарт‑карты на Python
linktitle: Подписание PDF со смарт‑картой
type: docs
weight: 30
url: /python-net/sign-pdf-document-from-smart-card/
description: Узнайте, как подписывать PDF‑документы с помощью смарт‑карт и внешних сертификатов на Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Подписать PDF‑документы со смарт‑карты на Python
Abstract: Это руководство объясняет, как цифрово подписывать PDF‑документы с использованием смарт‑карты и Aspose.PDF for Python via .NET. В нём показано, как получить доступ к сертификатам, хранящимся на аппаратных устройствах (например, USB‑токенах или смарт‑картах) через хранилище сертификатов Windows, и использовать их для подписи PDF‑файлов. Документация включает примеры кода, демонстрирующие, как найти нужный сертификат, настроить свойства подписи и встроить цифровую подпись в PDF. Это обеспечивает безопасную подпись, поддерживаемую аппаратным обеспечением, в соответствии с требованиями стандартов цифровой подписи, подходящую для высокодоверительных корпоративных и юридических процессов.
---

Aspose.PDF предоставляет надёжные возможности для интеграции визуальных и криптографических компонентов подписи, обеспечивая как подлинность, так и профессиональное представление в цифрово подписанных PDF‑документах.

Используйте этот рабочий процесс, когда ваш процесс подписи зависит от сертификатов, хранящихся в аппаратно‑защищённых устройствах, таких как смарт‑карты, USB‑токены или управляемые хранилища сертификатов.

## Подписать с помощью смарт‑карты, используя поле подписи

Этот пример демонстрирует, как цифрово подписать PDF‑документ с использованием внешнего сертификата с помощью Aspose.PDF for Python и применить пользовательское изображение внешнего вида подписи:

1. Открытие PDF‑документа.
1. Создание объекта PdfFileSignature и привязка его к документу.
1. Получение локального цифрового сертификата с использованием пользовательского метода `get_local_certificate()`.
1. Настройка ExternalSignature на основе выбранного сертификата.
1. Применение пользовательского изображения внешнего вида подписи (например, логотип компании или рукописная подпись).
1. Цифровая подпись первой страницы документа с указанными метаданными (причина, контакт, местоположение).
1. Сохранение подписанного документа в новый выходной файл.

Этот метод идеален для случаев, когда подписи должны применяться программно с использованием внешних сертификатов — таких как аппаратные токены, хранилища сертификатов или доверенные поставщики — и отображаться с персонализированным визуальным оформлением.

Ниже приведены фрагменты кода для подписи PDF‑документа с помощью смарт‑карты:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## Проверка цифровых подписей

Этот фрагмент кода демонстрирует, как проверить цифровые подписи в PDF‑документе с использованием Aspose.PDF for Python:

1. Открытие PDF‑файла.
1. Создание объекта 'PdfFileSignature' и привязка его к документу.
1. Получение списка всех имен полей подписи с помощью 'get_signature_names()'.
1. Перебор каждой подписи и проверка её действительности с помощью 'verify_signature()'.
1. Выброс исключения, если какая‑либо подпись не проходит проверку.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Подписать с использованием внешнего сертификата

Этот фрагмент кода демонстрирует, как добавить и подписать поле цифровой подписи в документе PDF с помощью Aspose.PDF for Python с внешним сертификатом:

1. Открытие PDF‑файла как бинарного потока.
1. Создание SignatureField и размещение его на первой странице документа в указанной позиции.
1. Получение локального цифрового сертификата с использованием пользовательского метода `get_local_certificate()`.
1. Настройка ExternalSignature с метаданными, такими как authority, reason и контактная информация.
1. Назначение уникального имени полю подписи (partial_name = "sig1").
1. Добавление поля подписи к полям формы PDF.
1. Подписание поля с использованием внешнего сертификата.
1. Сохранение подписанного документа в выходной файл.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## Связанные темы безопасности

- [Обеспечьте безопасность и подпишите PDF‑файлы с помощью Python](/pdf/ru/python-net/securing-and-signing/)
- [Цифровая подпись PDF файлов в Python](/pdf/ru/python-net/digitally-sign-pdf-file/)
- [Извлечь информацию о подписи из PDF в Python](/pdf/ru/python-net/extract-image-and-signature-information/)
- [Шифрование и расшифровка PDF‑файлов в Python](/pdf/ru/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

