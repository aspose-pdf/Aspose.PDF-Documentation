---
title: 복잡한 PDF 만들기
linktitle: 복잡한 PDF 만들기
type: docs
weight: 30
url: /ko/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET는 이미지, 텍스트 조각 및 표가 포함된 보다 복잡한 문서를 하나의 문서에 만들 수 있게 합니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 복잡한 PDF 만들기
Abstract: 이 문서는 "Hello, World" 예제에서 보여준 기본 PDF 생성 프로세스를 확장하여 Python과 Aspose.PDF를 사용해 보다 복잡한 PDF 문서를 만드는 방법을 설명합니다. 예제 문서는 가상의 여객 페리 서비스 회사를 위해 개발되었으며 이미지, 두 개의 텍스트 조각(헤더와 단락), 그리고 표를 포함합니다. 이 과정은 여러 단계로 이루어집니다 - 빈 PDF를 만들기 위해 `Document` 객체를 인스턴스화하고, `Page`를 추가한 뒤 페이지에 `Image`를 삽입합니다. 헤더를 위해 Arial 폰트 24pt 크기와 중앙 정렬을 사용하여 `TextFragment`를 생성하고 이를 페이지의 단락에 추가합니다. 설명을 위해 Times New Roman 폰트 14pt 크기와 왼쪽 정렬을 사용한 두 번째 `TextFragment`를 추가합니다. 그 다음, 특정 열 너비, 테두리 및 패딩으로 표를 생성하고 서식화합니다. 표는 강조된 셀을 가진 헤더 행과 반복을 통해 생성된 여러 데이터 행을 포함합니다.
---

[안녕, 세상](/pdf/python-net/hello-world-example/) 예제는 Python과 Aspose.PDF를 사용하여 PDF 문서를 만드는 간단한 단계를 보여줍니다. 이 문서에서는 Aspose.PDF for Python으로 더 복잡한 문서를 만드는 방법을 살펴봅니다. 예제로, 여객 페리 서비스를 운영하는 가상의 회사 문서를 사용해 보겠습니다. 우리의 문서는 이미지 하나, 두 개의 텍스트 조각(헤더와 단락), 그리고 표를 포함합니다.

문서를 처음부터 만들 경우 특정 단계들을 따라야 합니다:

1. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 인스턴스화합니다. 이 단계에서는 메타데이터가 포함된 빈 PDF 문서를 페이지 없이 생성합니다.
1. 문서 객체에 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 추가합니다. 이제 우리 문서는 한 페이지를 갖게 됩니다.
1. [이미지](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)를 페이지에 추가합니다.
1. 헤더용 [텍스트 조각](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)을 생성합니다. 헤더에는 Arial 폰트를 24pt 크기로 중앙 정렬하여 사용합니다.
1. 헤더를 페이지의 [단락](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties)에 추가합니다.
1. 설명용 [텍스트 조각](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)을 생성합니다. 설명에는 Arial 폰트를 24pt 크기로 중앙 정렬하여 사용합니다.
1. (description)를 페이지의 단락에 추가합니다.
1. 표를 만들고 스타일을 지정합니다. 열 너비, 테두리, 패딩 및 폰트를 설정합니다.
1. (table)를 페이지의 [단락](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties)에 추가합니다.
1. 문서 "Complex.pdf"를 저장합니다.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font(
        "Times New Roman"
    )
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(
        ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray
    )
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOX, 0.5, ap.Color.black
    )
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font(
        "Helvetica"
    )

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = (
            ap.Color.white_smoke
        )
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```

