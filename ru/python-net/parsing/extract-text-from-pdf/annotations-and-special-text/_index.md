---
title: Извлечение аннотаций и специального текста с помощью Python
linktitle: Аннотации и специальный текст
type: docs
weight: 40
url: /ru/python-net/annotation-and-special-text/
description: Узнайте, как извлекать текст из штамп-аннотаций, выделенного текста и надстрочного или подстрочного содержимого в PDF-документах с помощью Aspose.PDF for Python.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение текста из stamp-аннотаций

Используйте [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber), чтобы извлекать текст, встроенный в поток внешнего вида [StampAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation). Это полезно, когда содержимое штампа визуализируется как form XObject, а не хранится как обычный текст.

1. Откройте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Получите доступ к целевой аннотации из `page.annotations`.
1. Убедитесь, что это `StampAnnotation`, затем получите её XForm нормального внешнего вида.
1. Передайте XForm в `TextAbsorber.visit()`, чтобы извлечь встроенный текст.

```python
import os
import aspose.pdf as ap


def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## Извлечение выделенного текста

Переберите аннотации страницы и используйте [HighlightAnnotation.get_marked_text()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation), чтобы читать текстовые фрагменты, покрытые каждым выделением. Коллекция аннотаций страницы индексируется с 1.

1. Откройте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) и выберите целевую страницу.
1. Переберите `page.annotations`.
1. Используйте `is_assignable`, чтобы отфильтровать экземпляры [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation).
1. Приведите аннотацию к нужному типу и вызовите `get_marked_text()`, чтобы получить выделенное содержимое.

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## Извлечение надстрочного и подстрочного текста

Надстрочные и подстрочные элементы часто встречаются в формулах, математических выражениях и названиях химических соединений. Aspose.PDF for Python via .NET поддерживает извлечение такого содержимого через [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), который определяет метаданные позиционирования на уровне символов.

1. Откройте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Создайте экземпляр `TextFragmentAbsorber`.
1. Вызовите `document.pages[page_number].accept(absorber)`, чтобы обработать целевую страницу.
1. Получите полный извлечённый текст из `absorber.text`.
1. Запишите результат в файл и закройте документ.

```python
import os
import aspose.pdf as ap


def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1вЂ‘based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Переберите текстовые фрагменты для определения надстрочного и подстрочного текста

Для анализа по отдельным фрагментам переберите `absorber.text_fragments` и прочитайте логические флаги `text_state.superscript` и `text_state.subscript` у каждого [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. Откройте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) и создайте [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Примените поглотитель к целевой странице, чтобы заполнить `absorber.text_fragments`.
1. Для каждого фрагмента прочитайте `fragment.text`, `fragment.text_state.superscript` и `fragment.text_state.subscript`.
1. Запишите результаты в выходной файл и закройте документ.

```python
import os
import aspose.pdf as ap


def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1вЂ‘based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```
