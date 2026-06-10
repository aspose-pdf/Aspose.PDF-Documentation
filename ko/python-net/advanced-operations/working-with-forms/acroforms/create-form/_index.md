---
title: 아크로폼 만들기 - Python에서 채울 수 있는 PDF 만들기
linktitle: 아크로폼 만들기
type: docs
weight: 10
url: /ko/python-net/create-form/
description: .NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에서 처음부터 AcroForm 필드를 만들 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 사용하여 PDF로 아크로폼을 만드는 방법
Abstract: >
    이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에서 AcroForm 필드를 만드는 방법을 설명합니다.TextBoxField를 사용한 기본 필드 만들기, 다중 위젯 텍스트 상자 모양 사용자 지정, 추가 필드 유형 (예: 라디오 버튼, 콤보 상자, 확인란, 목록 상자, 서명 필드 및 바코드 필드) 에 대해 설명합니다.이러한 예제는 데이터 수집 및 문서 자동화 워크플로를 위한 대화형 PDF 양식을 작성하는 데 도움이 됩니다.
---

## 처음부터 양식 작성

### PDF 문서에 양식 필드 추가

더 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스는 라는 이름의 컬렉션을 제공합니다 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) PDF 문서의 양식 필드를 관리하는 데 도움이 됩니다.

양식 필드를 추가하려면:

1. 추가하려는 양식 필드를 생성합니다.
1. 양식 컬렉션으로 전화하기 [추가](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) 방법.

### 텍스트 상자 필드 추가

다음 예에서는 를 추가하는 방법을 보여 줍니다. [텍스트 상자 필드](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rectangle = ap.Rectangle(10, 600, 110, 620, True)
    text_box_field = ap.forms.TextBoxField(page, rectangle)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Text Box"

    text_box_field.default_appearance = ap.annotations.DefaultAppearance(
        "Arial", 10, drawing.Color.dark_blue
    )

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field, 1)
    document.save(output_file_name)
```

### PDF의 다중 위젯 텍스트 상자 필드

Python과 Aspose.PDF 를 사용하여 PDF에 여러 위젯 모양이 포함된 텍스트 상자 양식 필드를 만들 수 있습니다.페이지에 여러 텍스트 입력 영역을 배치하고, 각 위젯에 서로 다른 글꼴과 색상을 적용하고, 테두리를 사용자 지정하고, 대화형 PDF 양식의 배경 스타일을 설정합니다.

1. 새 PDF 문서 만들기.
1. 텍스트 필드 위치를 정의합니다.
1. 다양한 기본 모양 만들기
1. 텍스트 상자 필드 만들기
1. 각 위젯에 모양 적용
1. 테두리 스타일을 사용자 지정합니다.
1. 양식에 필드 추가
1. PDF 파일을 저장합니다.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field_nt(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rects = [
        ap.Rectangle(10, 600, 110, 620, normalize_coordinates=True),
        ap.Rectangle(10, 630, 110, 650, normalize_coordinates=True),
        ap.Rectangle(10, 660, 110, 680, normalize_coordinates=True),
    ]

    default_appearances = [
        ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
        ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
        ap.annotations.DefaultAppearance(
            ap.text.FontRepository.find_font("Calibri"), 14, drawing.Color.dark_magenta
        ),
    ]

    text_box_field = ap.forms.TextBoxField(page, rects)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Some text"

    for i, widget in enumerate(text_box_field):
        widget.default_appearance = default_appearances[i]

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field)
    document.save(output_file_name)
```

## 기타 양식 필드 추가

다음 코드 스니펫은 라디오 버튼, 콤보 상자, 확인란, 목록 상자, 서명 필드 및 바코드 필드와 같은 다양한 필드 유형을 추가하는 방법을 보여줍니다.각 함수는 새 PDF 문서를 만들고, 선택한 옵션이 포함된 대상 필드를 추가하고, 업데이트된 파일을 저장합니다.

1. 라디오 버튼 필드 추가
1. 콤보 상자 필드 추가
1. 체크박스 필드 추가
1. 목록 상자 필드 추가
1. 서명 필드 추가
1. 바코드 필드 추가

### 라디오 버튼 필드 추가

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_radio_button(output_file_name):
    document = ap.Document()
    document.pages.add()

    radio = ap.forms.RadioButtonField(document.pages[1])
    radio.add_option(
        "Option 1", ap.Rectangle(100, 640, 120, 680, normalize_coordinates=True)
    )
    radio.add_option(
        "Option 2", ap.Rectangle(140, 640, 160, 680, normalize_coordinates=True)
    )

    document.form.add(radio)
    document.save(output_file_name)
```

### 콤보 상자 필드 추가

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_combo_box(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    combo = ap.forms.ComboBoxField(
        page, ap.Rectangle(100, 640, 150, 656, normalize_coordinates=True)
    )
    combo.add_option("Red")
    combo.add_option("Yellow")
    combo.add_option("Green")
    combo.add_option("Blue")
    combo.selected = 3

    document.form.add(combo)
    document.save(output_file_name)
```

### 체크박스 필드 추가

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_checkbox_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    checkbox = ap.forms.CheckboxField(
        page, ap.Rectangle(50, 620, 100, 650, normalize_coordinates=True)
    )
    checkbox.characteristics.background = ap.Color.aqua.to_rgb()
    checkbox.style = ap.forms.BoxStyle.CIRCLE

    document.form.add(checkbox)
    document.save(output_file_name)
```

### 목록 상자 필드 추가

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_list_box_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    list_box = ap.forms.ListBoxField(
        page, ap.Rectangle(50, 650, 100, 700, normalize_coordinates=True)
    )
    list_box.partial_name = "list"
    list_box.add_option("Red")
    list_box.add_option("Green")
    list_box.add_option("Blue")

    document.form.add(list_box)
    document.save(output_file_name)
```

### 서명 필드 추가

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_signature_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    signature_field = ap.forms.SignatureField(
        page, ap.Rectangle(100, 700, 200, 800, True)
    )
    signature_field.partial_name = "Signature1"
    document.form.add(signature_field)
    document.save(output_file_name)
```

### 바코드 필드 추가

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_barcode_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    barcode = ap.forms.BarcodeField(page, ap.Rectangle(100, 700, 200, 740, True))
    barcode.partial_name = "Barcode1"
    barcode.add_barcode("1234567890")
    document.form.add(barcode)
    document.save(output_file_name)
```

## 관련 주제

- [아크로폼 채우기](/pdf/ko/python-net/fill-form/)
- [아크로폼 추출](/pdf/ko/python-net/extract-form/)
- [아크로폼 수정](/pdf/ko/python-net/modifying-form/)
- [양식 데이터 가져오기 및 내보내기](/pdf/ko/python-net/import-export-form-data/)
