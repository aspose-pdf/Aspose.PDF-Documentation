---
title: Python으로 PDF에서 표 데이터 추출
linktitle: 표 데이터 추출
type: docs
weight: 40
url: /ko/python-net/extract-data-from-table-in-pdf/
description: Aspose.PDF for Python을 사용하여 PDF에서 표를 추출하는 방법을 배우세요
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 통해 PDF에서 표 데이터를 추출하는 방법
Abstract: 이 문서는 Python 라이브러리인 Aspose.PDF를 사용하여 PDF 문서에서 표를 프로그래밍 방식으로 추출하고 처리하는 포괄적인 가이드를 제공합니다. 이 문서에서는 PDF 문서를 열고 각 페이지를 순회하며 `TableAbsorber` 클래스를 활용해 표를 추출하는 Python 스크립트를 소개합니다. 추출된 표 데이터는 구조화되어 추가 분석을 위해 출력됩니다. 이 섹션에서는 사각형 주석으로 둘러싸인 영역과 같이 PDF 내 특정 표시된 영역에서 표를 추출하는 방법을 설명합니다. 스크립트는 이러한 주석을 식별하고 `TableAbsorber`를 초기화한 뒤 표가 주석 영역 내에 있는지 확인하고 데이터를 추출 및 출력합니다. 마지막 섹션에서는 추출된 표 데이터를 CSV 파일 형식으로 변환하는 방법을 자세히 다룹니다.
---

## PDF에서 표를 프로그래밍적으로 추출하기

이 코드는 PDF 표를 추출하고 PDF 파일의 표 데이터를 읽기 쉽고 구조화된 형식으로 변환하여 추가 처리나 분석에 사용할 수 있게 합니다.

1. PDF 문서 열기
1. PDF 페이지 순회하기
1. 표 데이터 추출하기

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Iterate through each page in the document
    for page in document.pages:
        absorber = apdf.text.TableAbsorber()
        absorber.visit(page)

        for table in absorber.table_list:
            print("Table")
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## PDF 페이지의 특정 영역에서 표 추출하기

이 코드 스니펫은 강조된 박스나 특정 주석과 같은 PDF의 지정된 영역에서 표 데이터를 추출합니다.

1. PDF 문서 열기
1. 첫 번째 페이지 가져오기
1. 첫 번째 사각형 주석 찾기
1. TableAbsorber 초기화하기
1. 페이지의 표들을 순회하기
1. 표가 주석 영역 안에 있는지 확인하기

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Get the first page (index starts from 1 in Aspose.PDF)
    page = document.pages[1]

    # Find the first square annotation
    square_annotation = next(
        (
            ann
            for ann in page.annotations
            if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
        ),
        None,
    )

    if square_annotation is None:
        print("No square annotation found.")
        return

    # Initialize the TableAbsorber
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    # Iterate through tables on the page
    for table in absorber.table_list:
        table_rect = table.rectangle
        annotation_rect = square_annotation.rect

        # Check if the table is inside the annotation region
        is_in_region = (
            annotation_rect.llx < table_rect.llx
            and annotation_rect.lly < table_rect.lly
            and annotation_rect.urx > table_rect.urx
            and annotation_rect.ury > table_rect.ury
        )

        if is_in_region:
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## PDF에서 표 데이터를 추출하여 Excel 파일에 저장하기

다음 코드 스니펫은 PDF에서 표 데이터를 추출하고 이를 CSV 파일로 내보내어 Excel이나 Google Sheets와 같은 스프레드시트 애플리케이션에서 추가 분석이나 조작에 사용할 수 있게 합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```

