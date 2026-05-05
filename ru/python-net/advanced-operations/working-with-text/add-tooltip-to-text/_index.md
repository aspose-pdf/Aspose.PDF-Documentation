---
title: Добавить подсказки к тексту PDF в Python
linktitle: Подсказка PDF
type: docs
weight: 20
url: /ru/python-net/pdf-tooltip/
description: Узнайте, как добавить подсказки к фрагментам текста в PDF‑документах с помощью Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте подсказку к фрагменту текста в PDF, используя Python
Abstract: В этой статье представлены два примера кода на Python для улучшения интерактивности PDF‑документов с использованием библиотеки Aspose.PDF. Первый пример демонстрирует, как добавить всплывающие подсказки к отдельным фрагментам текста в PDF, создавая невидимые элементы ButtonField над текстом и устанавливая свойство `alternate_name` в качестве подсказки. Второй пример показывает, как создать плавающие текстовые блоки, которые становятся видимыми при наведении: когда находится `TextFragment`, в его позиции создаётся скрытый `TextBoxField`, а к невидимому `ButtonField` привязываются события `HideAction` для отображения или скрытия плавающего блока.
---

## Добавить всплывающую подсказку к найденному тексту в PDF

Этот фрагмент кода показывает, как наложить невидимый [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) элементы на конкретных [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) объекты в PDF для отображения всплывающих подсказок, когда пользователь наводит курсор на них. Он поддерживает как короткие, так и длинные сообщения всплывающих подсказок, используя `alternate_name` свойство `ButtonField`.

Используйте эту страницу, когда вам нужно сделать текст PDF более интерактивным, добавив подсказки при наведении, встроенные пояснения или контекстные заметки.

1. Создать новый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Сохраните первоначальный документ.
1. Повторно откройте PDF документ.
1. Поиск целевого текста с помощью [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Добавить невидимый [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) с короткой подсказкой.
1. Поиск второго целевого текста.
1. Добавить невидимый [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) с длинной всплывающей подсказкой над совпадающим фрагментом.
1. Сохраните окончательный Document.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

# region PDF Tooltip
def add_tool_tip_to_searched_text(outfile):
    # Create PDF document
    with ap.Document() as document:
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display a tooltip")
        )
        document.pages[1].paragraphs.add(
            ap.text.TextFragment(
                "Move the mouse cursor here to display a very long tooltip"
            )
        )
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a tooltip"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the extracted text fragments
        text_fragments = absorber.text_fragments

        # Loop through the fragments
        for fragment in text_fragments:
            # Create invisible button on text fragment position
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # alternate_name value will be displayed as tooltip by a viewer application
            field.alternate_name = "Tooltip for text."
            # Add button field to the document
            document.form.add(field)

        # Next will be sample of very long tooltip
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a very long tooltip"
        )
        document.pages.accept(absorber)
        text_fragments = absorber.text_fragments

        for fragment in text_fragments:
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # Set very long text
            field.alternate_name = (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                " sed do eiusmod tempor incididunt ut labore et dolore magna"
                " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                " Duis aute irure dolor in reprehenderit in voluptate velit"
                " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                " occaecat cupidatat non proident, sunt in culpa qui officia"
                " deserunt mollit anim id est laborum."
            )
            document.form.add(field)

        # Save document
        document.save(outfile)
```

## Создать скрытый текстовый блок, который появляется при наведении в PDF

Добавить интерактивный плавающий текст в документ PDF. Он накладывается как невидимый [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) на целевой фразе и раскрывает скрытый [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) когда пользователь наводит на него курсор. Эта техника идеальна для контекстной помощи, аннотаций или динамического представления контента.

1. Создайте новый PDF-документ.
1. Сохраните PDF, чтобы его можно было открыть заново для настройки интерактивности.
1. Повторно откройте PDF Document.
1. Найдите целевой текст, используя [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Создайте скрытый [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. Добавьте скрытое поле в документ [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) коллекция.
1. Создать невидимый [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. Назначить действия мыши (`on_enter`, `on_exit`) используя [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) показать/скрыть скрытое поле.
1. Сохранить окончательный документ.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

def create_hidden_text_block(outfile):
    # Create PDF document
    with ap.Document() as document:
        #  Add paragraph with text
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display floating text")
        )
        # Save PDF document
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the first extracted text fragment
        text_fragments = absorber.text_fragments
        fragment = text_fragments[1]

        # Create hidden text field for floating text in the specified rectangle of the page
        floating_field = ap.forms.TextBoxField(
            fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
        )
        # Set text to be displayed as field value
        floating_field.value = 'This is the "floating text field".'
        # We recommend to make field 'readonly' for this scenario
        floating_field.read_only = True
        # Set 'hidden' flag to make field invisible on document opening
        floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

        # Setting a unique field name isn't necessary but allowed
        floating_field.partial_name = "FloatingField_1"

        # Setting characteristics of field appearance isn't necessary but makes it better
        floating_field.default_appearance = ap.annotations.DefaultAppearance(
            "Helv", 10, drawing.Color.blue
        )
        floating_field.characteristics.background = drawing.Color.light_blue
        floating_field.characteristics.border = drawing.Color.dark_blue
        floating_field.border = ap.annotations.Border(floating_field)
        floating_field.border.width = 1
        floating_field.multiline = True

        # Add text field to the document
        document.form.add(floating_field)
        # Create invisible button on text fragment position
        button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Create new hide action for specified field (annotation) and invisibility flag.
        # (You also may refer floating field by the name if you specified it above.)
        # Add actions on mouse enter/exit at the invisible button field

        button_field.actions.on_enter = ap.annotations.HideAction(floating_field, False)
        button_field.actions.on_exit = ap.annotations.HideAction(floating_field)

        # Add button field to the document
        document.form.add(button_field)

        # Save document
        document.save(outfile)
```

## Связанные темы текста

- [Работа с текстом в PDF с помощью Python](/pdf/ru/python-net/working-with-text/)
- [Используйте FloatingBox для расположения текста PDF в Python](/pdf/ru/python-net/floating-box/)
- [Поиск и извлечение текста PDF в Python](/pdf/ru/python-net/search-and-get-text-from-pdf/)
- [Добавление текста в PDF](/pdf/ru/python-net/add-text-to-pdf-file/)