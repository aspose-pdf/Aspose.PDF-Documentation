---
title: Python에서 PDF에서 서명 정보 추출하기
linktitle: 서명에서 세부 정보 추출
type: docs
weight: 20
url: /ko/python-net/extract-image-and-signature-information/
description: Python에서 PDF 파일에서 서명 이미지, 인증서 및 디지털 서명 세부 정보를 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF에서 서명 이미지 및 인증서 세부 정보 추출
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 이미지 및 디지털 서명 정보를 추출하는 방법을 설명합니다.서명 이미지를 검색하고, 인증서 데이터를 추출하고, 서명 알고리즘을 검사하고, 서명된 PDF 파일에서 손상된 서명을 탐지하는 방법을 알아봅니다.
---

## 서명 필드에서 이미지 추출

.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하면 파일에 포함된 시각적 이미지를 검색할 수 있습니다. [시그니처 필드](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/).이는 전체 PDF를 렌더링하지 않고 서명 모양을 표시하거나 보관해야 하는 경우에 유용합니다.

아래 예제는 모든 양식 필드를 반복하여 각각을 찾습니다. `SignatureField`이미지를 JPEG 파일로 저장합니다.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)
```

## 시그니처 알고리즘 세부 정보 읽기

용도 `PdfFileSignature.get_signatures_info()` 다이제스트 알고리즘, 알고리즘 유형, 암호화 표준 및 서명 이름을 포함하여 문서의 각 서명에 대한 암호화 메타데이터를 읽으려면:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)
```

## 서명 필드에서 디지털 인증서 추출

사용 [추출_인증서](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) a에 대한 메서드 `SignatureField` 내장된 인증서를 바이트 스트림으로 검색하고 외부 검증을 위해 디스크에 저장하려면

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return
```

## PDF 파일 시그니처 파사드를 사용하여 인증서 추출

`PdfFileSignature.try_extract_certificate()` 서명 이름으로 인증서를 검색하는 다른 방법을 제공합니다.다음 예제에서는 모든 서명 이름을 반복하고 각각에 대해 추출을 시도합니다.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")
```

## 외부 디지털 서명 확인

서명 후 문서가 수정되지 않았는지 확인하려면 다음을 사용하여 각 외부 서명을 확인하십시오. `PdfFileSignature.verify_signature()`.아래 예에서는 검증에 실패한 모든 서명에 대해 예외를 발생시킵니다.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## 손상된 시그니처 감지

`SignaturesCompromiseDetector` 후속 변경으로 인해 문서의 디지털 서명이 무효화되었는지 여부를 확인합니다.문서 무결성이 보장되어야 하는 법률, 재무 또는 규정 준수 워크플로우에서 이 기능을 사용하십시오.

아래 예에서는 손상된 서명이 있는지 확인하고 문서의 전체 서명 범위와 함께 해당 이름을 보고합니다.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)
```

## 관련 보안 주제

- [파이썬으로 PDF 파일 보안 및 서명](/pdf/ko/python-net/securing-and-signing/)
- [파이썬으로 PDF 파일에 디지털 서명](/pdf/ko/python-net/digitally-sign-pdf-file/)
- [Python에서 스마트 카드에서 PDF 문서에 서명하기](/pdf/ko/python-net/sign-pdf-document-from-smart-card/)
- [Python에서 PDF 파일을 암호화 및 암호 해독하기](/pdf/ko/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
