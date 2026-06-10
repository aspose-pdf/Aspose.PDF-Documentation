---
title: 복잡한 PDF 만들기
linktitle: 복잡한 PDF 만들기
type: docs
weight: 30
url: /ko/python-net/complex-pdf-example/
description: .NET을 통한 Python용 Aspose.PDF 를 사용하면 하나의 문서에 이미지, 텍스트 조각 및 테이블을 포함하는 더 복잡한 문서를 만들 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 사용하여 복잡한 PDF 만들기
Abstract: 이 문서에서는 Python과 Aspose.PDF 를 사용하여 더 복잡한 PDF 문서를 만드는 방법을 설명함으로써 “Hello, World” 예제에서 설명한 기본 PDF 작성 프로세스를 확장합니다.예제 문서는 가상의 여객 페리 서비스 회사를 위해 개발되었으며 이미지, 두 개의 텍스트 부분 (머리글과 단락) 및 표를 포함합니다.이 프로세스에는 '문서' 객체를 인스턴스화하여 빈 PDF를 만들고, '페이지'를 추가한 다음, 페이지에 '이미지'를 삽입하는 등 여러 단계가 포함됩니다.크기가 24pt이고 가운데 정렬된 Arial 글꼴을 사용하여 머리글에 'TextFragment'를 만든 다음 페이지의 단락에 추가합니다.설명을 위해 두 번째 `TextFragment`가 추가되었는데, 14pt 크기의 Times New Roman 글꼴을 왼쪽 정렬하여 사용합니다.그런 다음 특정 열 너비, 테두리 및 패딩으로 표를 만들고 서식을 지정합니다.테이블에는 강조 표시된 셀이 있는 헤더 행과 반복을 통해 생성된 여러 데이터 행이 포함됩니다.
---

더 [헬로, 월드](/pdf/ko/python-net/hello-world-example/) 예제에서는 Python과 Aspose.PDF 를 사용하여 PDF 문서를 만드는 간단한 단계를 보여 주었습니다.이 글에서는 Aspose.PDF for Python을 사용하여 좀 더 복잡한 문서를 만드는 방법을 살펴보겠습니다.여객 페리 서비스를 운영하는 가상 회사의 문서를 예로 들어 보겠습니다.문서에는 이미지, 텍스트 조각 2개 (머리글과 단락), 표 한 개가 포함됩니다.

처음부터 문서를 만들려면 특정 단계를 따라야 합니다.

1. a 인스턴스화 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 목적.이 단계에서는 페이지가 없는 일부 메타데이터가 포함된 빈 PDF 문서를 만들 것입니다.
1. 추가 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 문서 객체에.자, 이제 문서는 한 페이지가 됩니다.
1. 추가 [이미지](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) 페이지로.
1. 만들기 [텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 헤더용.헤더에는 글꼴 크기가 24pt이고 가운데 정렬이 적용된 Arial 글꼴을 사용합니다.
1. 페이지에 헤더 추가 [문단](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. 만들기 [텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 설명을 위해.설명에는 글꼴 크기가 24pt이고 가운데 정렬이 적용된 Arial 글꼴을 사용합니다.
1. 페이지 단락에 설명을 추가합니다.
1. 테이블 만들기 및 스타일 지정열 너비, 테두리, 패딩 및 글꼴을 설정합니다.
1. 페이지에 표 추가 [문단](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. “Complex.pdf” 문서를 저장합니다.

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
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
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
