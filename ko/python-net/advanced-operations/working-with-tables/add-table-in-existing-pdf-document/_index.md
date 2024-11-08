---
title: Python을 사용하여 PDF에 테이블 생성 또는 추가 
linktitle: 테이블 생성 또는 추가
type: docs
weight: 10
url: /ko/python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF for Python via .NET은 PDF 테이블을 생성, 읽기 및 편집하는 데 사용되는 라이브러리입니다. 이 주제의 다른 고급 기능을 확인하세요.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Python을 사용하여 PDF에 테이블 생성 또는 추가",
    "alternativeHeadline": "Python을 통해 .NET으로 PDF에 테이블 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf에 테이블 생성, 테이블 추가",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Python via .NET은 PDF 테이블을 생성, 읽기 및 편집하는 데 사용되는 라이브러리입니다. 이 주제의 다른 고급 기능을 확인하세요."
}
</script>


## 파이썬을 사용하여 테이블 생성하기

테이블은 PDF 문서를 다룰 때 중요합니다. 체계적인 방식으로 정보를 표시하는 훌륭한 기능을 제공합니다. Aspose.PDF 네임스페이스에는 PDF 문서를 처음부터 생성할 때 테이블을 생성하는 기능을 제공하는 [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/)라는 클래스가 포함되어 있습니다.

테이블은 Table 클래스의 객체를 생성하여 만들 수 있습니다.

```python

    table = ap.Table()
```

### 기존 PDF 문서에 테이블 추가하기

Aspose.PDF for Python via .NET을 사용하여 기존 PDF 파일에 테이블을 추가하려면 다음 단계를 따르십시오:

1. 소스 파일을 로드합니다.
1. 테이블을 초기화하고 열과 행을 설정합니다.
1. 테이블 설정을 설정합니다 (여기서는 테두리를 설정했습니다).
1. 테이블을 채웁니다.
1. 페이지에 테이블을 추가합니다.
1. 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 소스 PDF 문서 불러오기
    doc = ap.Document(input_file)
    # 테이블의 새 인스턴스 초기화
    table = ap.Table()
    # 테이블 테두리 색상을 LightGray로 설정
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # 테이블 셀의 테두리 설정
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # 10개의 행을 추가하기 위한 루프 생성
    for row_count in range(0, 10):
        # 테이블에 행 추가
        row = table.rows.add()
        # 테이블 셀 추가
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # 입력 문서의 첫 번째 페이지에 테이블 객체 추가
    doc.pages[1].paragraphs.add(table)
    # 테이블 객체가 포함된 업데이트된 문서 저장
    doc.save(output_file)
```

### 테이블에서의 ColSpan 및 RowSpan

Aspose.PDF for Python via .NET은 테이블에서 열을 병합하기 위한 [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) 속성과 행을 병합하기 위한 [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) 속성을 제공합니다.

`Cell` 객체의 `col_span` 또는 `row_span` 속성을 사용하여 테이블 셀을 만듭니다. 필요한 속성을 적용한 후 생성된 셀을 테이블에 추가할 수 있습니다.

```python

    import aspose.pdf as ap

    # 빈 생성자를 호출하여 Document 객체를 초기화합니다.
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # 테이블의 새 인스턴스를 초기화합니다.
    table = ap.Table()
    # 테이블 테두리 색상을 LightGray로 설정합니다.
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # 테이블 셀의 테두리를 설정합니다.
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # 테이블에 첫 번째 행을 추가합니다.
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # 테이블 셀을 추가합니다.
        row1.cells.add("Test 1" + str(cellCount))

    # 테이블에 두 번째 행을 추가합니다.
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # 테이블에 세 번째 행을 추가합니다.
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # 테이블에 네 번째 행을 추가합니다.
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # 테이블에 다섯 번째 행을 추가합니다.
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # 입력 문서의 첫 번째 페이지에 테이블 객체를 추가합니다.
    pdf_document.pages[1].paragraphs.add(table)
    # 테이블 객체가 포함된 업데이트된 문서를 저장합니다.
    pdf_document.save(output_file)
