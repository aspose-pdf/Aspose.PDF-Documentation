---
title: 기존 PDF 문서의 테이블 조작
linktitle: 테이블 조작
type: docs
weight: 40
url: /ko/python-net/manipulating-tables/
description: Python을 사용하여 기존 PDF 문서의 테이블을 검사하고 수정하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 기존 PDF 테이블을 검사하고 수정합니다.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 이미 있는 테이블을 조작하는 방법을 설명합니다.TableAbsorber로 테이블을 찾고, 특정 행과 셀에 액세스하고, 테이블 텍스트 내용을 업데이트하고, 수정된 PDF를 Python으로 저장하는 방법을 알아봅니다.
---

## 기존 PDF의 표 조작

.NET을 통한 파이썬용 Aspose.PDF 파일을 사용하면 PDF 문서에 이미 존재하는 테이블을 업데이트할 수 있습니다.다음을 사용할 수 있습니다. [테이블 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 클래스는 페이지에서 테이블을 찾고, 행과 셀에 액세스하고, 텍스트 내용을 변경하고, 업데이트된 파일을 저장합니다.

전체 문서 레이아웃을 다시 만들지 않고 PDF의 기존 테이블 내용을 업데이트해야 하는 경우 이 페이지를 사용하십시오.

## PDF 표 셀에서 텍스트 찾기 및 바꾸기

이 예제에서는 1페이지에서 첫 번째 테이블을 찾고, 첫 번째 셀에 액세스하고, 텍스트를 바꾸고, 출력 PDF를 저장합니다.

1. 입력 PDF를 엽니다.
1. 테이블 업소버를 만들고 1페이지를 방문하세요.
1. 하나 이상의 테이블이 감지되었는지 확인합니다.
1. 첫 번째 테이블의 첫 번째 행에 있는 첫 번째 셀에 액세스합니다.
1. 셀에 텍스트 부분이 포함되어 있는지 확인한 다음 첫 번째 부분을 업데이트합니다.
1. 수정한 PDF를 저장합니다.

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## 기존 테이블을 새 테이블로 바꾸기

탐지된 테이블을 새로 만든 테이블로 바꿀 수도 있습니다.이 방법은 구조와 내용을 모두 변경해야 하는 경우에 유용합니다.

아래 코드는 PDF를 열고, 1페이지에서 첫 번째 테이블을 찾고, 대체 테이블을 만들고, 이전 테이블을 새 테이블로 바꾸고, 결과를 저장합니다.

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## 관련 테이블 주제

- [Python을 사용하여 PDF에서 표 작업하기](/pdf/ko/python-net/working-with-tables/)
- [파이썬을 사용하여 PDF에 표 추가](/pdf/ko/python-net/adding-tables/)
- [PDF 문서에서 표 추출](/pdf/ko/python-net/extracting-table/)
- [기존 PDF에서 표 제거](/pdf/ko/python-net/removing-tables/)
