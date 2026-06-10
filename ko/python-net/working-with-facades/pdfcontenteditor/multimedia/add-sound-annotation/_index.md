---
title: 사운드 주석 추가
linktitle: 사운드 주석 추가
type: docs
weight: 20
url: /ko/python-net/add-sound-annotation/
description: 이 예제에서는 입력 PDF를 바인딩하고, 1페이지에 사운드 주석을 추가하고, 수정된 PDF를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 사운드 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 오디오를 포함하는 방법을 보여줍니다.PDF 내에서 오디오 파일을 직접 재생하는 클릭 가능한 사운드 주석을 추가하는 방법을 보여줍니다.
---

PDF의 사운드 주석을 사용하면 음성 메모, 음악 또는 사운드 효과와 같은 오디오 콘텐츠를 문서에 추가할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)활성화 시 지정된 오디오 파일을 재생하는 페이지에서 클릭 가능한 작은 사각형을 정의할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 사운드 주석의 직사각형을 정의합니다.
1. 오디오 파일, 주석 이름, 페이지 번호 및 샘플링 속도를 지정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
