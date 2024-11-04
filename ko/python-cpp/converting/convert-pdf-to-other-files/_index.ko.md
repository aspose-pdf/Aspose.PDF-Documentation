---
title: Python에서 PDF를 텍스트로 변환
linktitle: PDF를 다른 형식으로 변환
type: docs
weight: 90
url: /python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: convert, PDF, EPUB, LaText, Text, XPS, Python
description: 이 주제에서는 PDF 파일을 Python을 사용하여 텍스트와 같은 다른 파일 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF를 텍스트로 변환

**Aspose.PDF for Python**은 전체 PDF 문서와 단일 페이지를 텍스트 파일로 변환하는 것을 지원합니다.

### PDF 문서를 텍스트 파일로 변환

'TextDevice' 클래스를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다.

1. 입력 및 출력 파일 경로 생성
1. [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)를 사용하여 PDF 추출기 파사드 인스턴스 생성
1. [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)를 사용하여 PDF 파일을 추출기에 바인딩

1. [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)를 사용하여 PDF 파일에서 텍스트 추출
1. 추출한 텍스트를 출력 파일에 작성
1. 'document.save' 메서드를 사용하여 출력 PDF 저장

다음 코드 스니펫은 모든 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```