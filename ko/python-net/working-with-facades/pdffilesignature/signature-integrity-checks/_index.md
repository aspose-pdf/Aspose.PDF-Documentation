---
title: 서명 무결성 검사
linktitle: 서명 무결성 검사
type: docs
weight: 70
url: /ko/python-net/signature-integrity-checks/
description: Python에서 PDFFileSignature를 사용하여 PDF 서명이 전체 문서를 포함하는지 확인하고 서명된 문서 무결성을 검증하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 서명 적용 범위 및 무결성 검증하기
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 서명된 PDF 문서의 디지털 서명 무결성을 검사하는 방법을 설명합니다.서명이 전체 문서를 포함하는지 확인하는 방법과 서명된 콘텐츠의 무결성을 검증하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 서명된 PDF 문서의 유효성을 검사하기 위한 외관.파일에 서명이 완료되면 이를 사용하여 서명이 전체 문서에 적용되는지 여부와 서명된 내용이 여전히 유효한지 확인할 수 있습니다.

이 예제는 두 가지 일반적인 무결성 검사를 보여줍니다.

1. 서명이 문서 전체를 덮는지 확인합니다.
1. 서명된 PDF 콘텐츠의 무결성을 검증합니다.

## 서명이 문서 전체를 덮는지 확인

용도 `covers_whole_document()` 서명이 내용 일부에만 적용되는 것이 아니라 전체 PDF에 적용되는지 확인해야 하는 경우이 예제에서는 사용 가능한 첫 번째 서명 이름을 읽고 적용 범위를 확인합니다.

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

## 문서 무결성 검증

용도 `verify_signed()` 서명이 적용된 후 서명된 문서 내용이 변경되지 않았는지 확인합니다.이 방법을 사용하면 선택한 서명에 대해 문서가 유효한지 확인할 수 있습니다.

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

