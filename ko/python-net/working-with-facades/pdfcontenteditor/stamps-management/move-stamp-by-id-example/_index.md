---
title: ID로 스탬프 이동
type: docs
weight: 80
url: /ko/python-net/move-stamp-by-id-example/
description: 이 예에서는 페이지 1에 고무 스탬프를 추가한 다음 업데이트된 문서를 저장하기 전에 해당 ID를 사용하여 새 위치로 이동합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에서 ID별로 러버 스탬프 이동
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF에서 기존 러버 스탬프 주석의 위치를 변경하는 방법을 보여줍니다.스탬프를 만든 다음 해당 ID를 사용하여 프로그래밍 방식으로 이동하는 방법을 보여줍니다.
---

PDF에 러버 스탬프 주석을 추가한 후 위치를 조정해야 할 수 있습니다.'move_stamp_by_id () '메서드를 사용하면 스탬프를 다시 만들지 않고도 식별자를 기반으로 스탬프의 위치를 변경할 수 있습니다.이는 스탬프 배치를 동적으로 조정해야 하는 자동화된 워크플로우에서 유용합니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. 러버 스탬프 주석을 추가합니다.
1. ID를 사용하여 스탬프를 이동합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
