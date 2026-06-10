---
title: 파이썬에서 PDF 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: /ko/python-net/add-pages/
description: Python에서 PDF 문서에 페이지를 추가하거나 삽입하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬으로 PDF 페이지 추가 또는 삽입
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 파일에 페이지를 추가하는 방법을 설명합니다.문서 및 PageCollection API를 사용하여 특정 위치에 빈 페이지를 삽입하고, 문서 끝에 페이지를 추가하고, 다른 PDF에서 페이지를 가져오는 방법을 알아봅니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 PDF 문서에 대한 유연한 페이지 수준 작업을 제공합니다.다음을 통해 페이지를 관리할 수 있습니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 에 페이지 추가 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 특정 위치 또는 파일 끝에

생성 워크플로우 중에 기존 PDF에 새 빈 페이지를 삽입하거나 문서 끝에 페이지를 추가해야 하는 경우 이 페이지를 사용합니다.

## PDF 파일에 페이지 추가 또는 삽입

.NET을 통한 파이썬용 Aspose.PDF 기능은 특정 색인에 페이지 삽입과 PDF 끝에 페이지 추가를 모두 지원합니다.

### PDF 파일에 빈 페이지 삽입

PDF 파일에 빈 페이지를 삽입하려면:

1. 기존 항목 열기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 적절한 방법을 사용합니다.
1. 를 사용하여 특정 색인에 새 빈 페이지를 삽입합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` 방법.
1. 수정한 내용 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 원하는 출력 경로로

기존 PDF 파일의 지정된 위치에 빈 페이지 삽입:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### PDF 파일 끝에 빈 페이지 추가

때로는 문서가 빈 페이지에서 끝나도록 하고 싶을 때가 있습니다.이 항목에서는 PDF 문서 끝에 빈 페이지를 삽입하는 방법을 설명합니다.

PDF 파일 끝에 빈 페이지를 삽입하려면:

1. 기존 항목 열기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 적절한 방법을 사용합니다.
1. 를 사용하여 문서 끝에 새 빈 페이지를 추가합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` 방법.
1. 업데이트 내용 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

다음 코드 스니펫은 PDF 파일 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### 다른 PDF 문서에서 페이지 추가

.NET을 통한 파이썬용 Aspose.PDF 파일을 사용하면 새로운 것을 만들 수 있습니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), 초기 페이지를 추가한 다음 다른 PDF의 페이지를 해당 페이지로 가져옵니다.

1. 새 만들기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 새 공백 추가 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 그리고 그 위에 글자를 써서 쓰세요 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. 다른 기존 항목 열기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 복사 a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 그 문서에서.
1. 복사한 페이지를 사용하여 기본 문서에 붙여넣기 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 결합된 파일을 저장합니다.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 페이지 이동](/pdf/ko/python-net/move-pages/)
- [파이썬에서 PDF 페이지 삭제](/pdf/ko/python-net/delete-pages/)
- [파이썬으로 PDF 페이지 추출하기](/pdf/ko/python-net/extract-pages/)
