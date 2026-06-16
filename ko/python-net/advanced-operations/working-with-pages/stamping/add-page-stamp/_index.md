---
title: Python에서 PDF에 페이지 스탬프 추가
linktitle: 페이지 스탬프 추가
type: docs
weight: 30
url: /ko/python-net/page-stamps-in-the-pdf-file/
description: Python에서 PDF 페이지 스탬프를 오버레이 또는 배경으로 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 페이지 스탬프를 추가하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에 페이지 스탬프를 추가하는 방법을 설명합니다.페이지 스탬프를 사용하면 로고, 워터마크 또는 주석과 같은 내용을 PDF의 특정 페이지에 오버레이하거나 언더레이할 수 있습니다.이 예제에서는 기존 PDF를 열고, 다른 PDF 페이지에서 PDFPageStamp 객체를 만들고, 이를 배경 스탬프로 구성하고, 특정 페이지에 적용하는 방법을 보여줍니다.그러면 스탬프가 찍힌 PDF가 새 문서로 저장됩니다.이 기법은 자동화된 PDF 워크플로우에서 페이지 수준의 내용을 브랜딩하거나 워터마킹하거나 강조하는 데 유용합니다.
---

.NET을 통한 Python용 Aspose.PDF 는 PDF의 특정 페이지에 페이지 스탬프 (워터마크 또는 오버레이) 를 적용하는 방법을 보여줍니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).페이지 스탬프는 배경 또는 전경 레이어로 사용되는 기존 PDF 페이지일 수 있습니다 (참조 [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).이는 로고, 워터마크 또는 기타 반복적인 페이지 콘텐츠를 추가하는 데 유용합니다.

1. 를 사용하여 PDF 문서 열기 `ap.Document()` (참조 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. 만들기 `PdfPageStamp` 스탬프로 사용할 PDF 페이지 또는 파일을 사용하는 객체 (참조 [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. 스탬프 속성을 설정합니다. 예: `background = True` 콘텐츠 뒤에 배치합니다.
1. 를 사용하여 특정 페이지에 스탬프 추가 `document.pages[page_number].add_stamp(page_stamp)` (참조 [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 과 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. 를 사용하여 수정한 PDF를 지정된 출력 파일에 저장합니다. [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## 관련 스탬핑 주제

- [파이썬으로 PDF 페이지에 스탬프 찍기](/pdf/ko/python-net/stamping/)
- [파이썬에서 PDF에 페이지 번호 추가](/pdf/ko/python-net/add-page-number/)
- [Python에서 PDF에 이미지 스탬프 추가](/pdf/ko/python-net/image-stamps-in-pdf-page/)
- [Python에서 PDF에 텍스트 스탬프 추가](/pdf/ko/python-net/text-stamps-in-the-pdf-file/)