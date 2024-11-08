---
title: PDF 문서 생성
linktitle: PDF 생성
type: docs
weight: 10
url: /ko/python-cpp/create-document/
description: 이 페이지는 Aspose.PDF for Python via C++ 라이브러리를 사용하여 처음부터 PDF 문서를 생성하는 방법을 설명합니다.
---

개발자에게는 프로그래밍적으로 PDF 파일을 생성해야 하는 많은 시나리오가 있습니다. 소프트웨어에서 프로그래밍적으로 PDF 보고서 및 기타 PDF 파일을 생성해야 할 수 있습니다. 처음부터 코드와 기능을 작성하는 것은 다소 길고 비효율적입니다. Python을 사용하여 PDF 파일을 생성하는 더 나은 솔루션은 **Aspose.PDF for Python via C++**입니다.

## Python을 사용하여 PDF 파일 생성

Python을 사용하여 PDF 파일을 생성하려면 다음 단계를 사용할 수 있습니다.

* Aspose.PDF for Python via C++ 라이브러리에서 모든 클래스 및 메서드를 가져옵니다.
* [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)를 사용하여 빈 PDF 문서를 나타내는 새 Document 객체를 생성합니다.

* 문서에 있는 모든 페이지를 포함하는 [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/) 객체를 가져옵니다.
* 문서 모음의 끝에 새 페이지를 추가하고 [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/) 추가된 페이지를 나타내는 Page 객체를 반환합니다.
* 현재 작업 디렉토리에 지정된 이름으로 파일에 문서를 저장합니다.
* 문서에 대한 핸들을 닫고 관련된 모든 리소스를 해제합니다.

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```

## DOM을 기반으로 PDF 파일 생성

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```