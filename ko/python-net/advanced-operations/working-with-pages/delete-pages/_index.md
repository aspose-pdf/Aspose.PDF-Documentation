---
title: 파이썬에서 PDF 페이지 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 80
url: /ko/python-net/delete-pages/
description: Python에서 PDF 파일의 페이지를 삭제하는 방법을 알아보세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 하나 이상의 PDF 페이지 삭제
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 파일에서 페이지를 제거하는 방법을 설명합니다.PageCollection API를 사용하여 문서에서 한 페이지 또는 여러 페이지를 삭제한 다음 업데이트된 PDF를 저장하는 방법을 알아봅니다.
---

.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.특정 페이지를 삭제하려면 다음을 사용하십시오. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 의 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

문서를 공유, 보관 또는 결합하기 전에 PDF에서 불필요한 페이지를 제거해야 하는 경우 이 워크플로우를 사용하십시오.

## PDF 파일에서 페이지 삭제

.NET을 통한 파이썬용 Aspose.PDF 파일은 입력 PDF에서 페이지 2를 삭제하고 업데이트된 문서를 새 파일에 저장합니다.이 기능은 문서의 나머지 부분을 변경하지 않고 원하지 않거나 민감한 페이지를 제거하는 데 유용합니다.

1. 입력 PDF를 a로 로드합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 를 사용하여 페이지를 삭제합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 전화해 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 업데이트된 PDF 파일을 저장하는 방법

다음 코드 스니펫은 Python을 사용하여 PDF 파일에서 특정 페이지를 삭제하는 방법을 보여줍니다.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## PDF 문서에서 여러 페이지 삭제

여러 페이지를 삭제하면 한 번의 작업으로 지정된 페이지 세트를 제거할 수 있으므로 페이지를 하나씩 삭제하는 것보다 효율적입니다.결과 PDF는 원본 문서를 그대로 유지하면서 새 파일에 저장됩니다.

1. 입력 PDF를 a로 로드합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 를 사용하여 페이지 배열에 나열된 페이지를 삭제합니다. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. 업데이트 내용 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 새 파일로.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 페이지 추가](/pdf/ko/python-net/add-pages/)
- [파이썬에서 PDF 페이지 이동](/pdf/ko/python-net/move-pages/)
- [파이썬으로 PDF 페이지 추출하기](/pdf/ko/python-net/extract-pages/)
