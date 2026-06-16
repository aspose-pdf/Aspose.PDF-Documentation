---
title: PDF를 끝으로 분할
linktitle: PDF를 끝으로 분할
type: docs
weight: 40
url: /ko/python-net/split-pdf-to-end/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서를 주어진 페이지에서 마지막 페이지로 분할합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF를 특정 페이지에서 끝까지 분할하기
Abstract: Python용 Aspose.PDF 를 사용하여 PDF 문서를 주어진 페이지에서 마지막 페이지로 분할하는 방법을 알아봅니다.이 예제에서는 지정된 페이지부터 시작하여 모든 페이지를 추출하여 새 PDF 파일을 만드는 방법을 보여줍니다.
---

문서의 뒷부분이 별도의 파일로 필요할 때 PDF를 특정 페이지에서 끝까지 분할하는 것이 유용합니다.파이썬에서 split_to_end 메서드를 사용하여, 파이썬에서 split_to_end 메서드를 사용하면 Aspose.PDF [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 클래스를 사용하면 임의의 페이지 번호부터 문서의 마지막 페이지까지 페이지를 추출할 수 있습니다.이 방법은 수동으로 편집하지 않고도 발췌문을 만들거나, 장을 추출하거나, 큰 PDF의 일부를 처리하는 데 적합합니다.

1. PDF 파일 편집기 개체 만들기
1. 특정 페이지에서 끝까지 PDF를 분할합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
