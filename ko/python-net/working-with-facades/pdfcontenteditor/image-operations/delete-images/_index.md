---
title: PDF에서 이미지 삭제
linktitle: PDF에서 이미지 삭제
type: docs
weight: 20
url: /ko/python-net/delete-images/
description:
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF 페이지에서 특정 이미지 삭제하기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 특정 이미지를 삭제하는 방법을 보여줍니다.특정 페이지의 이미지를 대상으로 지정하고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

경우에 따라 모든 시각적 개체를 지우지 않고 PDF에서 특정 이미지만 제거하고 싶을 수도 있습니다.를 사용하여 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)페이지 번호와 이미지 색인을 지정하여 선택한 이미지를 삭제할 수 있습니다.

이 코드 스니펫은 입력 PDF를 바인딩하고, 1페이지의 두 번째 이미지를 삭제하고, 다른 이미지는 그대로 두고 수정된 PDF를 저장합니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 지정된 페이지에서 특정 이미지를 삭제합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```
