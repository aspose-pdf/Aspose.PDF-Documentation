---
title: Set Size of PDF using pythob via C++
linktitle: Set Size of PDF
type: docs
weight: 30
url: /ko/python-cpp/get-and-set-page-properties/
description: 이 섹션에서는 Python을 통해 C++를 사용하여 문서의 크기와 같은 PDF 페이지 속성을 가져오거나 설정하는 방법을 보여줍니다.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일 크기 설정

Aspose.PDF for Python via C++를 사용하면 Python 응용 프로그램에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다.

다음 코드 스니펫은 PDF 파일을 열고, **Crop box**를 조정하여 첫 번째 페이지 크기를 조정하고(크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다), 수정된 문서를 새 파일로 저장합니다.

1. 입력 파일에서 문서 객체를 생성합니다
1. [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)를 사용하여 문서에서 페이지 컬렉션을 가져옵니다.

1. [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)을 사용하여 페이지 컬렉션에서 첫 번째 페이지를 가져옵니다.
1. [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)을 사용하여 페이지에서 크롭 박스 직사각형을 가져옵니다.
1. 크롭 박스의 새로운 좌표를 계산합니다.
1. 새로운 값으로 크롭 박스 좌표를 업데이트합니다.
1. 'document.save' 메서드를 사용하여 수정된 문서를 출력 파일에 저장합니다.

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # 현재 작업 디렉토리를 가져와 "samples" 디렉토리 경로를 만듭니다.
    dataDir = os.path.join(os.getcwd(), "samples")

    # 입력 및 출력 파일 경로를 만듭니다.
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # 입력 파일에서 문서 객체를 생성합니다.
    doc = apCore.document_create_from_file(inputFile)

    # 문서에서 페이지 컬렉션을 가져옵니다.
    pages = apCore.document_get_pages(doc)

    # 페이지 컬렉션에서 첫 번째 페이지를 가져옵니다.
    page = apCore.page_collection_get_page(pages, 1)

    # 페이지에서 크롭 박스 직사각형을 가져옵니다.
    crop_box = apCore.page_get_rectangle(page)

    # 크롭 박스의 새로운 좌표를 계산합니다.
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # 새로운 값으로 크롭 박스 좌표를 업데이트합니다.
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # 수정된 문서를 출력 파일에 저장합니다.
    apCore.document_save(doc, output_file)

    # 문서 핸들을 닫습니다.
    apCore.close_handle(doc)
```