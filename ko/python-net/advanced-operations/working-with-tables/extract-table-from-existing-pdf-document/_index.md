---
title: 파이썬에서 PDF에서 테이블 추출하기
linktitle: 추출 테이블
type: docs
weight: 20
url: /ko/python-net/extracting-table/
description: Python으로 기존 PDF 문서에서 테이블 데이터를 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에서 테이블 데이터를 추출합니다.
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에서 테이블을 추출하는 방법을 설명합니다.'TableAbsorber'를 사용하여 페이지별로 테이블을 검색하고, 행과 셀을 반복하고, 분석 및 다운스트림 데이터 처리를 위해 셀 텍스트를 검색하는 방법을 보여줍니다.
---

## PDF에서 표 추출

PDF에서 테이블을 추출하는 것은 보고, 데이터 마이그레이션 및 분석 워크플로우에 유용합니다..NET을 통한 Python용 Aspose.PDF 기능을 사용하면 기존 PDF 문서의 테이블 내용을 효율적으로 검색하고 읽을 수 있습니다.

이 코드 스니펫은 기존 PDF 파일을 열고, 각 페이지에서 표를 스캔하고, 셀 텍스트 내용을 추출합니다.를 사용합니다. `TableAbsorber` 테이블을 감지한 다음 행과 셀을 반복하여 추출된 텍스트를 인쇄합니다.

1. PDF를 AP.Document 개체에 로드합니다.
1. 페이지를 반복해서 살펴보세요.
1. 테이블 업소버 오브젝트를 만듭니다.
1. 테이블 전체를 반복하세요.
1. 행과 셀을 반복합니다.
1. 셀에서 텍스트를 추출하고 인쇄합니다.

이 예제에서는 PDF를 읽고, 모든 테이블을 찾고, 셀 내용을 행별로 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## 관련 테이블 주제

- [Python을 사용하여 PDF에서 표 작업하기](/pdf/ko/python-net/working-with-tables/)
- [파이썬을 사용하여 PDF에 표 추가](/pdf/ko/python-net/adding-tables/)
- [PDF 테이블을 데이터 소스와 통합](/pdf/ko/python-net/integrate-table/)
- [기존 PDF에서 표 제거](/pdf/ko/python-net/removing-tables/)