---
title: Создать AcroForm - Создать заполняемый PDF на Python
linktitle: Создать AcroForm
type: docs
weight: 10
url: /ru/python-net/create-form/
description: С помощью Aspose.PDF для Python вы можете создать форму с нуля в вашем PDF‑файле
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как создать AcroForm в PDF с помощью Python
Abstract: В статье представлено руководство по созданию поля формы в PDF‑документе с использованием библиотеки Aspose.PDF для Python. В ней вводится класс `Document`, который содержит коллекцию `Form` для управления полями формы. Процесс добавления поля формы включает создание нужного поля и использование метода `add` из коллекции `Form`. Приведён конкретный пример, показывающий добавление `TextBoxField` в PDF‑документ. Пример включает подробный код, демонстрирующий создание `TextBoxField`, установку его свойств, таких как позиция, имя, значение, граница и цвет, а также последующее добавление его в документ. Изменённый PDF затем сохраняется с вновь добавленным полем формы.
---

## Создать форму с нуля

### Добавить поле формы в PDF‑документ

Класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) предоставляет коллекцию под названием [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/), которая помогает управлять полями формы в PDF‑документе.

Чтобы добавить поле формы:

1. Создайте поле формы, которое хотите добавить.
1. Вызовите метод [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) коллекции Form.

### Добавление TextBoxField

Ниже приведён пример, показывающий, как добавить [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Open document
    pdfDocument = ap.Document(path_infile)

    # Create a field
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Add field to the document
    pdfDocument.form.add(textBoxField, 1)

    # Save modified PDF
    pdfDocument.save(path_outfile)
```


