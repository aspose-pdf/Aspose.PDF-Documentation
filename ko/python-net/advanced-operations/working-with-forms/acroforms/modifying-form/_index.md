---
title: 아크로폼 수정
linktitle: 아크로폼 수정
type: docs
weight: 45
url: /ko/python-net/modifying-form/
description: .NET을 통해 Python용 Aspose.PDF 를 사용하여 텍스트 지우기, 제한 설정, 필드 스타일 지정 및 필드 제거를 포함하여 PDF 문서의 AcroForm 필드를 수정할 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 양식 필드 관리 및 사용자 지정
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 AcroForm 필드를 수정하는 실제 예제를 제공합니다.타자기 양식 내용에서 텍스트 지우기, 텍스트 필드 문자 제한 설정 및 읽기, 사용자 지정 글꼴 모양 적용, 이름별 필드 제거에 대해 설명합니다.이러한 워크플로는 자동화된 PDF 처리 파이프라인에서 일반적인 양식 유지 관리 작업을 지원합니다.
---

## 양식의 텍스트 지우기

이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF의 타자기 양식 필드에서 텍스트를 지우는 방법을 보여줍니다.PDF의 첫 페이지를 스캔하고, 입력 양식을 식별하고, 내용을 제거하고, 업데이트된 문서를 저장합니다.이 방법은 PDF를 재배포하기 전에 양식 필드를 재설정하거나 삭제하는 데 유용합니다.

1. 입력 PDF 문서를 로드합니다.
1. 첫 페이지에서 양식에 액세스할 수 있습니다.
1. 각 양식을 반복하고 양식이 양식인지 확인하십시오. `Typewriter` 양식.
1. 텍스트 조각 흡수기를 사용하여 양식에서 텍스트 조각을 찾을 수 있습니다.
1. 각 조각의 텍스트를 지웁니다.
1. 수정한 PDF를 출력 파일에 저장합니다.

```python
import aspose.pdf as ap


def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## 필드 제한 설정

용도 `set_field_limit(field, limit)` ...에서 `FormEditor` 텍스트 필드에 허용되는 최대 문자 수를 정의합니다.

1. 만들기 `FormEditor` 목적.
1. 입력 PDF를 바인딩합니다.
1. 대상 필드의 필드 제한을 설정합니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## 필드 제한 가져오기

텍스트 필드에서 문자 제한을 읽을 수도 있습니다.

1. PDF 문서를 로드합니다.
1. 대상 양식 필드에 액세스합니다.
1. 필드가 a인지 확인하십시오. `TextBoxField`.
1. 읽기 및 인쇄 `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## 양식 필드에 사용자 지정 글꼴 설정

이 예제에서는 글꼴, 크기 및 색상을 포함하여 텍스트 상자 필드의 사용자 지정 기본 모양을 설정합니다.

1. PDF 문서를 로드합니다.
1. 대상 필드에 접근하여 유형을 확인합니다.
1. 에서 글꼴 찾기 `FontRepository`.
1. 새 항목 적용 `DefaultAppearance`.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## 기존 양식에서 필드 제거

이 코드는 PDF 문서에서 특정 양식 필드 (이름별) 를 제거하고.NET을 통해 Python용 Aspose.PDF 를 사용하여 업데이트된 파일을 저장합니다.

1. PDF 문서를 로드합니다.
1. 양식 필드를 이름별로 삭제합니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## 관련 주제

- [아크로폼 만들기](/pdf/ko/python-net/create-form/)
- [아크로폼 채우기](/pdf/ko/python-net/fill-form/)
- [아크로폼 추출](/pdf/ko/python-net/extract-form/)
- [양식 데이터 가져오기 및 내보내기](/pdf/ko/python-net/import-export-form-data/)
