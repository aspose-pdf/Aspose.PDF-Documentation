---
title: 새로운 기능
linktitle: 새로운 기능
type: docs
weight: 10
url: ko/python-net/whatsnew/
description: 이 페이지에서는 최근 릴리스에서 소개된 Aspose.PDF for Python via .NET의 가장 인기 있는 새로운 기능을 소개합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## Aspose.PDF 23.12의 새로운 기능

Aspose.PDF 23.12부터 새로운 변환 기능에 대한 지원이 추가되었습니다:

- PDF를 Markdown으로 변환 구현

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- OFD를 PDF로 변환 구현

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


Python 3.6에 대한 지원이 중단되었습니다.

## Aspose.PDF 23.11의 새로운 기능

23.11부터 숨겨진 텍스트를 제거할 수 있습니다. 다음 코드 스니펫을 사용할 수 있습니다:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # 이 옵션은 숨겨진 텍스트 교체 후 다른 텍스트 조각이 이동하는 것을 방지하는 데 사용할 수 있습니다.
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```    

## Aspose.PDF 23.8의 새로운 기능

23.8 버전부터 증분 업데이트 감지를 추가로 지원합니다.

PDF 문서에서 증분 업데이트를 감지하는 기능이 추가되었습니다.
 이 함수는 문서가 증분 업데이트로 저장된 경우 'true'를 반환합니다. 그렇지 않으면 'false'를 반환합니다.

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

또한, 23.8은 중첩된 체크박스 필드를 사용하는 방법을 지원합니다. 많은 작성 가능한 PDF 양식에는 라디오 그룹으로 작동하는 체크박스 필드가 있습니다:

- 다중 값 체크박스 필드 생성:

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # 첫 번째 체크박스 그룹 옵션 값 설정
    checkbox.export_value = "option 1"
    # 기존 옵션 바로 아래에 새 옵션 추가
    checkbox.add_option("option 2")
    # 주어진 사각형에 새 옵션 추가
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # 추가된 체크박스 선택
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- 다중 값 체크박스의 값 가져오기 및 설정:

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # 허용된 값은 AllowedStates 컬렉션에서 검색할 수 있습니다.
    # Value 속성을 사용하여 체크박스 값을 설정합니다.
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # 이전에 설정된 값, 예: "option 1"
    # 값은 AllowedStates의 요소여야 합니다.
    checkbox.value = "option 2"
    checkbox_value = checkbox.value  # option 2
    # Value를 "Off"로 설정하거나 Checked를 false로 설정하여 체크박스를 선택 해제합니다.
    checkbox.value = "Off"
    # 또는, 대안으로:
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- 사용자 클릭 시 체크박스 상태 업데이트:

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # 예를 들어, 마우스 클릭의 좌표
    # 옵션 1: 페이지의 주석을 살펴봅니다.
    page = document.pages[5]
    for annotation in page.annotations:
        if(annotation.rect.contains(point)):
            widget = cast(ap.annotations.WidgetAnnotation, annotation)
            checkbox = cast(ap.forms.CheckboxField, widget.parent)
            if(annotation.active_state == "Off"):
                checkbox.value = widget.get_checked_state_name()
            else:
                checkbox.value = "Off"
        break
    # 옵션 2: AcroForm의 필드를 살펴봅니다.
    for widget in document.form:
        field = cast(ap.forms.Field, widget)
        if(field == None):
            continue
        checkBoxFound = False
        for annotation in field:
            if(annotation.rect.contains(point)):
                checkBoxFound = True
                if(annotation.active_state=="Off"):
                    annotation.parent.value = annotation.get_checked_state_name()
                else:
                    annotation.parent.value = "Off"
            if(checkBoxFound):
                break
```


## Aspose.PDF 23.7의 새로운 기능

23.7 버전부터 도형 추출 추가를 지원합니다:

```python

    import aspose.pdf as ap

    input1_file = DIR_INPUT + "input_1.pdf"
    input2_file = DIR_INPUT + "input_2.pdf"

    source = ap.Document(input1_file)
    dest = ap.Document(input2_file)

    graphic_absorber = ap.vector.GraphicsAbsorber()
    graphic_absorber.visit(source.pages[1])
    area = ap.Rectangle(90, 250, 300, 400, True)
    dest.pages[1].add_graphics(graphic_absorber.elements, area)
```

텍스트 추가 시 오버플로우 감지 기능도 지원합니다:

```python

    import aspose.pdf as ap

    output_file = DIR_OUTPUT + "output.pdf"
    doc = ap.Document()
    paragraph_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan."
    fragment = ap.text.TextFragment(paragraph_content)
    rectangle = ap.Rectangle(100, 600, 500, 700, False)
    paragraph = ap.text.TextParagraph()
    paragraph.vertical_alignment = ap.VerticalAlignment.TOP
    paragraph.formatting_options.wrap_mode = ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.rectangle = rectangle
    is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    while is_fit_rectangle == False:
        fragment.text_state.font_size -= 0.5
        is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    paragraph.append_line(fragment)
    builder = ap.text.TextBuilder(doc.pages.add())
    builder.append_paragraph(paragraph)
    doc.save(output_file)
```


