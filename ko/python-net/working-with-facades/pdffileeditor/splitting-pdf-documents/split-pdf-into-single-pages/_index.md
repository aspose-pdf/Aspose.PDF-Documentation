---
title: PDF를 단일 페이지로 분할
linktitle: PDF를 단일 페이지로 분할
type: docs
weight: 30
url: /ko/python-net/split-pdf-into-single-pages/
description: 파이썬용 Aspose.PDF 를 사용하여 PDF 문서를 단일 페이지 PDF로 분할합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF를 개별 페이지로 분할하기
Abstract: Python용 Aspose.PDF 를 사용하여 PDF 문서를 단일 페이지 PDF로 나누는 방법을 알아봅니다.이 방법은 유연한 문서 관리 및 처리를 위해 원본 PDF에서 각 페이지를 추출하고 별도의 파일로 저장합니다.
---

PDF를 단일 페이지로 분할하면 문서 섹션을 페이지 단위로 처리, 인쇄 또는 배포하는 데 유용합니다.파이썬에서 Aspose.PDF 를 사용하는 'split_to_pages' 메서드는 [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 클래스는 소스 문서의 각 페이지에 대해 별도의 PDF 파일을 만듭니다.이 방법을 사용하면 원본 레이아웃과 콘텐츠를 보존하면서 보관, 검토 또는 개별 공유를 위해 페이지를 자동으로 추출할 수 있습니다.

1. PDF 파일 편집기 개체 만들기
1. PDF를 개별 페이지로 분할합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```
