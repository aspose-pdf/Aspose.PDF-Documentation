---
title: 기존 PDF 문서에서 표 제거
linktitle: 테이블 제거
description: Python의 기존 PDF 문서에서 하나 이상의 테이블을 제거하는 방법을 알아봅니다.
lastmod: "2026-06-10"
type: docs
weight: 50
url: /ko/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에서 하나 이상의 테이블을 삭제합니다.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 기존 PDF 문서에서 테이블을 제거하는 방법을 설명합니다.테이블을 찾기 위한 'TableAbsorber'를 소개하고 단일 테이블을 삭제하거나 페이지에서 탐지된 모든 테이블을 제거하는 방법을 보여줍니다.
---

## PDF 문서에서 표 제거

파이썬용 Aspose.PDF 파일을 사용하면 PDF에서 테이블을 제거할 수 있습니다.기존 PDF를 열고 첫 페이지의 첫 번째 테이블을 다음과 같이 감지합니다. `TableAbsorber`, 를 사용하여 해당 테이블을 삭제합니다. `remove()`를 클릭하고 업데이트된 PDF를 새 파일에 저장합니다.

표를 많이 사용하는 PDF를 정리하거나, 오래된 표 형식 내용을 제거하거나, 재배포하기 전에 문서를 단순화해야 할 때 이 페이지를 사용하십시오.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## PDF 문서에서 모든 표 제거

라이브러리를 사용하면 PDF의 특정 페이지에서 모든 표를 제거할 수 있습니다.코드는 기존 PDF를 열고, TableAbsorber를 사용하여 두 번째 페이지의 모든 테이블을 탐지하고, 감지된 테이블을 반복하고, 각 테이블을 제거한 다음 수정된 PDF를 새 파일에 저장합니다.나머지 PDF 내용은 그대로 두고 페이지에서 표를 대량으로 제거해야 할 때 유용합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## 관련 테이블 주제

- [Python을 사용하여 PDF에서 표 작업하기](/pdf/ko/python-net/working-with-tables/)
- [파이썬을 사용하여 PDF에 표 추가](/pdf/ko/python-net/adding-tables/)
- [PDF 문서에서 표 추출](/pdf/ko/python-net/extracting-table/)
- [기존 PDF의 표 조작](/pdf/ko/python-net/manipulating-tables/)