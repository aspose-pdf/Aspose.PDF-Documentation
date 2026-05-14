---
title: Управление подписями
linktitle: Управление подписями
type: docs
weight: 80
url: /python-net/signature-management/
description: Узнайте, как удалять цифровые подписи из PDF‑документов и при необходимости очищать поля подписи, используя PdfFileSignature в Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление подписей PDF и очистка полей подписи в Python
Abstract: В этой статье объясняется, как управлять существующими цифровыми подписями в PDF‑документах с помощью Aspose.PDF for Python via .NET. Показано, как удалить подпись из PDF и как удалить подпись вместе с соответствующим полем подписи.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Фасад для работы с существующими цифровыми подписями в PDF‑документах. Помимо чтения и проверки подписей, вы также можете удалять их, когда процесс требует обновления подписанного содержимого или очистки поля подписи.

Этот пример демонстрирует две распространённые задачи управления подписями:

1. Удалить подпись из PDF‑документа.
1. Удалить подпись и очистить связанное поле подписи.

## Удалить подпись из PDF

Используйте `remove_signature()` когда вы хотите удалить выбранную подпись из документа, сохраняя при этом структуру поля подписи. В примере открывается подписанный PDF, определяется имя подписи, удаляется и сохраняется обновлённый выходной файл.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Удалить подпись и очистить поле

Используйте перегрузку с дополнительным `True` флаг, когда вы хотите удалить подпись и также очистить связанное поле подписи. Это полезно, когда поле не должно оставаться в документе после удаления подписи.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
