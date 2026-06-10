---
title: PDF에서 모든 이미지 삭제
linktitle: PDF에서 모든 이미지 삭제
type: docs
weight: 10
url: /ko/python-net/delete-all-images/
description: 파이썬용 Aspose.PDF 파일을 사용하여 파사드 API를 통해 PDF 문서의 모든 이미지를 삭제합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF에서 모든 이미지 제거
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 Facades API를 통해 PDF 문서에서 모든 이미지를 삭제하는 방법을 보여줍니다.PDF를 바인딩하고, 포함된 모든 이미지를 제거하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

PDF 문서에는 일러스트레이션, 브랜딩 또는 장식용 이미지가 포함되어 있는 경우가 많습니다.파일 크기를 줄이거나 민감한 시각 자료를 보호하거나 텍스트 전용 버전을 준비하는 등 PDF에서 모든 이미지를 제거해야 하는 경우가 있을 수 있습니다.

사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)문서에 텍스트 내용만 포함되도록 프로그래밍 방식으로 PDF에서 모든 이미지를 제거할 수 있습니다.이 예제에서는 입력 PDF를 바인딩하고, 모든 이미지를 삭제하고, 수정된 파일을 저장합니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 모든 이미지를 삭제합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```
