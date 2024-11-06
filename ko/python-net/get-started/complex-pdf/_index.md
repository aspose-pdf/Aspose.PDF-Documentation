---
title: 복잡한 PDF 만들기
linktitle: 복잡한 PDF 만들기
type: docs
weight: 30
url: ko/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET을 사용하면 하나의 문서에 이미지, 텍스트 조각 및 테이블이 포함된 더 복잡한 문서를 만들 수 있습니다.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/python-net/hello-world-example/) 예제는 Python과 Aspose.PDF를 사용하여 PDF 문서를 만드는 간단한 단계를 보여주었습니다. 이 글에서는 Aspose.PDF for Python을 사용하여 더 복잡한 문서를 만드는 방법을 살펴보겠습니다. 예제로 여객 페리 서비스를 운영하는 가상의 회사의 문서를 가져오겠습니다. 우리의 문서에는 이미지, 두 개의 텍스트 조각(헤더 및 단락), 그리고 테이블이 포함될 것입니다.

문서를 처음부터 만들려면 특정 단계를 따라야 합니다:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 인스턴스화합니다. 이 단계에서는 메타데이터가 포함된 빈 PDF 문서를 생성하지만 페이지는 없습니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 추가합니다. 이제 문서에 한 페이지가 추가됩니다.
1. 페이지에 [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)를 추가합니다.
1. 헤더를 위한 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)를 생성합니다. 헤더에는 Arial 폰트, 글꼴 크기 24pt, 가운데 정렬을 사용할 것입니다.
1. 페이지 [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties)에 헤더를 추가합니다.
1. 설명을 위한 [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)를 생성합니다. 설명에는 Arial 폰트, 글꼴 크기 24pt, 가운데 정렬을 사용할 것입니다.
1. 페이지의 Paragraphs에 설명을 추가합니다.
1. 테이블을 생성하고, 테이블 속성을 추가합니다.

1. 페이지에 (테이블)을 추가합니다 [단락](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. 문서를 저장합니다 "Complex.pdf".

```python

    import aspose.pdf as ap

    # 문서 객체 초기화
    document = ap.Document()
    # 페이지 추가
    page = document.pages.add()

    # 이미지 추가
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # 헤더 추가
    header = ap.text.TextFragment("2020년 가을 새로운 페리 노선")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # 설명 추가
    descriptionText = "방문객은 온라인으로 티켓을 구매해야 하며, 티켓은 하루에 5,000개로 제한됩니다. \
    페리 서비스는 절반 용량으로 운영되며 일정이 축소됩니다. 대기줄을 예상하세요."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # 테이블 추가
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("출발 도시")
    headerRow.cells.add("출발 섬")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
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

    document.save(output_pdf)
```