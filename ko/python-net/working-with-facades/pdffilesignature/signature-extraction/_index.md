---
title: 시그니처 추출
type: docs
weight: 50
url: /ko/python-net/signature-extraction/
description: Python에서 PDFFileSignature를 사용하여 서명된 PDF에서 서명 이미지와 서명 인증서를 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF에서 서명 이미지 및 인증서 추출
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 서명된 PDF 문서에서 서명 관련 데이터를 추출하는 방법을 설명합니다.사용 가능한 첫 번째 서명을 읽고, 해당 이미지를 내보내고, 관련 인증서 스트림을 출력 파일에 저장하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 서명](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 서명된 PDF 문서에서 데이터를 검사하고 추출하기 위한 외관.PDF에 서명이 완료되면 이를 사용하여 시각적 서명 이미지 및 서명과 관련된 인증서와 같은 서명 리소스를 내보낼 수 있습니다.

이 예에서는 두 가지 일반적인 추출 작업을 보여줍니다.

1. 서명과 관련된 시각적 이미지를 추출합니다.
1. 서명된 PDF에서 서명 인증서를 추출합니다.

## 서명 이미지 추출

PDF에 눈에 보이는 서명이 포함되어 있고 해당 이미지 데이터를 내보내려는 경우 이 방법을 사용하십시오.이 예제에서는 서명된 문서를 열고, 사용 가능한 첫 번째 서명 이름을 가져오고, 이미지 스트림을 추출하고, 이를 파일에 씁니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## 서명 인증서 추출

용도 `extract_certificate()` 서명에 인증서 데이터를 첨부해야 하는 경우이는 검사, 검증 워크플로우 또는 서명자 인증서를 PDF 문서와 별도로 저장하는 데 유용합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

