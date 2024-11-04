---
title: 파이썬을 사용하여 PDF에서 텍스트 추출하기
linktitle: PDF에서 텍스트 추출
type: docs
weight: 10
url: /python-cpp/extract-text/
description: 이 섹션은 파이썬 라이브러리를 사용하여 PDF 문서에서 텍스트를 추출하는 방법을 설명합니다.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출하기

PDF에서 텍스트를 추출하는 것은 쉽지 않습니다. 많은 PDF 리더가 PDF 이미지나 스캔된 PDF에서 텍스트를 추출할 수 없습니다. 그러나 **C++를 통한 파이썬용 Aspose.PDF** 도구를 사용하면 모든 PDF 파일에서 쉽게 텍스트를 추출할 수 있습니다.

코드 스니펫을 확인하고 PDF에서 텍스트를 추출하는 단계를 따르세요:

1. 파이썬용 Aspose.PDF 라이브러리를 가져옵니다.
1. PDF 문서에서 텍스트와 이미지를 추출하는 데 사용되는 새로운 추출기 객체를 만듭니다.
1. 추출기 객체를 PDF 파일에 바인딩합니다. 이것이 추출의 원천입니다.
1. PDF 문서에서 모든 텍스트를 추출하고 일부 변수에 저장합니다.

1. 무엇이든지 하세요, 추출된 텍스트를 콘솔에 출력하고, 일부 조각을 검색하세요 등등

```python
from AsposePdfPython import *

extactor = Extract()
extractor_bind_pdf(extactor,"blank_pdf_document.pdf")
text = extractor_extract_text(extactor)

print(text)
```