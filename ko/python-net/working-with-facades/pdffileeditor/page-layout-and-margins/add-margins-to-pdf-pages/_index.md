---
title: PDF 페이지에 여백 추가
type: docs
weight: 10
url: /ko/python-net/add-margins-to-pdf-pages/
description: Python용 Aspose.PDF 파일을 사용하여 PDF의 선택된 페이지에 사용자 지정 여백을 추가합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 특정 PDF 페이지에 사용자 지정 여백 추가
Abstract: Python용 Aspose.PDF 파일을 사용하여 PDF의 선택된 페이지에 사용자 지정 여백을 추가하는 방법을 알아봅니다.이 예제에서는 개별 페이지의 위쪽, 아래쪽, 왼쪽 및 오른쪽 여백을 지정하여 페이지 경계를 확장하여 PDF의 인쇄 가능성과 시각적 일관성을 높이는 방법을 보여줍니다.
---

PDF 페이지에 여백을 추가하면 가독성이 향상되고 인쇄할 문서를 준비하거나 주석을 달 공간을 할당할 수 있습니다.개발자는 Aspose.PDF for Python을 사용하여 내용 레이아웃을 수정하지 않고도 프로그래밍 방식으로 PDF의 특정 페이지에 여백을 추가할 수 있습니다.

이 코드 스니펫에서는 [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 클래스는 입력 문서의 페이지 1과 3에 0.5인치 여백을 추가하는 데 사용됩니다.여백은 포인트 (1인치=72포인트) 단위로 정의되며 각 페이지의 왼쪽, 오른쪽, 위쪽, 아래쪽에 개별적으로 적용됩니다.

1. 원본 PDF 문서를 엽니다.
1. 'PDF 파일 편집기' 인스턴스를 생성합니다.
1. 수정할 여백과 페이지를 정의합니다.
1. 'add_margins' 메서드를 사용하여 여백을 적용합니다.
1. 업데이트된 PDF를 출력 파일에 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
