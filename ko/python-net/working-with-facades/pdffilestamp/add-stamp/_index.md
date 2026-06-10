---
title: PDF에 스탬프 추가
type: docs
weight: 40
url: /ko/python-net/add-stamp/
description: Python에서 PDFFileStamp를 사용하여 PDF 페이지에 스탬프를 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: Python에서 PDF에 텍스트 스탬프 추가
Abstract: 이 문서에서는 PDFFileStamp 파사드를 사용하여.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에 스탬프 콘텐츠를 추가하는 방법을 설명합니다.스탬프를 만들고, 페이지에 배치하고, 회전과 불투명도를 제어하고, 업데이트된 PDF를 저장하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 파일 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) PDF 페이지에 반복되는 내용을 추가하기 위한 외관.머리글, 바닥글 및 페이지 번호 외에도 문서의 각 페이지에 텍스트 기반 스탬프를 배치하는 데 사용할 수 있습니다.

## PDF에 스탬프 추가

스탬프를 구성한 후 입력 PDF를 다음 위치에 바인딩합니다. `PdfFileStamp`스탬프를 추가하고 출력 파일을 저장합니다.이렇게 하면 구성된 스탬프가 문서 전체에 적용됩니다.

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
