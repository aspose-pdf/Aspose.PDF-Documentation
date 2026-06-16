---
title: 파이썬을 통해 PDF로 양식 게시
linktitle: 게시 양식
type: docs
weight: 75
url: /ko/python-net/posting-form/
description: .NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF AcroForms에 제출 버튼 및 제출 작업을 추가합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 제출 버튼 및 양식 제출 작업을 추가하는 방법
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 양식에 제출 기능을 추가하는 두 가지 방법을 보여줍니다.FormEditor를 통해 미리 만들어진 제출 버튼을 추가하거나 고급 제어를 위해 SubmitFormAction으로 사용자 지정 버튼 필드를 만들 수 있습니다.이러한 패턴은 PDF 양식을 서버 측 양식 처리 엔드포인트와 통합하는 데 도움이 됩니다.
---

## 양식 편집기에 제출 버튼 추가

다음 코드 스니펫은.NET을 통해 파이썬용 Aspose.PDF 의 FormEditor 클래스를 사용하여 PDF 양식에 제출 버튼을 추가하는 방법을 보여줍니다.이 버튼은 클릭 시 지정된 URL에 양식 데이터를 전송하도록 구성되어 있습니다.

1. 만들기 `FormEditor` 목적.
1. 대상 페이지에 제출 버튼을 추가합니다.
1. 제출 URL과 버튼 좌표를 설정합니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## 사용자 지정 제출 작업 추가

다음 코드 스니펫은.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 양식에 사용자 지정 제출 버튼을 만드는 방법을 설명합니다.이 버튼은 클릭 시 지정된 URL로 양식 데이터를 전송하도록 구성되어 있습니다.

1. .문서 () 를 사용하여 PDF를 엽니다.
1. 제출 작업을 생성합니다.
1. 대상 URL 및 제출 플래그를 설정합니다.
1. 버튼 필드를 만들고 클릭 동작을 바인딩합니다.
1. 양식에 버튼을 추가합니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## 관련 주제

- [아크로폼 만들기](/pdf/ko/python-net/create-form/)
- [아크로폼 채우기](/pdf/ko/python-net/fill-form/)
- [아크로폼 수정](/pdf/ko/python-net/modifying-form/)
- [양식 데이터 가져오기 및 내보내기](/pdf/ko/python-net/import-export-form-data/)