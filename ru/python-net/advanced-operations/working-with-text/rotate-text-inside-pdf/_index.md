---
title: Повернуть текст внутри PDF с использованием Python
linktitle: Повернуть текст внутри PDF
type: docs
weight: 50
url: /ru/python-net/rotate-text-inside-pdf/
description: Узнайте, как вращать фрагменты текста и абзацы внутри PDF‑документов на Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как повернуть текст в PDF с помощью Python
Abstract: Статья предоставляет подробное руководство о том, как вращать текст в PDF‑документе с использованием библиотеки Aspose.PDF для Python через .NET. В ней описывается использование свойства `Rotation` класса `TextFragment` для выполнения вращения текста под различными углами, что полезно в различных сценариях генерации документов. Демонстрируется создание фрагментов текста с указанными углами вращения и их добавление на страницу PDF с помощью `TextBuilder`. Показано, как добавлять повернутые фрагменты текста к `TextParagraph` и затем добавлять абзац на страницу PDF. Показано, как добавить повернутые фрагменты текста непосредственно в коллекцию абзацев страницы. Объясняется вращение целого абзаца с несколькими фрагментами текста.
---

Повернуть фрагменты текста в PDF‑документе с помощью Aspose.PDF for Python via .NET. Он показывает, как точно контролировать позицию и вращение отдельных текстовых элементов, комбинируя классы 'TextFragment', 'TextState' и 'TextBuilder'. Регулируя угол вращения для каждого фрагмента текста, вы можете создавать визуально динамичные макеты, такие как диагональные заголовки, вертикальные метки или повернутые аннотации.

## Поворот фрагментов текста с использованием TextBuilder в PDF

Создаёт PDF‑файл с именем rotated_fragments.pdf, содержащий три фрагмента текста, выровненные по горизонтали:

- первый текст не повернут
- второй повернут на 45°
- третий повернут на 90°

1. Создайте новый PDF-документ.
1. Вставьте новую страницу, чтобы разместить повернутый текст.
1. Создайте первый фрагмент текста - Без вращения.
1. Создать второй текстовый фрагмент - 45° вращение.
1. Создать третий текстовый фрагмент - 90° вращение.
1. Добавить текстовые фрагменты с помощью TextBuilder.
1. Сохранить Document.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Поворот отдельных текстовых фрагментов внутри абзаца в PDF

Поворачивайте отдельные фрагменты текста внутри абзаца. Показано, как построить многострочный абзац (TextParagraph), содержащий несколько фрагментов (TextFragment), каждый со своим углом поворота. Эта техника полезна для создания визуально насыщенных документов, сочетающих горизонтально и диагонально ориентированный текст — например, стилизованные заголовки, схемы или аннотированные подписи.

Создаёт PDF с именем rotated_paragraph_fragments.pdf, содержащий абзац с тремя строками текста, каждая из которых повернута по‑разному:

 - первая строка повернута на 45°
 - вторая строка остаётся горизонтальной (0°)
 - третья строка повернута на -45°

1. Создайте новый PDF-документ.
1. Добавьте пустую страницу там, где появится повернутый текст.
1. Создайте TextParagraph.
1. Создайте и настройте первый Text Fragment - вращение 45°.
1. Создать второй фрагмент текста - без вращения.
1. Создать третий фрагмент текста - вращение 45°.
1. Добавить фрагменты текста к абзацу.
1. Добавить абзац на страницу с помощью TextBuilder.
1. Сохранить Document.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_text_inside_pdf_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Поворот текста с использованием абзацев страницы в PDF

Упрощенный метод поворота текста внутри PDF с использованием Aspose.PDF for Python via .NET.
В отличие от более низкоуровневых подходов с TextBuilder или TextParagraph, этот метод добавляет вращаемые текстовые фрагменты непосредственно в коллекцию абзацев страницы (page.paragraphs). Он идеален для случаев, когда вам нужен базовый поворот текста, но не требуется точное позиционирование или структурирование абзацев. Этот подход упрощает создание макета, автоматически обрабатывая размещение текста на странице, при этом позволяя контролировать поворот отдельного текста.

Генерирует файл с именем 'simple_rotated_text.pdf', содержащий:

 - главный горизонтальный фрагмент текста с поворотом 0°
 - фрагмент, повернутый на 315°
 - фрагмент, повернутый на 270°

1. Инициализировать новый PDF-документ.
1. Создайте страницу, на которой будет размещён повернутый текст.
1. Создайте первый фрагмент текста - Без вращения.
1. Создать второй фрагмент текста - вращение на 315°.
1. Создать третий Text Fragment — 270° Rotation.
1. Добавьте фрагменты текста непосредственно в абзацы страницы.
1. Сохранить PDF‑документ.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Повернуть целые абзацы в PDF

Наша библиотека демонстрирует продвинутый поворот текста на уровне абзацев в PDF. В отличие от поворота на уровне фрагментов (когда каждый фрагмент текста вращается отдельно), этот метод поворачивает целые абзацы как единые блоки под разными углами.
Каждый абзац содержит несколько стилизованных текстовых фрагментов, а весь абзац вращается под определенными углами — позволяя выполнять сложные, согласованные преобразования макета.
Это идеально подходит для художественных макетов, водяных знаков или PDF‑файлов с обильным дизайном, где целые текстовые секции нужно ориентировать в разных направлениях.

Создает 'rotated_paragraphs.pdf', содержащий четыре полностью стилизованных и повернутых абзаца:

- каждый повернут на уникальный угол (45°, 135°, 225° и 315°)
- каждый абзац содержит три строки текста с цветными фонами, подчёркиванием и единообразным оформлением

1. Создайте новый PDF-документ.
1. Добавьте пустую страницу, чтобы разместить повернутые абзацы.
1. Итерация для создания нескольких абзацев.
1. Создайте и разместите абзац.
1. Создать текстовые фрагменты с форматированием.
1. Применить форматирование текста.
1. Добавьте фрагменты текста в абзац.
1. Добавить абзац на страницу с помощью TextBuilder.
1. Повторите для всех четырёх поворотов.
1. Сохранить PDF‑документ.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_text_inside_pdf_4(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Связанные темы текста

- [Работа с текстом в PDF с помощью Python](/pdf/ru/python-net/working-with-text/)
- [Добавление текста в PDF](/pdf/ru/python-net/add-text-to-pdf-file/)
- [Форматировать текст PDF с помощью Python](/pdf/ru/python-net/text-formatting-inside-pdf/)
- [Заменить текст в PDF с помощью Python](/pdf/ru/python-net/replace-text-in-pdf/)