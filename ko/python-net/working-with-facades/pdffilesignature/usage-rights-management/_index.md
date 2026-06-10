---
title: 사용 권한 관리
type: docs
weight: 100
url: /ko/python-net/usage-rights-management/
description: Python에서 PDFFileSignature를 사용하여 PDF 문서에서 사용 권한을 감지하고 제거하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 PDF 사용 권한 제거
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 사용 권한을 검사하고 제거하는 방법을 설명합니다.PDF에 사용 권한이 있는지 확인하는 방법과 사용 권한이 제거된 후 새 버전의 문서를 저장하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 서명된 PDF 및 관련 사용 권한 설정 작업을 위한 외관일부 워크플로에서는 파일의 업데이트된 버전을 저장하기 전에 문서에 사용 권한이 있는지 여부를 검사하고 사용 권한을 제거해야 할 수 있습니다.

이 예에서는 일반적인 사용 권한 관리 작업 하나를 보여 줍니다.

1. PDF에 사용 권한이 있는지 확인합니다.
1. 문서에서 사용 권한을 제거합니다.
1. 업데이트된 PDF 파일을 저장합니다.

## PDF에 사용 권한이 있는지 확인

사용 권한을 제거하기 전에 예제에서는 를 호출하여 문서의 현재 상태를 확인합니다. `contains_usage_rights()`.이를 통해 변경하기 전에 사용 권한이 있는지 확인할 수 있습니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## PDF에서 사용 권한 제거

용도 `remove_usage_rights()` 문서가 기존 사용 권한 설정을 더 이상 유지하지 않아야 하는 경우이 예제에서는 초기 상태를 확인하고 권한을 제거한 다음 업데이트된 PDF를 새 파일에 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
