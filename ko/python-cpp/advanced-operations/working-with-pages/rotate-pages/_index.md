---
title: Python을 통한 C++로 PDF 페이지 회전
linktitle: PDF 페이지 회전
type: docs
weight: 20
url: ko/python-cpp/rotate-pages/
description: 이 주제는 Python을 통해 C++로 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

때때로 PDF 페이지는 스캔 또는 생성 문제로 인해 잘못된 방향을 가질 수 있습니다. 페이지를 회전하면 올바른 방향으로 표시되어 읽기와 보기가 더 쉬워집니다.
PDF 페이지를 회전하면 다양한 장치와 플랫폼에서 일관된 보기 경험을 유지할 수 있습니다. 

PDF 페이지를 회전하면 주석, 댓글 또는 서명 추가와 같은 편집 작업을 용이하게 할 수 있습니다. 페이지를 원하는 방향으로 회전시킴으로써, 편집 및 검토 프로세스를 보다 효율적으로 만들 수 있습니다.

또한, PDF 문서를 인쇄할 때 페이지가 올바르게 정렬되어 잘못된 정렬이나 자르기 문제를 피하는 것이 중요합니다.
 페이지를 인쇄하기 전에 필요한 경우 회전하면 인쇄 출력을 최적화하고 콘텐츠가 의도한 대로 표시되도록 할 수 있습니다.  
PDF 페이지를 회전하는 것은 다양한 맥락과 목적에 따라 문서의 가독성, 일관성 및 표현을 개선하는 데 유용한 기능입니다.

이 주제에서는 Python을 사용하여 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 업데이트하거나 변경하는 방법을 설명합니다.

## 페이지 방향 변경

C++를 통해 Aspose.PDF for Python은 페이지 방향 변경과 같은 훌륭한 기능을 지원합니다.

1. 입력 파일에서 문서 객체를 생성합니다.
1. 'apCore.document_get_pages'를 사용하여 문서에서 페이지 컬렉션을 가져옵니다.
1. 'apCore.page_collection_get_page'를 사용하여 페이지 컬렉션에서 첫 번째 페이지를 가져옵니다.
1. 'apCore.page_set_rotate'를 사용하여 페이지를 시계 방향으로 90도 회전합니다.
1. 'document.save' 메서드를 사용하여 수정된 문서를 출력 파일에 저장합니다.

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # 샘플 파일이 포함된 디렉토리의 경로 생성
    dataDir = os.path.join(os.getcwd(), "samples")

    # 입력 및 출력 파일의 경로 생성
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "rotated_document.pdf")

    # 입력 파일을 로드하여 문서 객체 생성
    doc = apCore.document_create_from_file(inputFile)

    # 문서에서 페이지 컬렉션 가져오기
    pages = apCore.document_get_pages(doc)

    # 컬렉션에서 첫 번째 페이지 가져오기
    page = apCore.page_collection_get_page(pages, 1)

    # 페이지를 시계 방향으로 90도 회전
    apCore.page_set_rotate(page, apCore.Rotation(apCore.on90))

    # 수정된 문서를 출력 파일에 저장
    apCore.document_save(doc, output_file)

    # 리소스를 해제하기 위해 문서 핸들 닫기
    apCore.close_handle(doc)
```