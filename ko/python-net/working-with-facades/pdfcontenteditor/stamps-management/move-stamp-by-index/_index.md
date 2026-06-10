---
title: 색인별 스탬프 이동
linktitle: 색인별 스탬프 이동
type: docs
weight: 90
url: /ko/python-net/move-stamp-by-index/
description: Python용 Aspose.PDF 페이지의 색인을 사용하여 PDF에서 러버 스탬프 주석의 위치를 변경하는 방법
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 인덱스 기반 위치 지정을 사용하여 PDF에서 러버 스탬프 이동
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 페이지가 포함된 페이지의 색인을 사용하여 PDF에서 러버 스탬프 주석의 위치를 변경하는 방법을 보여줍니다.여기서는 여러 스탬프를 만들고 이동 작업에 사용할 수 있도록 준비하는 방법을 중점적으로 설명합니다.
---

PDF 편집에서는 기존 러버 스탬프의 위치를 조정해야 할 수 있습니다.이 코드 스니펫은 다음과 같은 방법을 보여줍니다.

- 같은 페이지에 여러 스탬프 추가
- 색인을 사용하여 위치를 변경할 수 있도록 준비하십시오.
- 페이지, 색인 및 새 좌표를 지정하여 스탬프를 이동할 수도 있습니다.

'move_stamp (페이지_번호, 스탬프_인덱스, new_x, new_y) '메서드는 스탬프를 정확하게 재배치할 수 있습니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 목적.
1. PDF를 편집기에 바인딩합니다.
1. 페이지에 여러 개의 러버 스탬프를 추가합니다.
1. 이동 작업을 수행하기 전에 문서를 저장합니다.
1. 인덱스별로 특정 스탬프를 이동합니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    
