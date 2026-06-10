---
title: 파이썬에서 PDF 페이지 이동
linktitle: PDF 페이지 이동
type: docs
weight: 100
url: /ko/python-net/move-pages/
description: Python에서 문서 내에서 또는 문서 간에 PDF 페이지를 이동하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 문서 간에 PDF 페이지 이동
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF의 페이지를 이동하는 방법을 설명합니다.한 페이지 또는 여러 페이지를 다른 문서로 이동하는 방법과 문서 및 PageCollection API를 사용하여 동일한 PDF 내에서 페이지 위치를 변경하는 방법을 알아봅니다.
---

## 한 PDF 문서에서 다른 PDF 문서로 페이지 이동

Python용 Aspose.PDF 를 사용하면 한 PDF에서 다른 PDF로 페이지 (단순히 복사하는 것이 아님) 를 이동할 수 있습니다.원본 문서에서 선택한 페이지를 제거한 다음 새 PDF 파일에 추가합니다.

한 책에서 한 페이지를 잘라내어 다른 책에 붙이는 것으로 생각하시면 됩니다. 이동 후에는 원본 파일에 해당 페이지가 더 이상 존재하지 않습니다.

1. 를 사용하여 소스 PDF 문서 열기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.
1. 이동할 특정 페이지 (이 경우 2페이지) 를 선택합니다. 이는 a를 나타냅니다. [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 새 PDF 문서 만들기 (다른 PDF 문서 인스턴스화) [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. 대상 문서를 사용하여 선택한 페이지를 새 PDF 문서에 추가합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (예: `another_document.pages.add(page)`).
1. 해당 문서를 통해 원본 문서에서 페이지를 삭제합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (예: `document.pages.delete(index)`).
1. 두 문서를 모두 저장합니다.

다음 코드 스니펫은 한 페이지를 이동하는 방법을 보여줍니다.

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## 한 PDF 문서에서 다른 PDF 문서로 여러 페이지 이동

복사와 달리 이 작업은 선택한 페이지를 전송합니다. 즉, 소스 파일에서 페이지를 제거하고 새 PDF에 저장합니다.

1. 비어 있는 새 대상 문서 만들기 (`Document`).
1. 소스 문서에서 여러 페이지 (이 경우 1페이지와 3페이지) 를 선택합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 선택한 페이지를 반복하여 대상 문서에 각 페이지를 추가합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 이동한 페이지가 포함된 대상 문서를 저장합니다.
1. 소스 문서를 사용하여 이동한 페이지를 소스 문서에서 삭제합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 수정된 소스 문서를 새 파일 이름으로 저장하여 두 버전을 모두 보존합니다.

다음 코드 스니펫은 여러 페이지를 이동하는 방법을 보여줍니다.

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## 페이지를 동일한 PDF 문서의 새 위치로 이동

PDF 레이아웃을 재구성하거나 편집할 때 일반적으로 필요한 동일한 문서 내의 특정 페이지를 다른 위치로 이동하는 방법을 보여줍니다.

1. 를 사용하여 입력 PDF 문서를 로드합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.
1. 이동할 페이지를 선택합니다 (페이지 2) — 이것은 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 문서의 끝에 해당 문서를 사용하여 추가합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 를 통해 이전 위치에서 원본 페이지를 삭제합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 수정한 문서를 새 파일로 저장합니다.

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 페이지 추가](/pdf/ko/python-net/add-pages/)
- [파이썬에서 PDF 페이지 삭제](/pdf/ko/python-net/delete-pages/)
- [파이썬으로 PDF 페이지 추출하기](/pdf/ko/python-net/extract-pages/)
