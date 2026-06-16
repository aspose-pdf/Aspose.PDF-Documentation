---
title: PDF 메타데이터 설정
linktitle: PDF 메타데이터 설정
type: docs
weight: 50
url: /ko/python-net/set-pdf-metadata/
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서의 메타데이터를 수정하고 저장합니다.
lastmod: "2026-06-10"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 사용하여 PDF 메타데이터 업데이트
Abstract: 이 가이드는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서의 메타데이터를 수정하고 저장하는 방법을 설명합니다.제목, 주제, 키워드, 작성자와 같은 표준 PDF 속성과 사용자 지정 메타데이터 필드를 업데이트하는 방법을 보여줍니다.마지막에 이르면 프로그래밍 방식으로 PDF 메타데이터를 업데이트하고 변경 내용을 저장할 수 있습니다.
---

PDF 문서에는 표준 메타데이터 (제목, 주제, 키워드, 작성자, 작성자) 와 XMP 속성으로 저장된 사용자 정의 메타데이터가 모두 포함될 수 있습니다.Aspose.PDF 는 Python에서 이러한 속성을 수정할 수 있는 간단한 API를 제공합니다.이 가이드에서는 다음을 사용하여 이러한 필드를 업데이트하고 수정된 PDF 파일을 저장하는 방법을 설명합니다. [PDF 파일 정보](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) 수업.

1. PDF 파일을 로드합니다.
1. 표준 메타데이터를 업데이트합니다.
1. 맞춤 메타데이터를 추가하거나 업데이트합니다.
1. 업데이트된 메타데이터를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
