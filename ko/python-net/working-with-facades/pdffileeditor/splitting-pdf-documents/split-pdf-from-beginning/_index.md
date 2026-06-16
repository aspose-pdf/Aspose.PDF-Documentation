---
title: PDF를 처음부터 분리하기
linktitle: PDF를 처음부터 분리하기
type: docs
weight: 10
url: /ko/python-net/split-pdf-from-beginning/
description: 파이썬용 Aspose.PDF 를 사용하여 PDF 문서를 처음부터 분할합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 Aspose.PDF 파일을 사용하여 처음부터 PDF를 분리하기
Abstract: Python용 Aspose.PDF 를 사용하여 PDF 문서를 처음부터 분할하는 방법을 알아봅니다.이 예제에서는 첫 페이지부터 시작하여 특정 수의 페이지를 추출하여 새 PDF 문서를 만드는 방법을 보여줍니다.
---

문서의 처음 몇 페이지를 별도의 파일로 저장해야 하는 경우 PDF를 처음부터 분할하는 것이 유용합니다.파이썬에서 split_from_first 메서드를 사용하여, 파이썬에서 split_from_first 메서드를 사용했습니다. Aspose.PDF [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 클래스를 사용하면 페이지 1부터 시작하여 정의된 페이지 수를 추출할 수 있습니다.이 기능은 원본 파일을 수동으로 편집하지 않고도 큰 PDF의 발췌문, 미리 보기 또는 작은 부분을 생성하는 데 적합합니다.

1. PDF 파일 편집기 개체 만들기
1. 첫 페이지에서 PDF를 분할합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
