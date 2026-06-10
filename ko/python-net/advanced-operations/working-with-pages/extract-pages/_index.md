---
title: 파이썬에서 PDF 페이지 추출하기
linktitle: PDF 페이지 추출
type: docs
weight: 80
url: /ko/python-net/extract-pages/
description: Python에서 단일 또는 여러 PDF 페이지를 새 파일로 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 사용하여 PDF 페이지를 추출하는 방법
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 파일에서 페이지를 추출하는 방법을 설명합니다.1 기반 페이지 인덱싱과 PageCollection API를 사용하여 단일 페이지 또는 여러 페이지를 새 문서에 복사하는 방법을 알아봅니다.
---

## PDF에서 단일 페이지 추출

PDF 문서에서 특정 페이지를 추출하고 새 파일로 저장합니다.스크립트는 Aspose.PDF 라이브러리를 사용하여 원본 문서를 변경하지 않고 원하는 페이지를 새 PDF로 복사합니다.이는 PDF를 분할하거나 중요한 페이지를 분리하여 배포할 때 유용합니다.

1. 를 사용하여 소스 PDF를 로드합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. 새 만들기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 추출한 페이지를 보관합니다.
1. 원하는 항목 추가 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 원본 문서에서 대상 문서를 사용하여 새 PDF로 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - 이 예에서는 페이지 2가 추출됩니다 (1 기반 인덱싱).
1. 새 파일 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 추출된 페이지를 지정된 출력 파일로 가져옵니다.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## PDF에서 여러 페이지 추출

PDF 문서에서 특정 페이지를 여러 개 추출하여 새 파일에 저장합니다.Aspose.PDF 라이브러리를 사용하면 원본 문서는 그대로 두고 선택한 페이지가 새 PDF로 복사됩니다.이는 큰 문서의 관련 부분만 포함하는 작은 PDF를 만들 때 유용합니다.

1. 를 사용하여 소스 PDF를 로드합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. 새 만들기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 추출한 페이지를 보관할 수 있습니다.
1. 추출할 페이지를 선택합니다 (이 예에서는 1부터 시작하는 인덱싱을 사용하는 2페이지와 3페이지).
1. 선택한 각 항목 추가 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 원본 문서에서 해당 문서를 사용하여 새 PDF로 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 새 파일 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 추출된 페이지와 함께 지정된 출력 파일에

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 페이지 삭제](/pdf/ko/python-net/delete-pages/)
- [파이썬에서 PDF 페이지 이동](/pdf/ko/python-net/move-pages/)
- [파이썬으로 PDF 파일 분할하기](/pdf/ko/python-net/split-document/)
