---
title: Python에서 PDF 테이블을 데이터 소스와 통합하기
linktitle: 통합 테이블
type: docs
weight: 30
url: /ko/python-net/integrate-table/
description: Python에서 PDF 테이블을 데이터베이스 및 판다 데이터 프레임과 같은 데이터 소스와 통합하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 테이블을 데이터베이스 및 데이터프레임과 통합
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 테이블을 외부 데이터 소스와 통합하는 방법을 설명합니다.Pandas DataFrames 및 기타 구조화된 소스에서 PDF 테이블을 작성하고, 문서에 삽입하고, Python에서 PDF 페이지를 렌더링할 때 테이블 흐름을 제어하는 방법을 알아봅니다.
---

## 데이터프레임에서 PDF 작성

더 `create_pdf_from_dataframe` 함수는 새 PDF를 작성하고 팬더 데이터 프레임에서 생성된 테이블을 삽입합니다.이 방법은 데이터가 이미 표 형식으로 존재하는 워크플로를 보고하는 데 유용합니다.

함수는 다음 단계를 수행합니다.

1. 를 사용하여 빈 PDF 문서 만들기 `ap.Document()`.
1. 문서에 페이지를 추가합니다.
1. 를 호출하여 데이터프레임을 Aspose.PDF 테이블로 변환합니다. `create_table_from_dataframe(df, max_rows)`.
1. 를 사용하여 페이지에 표 추가 `page.paragraphs.add(table)`.
1. PDF를 출력 경로에 저장합니다.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_pdf_from_dataframe(
    outfile: str, df: pd.DataFrame, max_rows: int = 20
) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    table = create_table_from_dataframe(df, max_rows)

    # Add table object to first page of input document
    page.paragraphs.add(table)
    document.save(outfile)
```

## 데이터프레임에서 테이블 생성

더 `create_table_from_dataframe` 함수는 데이터 프레임을 Aspose.PDF 로 변환합니다 `Table` 모든 페이지에 추가할 수 있는 개체입니다.

다음과 같은 작업을 수행합니다.

1. 빈 항목 만들기 `ap.Table()` 예.
1. 일관된 서식을 위해 표와 셀 테두리를 설정합니다.
1. DataFrame 열 이름을 사용하여 헤더 행을 추가합니다.
1. 에서 데이터 행 추가 `df.head(max_rows)`.
1. 채워진 테이블 객체를 반환합니다.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_table_from_dataframe(df: pd.DataFrame, max_rows: int = 20) -> ap.Table:
    """Create an Aspose.PDF table from a pandas DataFrame."""
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False  # Prevent header row from being split across pages
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

## 관련 테이블 주제

- [Python을 사용하여 PDF에서 표 작업하기](/pdf/ko/python-net/working-with-tables/)
- [파이썬을 사용하여 PDF에 표 추가](/pdf/ko/python-net/adding-tables/)
- [PDF 문서에서 표 추출](/pdf/ko/python-net/extracting-table/)
- [기존 PDF의 표 조작](/pdf/ko/python-net/manipulating-tables/)