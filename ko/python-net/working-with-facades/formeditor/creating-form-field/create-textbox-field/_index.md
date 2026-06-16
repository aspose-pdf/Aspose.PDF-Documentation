---
title: 텍스트 상자 필드 생성
linktitle: 텍스트 상자 필드 생성
type: docs
weight: 60
url: /ko/python-net/create-textbox-field/
description: Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 PDF 문서에 텍스트 상자 필드를 추가하는 방법을 알아봅니다.이 자습서에서는 여러 텍스트 필드를 삽입하고, 기본값을 설정하고, 업데이트된 PDF 문서를 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 파일을 사용하여 PDF에 텍스트 상자 필드 만들기
Abstract: PDF 양식의 텍스트 상자 필드를 사용하면 텍스트를 입력하고 편집할 수 있으므로 문서를 대화형 방식으로 사용자 친화적으로 만들 수 있습니다.이 자습서에서는 파이썬용 Aspose.PDF FormEditor 클래스를 사용하여 PDF에서 텍스트 상자 양식 필드를 만드는 방법을 배웁니다.이 예제에서는 여러 필드를 추가하고, 기본값을 지정하고, 수정된 PDF를 저장하는 방법을 보여줍니다.
---

PDF 양식에는 사용자가 이름, 주소 또는 주석과 같은 텍스트를 입력해야 하는 경우가 많습니다.TextBox 필드는 PDF 문서 내에서 직접 편집 가능한 필드를 제공하여 이 기능을 활성화합니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스를 사용하면 텍스트 필드, 확인란, 라디오 버튼, 목록 상자, 콤보 상자 및 단추를 추가할 수 있으므로 대화형 PDF를 쉽게 만들 수 있습니다.

1. 기존 PDF 문서를 로드합니다.
1. 사용자 입력을 위한 여러 TextBox 필드를 추가합니다.
1. 각 필드에 기본값을 설정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
