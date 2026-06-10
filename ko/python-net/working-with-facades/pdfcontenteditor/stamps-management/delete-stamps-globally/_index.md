---
title: 전체 스탬프 삭제
type: docs
weight: 60
url: /ko/python-net/delete-stamps-globally/
description: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF의 모든 페이지에서 전체적으로 러버 스탬프 주석을 삭제하는 방법을 보여줍니다.개별 페이지를 지정하지 않고 ID별로 스탬프를 제거하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에서 러버 스탬프를 전체적으로 삭제하기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF의 모든 페이지에서 전체적으로 러버 스탬프 주석을 삭제하는 방법을 보여줍니다.개별 페이지를 지정하지 않고 ID별로 스탬프를 제거하는 방법을 보여줍니다.
---

여러 페이지로 작업할 때는 문서 전체에서 특정 스탬프를 제거해야 할 수 있습니다.'delete_stamp_by_id () '및 'delete_stamp_by_ids ()' 메서드를 사용하면 식별자를 기준으로 스탬프를 전체적으로 삭제할 수 있으므로 각 페이지를 수동으로 반복할 필요가 없습니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. 여러 페이지에 러버 스탬프를 추가합니다.
1. ID를 사용하여 전 세계에서 스탬프를 삭제합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```
