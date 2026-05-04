---
title: Поиск и извлечение текста PDF в Python
linktitle: Поиск и получение текста
type: docs
weight: 60
url: /python-net/search-and-get-text-from-pdf/
description: Узнайте, как выполнять поиск, проверку и извлечение текста из PDF‑документов на Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как выполнять поиск и получать текст со страниц в PDF
Abstract: Статья предоставляет подробное исследование возможностей извлечения и манипуляции текстом в PDF‑документах с использованием библиотеки Aspose.PDF for Python via .NET. В ней представляется класс TextFragmentAbsorber, который позволяет разработчикам выполнять поиск по всему документу или по конкретным страницам для заданных фраз или шаблонов регулярных выражений. Страница описывает различные практические сценарии — такие как получение текстового содержимого, определение его позиции (включая координаты и значения отступов) и извлечение свойств шрифта, например имени, размера, статуса встраивания и цвета, — из найденных текстовых фрагментов. Подробные примеры кода демонстрируют процесс пошагово, упрощая разработчикам интеграцию возможностей поиска текста в их приложения.
---

## Поиск текста в PDF

Ищите и извлекайте текст из заданной прямоугольной области в PDF‑документе с помощью класса TextAbsorber. Он использует режим чистого текстового форматирования для получения чистого, неформатированного вывода текста, что делает его идеальным для извлечения содержимого из структурированных областей, таких как заголовки, колонтитулы или области таблиц. Комбинируя TextExtractionOptions и TextSearchOptions с прямоугольными ограничениями, этот пример предоставляет точный контроль над тем, где и как извлекается текст из документа.

Используйте эту страницу, когда вам нужно провести аудит текста PDF, извлечь текст для анализа или проверить позиции и форматирование найденных текстовых фрагментов.

1. Загрузите PDF‑файл, используя 'ap.Document'.
1. Настройте параметры извлечения текста.
1. Определить область поиска с ограничениями прямоугольника.
1. Создайте и настройте TextAbsorber.
1. Обработать все страницы в документе.
1. Получить и отобразить извлечённый текст.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Поиск текста на определённой странице PDF

Поиск и извлечение текста с конкретной страницы и области в PDF с использованием TextAbsorber из Aspose.PDF. Он ориентируется на страницу 2 документа и извлекает только текст, найденный в заданной прямоугольной области.
Комбинируя TextExtractionOptions (для контроля форматирования) и TextSearchOptions (для ограничения области), вы можете эффективно выполнять точное извлечение текста, специфичное для страницы.

1. Загрузите PDF Document.
1. Настройте параметры извлечения текста.
1. Ограничить извлечение текста конкретной прямоугольной областью на странице.
1. Создайте и настройте TextAbsorber.
1. Обработать конкретную страницу.
1. Получить и отобразить извлечённый текст.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Анализировать и извлекать подробные свойства фрагмента текста из PDF

В отличие от TextAbsorber, который извлекает необработанный текст, TextFragmentAbsorber предоставляет детальную, низкоуровневую информацию о каждом фрагменте текста — такую как его позиция, атрибуты шрифта, цвет и детали встраивания.

1. Загрузите PDF Document.
1. Инициализировать TextFragmentAbsorber.
1. Обработать все страницы в документе.
1. Итерировать извлечённые фрагменты текста.
1. Печать базовой текстовой информации.
1. Печать шрифта и деталей форматирования.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Поиск конкретной текстовой фразы на отдельной странице PDF

Ищите определённую текстовую фразу на странице PDF‑документа с помощью TextFragmentAbsorber. В отличие от поиска по всему документу, этот метод ограничивает поиск одной страницей, делая его более эффективным для подтверждения наличия и местоположения текста в целевых областях, таких как колонтитулы, нижние колонтитулы или конкретные разделы содержимого.

1. Загрузите PDF Document.
1. Инициализировать TextFragmentAbsorber с поисковой фразой.
1. Применить поглотитель к конкретной странице.
1. Итерировать найденные фрагменты.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Последовательный поиск текста постранично с кумулятивными результатами

Ищите текст постепенно на нескольких страницах PDF‑документа, используя TextFragmentAbsorber из Aspose.PDF.
В отличие от поиска на одной странице или по всему документу, такой подход позволяет последовательно обрабатывать страницы, постепенно собирать результаты и анализировать фрагменты текста с учётом контекста конкретной страницы. Этот метод идеален для больших документов или рабочих процессов с прогрессивной обработкой.

