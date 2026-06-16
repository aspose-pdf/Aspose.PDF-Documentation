---
title: 고유한 접미사로 PDF 양식 연결
linktitle: 고유한 접미사로 PDF 양식 연결
type: docs
weight: 50
url: /ko/python-net/concatenate-pdf-forms/
description: 고유한 양식 필드 이름을 유지하면서 Python용 Aspose.PDF 를 사용하여 여러 PDF 양식을 연결합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 필드 이름 충돌을 피하면서 Python에서 PDF 양식 병합
Abstract: 고유한 양식 필드 이름을 유지하면서 Python용 Aspose.PDF 를 사용하여 여러 PDF 양식을 연결하는 방법을 알아봅니다.이 예제에서는 대화형 양식 필드가 포함된 PDF를 병합할 때 이름 충돌을 방지하기 위해 사용자 지정 접미사를 설정하는 방법을 보여줍니다.
---

여러 파일에 같은 이름의 필드가 있는 경우 PDF 양식을 병합하면 충돌이 발생할 수 있습니다.개발자는 Python용 Aspose.PDF 를 사용하여 연결 중에 양식 필드에 고유한 접미사를 할당할 수 있습니다.의 unique_suffix 속성은 [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class는 충돌하는 필드의 이름을 자동으로 변경하여 상호 작용을 유지하고 모든 양식 데이터가 제대로 작동하도록 합니다.이 방법은 설문조사, 응용 프로그램 또는 모든 대화형 PDF 문서를 프로그래밍 방식으로 결합하는 데 적합합니다.

1. PDFFileEditor 객체를 만들고 고유한 접미사를 설정합니다.
1. PDF 양식 병합.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_forms(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.unique_suffix = (
        "_xy_%NUM%"  # Set a unique suffix to avoid form field name conflicts
    )
    pdf_editor.concatenate(files_to_merge, output_file)
```