```


코드 실행 결과는 다음 이미지에 묘사된 표입니다:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## 경계선, 여백 및 패딩 작업

테이블의 경계선 스타일, 여백 및 셀 패딩을 설정하는 기능도 지원한다는 점에 유의하세요. 더 기술적인 세부사항으로 들어가기 전에, 아래 다이어그램에 제시된 경계선, 여백 및 패딩의 개념을 이해하는 것이 중요합니다:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

위 그림에서, 테이블, 행 및 셀의 경계선이 겹치는 것을 볼 수 있습니다. Aspose.PDF를 사용하여 테이블은 여백을 가질 수 있고 셀은 패딩을 가질 수 있습니다. 셀 여백을 설정하려면 셀 패딩을 설정해야 합니다.

### 경계선

Table, [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) 및 [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/) 객체의 경계선을 설정하려면, Table.border, Row.border 및 Cell.border 속성을 사용합니다.
 셀 테두리는 [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 또는 Row 클래스의 [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 속성을 사용하여 설정할 수 있습니다. 위에서 논의된 모든 테두리 관련 속성은 생성자를 호출하여 생성된 Row 클래스의 인스턴스에 할당됩니다. Row 클래스는 테두리를 사용자 지정하는 데 필요한 거의 모든 매개변수를 받는 많은 오버로드를 가지고 있습니다.

### 여백 또는 패딩

셀 패딩은 Table 클래스의 [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) 속성을 사용하여 관리할 수 있습니다. 모든 패딩 관련 속성은 사용자 정의 여백을 생성하기 위해 `left`, `right`, `top`, `bottom` 매개변수에 대한 정보를 받는 [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 클래스의 인스턴스에 할당됩니다.
다음 예제에서는 셀 테두리의 너비가 0.1 포인트로 설정되고, 테이블 테두리의 너비가 1 포인트로 설정되며, 셀 패딩이 5 포인트로 설정됩니다.

![PDF 테이블의 여백과 테두리](margin-border.png)

```python

    import aspose.pdf as ap

    # 빈 생성자를 호출하여 Document 객체를 인스턴스화합니다.
    doc = ap.Document()
    page = doc.pages.add()
    # 테이블 객체를 인스턴스화합니다.
    tab1 = ap.Table()
    # 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
    page.paragraphs.add(tab1)
    # 테이블의 열 너비를 설정합니다.
    tab1.column_widths = "50 50 50"
    # BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # 다른 사용자 지정 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # MarginInfo 객체를 생성하고 왼쪽, 아래, 오른쪽 및 위쪽 여백을 설정합니다.
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # 기본 셀 패딩을 MarginInfo 객체에 설정합니다.
    tab1.default_cell_padding = margin
    # 테이블에 행을 생성하고 행에 셀을 추가합니다.
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    my_text = ap.text.TextFragment("col3 with large text string")
    # Row1.Cells.Add("col3 with large text string to be placed inside cell")
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # PDF를 저장합니다.
    doc.save(output_file)
```


테이블을 둥근 모서리로 만들려면 [BorderInfo 클래스](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/)의 [rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties) 값을 사용하고 테이블 모서리 스타일을 둥글게 설정하세요.

```python
    
    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # 빈 BorderInfo 객체 생성
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # 반지름이 15인 둥근 테두리 설정
    b_info.rounded_border_radius = 15
    # 테이블 모서리 스타일을 둥글게 설정
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # 테이블 테두리 정보 설정
    tab1.border = b_info
```

## 테이블에 다양한 AutoFit 설정 적용하기

Microsoft Word와 같은 시각적 도구를 사용하여 테이블을 설계할 때, 테이블의 크기를 원하는 너비로 편리하게 조정하기 위해 자주 AutoFit 기능 중 하나를 사용합니다.
 예를 들어, 테이블의 너비를 페이지에 맞추기 위해 "AUTO_FIT_TO_WINDOW" 옵션을 사용할 수 있습니다 또는 AUTO_FIT_TO_CONTENT를 사용할 수 있습니다. 기본적으로, Aspose.Pdf를 사용하여 새 테이블을 만들 때, "Customized" 값으로 [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties)를 사용합니다. 다음 코드 스니펫에서는 테이블에 [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 및 [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) 객체의 매개변수를 설정합니다. 예제를 테스트하고 결과를 평가하세요.

```python
import aspose.pdf as ap

# 빈 생성자를 호출하여 Pdf 객체를 인스턴스화합니다.
doc = ap.Document()
# Pdf 객체에 섹션을 만듭니다.
sec1 = doc.pages.add()
# 테이블 객체를 인스턴스화합니다.
tab1 = ap.Table()
# 원하는 섹션의 문단 컬렉션에 테이블을 추가합니다.
sec1.paragraphs.add(tab1)
# 테이블의 열 너비를 설정합니다.
tab1.column_widths = "50 50 50"
tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
# BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
# 또 다른 사용자 정의 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
# MarginInfo 객체를 생성하고 왼쪽, 아래, 오른쪽, 위쪽 여백을 설정합니다.
margin = ap.MarginInfo()
margin.top = 5
margin.left = 5
margin.right = 5
margin.bottom = 5
# MarginInfo 객체에 기본 셀 패딩을 설정합니다.
tab1.default_cell_padding = margin
# 테이블에 행을 생성한 후 행에 셀을 생성합니다.
row1 = tab1.rows.add()
row1.cells.add("col1")
row1.cells.add("col2")
row1.cells.add("col3")
row2 = tab1.rows.add()
row2.cells.add("item1")
row2.cells.add("item2")
row2.cells.add("item3")
# 테이블 객체가 포함된 업데이트된 문서를 저장합니다.
doc.save(output_file)
```

### 테이블 너비 가져오기

때때로 테이블 너비를 동적으로 가져와야 할 때가 있습니다. Aspose.PDF.Table 클래스에는 이러한 목적을 위한 [get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods) 메서드가 있습니다. 예를 들어, 테이블 열 너비를 명시적으로 설정하지 않고 [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties)를 'AUTO_FIT_TO_CONTENT'로 설정한 경우, 다음과 같이 테이블 너비를 가져올 수 있습니다.

```python

    import aspose.pdf as ap

    # 새 문서 생성
    doc = ap.Document()
    # 문서에 페이지 추가
    page = doc.pages.add()
    # 새 테이블 초기화
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # 테이블에 행 추가
    row = table.rows.add()
    # 테이블에 셀 추가
    cell = row.cells.add("셀 1 텍스트")
    cell = row.cells.add("셀 2 텍스트")
    # 테이블 너비 가져오기
    print(table.get_width())
