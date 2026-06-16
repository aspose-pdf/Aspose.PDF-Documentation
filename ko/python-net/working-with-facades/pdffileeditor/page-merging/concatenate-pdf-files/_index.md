---
title: 여러 PDF 파일 연결
linktitle: 여러 PDF 파일 연결
type: docs
weight: 20
url: /ko/python-net/concatenate-pdf-files/
description: 파이썬용 Aspose.PDF 파일을 사용하여 여러 PDF 파일을 단일 문서로 결합합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 여러 PDF 파일을 하나의 PDF로 병합
Abstract: Python용 Aspose.PDF 를 사용하여 여러 PDF 파일을 단일 문서로 결합하는 방법을 알아봅니다.이 예제에서는 concatenate 메서드를 사용하여 내용과 서식을 유지하면서 여러 PDF를 원활하게 병합하는 방법을 보여줍니다.
---

PDF 파일 병합은 문서 관리, 보고 및 자동화된 워크플로우에서 흔히 하는 작업입니다.개발자는 Python용 Aspose.PDF 를 사용하여 여러 PDF 파일을 하나의 통합 문서로 쉽게 결합할 수 있습니다.의 연결 방법은 [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class는 입력 파일의 모든 페이지가 원래 레이아웃과 내용을 유지하면서 최종 출력에 보존되도록 합니다.이 방법은 포괄적인 보고서를 만들거나, 양식을 결합하거나, 여러 문서를 효율적으로 보관하는 데 유용합니다.

1. PDF 파일 편집기 개체 만들기
1. 여러 PDF 파일 병합.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
