---
title: Convert PDF to TXT in Python
linktitle: Convert PDF to TXT
type: docs
weight: 20
url: /python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: Aspose.PDF for Python via C++ library allows you to convert PDF to TXT format using Python. 
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Convert PDF to TXT

Aspose.PDF for Python via C++는 다음 단계를 따라 PDF 문서를 텍스트 파일로 변환하는 것을 지원합니다:

1. 입력 및 출력 파일 경로 생성
1. [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)를 사용하여 PDF 추출기 퍼사드 인스턴스 생성
1. [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)를 사용하여 PDF 파일을 추출기에 바인딩
1. [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)를 사용하여 PDF 파일에서 텍스트 추출
1. 추출된 텍스트를 출력 파일에 작성
1. 'document.save' 메서드를 사용하여 출력 PDF 저장.

다음 코드 스니펫은 Python을 통해 C++를 사용하여 JPG 이미지를 PDF로 변환하는 방법을 보여줍니다:

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # 데이터 디렉토리 경로 생성
    dataDir = os.path.join(os.getcwd(), "samples")

    # 입력 파일 경로 생성
    input_file = os.path.join(dataDir, "sample.pdf")

    # 출력 파일 경로 생성
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # PDF 추출기 외관의 인스턴스 생성
    extactor = apCore.facades_pdf_extractor_create()

    # PDF 파일을 추출기에 바인딩
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # PDF 파일에서 텍스트 추출
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # 추출한 텍스트를 출력 파일에 쓰기
    with open(output_file, 'w') as f:
        f.write(text)
```