## Aspose.PDF 23.6의 새로운 기능

HTML, Epub 페이지의 제목을 설정할 수 있는 기능 지원:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NEW PAGE & TITILE"  # <-- 이것이 추가됨

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## Aspose.PDF 23.5의 새로운 기능

23.5 버전부터 RedactionAnnotation FontSize 옵션 추가를 지원합니다. 이 작업을 해결하기 위해 다음 코드 스니펫을 사용하십시오:

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # 특정 페이지 영역에 대한 RedactionAnnotation 인스턴스 생성
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # 편집 주석에 인쇄할 텍스트
    annot.overlay_text = "(Unknown)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # 편집 주석 위에 오버레이 텍스트 반복
    annot.repeat = False
    # 여기에 새 속성 있음!
    annot.font_size = 20
    # 첫 페이지의 주석 컬렉션에 주석 추가
    doc.pages[1].annotations.add(annot, False)
    # 주석을 평면화하고 페이지 내용을 편집합니다 (즉, 편집된 주석 아래의 텍스트 및 이미지 제거)
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


파이썬 3.5에 대한 지원이 중단되었습니다. 파이썬 3.11에 대한 지원이 추가되었습니다.

## Aspose.PDF 23.3의 새로운 기능

버전 23.3에서는 이미지에 해상도를 추가하는 지원이 도입되었습니다. 이 문제를 해결하기 위해 두 가지 방법을 사용할 수 있습니다:

```python

    import aspose.pdf as ap

    input_file = DIR_INPUT + "input.jpg"
    table = ap.Table()
    table.column_widths = "600"
    image = ap.Image()
    image.is_apply_resolution = True
    image.file = input_file
    for i in range(0, 2):
        row = table.rows.add()
        cell = row.cells.add()
        cell.paragraphs.add(image)

    page.paragraphs.add(table)
```

이미지는 스케일된 해상도로 배치되며, IsApplyResolution 속성과 함께 FixedWidth 또는 FixedHeight 속성을 설정할 수 있습니다.

## Aspose.PDF 23.1의 새로운 기능

23.1 버전부터 프린터 마크 주석 생성을 지원합니다.

프린터 마크는 여러 판 작업의 구성 요소를 식별하고 생산 중 일관된 출력을 유지하는 데 도움을 주기 위해 페이지에 추가된 그래픽 심볼이나 텍스트입니다.
 인쇄 산업에서 일반적으로 사용되는 예는 다음과 같습니다:

- 판을 정렬하기 위한 등록 대상
- 색상 및 잉크 밀도를 측정하기 위한 회색 램프 및 색상 막대
- 출력 매체가 잘릴 위치를 나타내는 자르기 표시

우리는 색상 및 잉크 밀도를 측정하기 위한 색상 막대 옵션의 예를 보여드리겠습니다. 기본 추상 클래스 PrinterMarkAnnotation과 이에서 파생된 자식 클래스 ColorBarAnnotation이 있습니다. 이 클래스는 이미 이러한 줄무늬를 구현하고 있습니다. 예제를 확인해 봅시다:

```python

    import aspose.pdf as ap

    out_file = DIR_OUTPUT  + "ColorBarTest.pdf"
    doc = ap.Document()
    page = doc.pages.add()
    page.trim_box = ap.Rectangle(20, 20, 580, 820, True)
    add_annotations(page)
    doc.save(out_file)


def add_annotations(page: ap.Page):
    rect_black = ap.Rectangle(100, 300, 300, 320, True)
    rect_cyan = ap.Rectangle(200, 600, 260, 690, True)
    rect_magenta = ap.Rectangle(10, 650, 140, 670, True)
    color_bar_black = ap.annotations.ColorBarAnnotation(page, rect_black, ap.annotations.ColorsOfCMYK.BLACK)
    color_bar_cyan = ap.annotations.ColorBarAnnotation(page, rect_cyan, ap.annotations.ColorsOfCMYK.CYAN)
    color_ba_magenta = ap.annotations.ColorBarAnnotation(page, rect_magenta, ap.annotations.ColorsOfCMYK.BLACK)
    color_ba_magenta.color_of_cmyk = ap.annotations.ColorsOfCMYK.MAGENTA
    color_bar_yellow = ap.annotations.ColorBarAnnotation(page, ap.Rectangle(400, 250, 450, 700, True), ap.annotations.ColorsOfCMYK.YELLOW)
    page.annotations.add(color_bar_black, False)
    page.annotations.add(color_bar_cyan, False)
    page.annotations.add(color_ba_magenta, False)
    page.annotations.add(color_bar_yellow, False)
```
Also support the vector images extraction. 벡터 이미지 추출도 지원합니다. Try using the following code to detect and extract vector graphics: 다음 코드를 사용하여 벡터 그래픽을 감지하고 추출해 보세요:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```