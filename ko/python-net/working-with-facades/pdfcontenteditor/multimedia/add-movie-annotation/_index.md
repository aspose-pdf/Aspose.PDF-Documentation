---
title: 동영상 주석 추가
linktitle: 동영상 주석 추가
type: docs
weight: 10
url: /ko/python-net/add-movie-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고, 1페이지에 동영상 주석을 추가하고, 업데이트된 PDF를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF에 동영상 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 동영상 (비디오) 을 포함하는 방법을 보여줍니다.PDF 내에서 비디오를 직접 재생하는 클릭 가능한 주석을 추가하는 방법을 보여줍니다.
---

PDF의 동영상 주석을 사용하면 비디오와 같은 멀티미디어 콘텐츠를 문서에 포함할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 비디오가 표시될 페이지에 사각형을 정의할 수 있습니다.클릭하면 PDF에서 직접 비디오를 재생할 수 있으므로 문서를 더욱 인터랙티브하고 매력적으로 만들 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 동영상 주석의 사각형을 정의합니다.
1. 삽입할 비디오 파일을 지정합니다.
1. 주석의 페이지 번호를 지정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
