---
title: Python에서 디지털 서명 추가 또는 PDF에 디지털 서명
linktitle: PDF에 디지털 서명
type: docs
weight: 10
url: /ko/python-net/digitally-sign-pdf-file/
description: Python에서 PDF 문서에 디지털 서명하고, 타임스탬프를 추가하고, 서명의 유효성을 검사하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬으로 PDF 파일에 디지털 서명
Abstract: 이 가이드에서는 파이썬용 Aspose.PDF 파일을.NET을 통해 PDF 문서에 디지털 서명하는 방법을 설명합니다.표준 및 고급 디지털 서명을 적용하고, 인증서 (PFX 및 PKCS #12) 를 활용하고, 서명 모양과 동작을 사용자 지정하는 프로세스를 자세히 설명합니다.설명서에는 기존 PDF에 서명하고, 타임스탬프를 추가하고, 서명 유효성을 확인하는 방법을 보여주는 코드 예제가 포함되어 있습니다.이를 통해 개발자는 Python 애플리케이션에서 문서의 신뢰성, 무결성 및 디지털 서명 표준 준수를 보장할 수 있습니다.
---

## 디지털 서명으로 PDF에 서명

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**PKCS #7 분리 서명**은 콘텐츠를 서명 블록에 포함하지 않고 문서에 디지털 서명을 추가합니다.

PDF 파일에 인증서 기반 서명을 적용하거나, 서명의 유효성을 확인하거나, 서명된 문서에 신뢰할 수 있는 타임스탬프를 추가해야 할 때 이러한 예를 사용하십시오.

다음 예제에서는 PKCS #7 분리 디지털 서명을 사용하여 지정된 사각형 영역의 첫 페이지에 서명을 적용하여 PDF 문서에 서명합니다.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**PDF 문서의 모든 디지털 서명 확인**

1. PDF의 서명과 상호 작용할 수 있는 PDFFileSignature 인스턴스를 만듭니다.
1. 서명 이름 목록 가져오기 `get_signature_names(True)`.
1. 목록의 첫 번째 서명을 확인합니다. `verify_signature` 지정된 인증서를 준수하기 위해

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**공개 키 인증서 파일로 서명 확인**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

**파일에서 추출한 인증서로 서명 확인**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**인증서 체인 검증이 활성화된 상태에서 서명 확인**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## 디지털 서명에 타임스탬프 추가

### 타임스탬프로 PDF에 디지털 서명하는 방법

Python용 Aspose.PDF 는 타임스탬프 서버 또는 웹 서비스를 사용하여 PDF에 디지털 서명을 할 수 있도록 지원합니다.

이 요구 사항을 충족하기 위해 [타임스탬프 설정](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) 클래스가 Aspose.PDF 네임스페이스에 추가되었습니다.타임스탬프를 가져와 PDF 문서에 추가하는 다음 코드 스니펫을 살펴보세요.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## ECDSA를 사용하여 PDF 문서에 서명

ECDSA (타원 곡선 디지털 서명 알고리즘) 를 사용하여 PDF 문서에 서명하려면 타원 곡선 암호화를 활용하여 디지털 서명을 생성해야 합니다.

위의 코드 스니펫은 Python용 Aspose.PDF 를 사용하여 PDF 문서에 PKCS #7 분리 디지털 서명을 적용하는 방법을 보여줍니다.이 예제에서는 문서를 로드하고, 서명 모양과 보안 설정을 구성하고, 결과를 저장함으로써 PDF 파일에 디지털 서명을 위한 완전하고 안정적인 워크플로우를 보여줍니다.

이 방법은 첫 페이지에 안전하고 확인 가능한 서명을 삽입하여 문서의 신뢰성과 무결성을 보장합니다.SHA-256 알고리즘을 다이제스트 알고리즘으로 사용하면 최신 암호화 표준을 충족할 수 있으며, 서명 배치를 제어할 수 있어 승인 표시를 유연하게 확인할 수 있습니다.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**PDF 문서에서 ECDSA 서명을 확인하십시오**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## 관련 보안 주제

- [파이썬으로 PDF 파일 보안 및 서명](/pdf/ko/python-net/securing-and-signing/)
- [Python에서 이미지 및 서명 정보 추출](/pdf/ko/python-net/extract-image-and-signature-information/)
- [Python에서 스마트 카드에서 PDF 문서에 서명하기](/pdf/ko/python-net/sign-pdf-document-from-smart-card/)
- [Python에서 PDF 파일을 암호화 및 암호 해독하기](/pdf/ko/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)