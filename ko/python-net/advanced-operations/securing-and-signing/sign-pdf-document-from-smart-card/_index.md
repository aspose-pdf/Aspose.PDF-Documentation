---
title: Python에서 스마트 카드에서 PDF 문서에 서명하기
linktitle: 스마트 카드를 사용한 PDF 서명
type: docs
weight: 30
url: /ko/python-net/sign-pdf-document-from-smart-card/
description: Python에서 스마트 카드 및 외부 인증서로 PDF 문서에 서명하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 스마트 카드에서 PDF 문서에 서명하기
Abstract: >
    이 가이드에서는 .NET을 통해 Python용 Aspose.PDF 스마트 카드를 사용하여 PDF 문서에 디지털 서명하는 방법을 설명합니다.Windows 인증서 저장소를 통해 하드웨어 장치 (예: USB 토큰 또는 스마트 카드) 에 저장된 인증서에 액세스하고 이를 PDF 파일 서명에 적용하는 방법을 보여줍니다.설명서에는 적절한 인증서를 찾고, 서명 속성을 구성하고, PDF에 디지털 서명을 포함하는 방법을 보여주는 코드 예제가 포함되어 있습니다.이를 통해 디지털 서명 표준을 준수하는 하드웨어 기반 보안 서명이 가능하므로 신뢰도가 높은 기업 및 법률 워크플로우에 적합합니다.
---

Aspose.PDF 는 시각적 서명 구성 요소와 암호화 서명 구성 요소를 통합하는 강력한 기능을 제공하여 디지털 서명된 PDF 문서의 신뢰성과 전문적인 프레젠테이션을 모두 보장합니다.

서명 프로세스가 스마트 카드, USB 토큰 또는 관리형 인증서 저장소와 같은 하드웨어 지원 장치에 저장된 인증서에 의존하는 경우 이 워크플로를 사용하십시오.

## 서명 필드를 사용하여 스마트 카드로 서명

이 예제에서는 Python용 Aspose.PDF 가 포함된 외부 인증서를 사용하여 PDF 문서에 디지털 서명하고 사용자 지정 서명 모양 이미지를 적용하는 방법을 보여줍니다.

1. PDF 문서를 엽니다.
1. PDFFileSignature 객체를 만들어 문서에 바인딩합니다.
1. 사용자 지정 방법을 사용하여 로컬 디지털 인증서 검색 `get_local_certificate()`.
1. 선택한 인증서를 기반으로 외부 서명을 설정합니다.
1. 사용자 지정 서명 모양 이미지 적용 (예: 회사 로고 또는 친필 서명)
1. 지정된 메타데이터 (이유, 연락처, 위치) 를 사용하여 문서의 첫 페이지에 디지털 서명합니다.
1. 서명된 문서를 새 출력 파일에 저장

이 방법은 하드웨어 토큰, 인증서 저장소 또는 신뢰할 수 있는 제공자와 같은 외부 인증서를 사용하여 프로그래밍 방식으로 서명을 적용하고 개인화된 시각적 레이아웃으로 표시해야 하는 경우에 적합합니다.

다음은 스마트 카드에서 PDF 문서에 서명하는 코드 스니펫입니다.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## 디지털 서명 확인

이 코드 스니펫은 Python용 Aspose.PDF 를 사용하여 PDF 문서의 디지털 서명을 확인하는 방법을 보여줍니다.

1. PDF 파일을 엽니다.
1. 'PDF파일 서명 객체'를 만들어 문서에 바인딩합니다.
1. 'get_signature_names () '를 사용하여 모든 서명 필드 이름 목록을 검색합니다.
1. 각 서명을 반복하고 'verify_signature () '를 사용하여 유효성을 확인합니다.
1. 서명이 검증에 실패하면 예외를 발생시킵니다.

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

## 외부 인증서로 서명

이 코드 스니펫은 외부 인증서와 함께 Python용 Aspose.PDF 를 사용하여 PDF 문서에 디지털 서명 필드를 추가하고 서명하는 방법을 보여줍니다.

1. PDF 파일을 바이너리 스트림으로 엽니다.
1. SignatureField를 생성하여 문서의 첫 페이지에 지정된 위치에 배치합니다.
1. 사용자 지정 방법을 사용하여 로컬 디지털 인증서 검색 `get_local_certificate()`.
1. 권한, 이유, 연락처 정보와 같은 메타데이터를 사용하여 외부 서명을 설정합니다.
1. 서명 필드에 고유한 필드 이름 지정 (partial_name = “sig1").
1. PDF의 양식 필드에 서명 필드 추가.
1. 외부 인증서로 필드에 서명합니다.
1. 서명된 문서를 출력 파일에 저장.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## 관련 보안 주제

- [파이썬으로 PDF 파일 보안 및 서명](/pdf/ko/python-net/securing-and-signing/)
- [파이썬으로 PDF 파일에 디지털 서명](/pdf/ko/python-net/digitally-sign-pdf-file/)
- [Python에서 PDF에서 서명 정보를 추출합니다.](/pdf/ko/python-net/extract-image-and-signature-information/)
- [Python에서 PDF 파일을 암호화 및 암호 해독하기](/pdf/ko/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

