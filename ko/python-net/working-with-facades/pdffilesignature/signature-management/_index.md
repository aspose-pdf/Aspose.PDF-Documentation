---
title: 시그니처 매니지먼트
type: docs
weight: 80
url: /ko/python-net/signature-management/
description: Python의 PDFFileSignature를 사용하여 PDF 문서에서 디지털 서명을 제거하고 선택적으로 서명 필드를 정리하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 서명 제거 및 서명 필드 정리하기
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 기존 디지털 서명을 관리하는 방법을 설명합니다.PDF에서 서명을 제거하는 방법 및 관련 서명 필드와 함께 서명을 제거하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) PDF 문서의 기존 디지털 서명 작업을 위한 외관서명을 읽고 유효성을 검사하는 것 외에도 워크플로우에서 서명된 내용을 업데이트하거나 서명 필드를 지워야 하는 경우 서명을 제거할 수도 있습니다.

이 예에서는 두 가지 일반적인 서명 관리 작업을 보여 줍니다.

1. PDF 문서에서 서명을 제거합니다.
1. 서명을 제거하고 관련 서명 필드를 정리합니다.

## PDF에서 서명 제거

용도 `remove_signature()` 기본 서명 필드 구조를 그대로 유지하면서 문서에서 선택한 서명을 삭제하려는 경우이 예제에서는 서명된 PDF를 열고, 서명 이름을 확인하고, 제거하고, 업데이트된 출력 파일을 저장합니다.

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

## 서명 제거 및 필드 정리

추가 기능과 함께 오버로드 사용 `True` 서명을 제거하고 관련 서명 필드를 정리하려는 경우 플래그를 지정합니다.이는 서명이 삭제된 후 필드가 문서에 남아 있지 않아야 하는 경우에 유용합니다.

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