```

## 테이블 셀에 SVG 이미지 추가

Aspose.PDF for Python via .NET은 PDF 파일에 테이블 셀을 삽입할 수 있는 기능을 제공합니다.
 When constructing a table, you can include both text and images within these cells. Additionally, the API offers the functionality to transform SVG files into PDF format. By leveraging these functionalities together, you can load an SVG image and place it within a table cell.

테이블을 구성할 때 이러한 셀 내에 텍스트와 이미지를 모두 포함할 수 있습니다. 또한, API는 SVG 파일을 PDF 형식으로 변환하는 기능을 제공합니다. 이러한 기능을 함께 활용하여 SVG 이미지를 로드하고 테이블 셀 내에 배치할 수 있습니다.

The following code excerpt demonstrates the process of creating a table object and embedding an SVG image inside one of its cells.

다음 코드 예제는 테이블 객체를 생성하고 해당 셀 중 하나에 SVG 이미지를 포함하는 과정을 보여줍니다.

```python

    import aspose.pdf as ap

    # Document 객체 인스턴스화
    doc = ap.Document()
    # 이미지 인스턴스 생성
    img = ap.Image()
    # 이미지 유형을 SVG로 설정
    img.file_type = ap.ImageFileType.SVG
    # 소스 파일 경로
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # 이미지 인스턴스의 너비 설정
    img.fix_width = 50
    # 이미지 인스턴스의 높이 설정
    img.fix_height = 50
    # 테이블 인스턴스 생성
    table = ap.Table()
    # 테이블 셀의 너비 설정
    table.column_widths = "100 100"
    # 행 객체 생성 및 테이블 인스턴스에 추가
    row = table.rows.add()
    # 셀 객체 생성 및 행 인스턴스에 추가
    cell = row.cells.add()
    # 셀 객체의 문단 컬렉션에 텍스트 프래그먼트 추가
    cell.paragraphs.add(ap.text.TextFragment("첫 번째 셀"))
    # 행 객체에 또 다른 셀 추가
    cell = row.cells.add()
    # 최근에 추가된 셀 인스턴스의 문단 컬렉션에 SVG 이미지 추가
    cell.paragraphs.add(img)
    # 페이지 객체 생성 및 문서 인스턴스의 페이지 컬렉션에 추가
    page = doc.pages.add()
    # 페이지 객체의 문단 컬렉션에 테이블 추가
    page.paragraphs.add(table)
    # PDF 파일 저장
    doc.save(output_file)
```

## 테이블의 행 사이에 페이지 나누기 삽입

기본적으로 PDF 파일 내에서 테이블을 생성할 때 테이블이 테이블의 하단 여백을 초과하면 여러 페이지에 걸쳐 표시됩니다. 그러나 특정 행 수가 테이블에 추가된 후 페이지 나누기를 강제해야 하는 상황이 있을 수 있습니다. 다음 코드 예제는 테이블에 10개의 행이 포함되었을 때 페이지 나누기를 삽입하는 과정을 설명합니다.

```python

    import aspose.pdf as ap

    # Document 인스턴스 생성
    doc = ap.Document()
    # PDF 파일의 페이지 컬렉션에 페이지 추가
    doc.pages.add()
    # 테이블 인스턴스 생성
    tab = ap.Table()
    # 테이블의 테두리 스타일 설정
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # 테두리 색상이 빨간색인 기본 테두리 스타일 설정
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # 테이블 열 너비 지정
    tab.column_widths = "100 100"
    # 테이블에 200개의 행을 추가하기 위한 루프 생성
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # 10개의 행이 추가되면 새 페이지에 새 행을 렌더링
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # 테이블을 PDF 파일의 문단 컬렉션에 추가
    doc.pages[1].paragraphs.add(tab)
    # PDF 문서 저장
    doc.save(output_file)
```


## 새 페이지에 테이블 렌더링

기본적으로 단락은 페이지 객체의 Paragraphs 컬렉션에 추가됩니다. 그러나 페이지에 이전에 추가된 단락 수준의 객체 바로 뒤에 테이블을 렌더링하는 대신 새 페이지에 테이블을 렌더링할 수 있습니다.

### 샘플: Python을 사용하여 새 페이지에 테이블 렌더링하는 방법

새 페이지에 테이블을 렌더링하려면 [BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/) 클래스의 [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 속성을 사용하세요. 다음 코드 스니펫은 그 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # 페이지 추가됨.
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # 테이블 1을 다음 페이지에 유지하고 싶습니다...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF 조작 라이브러리 for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>