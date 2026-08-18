---
title: Извлечение текста в заданной области с помощью Python
linktitle: Извлечение текста по области
type: docs
weight: 20
url: /ru/python-net/region-based-extraction/
description: Узнайте, как извлекать текст из определённой области страницы или из структуры абзацев в PDF-документах с помощью Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение текста из определённой области страницы

Используйте [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) вместе с [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/), чтобы ограничить извлечение конкретной областью страницы. Такой подход полезен для зонального извлечения из верхних и нижних колонтитулов, ячеек таблиц, полей форм, счетов и других участков фиксированного макета, где положение текста заранее известно.

1. Откройте исходный PDF как [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте экземпляр `TextAbsorber`.
1. Настройте `text_search_options`, чтобы ограничить извлечение прямоугольной областью.
1. Примените поглотитель к целевой странице.
1. Запишите извлечённый текст в выходной файл.

```python
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

## Извлечение абзацев с визуализацией ограничивающего многоугольника

Вы также можете использовать [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/), чтобы анализировать геометрию абзацев. Помимо извлечения текста, этот подход фиксирует прямоугольник каждого раздела и многоугольник каждого абзаца, что полезно для картирования макета, анализа документов, средств доступности и постобработки с учётом области.

1. Откройте исходный PDF как [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте экземпляр `ParagraphAbsorber`.
1. Обработайте целевую страницу.
1. Прочитайте разметку страницы из `absorber.page_markups`.
1. Переберите разделы и абзацы, чтобы получить геометрию и текст.
1. Запишите данные о прямоугольнике, многоугольнике и тексте в выходной файл.

```python
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
        with open(outfile, "w", encoding="utf-8") as tw:
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