1. Загрузите PDF Document.
1. Инициализировать TextFragmentAbsorber и установить поисковую фразу.
1. Обработайте первую страницу. Ищите только страницу 1. Выводит текст, номер страницы и позицию. Предоставьте изолированные результаты, специфичные для страницы, для ясности.
1. Обработать следующую страницу последовательно. Перейти к странице 2 и при желании продолжить через остальной документ. Метод 'absorber.visit()' обеспечивает накопление результатов со всех посещённых страниц. Выводит совокупные результаты поиска, показывая как текст, так и расположение.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Поиск целевой фразы в прямоугольной области

Поиск конкретной фразы в PDF с ограничением поиска конкретной прямоугольной областью на одной странице.
Комбинируя поиск фраз с пространственными ограничениями, вы можете точно определять контент в заданных областях без сканирования всей страницы или документа. Это особенно полезно для форм, заголовков, нижних колонтитулов или структурированных отчётов, где контент располагается в предсказуемых местах.

1. Загрузите PDF Document.
1. Инициализировать TextFragmentAbsorber с Phrase и прямоугольными ограничениями
1. Применить Absorber к странице 2. Ограничивает обработку только страницей 2, снижая ненужные вычисления. Обеспечивает поиск, специфичный для страницы.
1. Итерировать найденные фрагменты и печатать

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Поиск шаблонов текста в PDF с использованием регулярных выражений

Ищите текстовые шаблоны в PDF с помощью регулярных выражений. Включив режим regex в TextFragmentAbsorber, вы можете находить сложные шаблоны, такие как числа, даты, цены, координаты или пользовательские текстовые форматы. Функция ограничивает поиск конкретной страницей, делая его эффективным для целевого извлечения структурированных данных.

1. Загрузите PDF Document.
1. Инициализировать TextFragmentAbsorber с шаблоном регулярного выражения.
1. Применить Absorber к странице 2. Ограничивает поиск страницей 2 для эффективности и точности. Анализируется только текст на этой странице.
1. Итерировать найденные фрагменты. Печатает соответствующие текстовые фрагменты и их координаты. Предоставляет точную информацию о местоположении извлечённых шаблонов.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Преобразование совпадающих текстов в гиперссылки в PDF с помощью TextFragmentAbsorber

Ищите определённые текстовые фразы в PDF и преобразуйте их в кликабельные гиперссылки. С помощью TextFragmentAbsorber и шаблонов регулярных выражений находятся целевые слова и применяется визуальное оформление (цвет и подчёркивание) вместе с интерактивными ссылками.

1. Загрузите PDF Document.
1. Инициализировать TextFragmentAbsorber с шаблоном регулярного выражения.
1. Применить Absorber к странице 1.
1. Оформить и добавить гиперссылки к совпадениям.
1. Сохранить изменённый PDF.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Поиск и определение стилизованного текста в PDF с помощью TextFragmentAbsorber

Ищите фрагменты текста в PDF на основе их форматирующих свойств, а не содержимого. С помощью TextFragmentAbsorber он определяет текст с определёнными стилями, например жирный текст.

1. Загрузите PDF Document.
1. Инициализировать TextFragmentAbsorber.
1. Применить Absorber к странице 1.
1. Проверка текстовых фрагментов на основе форматирования. Проверяется стиль шрифта на полужирное форматирование.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Визуальное выделение текста на страницах PDF

Эта функция объединяет распознавание текста и визуализацию в один рабочий процесс. Она не только извлекает текст, но и визуализирует его, выделяя фрагменты, сегменты и символы в прямоугольниках с цветовой кодировкой на PNG‑изображениях каждой страницы.

Наш пример выполняет продвинутую визуализацию текста в PDF с помощью:

- поиск всех видимых фрагментов текста с использованием регулярных выражений
- отображение каждой страницы PDF в изображение PNG высокого разрешения
- рисование цветных прямоугольников вокруг фрагментов текста, сегментов текста и отдельных символов

1. Установите разрешение выходного изображения. Каждая страница PDF преобразуется в PNG‑изображение с разрешением 150 DPI.
1. Откройте PDF и инициализируйте Text Absorber.
1. Обработать каждую страницу. Применить абсорбер к каждой странице. Собрать все обнаруженные фрагменты текста и их геометрические позиции.
1. Преобразовать Page в поток PNG.
1. Подготовьте графический объект для рисования.
1. Применить преобразование координат. Преобразовать координаты PDF в пиксели изображения.
1. Нарисовать прямоугольники для текстовых элементов.
1. Сохраните результат.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```

## Связанные темы текста

- [Работа с текстом в PDF с помощью Python](/pdf/ru/python-net/working-with-text/)
- [Заменить текст в PDF с помощью Python](/pdf/ru/python-net/replace-text-in-pdf/)
- [Добавить всплывающие подсказки к тексту PDF в Python](/pdf/ru/python-net/pdf-tooltip/)
- [Добавление текста в PDF](/pdf/ru/python-net/add-text-to-pdf-file/)