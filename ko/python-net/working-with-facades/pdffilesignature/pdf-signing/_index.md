---
title: PDF 문서에 서명
type: docs
weight: 10
url: /ko/python-net/pdf-signing/
description: 인증서 기반의 이름이 지정되고 가시적인 디지털 서명이 포함된 PDFFileSignature를 사용하여 Python에서 PDF 문서에 서명하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 디지털 서명으로 PDF 문서에 서명
Abstract: 이 문서에서는 PDFFileSignature 파사드를 사용하여.NET을 통해 파이썬용 Aspose.PDF 파일로 PDF 문서에 서명하는 방법을 보여줍니다.인증서 구성, 기본 매개 변수를 사용한 서명, PKCS7 객체로 서명, 서명 이름 지정, 가시적인 서명 모양 적용 등을 다룹니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 기존 PDF 문서에 디지털 서명을 적용하기 위한 외관.인증서 파일을 사용하여 프로그래밍 방식으로 문서에 서명하고, 페이지에 서명을 배치하고, 서명 메타데이터를 할당하고, 서명이 표시되는 방식을 사용자 지정할 수 있습니다.

이 문서에서는 몇 가지 일반적인 서명 워크플로를 보여줍니다.

1. a 생성 및 바인딩 `PdfFileSignature` 입력 PDF의 대상입니다.
1. 서명 인증서를 구성합니다.
1. 대상 페이지에 디지털 서명을 적용합니다.
1. 선택적으로 서명 이름과 눈에 보이는 모양을 지정할 수 있습니다.
1. 서명된 PDF를 저장합니다.

## 재사용 가능한 서명 도우미 준비

PDF에 디지털 서명을 적용하기 전에 재사용 가능한 도우미 함수를 소그룹으로 설정하는 것이 좋습니다.이러한 도우미는 서명 핸들러를 초기화하고, 가시적인 서명 영역을 정의하고, 인증서를 구성하고, 재사용 가능한 PKCS #7 서명 객체를 만들어 아래의 서명 예제가 독립적이고 쉽게 따라할 수 있도록 합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(
    pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(
    certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```

## 기본 인증서 매개 변수로 PDF에 서명

이 접근 방식은 에서 직접 인증서를 구성합니다. `PdfFileSignature` 목적.표준 서명 메타데이터를 사용하고 별도의 서명 객체 관리 없이 간단한 서명 흐름을 원할 때 유용합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_basic_parameters(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature, certificate_path)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## PKCS7 개체가 포함된 PDF에 서명

a를 사용하세요 `PKCS7` 먼저 서명을 준비한 다음 서명 호출에 전달해야 하는 경우 객체를 지정합니다.이 패턴을 사용하면 서명 설정을 더 세밀하게 제어할 수 있으며 고급 워크플로를 위한 좋은 기반이 됩니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_certificate_object(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 이름이 지정된 서명으로 PDF에 서명

문서 워크플로에서 사전 정의된 서명 필드 이름을 사용하는 경우 해당 이름을 에 전달하십시오. `sign()`.이렇게 하면 나중에 서명을 참조하여 검증, 처리 또는 승인 워크플로우와의 통합을 쉽게 수행할 수 있습니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_named_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Approved by signing workflow"
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 눈에 보이는 서명 적용

에 사용자 정의 모양을 지정하여 PDF 페이지에 서명이 표시되도록 할 수 있습니다. `PKCS7` 목적.이는 출력 문서에서 최종 사용자에게 이유, 위치 및 연락처 정보와 같은 승인 세부 정보를 표시해야 할 때 유용합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_visible_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Visible approval signature"
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
