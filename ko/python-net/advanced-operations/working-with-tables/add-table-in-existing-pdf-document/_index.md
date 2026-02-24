---
title: Python을 사용하여 PDF에 테이블 추가
linktitle: 테이블 추가
type: docs
weight: 10
url: /ko/python-net/adding-tables/
description: Aspose.PDF for Python via .NET은 PDF 테이블을 만들고, 읽고, 편집하는 데 사용되는 라이브러리입니다. 이 주제의 다른 고급 기능을 확인하세요.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 테이블 추가하는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서에서 테이블을 만들고 조작하는 포괄적인 가이드를 제공합니다. 기존 PDF 파일에 테이블을 추가하는 단계, 테이블 테두리, 여백 및 패딩 설정을 자세히 설명합니다. 또한 `col_span` 및 `row_span`을 사용하여 열과 행을 병합하고, 다양한 AutoFit 설정을 적용하며, 테이블 너비를 동적으로 가져오는 고급 기능을 탐구합니다. 본문에서는 SVG 이미지를 테이블 셀에 삽입하고 페이지 나누기를 강제하거나 새 페이지에 테이블을 렌더링하는 방법도 보여줍니다. 코드 스니펫은 각 기능을 예시하며 PDF 문서에서 테이블 레이아웃과 내용을 효과적으로 관리하는 방법을 보여줍니다.
---

기존 PDF 문서에 테이블을 추가하는 것은 데이터 표현을 향상하고, 정보를 구조화하며, 보고서를 생성하는 데 일반적인 필요입니다. **Aspose.PDF for Python via .NET**은 이 작업을 위한 포괄적인 솔루션을 제공하며, 개발자가 기존 PDF에 테이블을 원활하게 삽입할 수 있게 합니다.

이 가이드는 Aspose.PDF for Python via .NET을 사용하여 기존 PDF 문서에 테이블을 추가하는 단계별 접근 방식을 제공합니다. 테이블 초기화, 열 너비 설정, 테두리 정의, 행과 셀 채우기, 수정된 문서 저장을 다룹니다. 또한 셀 테두리 처리, 여백 및 패딩 적용, AutoFit 설정을 활용하여 테이블 차원을 동적으로 조정하는 고급 기능도 탐구합니다.

PDF의 시각적 매력을 향상시키거나 데이터를 보다 효율적으로 정리하려는 경우, 이 가이드는 Aspose.PDF for Python의 강력한 테이블 조작 기능을 활용하기 위한 귀중한 자료가 됩니다.

## 기본 테이블 만들기

## 테이블 만들기

이 예제는 테두리와 여러 행이 있는 PDF 문서에서 테이블을 만드는 방법을 보여줍니다.

1. 새 PDF 문서를 생성합니다.
1. 문서에 빈 페이지를 추가합니다.
1. 테이블을 초기화합니다.
1. 전체 테이블 테두리를 설정합니다.
1. 개별 셀의 테두리를 설정합니다.
1. 행과 셀을 추가합니다.
1. 페이지에 테이블을 삽입합니다.
1. 지정된 경로에 PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save updated document containing table object
    document.save(path_outfile)
```

### 테이블 셀에 이미지 추가

이 코드 스니펫은 PDF 문서의 테이블 셀에 이미지를 삽입하는 방법을 보여줍니다.

1. 새 PDF 문서를 생성합니다.
1. 테이블을 초기화합니다.
1. 열 너비를 포인트 단위로 설정합니다.
1. 첫 번째 셀에 텍스트 조각을 추가합니다.
1. 두 번째 셀에 'ap.Image()' 인스턴스를 추가합니다.
1. 'img.file'을 사용하여 이미지 파일 경로를 설정합니다.
1. 'img.fix_width'와 'img.fix_height'가 셀 내부 이미지 크기를 제어합니다.
1. PDF 페이지에 테이블을 삽입합니다.
1. PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"

    # Create row object and add it to table instance
    row = table.rows.add()
    # Create cell object and add it to row instance
    cell = row.cells.add()
    # Add textfragment to paragraphs collection of cell object
    cell.paragraphs.add(ap.text.TextFragment(image))
    # Create an image instance
    img = ap.Image()
    # Set image type as SVG
    # Path for source file
    img.file = path.join(self.data_dir, image)
    # Set width for image instance
    img.fix_width = 50
    # Set height for image instance
    img.fix_height = 50
    # Add another cell to row object
    cell = row.cells.add()
    # Add SVG image to paragraphs collection of recently added cell instance
    cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(path_outfile)
```

