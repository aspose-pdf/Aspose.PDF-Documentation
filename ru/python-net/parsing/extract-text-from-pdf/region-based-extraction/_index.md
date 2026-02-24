---
title: Извлечение по регионам с использованием Python
linktitle: Извлечение по регионам
type: docs
weight: 20
url: /ru/python-net/region-based-extraction/
description: Этот раздел содержит статьи об извлечении по регионам из PDF‑документов с использованием Aspose.PDF в Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста из конкретного региона страницы

Извлеките текст из заданного прямоугольного региона на определённой странице PDF с помощью Aspose.PDF для Python. Указывая координаты, можно сосредоточить извлечение на конкретной области — например, ячейке таблицы, блоке абзаца или области поля формы.

Идеально подходит для извлечения текста по зонам, например, получения данных из заголовков, нижних колонтитулов, счетов‑фактур или отчётов фиксированного макета, где текст находится в предсказуемых позициях.

1. Откройте PDF‑документ.
1. Создайте 'TextAbsorber'.
1. Настройте 'text_search_options' для ограничения прямоугольным регионом.
1. Примените поглотитель к конкретной странице.
1. Запишите извлечённый текст.

```python

import os
import aspose.pdf as ap

def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Извлечение абзацев путем их итерации

Мы можем получить текст из PDF‑документа, выполняя поиск определённого текста (используя \"обычный текст\" или \"регулярные выражения\") на отдельной странице или во всём документе, а также получить полный текст одной страницы, диапазона страниц или всего документа. Однако в некоторых случаях требуется извлекать абзацы из PDF‑документа или текст в виде абзацев. Мы реализовали функциональность поиска разделов и абзацев в тексте страниц PDF‑документа. Мы представили класс ParagraphAbsorber (как TextFragmentAbsorber и TextAbsorber), который можно использовать для извлечения абзацев из PDF‑документов.

Библиотека Aspose.PDF позволяет читать PDF‑файл и извлекать весь текст абзацев с каждой страницы с помощью 'ParagraphAbsorber'. Она организует вывод по страницам, разделам и абзацам и записывает извлечённое содержимое в обычный текстовый файл. Это полезно для анализа текста, архивирования или преобразования структурированного PDF‑содержимого в удобочитаемые форматы.

1. Откройте PDF‑документ.
1. Создайте экземпляр 'ParagraphAbsorber'.
1. Вызовите 'absorber.visit(document)' для сканирования всех страниц в поисках абзацев.
1. Пройдитесь по коллекции 'page_markups' поглотителя.
1. Для каждого page‑markup пройдитесь по его 'sections', затем по каждому 'paragraph' в разделе.
1. Внутри каждого абзаца проходите по 'lines', затем по каждому 'fragment' в строке, собирая 'fragment.text'.
1. Запишите каждый абзац (с индексами страницы/раздела/абзаца) в выходной файл.
1. Закройте документ после завершения.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf‑8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Извлечение абзацев с визуализацией ограничивающего полигона

Этот фрагмент кода извлекает текст уровней абзацев и информацию о макете с конкретной страницы PDF. Он захватывает ограничивающий прямоугольник и координаты полигона каждого абзаца, а также фактическое содержание текста, и записывает результаты в текстовый файл. Это полезно для анализа структуры документа, построения карты макета или подготовки данных для задач доступности и извлечения контента.

1. Откройте PDF и загрузите документ.
1. Создайте экземпляр 'ParagraphAbsorber'.
1. Вызовите 'absorber.visit(page)' для нужной вам конкретной страницы.
1. Получите первый 'page_markup' из 'absorber.page_markups'.
1. Для каждого раздела в этом markup:
- Получите его 'rectangle'.
1. Для каждого абзаца в разделе:
- Получите его 'points' (полигон).
- Извлеките текст, проходя по 'paragraph.lines' — 'fragment.text'.
1. Запишите информацию о геометрии и тексте в выходной файл.
1. Закройте документ.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf‑8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```

