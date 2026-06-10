---
title: 파이썬으로 PDF 파일 만들기
linktitle: PDF 문서 만들기
type: docs
weight: 10
url: /ko/python-net/create-pdf-document/
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 파이썬에서 PDF 파일을 만들고 검색 가능한 PDF를 작성하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬으로 PDF 파일 만들기
Abstract: .NET을 통한 파이썬용 Aspose.PDF 는 개발자가.NET 프레임워크를 대상으로 하는 파이썬 응용 프로그램 내에서 PDF 파일을 조작할 수 있도록 설계된 다용도 API입니다.이를 통해 사용자는 PDF 문서를 손쉽게 작성, 로드, 수정 및 변환할 수 있습니다.이 문서에서는 Aspose.PDF 를 사용하여 간단한 PDF 파일을 만드는 방법을 단계별로 설명합니다.이 프로세스에는 '문서' 객체 초기화, 문서에 '페이지' 추가, 페이지 단락에 'TextFragment'를 삽입하고 파일을 PDF로 저장하는 작업이 포함됩니다.포함된 Python 코드 스니펫은 “Hello World!” 텍스트가 포함된 PDF 문서를 만들어 이러한 단계를 보여줍니다.이 API는 최소한의 코드로 PDF 처리를 간소화하여.NET 환경에서 PDF로 작업하는 개발자의 생산성을 향상시킵니다.
---

**.NET을 통한 파이썬용 Aspose.pdf**는 개발자가 단 몇 줄의 코드만으로.NET 응용 프로그램용 파이썬에서 직접 PDF 파일을 작성, 로드, 수정 및 변환할 수 있는 PDF 조작 API입니다.

새 PDF 파일을 처음부터 생성하거나 OCR 출력을 Python에서 검색 가능한 PDF 문서로 변환해야 할 때 이 예제를 사용하십시오.

## 간단한 PDF 파일을 만드는 방법

.NET을 통해 Aspose.PDF 파일을 사용하여 Python을 사용하여 PDF를 만들려면 다음 단계를 따르세요.

1. 의 객체 생성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업
1. 추가 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 에 대한 반대 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 문서 객체의 컬렉션
1. 추가 [텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 에 [문단](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 페이지 컬렉션
1. 결과 PDF 문서 저장

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## 검색 가능한 PDF 문서를 만드는 방법

.NET을 통한 파이썬용 Aspose.PDF 파일을 사용하면 기존 PDF 문서를 만들고 조작할 수 있습니다.PDF 파일에 텍스트 요소를 추가하면 결과 PDF를 검색할 수 있습니다.그러나 텍스트가 포함된 이미지를 PDF 파일로 변환할 때는 결과 PDF의 내용을 검색할 수 없습니다.이 문제를 해결하려면 결과 파일에 OCR을 적용하여 검색 가능하게 만들 수 있습니다.

다음은 이 요구 사항을 충족하기 위한 전체 코드입니다.

1. 'AP.Document'를 사용하여 PDF를 로드합니다.
1. 렌더링 해상도를 구성합니다.
1. 선택한 PDF 페이지를 이미지로 변환하려면 'PNGDevice.Process'를 사용하십시오.
1. 생성된 이미지에서 OCR을 실행합니다.
1. OCR 출력에서 새 PDF를 생성합니다.
1. 검색 가능한 PDF를 저장합니다.

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## 관련 문서 주제

- [파이썬에서 PDF 문서로 작업하기](/pdf/ko/python-net/working-with-documents/)
- [파이썬으로 PDF 문서 포맷 지정하기](/pdf/ko/python-net/formatting-pdf-document/)
- [파이썬에서 PDF 문서 조작하기](/pdf/ko/python-net/manipulate-pdf-document/)
- [파이썬에서 PDF 파일 최적화하기](/pdf/ko/python-net/optimize-pdf/)