PDF 문서의 테이블 셀에 SVG 이미지를 추가할 수 있습니다:

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"
    for image in images:
        # Create row object and add it to table instance
        row = table.rows.add()
        # Create cell object and add it to row instance
        cell = row.cells.add()
        # Add textfragment to paragraphs collection of cell object
        cell.paragraphs.add(ap.text.TextFragment(image))
        # Create an image instance
        img = ap.Image()
        # Set image type as SVG
        img.file_type = ap.ImageFileType.SVG
        # Path for source file
        img.file = path.join(self.data_dir, image)
        # Set width for image instance
        img.fix_width = 50
        # Set height for image instance
        img.fix_height = 50
        # Add another cell to row object
        cell = row.cells.add()
        # Add SVG image to paragraphs collection of recently added cell instance
        cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(path_outfile)
```

### 테이블의 ColSpan 및 RowSpan

이 예제는 복잡한 테이블 레이아웃을 만들기 위해 테이블 셀을 수직 및 수평으로 병합하는 방법을 보여줍니다.

1. 전체 테이블 테두리를 설정합니다.
1. 기본 셀 테두리를 설정합니다.
1. 두 개의 셀을 수평으로 하나로 병합합니다.
1. 셀을 수직으로 두 행에 걸쳐 병합합니다.
1. 5번째 행은 병합된 열을 건너뛰어 rowspan을 반영합니다.
1. 페이지에 테이블을 삽입합니다.
1. PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.black
    )
    # Add 1st row to table
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Add table cells
        row1.cells.add("Test 1" + str(cellCount))

    # Add 2nd row to table
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Add 3rd row to table
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Add 4th row to table
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Add 5th row to table
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

![ColSpan 및 RowSpan 데모](colspan_rowspan.png)

### 테이블 및 셀에 테두리 적용

이 예제는 셀 패딩, 표 여백을 설정하고 표 셀의 텍스트에 대한 단어 줄바꿈을 제어하는 방법을 보여줍니다.

1. 열의 너비를 설정합니다.
1. 표와 셀 테두리를 정의합니다.
1. 일관된 간격을 위해 셀 내부에 패딩을 설정합니다.
1. 기본적으로 모든 셀에 패딩을 적용합니다.
1. 텍스트를 추가하고 줄바꿈을 제어합니다.
1. 행과 셀을 추가합니다.
1. PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)
    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    tab1 = ap.Table()
    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(tab1)
    # Set with column widths of the table
    tab1.column_widths = "50 50 50"
    # Set default cell border using BorderInfo object
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Set table border using another customized BorderInfo object
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Set the default cell padding to the MarginInfo object
    tab1.default_cell_padding = margin
    # Create rows in the table and then cells in the rows
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    text = ap.text.TextFragment("col3 with large text string")
    # Row1.Cells.Add("col3 with large text string to be placed inside cell")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Save updated document containing table object
    document.save(path_outfile)
```

![PDF 표의 여백 및 테두리](margin-border.png)

## 표 레이아웃 및 크기 조정

### 열과 행 자동 맞춤

이 코드 조각은 페이지에 맞게 표 열 너비를 자동으로 조정하는 방법을 보여줍니다.
매개변수 table.column_widths = "50 50 50" 은 포인트 단위임을 유의하세요. 하지만 센티미터(cm), 인치 또는 % 로도 지정할 수 있습니다.

