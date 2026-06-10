---
title: 두 개의 PDF 파일 연결
linktitle: 두 개의 PDF 파일 연결
type: docs
weight: 60
url: /ko/python-net/concatenate-two-files/
description: 파이썬용 Aspose.PDF 파일을 사용하여 두 개의 PDF 파일을 단일 문서로 연결합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 두 개의 PDF 파일을 하나의 PDF로 병합
Abstract: Python용 Aspose.PDF 를 사용하여 두 개의 PDF 파일을 단일 문서로 연결하는 방법을 알아봅니다.이 예제에서는 원본 내용과 서식을 유지하면서 두 PDF를 원활하게 병합하는 방법을 보여줍니다.
---

두 PDF 파일을 결합하는 것은 보고서, 계약 또는 양식을 통합할 때 자주 하는 작업입니다.Python용 Aspose.PDF 파일을 사용하면 concatenate 메서드를 사용하여 프로그래밍 방식으로 두 개의 PDF를 단일 문서로 병합할 수 있습니다. [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 수업.이렇게 하면 원본 레이아웃, 내용 및 구조를 유지하면서 두 파일의 모든 페이지가 출력 PDF에 포함됩니다.

1. PDF 파일 편집기 개체 만들기
1. 두 개의 PDF 파일 병합.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
