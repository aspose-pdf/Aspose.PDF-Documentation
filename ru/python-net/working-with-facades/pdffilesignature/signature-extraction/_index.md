---
title: Извлечение подписи
type: docs
weight: 50
url: /python-net/signature-extraction/
description: Узнайте, как извлечь изображение подписи и сертификат подписи из подписанного PDF, используя PdfFileSignature в Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение изображения подписи и сертификата из PDF в Python
Abstract: В этой статье объясняется, как извлекать данные, связанные с подписью, из подписанных PDF‑документов с помощью Aspose.PDF for Python via .NET. Показано, как прочитать первую доступную подпись, экспортировать её изображение и сохранить связанный поток сертификата в выходной файл.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) фасад для проверки и извлечения данных из подписанных PDF‑документов. После подписания PDF вы можете использовать его для экспорта ресурсов подписи, таких как визуальное изображение подписи и сертификат, связанный с подписью.

В этом примере демонстрируются два распространённых задания по извлечению:

1. Извлечь визуальное изображение, связанное с подписью.
1. Извлечь сертификат подписи из подписанного PDF.

## Извлечь изображение подписи

Используйте этот метод, когда PDF содержит видимую подпись и вы хотите экспортировать данные её изображения. В примере открывается подписанный документ, получается первое доступное имя подписи, извлекается поток изображения и записывается в файл.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## Извлечь сертификат подписи

Используйте `extract_certificate()` когда вам нужны данные сертификата, прикреплённые к подписи. Это полезно для проверки, процессов валидации или отдельного хранения сертификата подписывающего от PDF‑документа.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