1. 초기 열 너비를 설정합니다.
1. 열을 자동으로 조정하여 페이지 너비에 맞춥니다.
1. 셀 및 표 테두리를 정의합니다.
1. 'table.default_cell_padding' 은 셀 내부의 일관된 간격을 위해 'MarginInfo()' 를 사용합니다.
1. 'table.rows.add()' 로 행을 추가하고, 'row.cells.add()' 로 셀을 추가합니다.
1. PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    page.paragraphs.add(table)

    table.column_widths = "50 50 50"
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW

    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    table.default_cell_padding = margin

    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    document.save(path_outfile)
```

### 콘텐츠 주변 간격 조정

이 예제는 여러 페이지에 걸쳐 표를 만들고, 셀의 긴 텍스트를 처리하며, 패딩과 테두리를 적용하는 방법을 보여줍니다.

1. 'page.paragraphs.add(table)' 을 사용하여 페이지에 새 표를 추가합니다.
1. 'table.column_widths' 로 열의 너비를 정의합니다.
1. 'table.default_cell_border' 로 개별 셀 테두리를 설정합니다.
1. 'table.border' 로 표 전체 테두리를 설정합니다.
1. 'MarginInfo()' 를 사용하여 셀의 기본 패딩을 정의합니다.
1. 'TextFragment' 로 텍스트를 추가합니다.
1. 다른 행을 추가합니다.
1. PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    table = ap.Table()
    # Add page
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(table)

    # Set column widths of the table
    table.column_widths = "50 50 50"

    # Set default cell border using BorderInfo object
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    # Set table border using another customized BorderInfo object
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    # Set the default cell padding to the MarginInfo object
    table.default_cell_padding = margin

    # Create rows and cells
    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()

    # Add a long text fragment into the third cell
    text = ap.text.TextFragment("col3 with large text string")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False

    # Add another row
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    # Save PDF document
    document.save(path_outfile)
```

![테두리, 여백 및 패딩](set-border-style-margins-and-padding-of-table_1.png)

### 표 모서리 스타일링

Aspose.PDF for Python via .NET 은 표에 둥근 모서리를 적용하고 테두리 반경을 사용자 정의하는 방법을 보여줍니다.

1. 새 표 인스턴스를 생성합니다.
1. 모든 면에 대한 테두리를 초기화합니다.
1. 모서리 반경을 설정합니다.
1. 둥근 모서리 스타일을 적용합니다.
1. 행과 셀을 추가합니다.
1. 'page.paragraphs.add(table)' 로 표를 PDF 페이지에 삽입합니다.
1. PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()

    # Create a table
    table = ap.Table()

    # Create a blank BorderInfo object
    b_info = ap.BorderInfo(ap.BorderSide.ALL)

    # Set the border a rounded border where radius of round is 15
    b_info.rounded_border_radius = 15

    # Set the table corner style as Round
    table.corner_style = ap.BorderCornerStyle.ROUND

    # Set the table border information
    table.border = b_info

    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## 표에 콘텐츠 추가

### 셀에서 HTML 조각 사용

이 예제는 HTML 형식의 콘텐츠를 표 셀에 삽입하는 방법을 보여줍니다.

1. 표와 셀 테두리를 정의합니다.
1. HTML 콘텐츠를 추가합니다.
1. 행을 추가합니다. 루프를 사용하여 각 셀에 HTML 형식의 콘텐츠가 있는 여러 행을 추가합니다.
1. 'page.paragraphs.add(table)' 로 표를 PDF 페이지에 삽입합니다.
1. PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <strong>({row_count}, 1)</strong>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='color:red'>({row_count}, 2)</span>"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='text-decoration: underline'>({row_count}, 3)</span>"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

### 셀에서 LaTeX 조각 사용

