---
title: 시그니처 검증
linktitle: 시그니처 검증
type: docs
weight: 90
url: /ko/python-net/signature-verification/
description: Python에서 PDFFileSignature를 사용하여 디지털 서명을 확인하고 PDF에 서명이 포함되어 있는지 확인하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 PDF 서명 확인
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 디지털 서명을 확인하는 방법을 설명합니다.기존 서명의 유효성을 검사하는 방법과 PDF에 서명이 포함되어 있는지 확인하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 서명된 PDF 문서의 유효성을 검사하기 위한 외관.PDF에 서명이 완료되면 이를 사용하여 서명이 유효한지 확인하고 문서에 서명 항목이 포함되어 있는지 확인할 수 있습니다.

이 예에서는 두 가지 일반적인 확인 작업을 보여줍니다.

1. 기존 PDF 서명이 유효한지 확인합니다.
1. PDF에 서명이 포함되어 있는지 확인합니다.

## PDF 서명 확인

용도 `verify_signature()` 문서의 특정 서명의 유효성을 검사해야 할 때.이 예제에서는 사용 가능한 첫 번째 서명 이름을 확인하고 해당 서명이 유효한지 여부를 확인합니다.

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

## PDF에 서명이 포함되어 있는지 확인

용도 `contains_signature()` PDF에 서명이 포함되어 있는지 여부만 알면 됩니다.이는 보다 상세한 검증 또는 추출 로직을 실행하기 전에 빠르게 확인하는 데 유용합니다.

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
