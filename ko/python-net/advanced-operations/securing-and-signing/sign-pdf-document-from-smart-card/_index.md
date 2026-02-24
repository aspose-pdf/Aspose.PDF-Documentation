---
title: 스마트 카드 서명을 PDF에 추가하는 방법
linktitle: 스마트 카드로 PDF 서명
type: docs
weight: 30
url: /ko/python-net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for Python via .NET를 사용하면 서명 필드를 이용해 스마트 카드로 PDF 문서에 서명할 수 있습니다.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 스마트 카드에서 PDF 문서 서명하기
Abstract: 이 가이드는 Aspose.PDF for Python via .NET를 사용하여 스마트 카드를 이용해 PDF 문서에 디지털 서명하는 방법을 설명합니다. Windows 인증서 저장소를 통해 하드웨어 장치(예 USB 토큰 또는 스마트 카드)에 저장된 인증서에 접근하고 이를 PDF 파일 서명에 적용하는 방법을 보여줍니다. 문서에는 적절한 인증서를 찾고, 서명 속성을 구성하며, 디지털 서명을 PDF에 삽입하는 코드 예제가 포함되어 있습니다. 이를 통해 디지털 서명 표준을 준수하는 보안적인 하드웨어 기반 서명이 가능해져, 높은 신뢰가 요구되는 기업 및 법률 워크플로에 적합합니다.
---

Aspose.PDF는 시각적 및 암호화 서명 구성 요소를 통합하는 강력한 기능을 제공하여 디지털 서명 PDF 문서에서 진위와 전문적인 프레젠테이션을 모두 보장합니다.

## 스마트 카드로 서명 필드 사용하여 서명하기

이 예제는 Aspose.PDF for Python을 사용하여 외부 인증서로 PDF 문서에 디지털 서명을 하고 사용자 지정 서명 외관 이미지를 적용하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. PdfFileSignature 객체를 생성하고 문서에 연결합니다.
1. 사용자 정의 메서드 `get_local_certificate()`를 사용하여 로컬 디지털 인증서를 검색합니다.
1. 선택한 인증서를 기반으로 ExternalSignature을 설정합니다.
1. 사용자 지정 서명 외관 이미지(예: 회사 로고 또는 손글씨 서명)를 적용합니다.
1. 지정된 메타데이터(이유, 연락처, 위치)를 사용해 문서 첫 페이지에 디지털 서명을 합니다.
1. 서명된 문서를 새 출력 파일에 저장합니다.

이 방법은 하드웨어 토큰, 인증서 저장소 또는 신뢰할 수 있는 제공자와 같은 외부 인증서를 사용해 프로그래밍 방식으로 서명을 적용하고, 개인화된 시각 레이아웃으로 표시해야 하는 경우에 이상적입니다.

다음은 스마트 카드에서 PDF 문서에 서명하기 위한 코드 스니펫입니다:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pngfile = self.data_dir + pngfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            # Bind PDF document
            pdf_signature.bind_pdf(document)
            selected_certificates = self.get_local_certificate()
            # Set an external signature settings
            external_signature = ap.forms.ExternalSignature(selected_certificates)
            pdf_signature.signature_appearance = path_pngfile
            # Sign the document
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## 디지털 서명 검증

이 코드 스니펫은 Aspose.PDF for Python을 사용하여 PDF 문서의 디지털 서명을 검증하는 방법을 보여줍니다:

1. PDF 파일을 엽니다.
1. 'PdfFileSignature 객체'를 생성하고 문서에 연결합니다.
1. 'get_signature_names()'를 사용하여 모든 서명 필드 이름 목록을 가져옵니다.
1. 각 서명을 반복하면서 'verify_signature()'로 유효성을 검증합니다.
1. 서명 검증에 실패하면 예외를 발생시킵니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            signature_names = pdf_signature.get_signature_names(True)
            for index in range(len(signature_names)):
                if not pdf_signature.verify_signature(signature_names[index]):
                    raise Exception("Not verified")
```

## 외부 인증서로 서명

이 코드 스니펫은 Aspose.PDF for Python과 외부 인증서를 사용하여 PDF 문서에 디지털 서명 필드를 추가하고 서명하는 방법을 보여줍니다:

1. PDF 파일을 바이너리 스트림으로 엽니다.
1. SignatureField를 생성하고 지정된 위치에 문서 첫 페이지에 배치합니다.
1. 사용자 정의 메서드 `get_local_certificate()`를 사용하여 로컬 디지털 인증서를 검색합니다.
1. 권한, 이유, 연락처 정보와 같은 메타데이터를 포함한 ExternalSignature을 설정합니다.
1. 서명 필드에 고유한 필드 이름을 할당합니다(partial_name = "sig1").
1. 서명 필드를 PDF의 폼 필드에 추가합니다.
1. 외부 인증서로 필드에 서명합니다.
1. 서명된 문서를 출력 파일에 저장합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
        selected_certificate = self.get_local_certificate()

        # Set external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"

        # Set a name of signature field
        signature_field.partial_name = "sig1"

        # Add the signature field to the document
        document.form.add(signature_field, 1)

        # Sign the document
        signature_field.sign(external_signature)

        # Save PDF document
        document.save(path_outfile)
```