이 예제는 수학식이나 스타일된 표현을 위해 LaTeX 형식의 콘텐츠를 표 셀에 삽입하는 방법을 보여줍니다.

1. 표와 셀 테두리를 정의합니다.
1. LaTeX 콘텐츠 추가.
1. 행 추가. 루프를 사용해 각 셀에 LaTeX 형식의 콘텐츠가 포함된 여러 행을 추가합니다.
1. 'page.paragraphs.add(table)'을 사용해 테이블을 PDF 페이지에 삽입합니다.
1. PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\mathbf{{({row_count}, 1)}}$")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\textcolor{{red}}{{({row_count}, 2)}}$"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\underline{{({row_count}, 3)}}$"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## 고급 테이블 기능

### 페이지에 걸친 테이블 삽입

이 예제는 PDF에 여러 테이블을 만들고, 페이지 여백을 설정하며, 테이블을 새 페이지에서 시작하도록 강제하는 방법을 보여줍니다.

1. 'page_info.margin'을 사용해 페이지 여백을 설정합니다.
1. 'page_info.is_landscape'를 사용해 페이지 방향을 가로 모드로 설정합니다.
1. 첫 번째 테이블:
- 지정된 너비로 두 개의 열을 정의합니다.
- 'row.fixed_row_height'를 사용해 루프에서 행을 추가합니다.
- 셀을 텍스트 조각으로 채웁니다.
1. 두 번째 테이블:
- 'table1.column_widths'를 사용해 새 테이블을 만듭니다.
- 테이블이 새 페이지에서 시작하도록 강제합니다.
1. 첫 번째 테이블을 추가합니다.
1. 새 페이지에 두 번째 테이블을 추가합니다.
1. 문서를 저장합니다

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Set page and margin information
    page_info = document.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37
    page_info.is_landscape = True

    # First table with 120 rows
    table = ap.Table()
    table.column_widths = "50 100"

    cur_page = document.pages.add()

    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 2"))

    cur_page.paragraphs.add(table)

    # Second table with 10 rows
    table1 = ap.Table()
    table1.column_widths = "100 100"

    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 3"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 4"))

    table1.is_in_new_page = True  # Force table to new page
    cur_page.paragraphs.add(table1)

    # Save updated document containing table object
    document.save(path_outfile)
```

### 테두리 없는 테이블 만들기

이 예제는 페이지를 가로질러 수직으로 분할될 수 있는 큰 테이블을 만들고, 열을 반복하며, 헤더 셀에 서로 다른 배경색을 적용하는 방법을 보여줍니다.

1. 테이블을 초기화합니다.
1. 모든 셀에 기본 테두리를 설정합니다.
1. 헤더 셀은 'col_span'을 사용해 여러 열을 병합합니다.
1. 'background_color set'을 사용해 시각적 구분을 위해 셀 배경을 설정합니다.
1. 행을 추가합니다.
1. 'page.paragraphs.add(table)'을 사용해 테이블을 PDF 페이지에 삽입합니다.
1. PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)
    table.repeating_columns_count = 2
    page.paragraphs.add(table)

    # Add header Row
    row = table.rows.add()
    cell = row.cells.add("header 1")
    cell.col_span = 2
    cell.background_color = ap.Color.light_gray
    row.cells.add("header 3")

    cell2 = row.cells.add("header 4")
    cell2.col_span = 2
    cell2.background_color = ap.Color.light_blue
    row.cells.add("header 6")

    cell3 = row.cells.add("header 7")
    cell3.col_span = 2
    cell3.background_color = ap.Color.light_green
    cell4 = row.cells.add("header 9")

    cell4.col_span = 3
    cell4.background_color = ap.Color.light_coral
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")

    row_counter = 0
    while row_counter < 3:
        # Create rows in the table and then cells in the rows
        row1 = table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 8")
        row1.cells.add("col " + str(row_counter) + ", 9")
        row1.cells.add("col " + str(row_counter) + ", 10")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
        row_counter += 1

    document.save(path_outfile)
```

