---
title: 제출 URL 설정
type: docs
weight: 40
url: /ko/python-net/set-submit-url/
description: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 양식의 버튼 필드에 대한 제출 작업을 구성하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 버튼의 제출 URL 설정
Abstract: 이 문서에서는 기존 PDF 양식을 열고, FormEditor 클래스를 사용하여 단추 필드의 제출 URL을 정의하고, 작업이 성공하는지 확인하고, 업데이트된 PDF 문서를 저장하는 방법을 설명합니다.
---

사용자가 [제출] 단추를 클릭할 때 웹 서버에 데이터를 전송하도록 PDF 양식을 디자인할 수 있습니다.개발자는 Aspose.PDF for Python을 사용하여 양식 필드에 대한 제출 작업을 프로그래밍 방식으로 구성할 수 있습니다.
제출 URL을 설정하면 버튼을 클릭할 때 양식에서 사용자가 입력한 데이터를 서버로 보낼 수 있습니다.이 기능은 PDF 양식이 웹 응용 프로그램, 데이터베이스 또는 처리 서비스에 정보를 제출해야 하는 워크플로우에 유용합니다.

를 사용하여 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 에서 수업 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈을 통해 개발자는 기존 PDF 양식의 버튼 필드에 제출 URL을 프로그래밍 방식으로 할당할 수 있습니다.

1. 기존 PDF 양식을 엽니다.
1. Script_Demo_Button이라는 버튼 필드를 찾으십시오.
1. 양식 데이터를 제출할 URL을 지정합니다.
1. 작업이 성공적으로 적용되었는지 확인합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
