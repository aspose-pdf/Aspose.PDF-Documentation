---
title: 파이썬을 통해 C++로 PDF 병합하는 방법
linktitle: PDF 파일 병합하기
type: docs
weight: 10
url: /ko/python-cpp/merge-pdf-documents/
description: 이 페이지는 파이썬을 사용하여 여러 PDF 문서를 하나의 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 파이썬을 통해 C++로 여러 PDF를 하나의 PDF로 병합 또는 결합하기

파이썬과 Aspose의 C++ 라이브러리를 활용하여 여러 PDF 파일을 손쉽게 하나의 PDF로 효율적으로 병합할 수 있습니다.

두 개의 PDF 파일을 연결하려면:

1. 첫 번째 문서를 엽니다
1. 그런 다음 두 번째 문서의 페이지를 첫 번째 문서에 추가합니다
1. 'document.save' 메서드를 사용하여 연결된 출력 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일을 연결하는 방법을 보여줍니다.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # 첫 번째 문서 열기
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # 두 번째 문서의 페이지를 첫 번째 문서에 추가
    document1.pages.add(document2.pages)

    # 연결된 출력 파일 저장
    document1.save(output_file)
```