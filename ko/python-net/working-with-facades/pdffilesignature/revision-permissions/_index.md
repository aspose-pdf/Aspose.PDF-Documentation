---
title: 개정 및 사용 권한
type: docs
weight: 40
url: /ko/python-net/revision-permissions/
description: Python에서 PDFFileSignature를 사용하여 PDF 파일의 서명 개정, 문서 개정 및 인증 권한을 검사하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 서명 수정 및 액세스 권한 데이터 읽기
Abstract: 이 문서에서는 .NET을 통해 Python용 Aspose.PDF 파일을 사용하여 서명되거나 인증된 PDF 파일의 수정 및 권한 정보를 검사하는 방법을 설명합니다.이 문서에서는 서명의 수정 번호를 얻고, 전체 문서 수정 횟수를 계산하고, 인증된 PDF에서 읽기 액세스 권한을 얻는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 서명되고 인증된 PDF 문서 작업을 위한 외관.서명을 추가하는 것 외에도 서명 메타데이터를 검사하여 문서에 포함된 수정 버전 수와 인증 후 허용되는 변경 사항을 파악할 수 있습니다.

이 예에서는 세 가지 일반적인 검사 작업을 보여줍니다.

1. 기존 서명의 수정 번호를 가져옵니다.
1. 서명된 문서의 총 수정 횟수를 가져옵니다.
1. 인증된 PDF에서 액세스 권한을 읽어 보십시오.

## 서명의 수정 번호 가져오기

PDF에 이미 하나 이상의 서명이 포함되어 있고 특정 서명과 관련된 수정 버전을 식별해야 하는 경우 이 방법을 사용하십시오.이 예제에서는 사용 가능한 첫 번째 서명 이름을 확인한 다음 호출합니다. `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## 전체 문서 수정 횟수 가져오기

용도 `get_total_revision()` 서명된 PDF에 얼마나 많은 수정이 저장되어 있는지 알아야 할 때.이는 원본 서명이 적용된 후 문서가 여러 번 업데이트되었는지 여부를 확인하는 데 유용합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## 인증된 PDF에서 액세스 권한 받기

인증 문서는 인증 후 허용되는 변경 사항을 정의할 수 있습니다.용도 `get_access_permissions()` 해당 권한 수준을 검사하여 문서에 변경, 양식 작성 또는 기타 통제된 수정이 허용되지 않는지 확인합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```