### 여러 페이지에 걸친 헤더 행 반복

이 예제는 여러 페이지에 걸쳐 테이블을 만들면서 각 페이지에서 헤더 행이 보이도록 유지하는 방법을 보여줍니다.

1. 테이블을 초기화합니다.
1. 글꼴, 크기 및 색상을 포함한 헤더 행을 반복합니다.
1. 열 너비를 설정하고 테이블에 테두리를 적용합니다.
1. 헤더 행을 추가합니다.
1. 많은 데이터 행을 추가해 테이블이 여러 페이지에 걸치도록 합니다.
1. 'page.paragraphs.add(table)'을 사용해 테이블을 PDF 페이지에 삽입합니다.
1. PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Set the table to break across pages
    table.broken = ap.TableBroken.VERTICAL

    # Set number of repeating header rows
    table.repeating_rows_count = 2

    text_state = ap.text.TextState()
    text_state.font_size = 12
    text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_state.foreground_color = ap.Color.red
    table.repeating_rows_style =  text_state

    # Set column widths
    table.column_widths = "100 100 100"

    # Set borders
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.black)

    # Add header rows that will repeat on each page
    header_row1 = table.rows.add()
    header_row1.cells.add("Header 1-1")
    header_row1.cells.add("Header 1-2")
    header_row1.cells.add("Header 1-3")

    # Set background color for header rows
    for cell in header_row1.cells:
        cell.background_color = ap.Color.light_gray

    header_row2 = table.rows.add()
    header_row2.cells.add("Header 2-1")
    header_row2.cells.add("Header 2-2")
    header_row2.cells.add("Header 2-3")

    for cell in header_row2.cells:
        cell.background_color = ap.Color.light_blue

    # Add many data rows to force table across multiple pages
    for i in range(1, 101):
        row = table.rows.add()
        row.cells.add(f"Data {i}-1")
        row.cells.add(f"Data {i}-2")
        row.cells.add(f"Data {i}-3")

    # Add table to page
    page.paragraphs.add(table)

    # Save document
    document.save(path_outfile)
```

### 열 반복

'add_repeating_columns' 함수는 반복되는 열이 있는 테이블을 포함한 PDF 문서를 생성합니다. 테두리가 있는 테이블을 설정하고, 헤더를 추가하며, 데이터 행을 채우고, 생성된 PDF 파일을 지정된 위치에 저장합니다. 이 속성을 설정하면 테이블이 다음 페이지에서 열 단위로 분할되고, 다음 페이지 시작 시 지정된 열 수가 반복됩니다.

1. 새 PDF 문서를 초기화합니다.
1. 사용자 정의 크기의 페이지를 추가합니다.
1. 테이블 테두리 스타일을 설정합니다.
1. 테이블을 초기화합니다.
1. 테이블을 PDF 페이지에 추가합니다.
1. 헤더 행을 추가합니다.
1. 데이터 행을 추가합니다.
1. PDF 문서를 저장합니다.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()
    page.set_page_size(ap.PageSize.A5.height, ap.PageSize.A5.width)

    # Define border
    border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)

    # Create table
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    table.repeating_columns_count = 5
    table.border = border
    table.default_cell_border = border

    # Add table to page
    page.paragraphs.add(table)

    # Add header row
    row = table.rows.add()
    for i in range(1, 6):
        cell = row.cells.add(f"header {i}")
        cell.background_color = ap.Color.light_gray

    for i in range(6, 18):
        row.cells.add(f"header {i}")

    # Add data rows
    for row_counter in range(1, 6):
        row = table.rows.add()
        for i in range(1, 6):
            cell = row.cells.add(f"cell {row_counter},{i}")
            cell.background_color = ap.Color.light_gray
        for i in range(6, 18):
            row.cells.add(f"cell {row_counter},{i}")

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
