---
title: 두 개의 PDF 파일을 연결해 보십시오
type: docs
weight: 90
url: /ko/python-net/try-concatenate-two-files/
description: 파이썬용 Aspose.PDF 파일을 사용하여 두 개의 PDF 파일을 연결합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 예외 없이 두 개의 PDF 파일을 안전하게 병합
Abstract: Python용 Aspose.PDF 파일을 사용하여 두 개의 PDF 파일을 안전하게 연결하는 방법을 알아봅니다.try_concatenate 메서드는 예외를 발생시키지 않고 파일을 병합하므로 작업 실패 시 적절한 오류 처리가 가능합니다.
---

파일 손상, 호환되지 않는 형식 또는 기타 문제로 인해 두 PDF 파일 병합이 실패할 수 있습니다.파이썬용 Aspose.PDF 파일을 사용하면 PDFFileEditor 클래스의 try_concatenate 메서드를 사용하면 두 PDF를 안전하게 병합할 수 있습니다.작업이 실패하면 예외를 발생시키는 대신 False를 반환하므로 자동화된 워크플로우 또는 일괄 처리에서의 오류 처리를 완전히 제어할 수 있습니다.

1. PDF 파일 편집기 개체 만들기
1. 두 개의 PDF 파일을 병합해 봅니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
