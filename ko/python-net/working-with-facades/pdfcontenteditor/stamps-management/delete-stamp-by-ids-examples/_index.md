---
title: ID별 스탬프 삭제
linktitle: ID별 스탬프 삭제
type: docs
weight: 85
url: /ko/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFContentEditor를 사용하여 PDF에서 단일 또는 다중 ID로 러버 스탬프 삭제
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 고유 ID를 기반으로 PDF에서 러버 스탬프 주석을 제거하는 방법을 보여줍니다.여기에는 단일 ID 삭제와 다중 ID 삭제에 대한 내용이 모두 포함됩니다.
---

여러 스탬프가 포함된 PDF로 작업할 때는 다른 스탬프에 영향을 주지 않고 특정 스탬프를 제거해야 하는 경우가 종종 있습니다.ID 기반 삭제를 사용하면 제거할 스탬프를 정확하게 제어할 수 있습니다.

- 'delete_stamp_by_id (스탬프_ID, 페이지_번호) '— 특정 페이지에서 해당 ID로 단일 스탬프를 삭제합니다.
- 'delete_stamp_by_ids (페이지_번호, 스탬프_ID) '— 특정 페이지에서 해당 ID별로 여러 스탬프를 삭제합니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. ID가 다른 고무 스탬프 두 개를 추가하세요.
1. 단일 ID 및 다중 ID 삭제 방법을 모두 사용하여 스탬프를 삭제합니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

