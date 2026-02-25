---
title: 데이터 소스 PDF와 테이블 통합
linktitle: 테이블 통합
type: docs
weight: 30
url: /ko/python-net/integrate-table/
description: 이 문서는 PDF 테이블을 통합하는 방법을 보여줍니다. 데이터베이스와 테이블을 통합하고 현재 페이지에서 테이블이 분할되는지 여부를 판단합니다.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## DataFrame에서 PDF 만들기

함수 'create_pdf_from_dataframe'는 DataFrame을 받아 새 PDF 안에 테이블로 변환합니다. 새 PDF 문서를 생성하고, 페이지를 추가하고, DataFrame에서 테이블을 생성(헬퍼 메서드 사용)한 후 결과를 지정된 파일 경로에 저장합니다. 그리고 이것은 가능할 뿐만 아니라 매우 쉽습니다.

1. 'ap.Document()'로 빈 PDF 문서를 초기화합니다.
1. 'self.create_table_from_dataframe(df, max_rows)' 함수는 DataFrame을 Aspose.PDF 테이블 객체로 변환합니다.
1. 테이블을 PDF 페이지에 삽입합니다. 생성된 테이블을 첫 번째 페이지의 내용(page.paragraphs.add(table))에 추가합니다.
1. PDF 문서를 저장합니다.

```python

from os import path
import pandas as pd
import aspose.pdf as ap

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

max_rows = 3  # Number of rows to include in the table
path_outfile = "output.pdf"

# Define the function to create a table from DataFrame
def create_table_from_dataframe(df, max_rows):
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )
    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray
    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))
    return table

# Load source PDF document
document = ap.Document()
page = document.pages.add()

table = create_table_from_dataframe(df, max_rows)

# Add table object to first page of input document
page.paragraphs.add(table)
document.save(path_outfile)
```

## DataFrame에서 테이블 만들기

이 코드는 DataFrame을 Aspose.PDF Table 객체로 변환합니다. 테이블 테두리를 설정하고, 열 이름이 포함된 헤더 행을 추가하며, DataFrame의 처음 max_rows 행으로 테이블을 채웁니다. 결과 Table은 PDF 문서에 추가될 수 있습니다.

1. 빈 'ap.Table()' 객체를 생성합니다.
1. 테이블 테두리를 설정합니다.
1. 기본 셀 테두리를 설정합니다.
1. 헤더 행을 추가합니다.
1. 데이터 행을 추가합니다.
1. 테이블을 반환합니다.

```python

    from os import path
    import pandas as pd
    import aspose.pdf as ap

    
    table = ap.Table()  # Initializes a new instance of the Table
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = (
        False  # Prevent header row from being split across pages
    )
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray

    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))

    return table
```
