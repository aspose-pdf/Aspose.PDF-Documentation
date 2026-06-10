---
title: PDF 메타데이터 지우기
type: docs
weight: 10
url: /ko/python-net/clear-pdf-metadata/
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서에서 모든 메타데이터를 제거합니다.
lastmod: "2026-06-10"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 를 사용하여 PDF 메타데이터 지우기
Abstract: 이 가이드는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 모든 메타데이터를 제거하는 방법을 설명합니다.표준 메타데이터 필드와 사용자 지정 메타데이터 필드를 모두 지우고 정리된 PDF를 저장하는 방법을 배우게 됩니다.이는 개인 정보 보호, 보안 또는 공개 릴리스를 위한 PDF 준비에 유용합니다.
---

PDF에는 제목, 작성자, 키워드, 작성 날짜 및 사용자 지정 필드와 같은 메타데이터가 포함되어 있는 경우가 많습니다.일부 시나리오에서는 배포 또는 보관 전에 PDF에서 모든 메타데이터를 제거해야 할 수 있습니다.Aspose.PDF 에서는 모든 메타데이터를 쉽게 제거할 수 있는 clear_info () 메서드를 제공합니다.지운 후에는 save () 메서드를 사용하여 PDF를 저장할 수 있습니다.

1. PDF 파일을 로드합니다.
1. 모든 메타데이터를 지웁니다.
1. 깨끗한 PDF를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
