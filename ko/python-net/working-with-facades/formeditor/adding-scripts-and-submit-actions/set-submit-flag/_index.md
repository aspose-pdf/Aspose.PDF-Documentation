---
title: 제출 플래그 설정
linktitle: 제출 플래그 설정
type: docs
weight: 50
url: /ko/python-net/set-submit-flag/
description: Python용 Aspose.PDF 를 사용하여 PDF 양식 버튼의 제출 플래그를 프로그래밍 방식으로 설정하는 방법을 알아봅니다.이렇게 하면 사용자가 버튼을 클릭했을 때 XFDF와 같은 특정 형식으로 양식 데이터를 제출할 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 파일을 사용하여 PDF 양식 버튼의 제출 플래그 설정하기
Abstract: 양식 데이터를 다른 형식으로 서버나 엔드포인트에 전송하도록 PDF 양식을 구성할 수 있습니다.개발자는 버튼 필드에 제출 플래그를 설정하여 데이터 전송 방식을 정의할 수 있습니다.이 자습서에서는 FormEditor 클래스를 사용하여 PDF 문서의 기존 제출 단추에 제출 플래그를 설정하고 업데이트된 파일을 저장하는 방법을 보여줍니다.
---

PDF 양식에는 사용자 입력을 서버로 보내는 [전송] 단추가 포함되어 있는 경우가 많습니다.제출 플래그는 전송되는 데이터 형식 (예: XFDF, FDF, HTML) 을 결정합니다.

1. PDF 문서를 바인딩합니다.
1. 기존 제출 버튼에 액세스합니다.
1. 원하는 형식의 제출 플래그를 설정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
