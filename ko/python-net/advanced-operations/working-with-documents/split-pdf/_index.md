---
title: 파이썬에서 PDF 파일 분할하기
linktitle: PDF 파일 분할
type: docs
weight: 60
url: /ko/python-net/split-pdf-document/
description: Python에서 PDF 파일을 개별 페이지, 동일한 부분, 고정 크기 그룹, 사용자 지정 페이지 범위, 홀수 또는 짝수 페이지로 분할하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF를 페이지 및 페이지 범위로 분할합니다.
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 파일을 분할하는 방법을 보여줍니다.PDF를 개별 페이지, 두 개의 동일한 부분, 고정 크기 페이지 그룹, 사용자 지정 페이지 범위, 이름이 지정된 페이지 그룹, 안정적인 파일 이름, 홀수 또는 짝수 페이지 파일로 분할하는 방법을 다룹니다.
---

이 페이지에서는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 파이썬에서 PDF 파일을 **분할**하는 방법을 보여줍니다.

배포, 검토 또는 다운스트림 처리를 위해 큰 PDF를 단일 페이지 파일, 동일한 부분, 고정 크기 그룹, 사용자 지정 페이지 범위 또는 홀수/짝수 페이지 세트로 나누어야 하는 경우 이러한 예를 사용하십시오.

## PDF 온라인 분할 예제

[Aspose.PDF 스플리터](https://products.aspose.app/pdf/splitter) PDF 분할 기능을 테스트할 수 있는 온라인 웹 응용 프로그램입니다.

[![어스포즈 스플릿 PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Python에서 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따르십시오.

1. PDF 문서의 페이지를 반복하여 살펴보세요. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 사물의 [페이지 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 수집
1. 각 이터레이션에 대해 새 Document 객체를 만들고 개별 객체를 추가합니다. [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 빈 문서에 개체 추가
1. 를 사용하여 새 PDF 저장 [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법

## Python에서 PDF를 여러 파일로 분할하기

다음 Python 코드 스니펫은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## PDF를 두 개의 동일한 부분으로 분할

1. PDF 문서를 로드합니다.
1. 총 페이지 수를 결정하십시오.
1. 중간점을 계산합니다.
1. 첫 번째 출력 문서를 생성합니다.
1. 첫 번째 문서에서 후반부 페이지를 제거합니다.
1. 첫 번째 부분을 저장합니다.
1. 두 번째 출력 문서를 생성합니다.
1. 두 번째 문서에서 전반부 페이지를 제거합니다.
1. 두 번째 부분을 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## PDF를 N페이지마다 여러 파일로 분할

Python용 Aspose.PDF 를 사용하여 고정된 페이지 수를 기준으로 PDF 문서를 여러 개의 작은 파일로 분할합니다.

1. PDF 문서를 로드합니다.
1. 총 페이지 수를 결정하십시오.
1. 파트별 페이지를 정의합니다.
1. 문서를 여러 청크 단위로 반복합니다.
1. 각 부품의 페이지 범위를 계산합니다.
1. 각 부품에 대해 새 문서를 작성합니다.
1. 페이지를 새 문서에 복사합니다.
1. 분할된 문서를 저장합니다.
1. 모든 페이지가 처리될 때까지 반복합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## 사용자 지정 페이지 범위로 PDF 분할

Python용 Aspose.PDF 를 사용하여 사용자 정의 페이지 범위를 기반으로 PDF 문서를 여러 파일로 분할합니다.

1. PDF 문서를 로드합니다.
1. 총 페이지 수를 결정하십시오.
1. (시작_페이지, 끝_페이지) 범위를 나타내는 튜플 목록을 만듭니다.
1. 정의된 범위를 반복합니다.
1. 시작 페이지의 유효성을 검사합니다.
1. 최종 페이지를 조정하세요.
1. 유효 범위를 검증합니다.
1. 각 범위에 대해 새 문서를 만듭니다.
1. 페이지를 새 문서에 복사합니다.
1. 분할된 각 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## PDF를 첫 페이지와 나머지 페이지로 분할

Python용 Aspose.PDF 를 사용하여 PDF 문서의 첫 페이지를 나머지 페이지와 분리합니다.

1. PDF 문서를 로드합니다.
1. 총 페이지 수를 결정하십시오.
1. 문서가 비어 있는지 확인합니다.
1. 첫 페이지에 사용할 문서를 만듭니다.
1. 첫 페이지를 추가합니다.
1. 첫 페이지 문서를 저장합니다.
1. 추가 페이지가 있는지 확인하세요.
1. 남은 페이지를 위한 문서를 생성합니다.
1. 남은 페이지를 복사합니다.
1. 나머지 페이지 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## PDF를 마지막 페이지와 이전 페이지로 분할

Python용 Aspose.PDF 를 사용하여 PDF 문서의 마지막 페이지를 추출하고 나머지 페이지와 분리합니다.

1. PDF 문서를 로드합니다.
1. 총 페이지 수를 결정하십시오.
1. 문서가 비어 있는지 확인합니다.
1. 마지막 페이지에 사용할 문서를 만듭니다.
1. 마지막 페이지를 추가합니다.
1. 마지막 페이지 문서를 저장합니다.
1. 단일 페이지 문서를 확인하십시오.
1. 원본 문서에서 마지막 페이지를 제거합니다.
1. 나머지 페이지를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## PDF를 세 부분으로 나누기

파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서를 세 부분으로 분리합니다.

1. PDF 문서를 로드합니다.
1. 총 페이지 수를 결정하십시오.
1. 문서가 비어 있는지 확인합니다.
1. 부품 크기 계산
1. 세 부분을 반복해 보세요.
1. 각 부품의 페이지 범위를 결정합니다.
1. 페이지 범위를 확인합니다.
1. 각 부품에 대해 새 문서를 작성합니다.
1. 파트 문서에 페이지를 복사합니다.
1. 각 부분을 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## 사용자 지정 PDF 페이지 스플리터

Python용 Aspose.PDF 를 사용하여 사용자 정의 페이지 그룹을 기반으로 PDF 문서를 여러 파일로 분할합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## PDF를 안정적인 파일 이름으로 개별 페이지로 분할

Python용 Aspose.PDF 를 사용하여 PDF 문서를 개별 페이지로 분할하고 안정적인 파일 이름으로 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## PDF를 홀수 및 짝수 페이지로 분할

Python용 Aspose.PDF 를 사용하여 PDF 문서를 각각 홀수 페이지와 짝수 페이지를 포함하는 두 개의 개별 파일로 분할합니다.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## 관련 문서 주제

- [파이썬에서 PDF 문서로 작업하기](/pdf/ko/python-net/working-with-documents/)
- [파이썬으로 PDF 파일 병합](/pdf/ko/python-net/merge-pdf-documents/)
- [파이썬에서 PDF 파일 최적화하기](/pdf/ko/python-net/optimize-pdf/)
- [파이썬에서 PDF 문서 조작하기](/pdf/ko/python-net/manipulate-pdf-document/)

