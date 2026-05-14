---
title: Проверки целостности подписи
type: docs
weight: 70
url: /python-net/signature-integrity-checks/
description: Узнайте, как проверить, охватывает ли подпись PDF весь документ, и подтвердить целостность подписанного документа с помощью PdfFileSignature в Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка охвата подписи PDF и её целостности в Python
Abstract: В этой статье объясняется, как проверять целостность цифровой подписи в подписанных PDF‑документах с помощью Aspose.PDF for Python via .NET. Показано, как проверить, охватывает ли подпись весь документ, и как подтвердить целостность подписанного содержимого.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) фасад для проверки подписанных PDF‑документов. После того как файл подписан, вы можете использовать его, чтобы проверить, применяется ли подпись ко всему документу и всё ли ещё действительна подписанная информация.

В этом примере демонстрируются два распространённых контроля целостности:

1. Проверьте, покрывает ли подпись весь документ.
1. Проверьте целостность подписанного содержимого PDF.

## Проверьте, покрывает ли подпись весь документ

Использовать `covers_whole_document()` когда необходимо подтвердить, что подпись применяется к полному PDF, а не только к части его содержимого. Пример считывает первое доступное имя подписи и проверяет её охват.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## Проверка целостности документа

Используйте `verify_signed()` чтобы подтвердить, что содержимое подписанного документа не было изменено после применения подписи. Этот метод помогает проверить, остается ли документ действительным для выбранной подписи.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

