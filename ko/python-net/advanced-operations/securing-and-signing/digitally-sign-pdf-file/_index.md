---
title: Python에서 디지털 서명을 추가하거나 PDF에 디지털 서명하기
linktitle: PDF에 디지털 서명
type: docs
weight: 10
url: /ko/python-net/digitally-sign-pdf-file/
description: Python을 사용하여 PDF 문서에 디지털 서명을 하고, 서명된 PDF를 확인하거나 검증합니다.
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 파일에 디지털 서명
Abstract: 이 가이드는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 디지털 서명을 하는 방법을 설명합니다. 표준 및 고급 디지털 서명을 적용하고, 인증서(PFX 및 PKCS#12)를 활용하며, 서명 모양과 동작을 사용자 정의하는 과정을 자세히 다룹니다. 문서에는 기존 PDF에 서명하고, 타임스탬프를 추가하며, 서명의 유효성을 확인하는 코드 예제가 포함되어 있습니다. 이를 통해 개발자는 Python 애플리케이션에서 문서의 진위성, 무결성 및 디지털 서명 표준 준수를 보장할 수 있습니다.
---

## 디지털 서명으로 PDF 서명하기

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 object for sign
            pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

A **PKCS#7 detached signature**는 서명 블록에 내용을 포함시키지 않고 문서에 디지털 서명을 추가합니다.

다음 예제는 PKCS#7 detached 디지털 서명을 사용하여 PDF 문서에 서명하고, 지정된 사각형 영역의 첫 페이지에 서명을 적용합니다.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object using the opened document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 detached object for sign
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

이 Python 코드 스니펫은 'file_sign.verify_signature()' 메서드를 사용하여 PDF 파일의 디지털 서명을 검증합니다.

1. PDF의 서명과 상호작용할 수 있는 PdfFileSignature 인스턴스를 생성합니다.
1. 서명 이름 목록을 가져옵니다 `get_signature_names(True)`.
1. 목록의 첫 번째 서명 `verify_signature`을 확인하여 지정된 인증서와의 일치를 검사합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

## 디지털 서명에 타임스탬프 추가

### 타임스탬프와 함께 PDF에 디지털 서명하는 방법

Aspose.PDF for Python은 타임스탬프 서버 또는 웹 서비스를 사용하여 PDF에 디지털 서명을 지원합니다.

이 요구 사항을 달성하기 위해 Aspose.PDF 네임스페이스에 [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) 클래스를 추가했습니다. 다음 코드 스니펫을 확인하십시오. 이 코드는 타임스탬프를 가져와 PDF 문서에 추가합니다:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(path_pfxfile, password)
            # Create TimestampSettings settings
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## ECDSA를 사용한 PDF 문서 서명

ECDSA(타원곡선 디지털 서명 알고리즘)를 사용하여 PDF 문서에 서명하는 것은 타원곡선 암호화를 활용해 디지털 서명을 생성하는 것을 포함합니다.

위의 코드 스니펫은 Aspose.PDF for Python을 사용하여 PDF 문서에 PKCS#7 detached 디지털 서명을 적용하는 방법을 보여줍니다. 문서를 로드하고, 서명 모양 및 보안 설정을 구성한 뒤 결과를 저장함으로써, 이 예제는 PDF 파일에 디지털 서명을 하는 완전하고 신뢰할 수 있는 워크플로를 시연합니다.

이 방법은 첫 페이지에 안전하고 검증 가능한 서명을 삽입함으로써 문서의 진위성과 무결성을 보장합니다. 해시 알고리즘으로 SHA-256을 사용하여 최신 암호화 표준을 충족하고, 서명 위치를 제어할 수 있어 가시적인 승인 표시를 유연하게 적용할 수 있습니다.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature to sign the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create a PKCS7Detached object using the provided certificate and password
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
