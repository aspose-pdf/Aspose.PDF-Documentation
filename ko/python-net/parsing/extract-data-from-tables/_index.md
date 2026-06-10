---
title: Python을 사용하여 PDF의 테이블에서 데이터 추출
linktitle: 테이블에서 데이터 추출
type: docs
weight: 40
url: /ko/python-net/extract-data-from-table-in-pdf/
description: Python용 Aspose.PDF 를 사용하여 PDF 파일에서 테이블 데이터를 추출하고 추가 처리를 위해 결과를 내보내는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 통해 PDF의 테이블에서 데이터를 추출하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 테이블 데이터를 추출하고 처리하는 방법을 설명합니다.TableAbsorber로 각 페이지를 스캔하고, 탐지된 테이블에서 행과 셀을 읽고, 주석이 달린 특정 영역으로 추출을 제한하고, 스프레드시트 도구 및 다운스트림 처리에 사용하기 위해 PDF 콘텐츠를 CSV 형식으로 내보내는 방법을 보여줍니다.
---

## 프로그래밍 방식으로 PDF에서 표 추출

용도 [테이블 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) a의 각 페이지에서 테이블을 감지합니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).페이지를 방문한 후 반복해서 살펴보세요. `table_list`그런 다음 각 행과 셀을 살펴보면서 읽을 수 있는 텍스트 형식으로 표 내용을 재구성합니다.

1. PDF를 다음과 같이 엽니다. `Document`.
1. 의 페이지를 반복해서 살펴보세요. `document.pages`.
1. 만들기 `TableAbsorber` 각 페이지 및 전화에 대해 `visit(page)`.
1. 탐지된 테이블, 행, 셀을 순회합니다.
1. 각 셀에서 텍스트 조각을 읽고 추출된 행 출력값을 조합합니다.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## PDF 페이지의 특정 영역에서 표 추출

표시된 영역 내에 있는 테이블만 추출해야 하는 경우 결합하십시오. [테이블 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 와 함께 [사각형 주석](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/).이 예에서는 주석 사각형을 경계로 사용하고 해당 영역 내에 완전히 포함된 테이블만 처리됩니다.

1. PDF를 다음과 같이 엽니다. `Document`.
1. 대상 페이지를 선택합니다.
1. 관심 영역을 표시하는 사각형 주석을 찾으십시오.
1. 만들기 `TableAbsorber` 페이지를 방문하십시오.
1. 탐지된 각 테이블 사각형을 주석 사각형과 비교합니다.
1. 표시된 영역 내에 완전히 들어 있는 테이블만 처리하십시오.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## PDF에서 CSV로 테이블 데이터 내보내기

스프레드시트에 적합한 형식으로 추출된 데이터가 필요한 경우 다음을 사용하여 PDF를 저장하십시오. [엑셀 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 출력 형식을 CSV로 설정합니다.결과 파일은 Excel, Google 스프레드시트에서 열거나 분석 워크플로우로 가져올 수 있습니다.

1. 소스 PDF를 다음과 같이 엽니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 생성하기 `ExcelSaveOptions` 예.
1. 세트 `excel_save.format` 에 `ExcelSaveOptions.ExcelFormat.CSV`.
1. 대상 CSV 경로에 문서를 저장합니다.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
