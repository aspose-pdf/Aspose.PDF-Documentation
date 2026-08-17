---
title: Извлеките текст базовым способом с помощью Python
linktitle: Извлеките текст базовым способом
type: docs
weight: 10
url: /ru/python-net/basic-text-extraction/
description: Узнайте, как извлекать текст из PDF-документов с помощью Aspose.PDF for Python — сразу со всех страниц или с конкретной страницы.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлеките текст со всех страниц PDF-документа

Используйте [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber), чтобы собрать весь текст со всех страниц PDF-документа и записать его в текстовый файл. Этот подход хорошо подходит для преобразования PDF в пригодный для поиска текст, анализа содержимого или подготовки данных для индексирования и последующей обработки.

1. Откройте PDF-документ с помощью [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Создайте экземпляр `TextAbsorber`.
1. Вызовите `document.pages.accept(text_absorber)`, чтобы обработать все страницы.
1. Получите извлечённый текст из `text_absorber.text`.
1. Запишите результат в выходной текстовый файл.

```python
import os
import aspose.pdf as ap


def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Извлеките текст с определённой страницы

Примените [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) к одной странице, чтобы изолировать и сохранить текст из нужной части многостраничного документа. Это полезно, когда содержимое требуется только с одной страницы, например из счёта, раздела отчёта или сводки формы.

1. Откройте PDF-документ с помощью [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Создайте экземпляр `TextAbsorber`.
1. Вызовите `accept` для целевой страницы: `document.pages[page_number].accept(text_absorber)`.
1. Получите извлечённый текст и запишите его в файл.

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Извлеките абзацы с помощью их перебора

Используйте [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/), если вам нужно извлечение с учётом структуры абзацев, а не только плоский текст страницы. В отличие от [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) и [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), этот API организует результат по страницам, разделам и абзацам, что удобно для текстового анализа, структурированного экспорта и обработки с учётом макета.

1. Откройте исходный PDF как [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте экземпляр `ParagraphAbsorber`.
1. Вызовите `absorber.visit(document)`, чтобы проанализировать все страницы.
1. Переберите `page_markups`, затем каждый раздел и абзац.
1. Прочитайте текстовые фрагменты каждого абзаца и запишите результат в файл.

```python
import aspose.pdf as ap


def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraphвЂ™s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf-8") as tw:
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
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```
