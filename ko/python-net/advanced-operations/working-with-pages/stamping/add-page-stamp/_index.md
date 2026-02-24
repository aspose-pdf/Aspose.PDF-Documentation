---
title: Python으로 PDF에 페이지 스탬프 추가
linktitle: 페이지 스탬프 추가
type: docs
weight: 30
url: /ko/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python via .NET를 사용하면 PDF 파일에 페이지 스탬프를 추가할 수 있습니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 페이지 스탬프를 추가하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Python을 사용하여 PDF 문서에 페이지 스탬프를 추가하는 방법을 설명합니다. 페이지 스탬프를 사용하면 로고, 워터마크 또는 주석과 같은 콘텐츠를 PDF의 특정 페이지에 오버레이하거나 언더레이할 수 있습니다. 예제에서는 기존 PDF를 열고, 다른 PDF 페이지에서 PdfPageStamp 객체를 생성한 뒤, 이를 배경 스탬프로 구성하고 특정 페이지에 적용하는 방법을 보여줍니다. 스탬프가 적용된 PDF는 새 문서로 저장됩니다. 이 기술은 자동화된 PDF 워크플로에서 브랜딩, 워터마킹 또는 페이지 수준 콘텐츠 강조에 유용합니다.
---

Aspose.PDF for Python via .NET는 PDF의 특정 페이지에 페이지 스탬프(워터마크 또는 오버레이)를 적용하는 방법을 보여줍니다 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). 페이지 스탬프는 배경 또는 전경 레이어로 사용되는 기존 PDF 페이지일 수 있습니다 (see [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). 로고, 워터마크 또는 기타 반복적인 페이지 콘텐츠를 추가하는 데 유용합니다.

1. `ap.Document()`를 사용하여 PDF 문서를 엽니다 (see [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. 스탬프로 사용할 PDF 페이지 또는 파일을 이용하여 `PdfPageStamp` 객체를 생성합니다 (see [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. 스탬프 속성을 설정합니다. 예: 콘텐츠 뒤에 배치하려면 `background = True`로 지정합니다.
1. `document.pages[page_number].add_stamp(page_stamp)`를 사용하여 특정 페이지에 스탬프를 추가합니다 (see [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) and [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)를 사용하여 수정된 PDF를 지정된 출력 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

