---
title: 최적화를 통한 PDF 파일 연결
linktitle: 최적화를 통한 PDF 파일 연결
type: docs
weight: 30
url: /ko/python-net/concatenate-pdf-files-with-optimization/
description: 파이썬용 Aspose.PDF 파일을 사용하여 여러 PDF 파일을 최적화된 단일 PDF로 연결합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 최적화된 출력으로 PDF 파일 병합
Abstract: Python용 Aspose.PDF 를 사용하여 여러 PDF 파일을 최적화된 단일 PDF로 연결하는 방법을 알아봅니다.이 예제에서는 크기 최적화를 활성화하여 내용과 서식을 보존하면서 출력 파일 크기를 줄이는 방법을 보여줍니다.
---

여러 PDF를 병합할 때 특히 이미지나 복잡한 내용이 포함된 경우 결과 파일이 커질 수 있습니다.개발자는 Aspose.PDF for Python을 사용하여 연결 중에 최적화를 통해 품질 저하 없이 파일 크기를 줄일 수 있습니다.에 있는 optimize_size 프로퍼티는 [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 클래스를 사용하면 병합된 PDF가 간결하고 효율적이므로 공유, 저장 또는 보관에 적합합니다.

1. PDF 파일 편집기 개체를 만들고 최적화를 활성화합니다.
1. PDF 파일 병합.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
