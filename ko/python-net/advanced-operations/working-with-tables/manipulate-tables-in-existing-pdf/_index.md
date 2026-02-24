---
title: 기존 PDF에서 테이블 조작
linktitle: 테이블 조작
type: docs
weight: 40
url: /ko/python-net/manipulating-tables/
description: Aspose.PDF for Python via .NET를 사용하여 기존 PDF의 테이블을 다루는 방법을 배우고, 문서 수정에 대한 유연성을 제공합니다.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF에서 테이블 조작

Aspose.PDF for Python은 PDF 문서의 테이블 내 특정 셀 내용을 수정하는 방법을 보여 줍니다. TableAbsorber 클래스를 사용하여 첫 페이지의 테이블을 찾고, 첫 번째 테이블의 첫 번째 셀에 있는 특정 텍스트 조각에 접근하여 텍스트를 업데이트한 다음, 수정된 PDF를 새 파일에 저장합니다.

1. 'ap.Document()'를 사용하여 PDF 파일을 엽니다.
1. PDF에서 테이블을 감지하기 위해 TableAbsorber 객체를 생성합니다.
1. absorber.visit()를 호출하여 첫 페이지의 모든 테이블을 찾습니다.
1. 특정 텍스트 조각에 접근합니다:
- 첫 번째 테이블을 가져옵니다.
- 테이블의 첫 번째 행을 가져옵니다.
- 셀 안의 두 번째 텍스트 조각을 선택합니다.
1. 텍스트를 수정합니다.
1. 업데이트된 PDF를 저장합니다.
1. 저장된 파일에 대한 확인 메시지를 출력합니다.

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## PDF 문서에서 기존 테이블을 새 테이블로 교체

Aspose.PDF는 PDF 내 기존 테이블을 새 테이블로 교체할 수 있도록 합니다. 코드 조각은 PDF를 열고, TableAbsorber를 사용하여 첫 번째 페이지의 첫 번째 테이블을 식별한 뒤, 사용자 정의 열 너비와 내용을 가진 새 테이블을 생성하고 원래 테이블을 새 테이블로 교체합니다. 마지막으로, 업데이트된 PDF를 새 파일에 저장합니다.

문서의 다른 부분을 변경하지 않고 PDF에서 테이블 구조와 내용을 수정하는 방법을 보여 줍니다.

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

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

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
