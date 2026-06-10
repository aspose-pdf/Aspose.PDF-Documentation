---
title: 필드 콤 번호 설정
type: docs
weight: 70
url: /ko/python-net/set-field-comb-number/
description: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 양식 필드에 대한 콤 번호를 설정하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드의 콤 번호 설정하기
Abstract: 개발자는 Aspose.PDF for Python을 사용하여 양식 필드의 상자 수 (빗 번호) 를 프로그래밍 방식으로 설정하여 고정 길이 입력을 적용할 수 있습니다.이 문서에서는 “PIN”이라는 필드의 콤 번호를 설정하는 방법을 보여줍니다.
---

콤보 번호는 필드 내용이 동일한 간격의 상자로 분할되는 방식을 정의합니다. 이 상자는 PIN 코드, 일련 번호 또는 기타 고정 길이 입력 필드에 주로 사용됩니다.코드는 기존 PDF를 열고, 필드의 조합 번호를 설정하고, 수정된 문서를 저장합니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 양식 필드의 상자 (문자) 수를 정의하는 'set_field_comb_number' 메서드를 제공합니다.

1. 기존 PDF 양식을 엽니다.
1. 폼에디터 객체를 만듭니다.
1. 이름이 “PIN”인 필드의 조합 번호를 5로 설정합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```
