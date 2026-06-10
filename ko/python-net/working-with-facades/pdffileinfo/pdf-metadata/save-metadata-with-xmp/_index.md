---
title: XMP로 메타데이터 저장
linktitle: XMP로 메타데이터 저장
type: docs
weight: 30
url: /ko/python-net/save-metadata-with-xmp/
description: .NET을 통해 파이썬용 Aspose.PDF 파일과 함께 XMP를 사용하여 PDF 메타데이터를 저장합니다.
lastmod: "2026-06-10"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 파일을 사용하여 XMP에 PDF 메타데이터 저장하기
Abstract: 이 가이드는.NET을 통해 Python용 Aspose.PDF 와 함께 XMP (확장 가능한 메타데이터 플랫폼) 를 사용하여 PDF 메타데이터를 저장하는 방법을 보여줍니다.XMP를 사용하면 표준 메타데이터와 사용자 지정 메타데이터가 모두 PDF에 표준화된 XML 형식으로 내장되므로 응용 프로그램과 워크플로우 간의 호환성이 향상됩니다.
---

PDF 메타데이터는 여러 가지 방법으로 저장할 수 있으며, XMP는 PDF 파일에 메타데이터를 포함하기 위한 현대적이고 표준화된 방법입니다.Aspose.PDF 기능을 사용하면 제목, 주제, 키워드, 작성자 등의 표준 필드를 업데이트한 다음 XMP 형식으로 저장하여 호환성을 높이고 미래에 대비할 수 있습니다.기존 메타데이터 저장 방법보다 이 방법을 사용하는 것이 좋습니다.

1. PDF 파일을 로드합니다.
1. 표준 메타데이터 필드를 설정합니다.
1. 메타데이터를 XMP 형식으로 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
