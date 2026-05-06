---
title: Создать AcroForm — создать заполняемый PDF в Python
linktitle: Создать AcroForm
type: docs
weight: 10
url: /ru/python-net/create-form/
description: Создайте поля AcroForm с нуля в PDF‑документах, используя Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как создать AcroForm в PDF, используя Python
Abstract: В этой статье объясняется, как создавать поля AcroForm в PDF‑документах, используя Aspose.PDF for Python via .NET. Охватывается базовое создание полей с TextBoxField, настройка внешнего вида многовидовых текстовых полей, а также дополнительные типы полей, такие как radio buttons, combo boxes, checkboxes, list boxes, signature fields и barcode fields. Эти примеры помогут вам создавать интерактивные PDF‑формы для сбора данных и автоматизации рабочих процессов с документами.
---

## Создать форму с нуля

### Добавление полей формы в PDF Document

Определённый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс предоставляет коллекцию с именем [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) что помогает управлять полями формы в PDF‑документе.

Чтобы добавить поле формы:

1. Создайте поле формы, которое вы хотите добавить.
1. Вызовите Form collection’s [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) метод.

### Добавление TextBoxField

В следующем примере показано, как добавить [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

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

### Текстовое поле с несколькими виджетами в PDF

Создайте текстовое поле формы с несколькими внешними видами виджетов в PDF, используя Python и Aspose.PDF. Оно размещает несколько областей ввода текста на странице, применяет разные шрифты и цвета к каждому виджету, настраивает границы и задаёт стили фона для интерактивной PDF‑формы.

1. Создайте новый PDF документ.
1. Определите позиции текстовых полей.
1. Создайте разные внешние виды по умолчанию.
1. Создайте текстовое поле.
1. Примените внешний вид к каждому виджету.
1. Настройте стиль границы.
1. Добавьте поле в форму.
1. Сохраните PDF‑файл.

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

## Добавление других полей формы

Следующие фрагменты кода показывают, как добавить различные типы полей, такие как переключатели, комбинированные списки, флажки, списки, поля подписи и поля штрих‑кода. Каждая функция создаёт новый PDF‑документ, добавляет целевое поле с выбранными параметрами и сохраняет обновлённый файл.

1. Добавьте поле переключателя
1. Добавьте поле комбобокса
1. Добавьте поле флажка
1. Добавьте поле списка
1. Добавьте поле подписи
1. Добавьте поле штрих‑кода

### Добавить поле переключателя

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

### Добавить поле комбобокса

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

### Добавить поле флажка

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

### Добавить поле списка

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

### Добавить поле подписи

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

### Добавить поле штрих‑кода

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

## Связанные темы

- [Заполнить AcroForm](/pdf/ru/python-net/fill-form/)
- [Извлечь AcroForm](/pdf/ru/python-net/extract-form/)
- [Изменение AcroForm](/pdf/ru/python-net/modifying-form/)
- [Импорт и экспорт данных формы](/pdf/ru/python-net/import-export-form-data/)
