---
title: Проверка подписи
linktitle: Проверка подписи
type: docs
weight: 90
url: /ru/python-net/signature-verification/
description: Узнайте, как проверять цифровые подписи и проверять, содержит ли PDF подписи, используя PdfFileSignature в Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка подписей PDF в Python
Abstract: В этой статье объясняется, как проверять цифровые подписи в PDF‑документах с помощью Aspose.PDF for Python via .NET. Показано, как подтвердить существующую подпись и как проверить, содержит ли PDF какие‑либо подписи.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) фасад для проверки подписанных PDF‑документов. После того как PDF был подписан, вы можете использовать его, чтобы подтвердить, что подпись действительна, и обнаружить, содержит ли документ какие‑либо записи о подписи.

В этом примере демонстрируются две распространённые задачи проверки:

1. Проверьте, действительна ли существующая подпись PDF.
1. Проверьте, содержит ли PDF какие-либо подписи.

## Проверка подписи PDF

Используйте `verify_signature()` когда вам нужно проверить конкретную подпись в документе. Пример определяет первое доступное имя подписи и проверяет, действительна ли эта подпись.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## Проверьте, содержит ли PDF подписи

Используйте `contains_signature()` когда вам нужно лишь узнать, содержит ли PDF какие-либо подписи вообще. Это полезно как быстрая проверка перед запуском более детальной проверки или извлечения логики.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```

