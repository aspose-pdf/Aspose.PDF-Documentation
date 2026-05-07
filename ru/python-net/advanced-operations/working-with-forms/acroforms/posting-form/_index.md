---
title: Отправка данных из форм в PDF с помощью Python
linktitle: Отправка данных из форм
type: docs
weight: 75
url: /ru/python-net/posting-form/
description: Добавьте кнопки отправки и действия отправки в PDF AcroForms, используя Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить кнопки отправки и действия отправки формы в PDF, используя Python
Abstract: В этой статье показаны два подхода к добавлению функции отправки в PDF‑формы с помощью Aspose.PDF for Python via .NET. Вы можете добавить готовую кнопку отправки через FormEditor или создать пользовательское поле кнопки с SubmitFormAction для расширенного управления. Эти шаблоны помогают интегрировать PDF‑формы с конечными точками серверной обработки форм.
---

## Добавить кнопку отправки с помощью FormEditor

Следующий фрагмент кода демонстрирует, как добавить кнопку отправки в PDF-форму с использованием класса FormEditor в Aspose.PDF for Python via .NET. Кнопка настроена на отправку данных формы по указанному URL при нажатии.

1. Создайте `FormEditor` объект.
1. Добавьте кнопку отправки на целевую страницу.
1. Установите URL отправки и координаты кнопки.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## Добавить пользовательское действие отправки

Следующий фрагмент кода объясняет, как создать пользовательскую кнопку отправки в PDF-форме с использованием Aspose.PDF for Python via .NET. Кнопка настроена на отправку данных формы по указанному URL при нажатии.

1. Откройте PDF с помощью ap.Document().
1. Создайте действие отправки.
1. Установите целевой URL и флаги отправки.
1. Создайте поле кнопки и привяжите к нему действие щелчка.
1. Добавьте кнопку в форму.
1. Сохраните обновлённый PDF.

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

## Связанные темы

- [Создать AcroForm](/pdf/ru/python-net/create-form/)
- [Заполнить AcroForm](/pdf/ru/python-net/fill-form/)
- [Изменение AcroForm](/pdf/ru/python-net/modifying-form/)
- [Импорт и экспорт данных формы](/pdf/ru/python-net/import-export-form-data/)