---
title: 제출 버튼 생성
linktitle: 제출 버튼 생성
type: docs
weight: 50
url: /ko/python-net/create-submit-button/
description: Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 PDF 문서에 제출 버튼을 추가하는 방법을 알아봅니다.이 자습서에서는 양식 데이터를 지정된 URL로 제출하고 업데이트된 PDF를 저장하는 버튼을 만드는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 파일을 사용하여 PDF에 제출 버튼 만들기
Abstract: PDF 양식의 [전송] 단추를 사용하면 양식 데이터를 서버나 엔드포인트로 직접 보낼 수 있습니다.이 가이드에서는 Python용 Aspose.PDF 의 FormEditor 클래스를 사용하여 PDF에 제출 버튼 필드를 추가하는 방법을 배웁니다.이 예제에서는 단추의 이름, 레이블, 대상 URL 및 위치를 구성한 다음 업데이트된 PDF 문서를 저장하는 방법을 보여줍니다.
---

대화형 PDF 양식에서는 설문 조사 결과, 신청서 양식 또는 피드백 데이터 전송과 같은 처리를 위해 사용자가 입력 내용을 제출해야 하는 경우가 많습니다.제출 버튼 필드는 버튼을 웹 엔드포인트에 연결하여 이 기능을 제공합니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 버튼, 체크 박스, 라디오 버튼, 텍스트 필드 및 기타 양식 컨트롤을 추가할 수 있습니다.

1. 기존 PDF 문서를 로드합니다.
1. 특정 페이지에 제출 버튼 필드를 추가합니다.
1. 버튼 레이블과 대상 제출 URL을 설정합니다.
1. 새 버튼으로 업데이트된 PDF를 저장합니다.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
