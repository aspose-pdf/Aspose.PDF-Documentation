---
title: C++를 통한 Python에서 PDF에 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: ko/python-cpp/add-pages/
description: 이 문서는 C++를 사용하여 Python에서 원하는 위치에 PDF 파일에 페이지를 삽입(추가)하는 방법을 가르칩니다.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 원하는 위치에 PDF 파일에 빈 페이지 삽입

이 코드 스니펫은 PDF 문서를 열고, 빈 페이지를 추가하며, 수정된 문서를 새로운 PDF 파일로 저장합니다.

PDF 파일에 빈 페이지를 삽입하려면:

1. PDF 문서를 엽니다
1. 문서에 새로운 빈 페이지를 추가합니다
1. 'document.save' 메서드를 사용하여 수정된 문서를 출력 파일로 저장합니다

다음 코드 스니펫은 PDF 파일에 페이지를 삽입하는 방법을 보여줍니다:

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # 샘플 PDF 파일이 위치한 디렉토리 경로 설정
    dataDir = os.path.join(os.getcwd(), "samples")

    # 입력 파일 경로 설정
    input_file = os.path.join(dataDir, "sample0.pdf")

    # 출력 파일 경로 설정
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # PDF 문서 열기
    document = apw.Document(input_file)

    # 문서에 새로운 빈 페이지 추가
    document.pages.add()

    # 수정된 문서를 출력 파일로 저장
    document.save(output_file)
```