---
title: Изменение AcroForm
linktitle: Изменение AcroForm
type: docs
weight: 45
url: /ru/python-net/modifying-form/
description: Изменять поля AcroForm в PDF‑документах с помощью Aspose.PDF for Python via .NET, включая очистку текста, установку ограничений, стилизацию полей и удаление полей.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление и настройка полей PDF‑форм
Abstract: В этой статье представлены практические примеры изменения полей AcroForm с помощью Aspose.PDF for Python via .NET. Описывается очистка текста из содержимого формы Typewriter, установка и чтение ограничений количества символов в текстовом поле, применение пользовательского внешнего вида Font и удаление полей по имени. Эти рабочие процессы поддерживают типовые задачи обслуживания форм в автоматизированных конвейерах обработки PDF.
---

## Очистить текст в форме

Этот пример демонстрирует, как очистить текст из полей формы Typewriter в PDF с помощью Aspose.PDF for Python via .NET. Он сканирует первую страницу PDF, определяет формы Typewriter, удаляет их содержимое и сохраняет обновлённый документ. Такой подход полезен для сброса или санитизации полей формы перед повторным распространением PDF.

1. Загрузите входной PDF‑документ.
1. Получите доступ к формам на первой странице.
1. Итерируйтесь по каждой форме и проверьте, является ли она `Typewriter` Form.
1. Используйте TextFragmentAbsorber для поиска текстовых фрагментов в форме.
1. Очистите текст каждого фрагмента.
1. Сохраните измененный PDF в выходной файл.

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

## Установить ограничение поля

Использовать `set_field_limit(field, limit)` из `FormEditor` определить максимальное количество символов, разрешённых в текстовом поле.

1. Создать `FormEditor` объект.
1. Привяжите входной PDF.
1. Установите ограничение поля для целевого поля.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## Получить ограничение поля

Вы также можете прочитать ограничение количества символов из текстового поля.

1. Загрузите PDF-документ.
1. Получите доступ к целевому полю формы.
1. Убедитесь, что поле является `TextBoxField`.
1. Читать и печатать `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## Установить пользовательский шрифт для поля формы

Этот пример задает пользовательское оформление по умолчанию для поля ввода текста, включая шрифт, размер и цвет.

1. Загрузите PDF-документ.
1. Получите доступ к целевому полю и проверьте его тип.
1. Найдите шрифт в `FontRepository`.
1. Применить новое `DefaultAppearance`.
1. Сохраните обновлённый PDF.

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

## Удалить поля в существующей Form

Этот код удаляет конкретное поле формы (по его имени) из PDF‑документа и сохраняет обновлённый файл, используя Aspose.PDF for Python via .NET.

1. Загрузите PDF-документ.
1. Удалить поле Form по имени.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## Связанные темы

- [Создать AcroForm](/pdf/ru/python-net/create-form/)
- [Заполнить AcroForm](/pdf/ru/python-net/fill-form/)
- [Извлечь AcroForm](/pdf/ru/python-net/extract-form/)
- [Импорт и экспорт данных формы](/pdf/ru/python-net/import-export-form-data/)
