---
title: Информация о подписи
type: docs
weight: 60
url: /python-net/signature-information/
description: Узнайте, как читать имена подписей, данные подписанта, метки времени и метаданные подписи из подписанных PDF‑файлов с помощью PdfFileSignature в Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Чтение деталей подписи из PDF‑документов в Python
Abstract: В этой статье объясняется, как просматривать метаданные подписи в подписанных PDF‑документах с помощью Aspose.PDF for Python via .NET. Показано, как вывести список имён подписей, прочитать данные подписанта, получить дату и время подписи, а также извлечь причину и место подписи.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) фасад для инспектирования цифровых подписей в PDF‑документах. После подписания документа вы можете использовать его для чтения имён подписей и получения метаданных, таких как имя подписанта, контактная информация, время подписи, причина и место.

Этот пример демонстрирует четыре распространённых задачи по работе с информацией о подписи:

1. Перечислите все имена подписей в подписанном PDF.
1. Прочитайте детали подписанта для выбранной подписи.
1. Получите дату и время подписи.
1. Прочитайте причину и место подписи.

## Получить имена подписей

Используйте этот метод, когда PDF может содержать одну или несколько подписей, и вы хотите проверить, какие записи подписи доступны. Пример открывает документ и выводит список, возвращённый `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## Получить сведения о подписанте

Как только вы узнаете название подписи, вы можете получить метаданные, специфичные для подписанта. В этом примере читаются имя подписанта и контактная информация для первой доступной подписи в документе.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## Получить дату и время подписи

Используйте `get_date_time()` чтобы определить, когда была применена конкретная подпись. Это полезно для аудита и отображения истории подписей в рабочих процессах с документами.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## Получить причину подписи и местоположение

Цифровые подписи также могут хранить описательные метаданные, такие как причина подписи и место её создания. В этом примере оба значения извлекаются для выбранной подписи и выводятся вместе.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```

