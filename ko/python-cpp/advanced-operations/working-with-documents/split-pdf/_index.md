---
title: 파이썬으로 PDF 프로그램으로 나누기
linktitle: PDF 파일 분할
type: docs
weight: 20
url: ko/python-cpp/split-pdf-document/
keywords: split pdf into multiple files, split pdf into separate pdfs, split pdf python
description: 이 주제는 C++ 응용 프로그램을 통해 파이썬에서 PDF 페이지를 개별 PDF 파일로 나누는 방법을 보여줍니다.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 페이지를 분할하는 것은 큰 파일을 개별 페이지 또는 페이지 그룹으로 나누고자 하는 사람들에게 유용한 기능일 수 있습니다.

## 실시간 예제

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter)는 프레젠테이션 분할 기능이 어떻게 작동하는지 조사할 수 있는 무료 온라인 웹 응용 프로그램입니다.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

이 주제는 Python C++ 응용 프로그램에서 PDF 페이지를 개별 PDF 파일로 나누는 방법을 보여줍니다. Python을 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따를 수 있습니다:

코드 스니펫은 필요한 디렉토리와 파일 경로를 설정하고, PDF 문서를 열고, 그런 다음 문서의 각 페이지를 반복합니다.
 각 페이지마다 새 문서를 만들고, 현재 페이지를 새 문서로 복사한 후, 특정 명명 규칙에 따라 새 문서를 별도의 PDF 파일로 저장합니다.

1. 입력 문서 열기
1. 페이지 수 초기화
1. 문서의 모든 페이지를 반복

## Python에서 PDF를 여러 파일 또는 개별 PDF로 분할하기

다음 Python 코드 스니펫은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # 문서 열기
    document = apw.Document(inputFile)

    pageCount = 1

    # 모든 페이지를 반복

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```