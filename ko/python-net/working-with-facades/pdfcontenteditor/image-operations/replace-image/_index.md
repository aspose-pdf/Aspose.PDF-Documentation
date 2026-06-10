---
title: PDF의 이미지 바꾸기
type: docs
weight: 30
url: /ko/python-net/replace-image/
description: 이 예제에서는 입력 PDF를 바인딩하고 1페이지의 첫 번째 이미지를 새 이미지로 바꾸고 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF의 이미지 바꾸기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 기존 이미지를 바꾸는 방법을 보여줍니다.페이지의 특정 이미지를 대상으로 지정하고 새 이미지로 바꾼 다음 업데이트된 PDF를 저장하는 방법을 보여줍니다.
---

PDF에는 로고, 다이어그램 또는 사진과 같이 업데이트하거나 교체해야 할 수 있는 이미지가 포함되어 있는 경우가 많습니다.와 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)페이지 번호, 이미지 색인 및 새 이미지 파일 경로를 제공하여 특정 페이지의 특정 이미지를 바꿀 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 특정 페이지의 특정 이미지를 대체합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
