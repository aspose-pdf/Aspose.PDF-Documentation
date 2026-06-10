---
title: 시그니처 정보
type: docs
weight: 60
url: /ko/python-net/signature-information/
description: Python에서 PDFFileSignature를 사용하여 서명된 PDF 파일에서 서명 이름, 서명자 세부 정보, 타임스탬프 및 서명 메타데이터를 읽는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 문서의 서명 세부 정보 읽기
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 서명된 PDF 문서의 서명 메타데이터를 검사하는 방법을 설명합니다.서명 이름을 나열하고, 서명자 세부 정보를 읽고, 서명 날짜 및 시간을 가져오고, 서명 이유와 위치를 추출하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) PDF 문서의 디지털 서명을 검사하기 위한 외관.문서에 서명이 완료되면 이를 사용하여 서명 이름을 읽고 서명자 이름, 연락처 정보, 서명 시간, 이유 및 위치와 같은 메타데이터를 검색할 수 있습니다.

이 예에서는 네 가지 일반적인 서명 정보 작업을 보여 줍니다.

1. 서명된 PDF의 모든 서명 이름을 나열합니다.
1. 선택한 서명에 대한 서명자 세부 정보를 읽습니다.
1. 서명 날짜 및 시간을 확인하세요.
1. 서명 이유와 위치를 읽어 보십시오.

## 서명 이름 가져오기

PDF에 하나 이상의 서명이 포함되어 있고 사용 가능한 서명 항목을 검사하려는 경우 이 방법을 사용하십시오.이 예제에서는 문서를 열고 에서 반환한 목록을 인쇄합니다. `get_sign_names()`.

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

## 서명자 세부 정보 가져오기

서명 이름을 알면 서명자별 메타데이터를 검색할 수 있습니다.이 예제에서는 문서에서 사용 가능한 첫 번째 서명에 대한 서명자 이름과 연락처 정보를 읽습니다.

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

## 서명 날짜 및 시간 가져오기

용도 `get_date_time()` 특정 서명이 적용된 시기를 결정합니다.이는 문서 워크플로우에서 서명 기록을 감사하고 표시하는 데 유용합니다.

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

## 서명 이유 및 위치 가져오기

디지털 서명에는 서명 이유 및 위치와 같은 설명 메타데이터도 저장할 수 있습니다.이 예제에서는 선택한 서명의 두 값을 모두 검색하여 함께 인쇄합니다.

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

