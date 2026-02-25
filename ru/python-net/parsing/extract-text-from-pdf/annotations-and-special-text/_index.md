---
title: Аннотации и специальный текст с использованием Python
linktitle: Аннотации и специальный текст
type: docs
weight: 40
url: /ru/python-net/annotation-and-special-text/
description: Этот раздел содержит статьи об аннотациях и извлечении специального текста из PDF-документов с помощью Aspose.PDF на Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста из штамповых аннотаций

Библиотека Aspose.PDF для Python позволяет извлекать текст из штамповой аннотации (конкретно StampAnnotation) на странице PDF.

1. Откройте документ.
1. Получите доступ к штамповой аннотации из коллекции аннотаций страницы.
1. Получите поток отображения штампа (XForm).
1. Используйте 'TextAbsorber' для извлечения встроенного текста из этого отображения.

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

Стандарт PDF предоставляет возможность выделять части текста в документе. Чтобы извлечь такой выделенный контент, выполните следующие действия:

1. Импортировать `aspose.pdf as ap` и любые вспомогательные функции, которые вы используете (`is_assignable`, `cast`).
2. Вызовите `ap.Document(infile)`, чтобы открыть PDF.
3. Выберите нужную страницу с помощью `document.pages` (коллекция страниц нумеруется с 1).
4. Пройдитесь по `page.annotations`, чтобы просмотреть каждую аннотацию на странице.
5. Отфильтруйте аннотации, чтобы обрабатывались только выделения.
6. Приведите аннотацию к типу `HighlightAnnotation` и вызовите `get_marked_text()`, чтобы прочитать выделенный текст.
7. Выведите или иначе обработайте полученный текст.

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

## Извлечение текста надстрочных и подстрочных

**Подстрочные и надстрочные** обычно используются в формулах, математических выражениях и обозначениях химических соединений. Трудно их редактировать, когда их много в одном отрывке текста.
В одном из последних релизов библиотека Aspose.PDF for Python via .NET добавила поддержку извлечения текста надстрочных и подстрочных знаков из PDF. Извлеките весь текст (включая надстрочные и подстрочные) с конкретной страницы PDF-документа с помощью 'TextFragmentAbsorber'.

1. Загрузите PDF-документ.
1. Создайте экземпляр 'TextFragmentAbsorber()', который поддерживает обнаружение надстрочного/подстрочного текста в соответствии с возможностями версии.
1. Вызовите 'document.pages[page_number].accept(absorber)', чтобы просканировать только указанную страницу.
1. Получите извлеченный текст через 'absorber.text'.
1. Запишите текст в выходной файл, используя стандартный ввод-вывод файлов.
1. Закройте документ, чтобы освободить ресурсы.

```python

import os
import aspose.pdf as ap

def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Итерация по TextFragments для обнаружения надстрочных/подстрочных

Пройдитесь по каждому фрагменту текста на странице, проверьте, является ли он надстрочным или подстрочным, и обработайте соответственно.

1. Загрузите PDF-документ.
1. Создайте 'TextFragmentAbsorber()' и примите его на выбранной странице.
1. Получите доступ к 'absorber.text_fragments', который возвращает коллекцию фрагментов, найденных на этой странице.
1. Для каждого фрагмента:
- Получите 'fragment.text'.
- Проверьте 'fragment.text_state.superscript' и 'fragment.text_state.subscript'.
- Запишите строку в выходной файл с текстом фрагмента и флагами.
1. Закройте файл и документ.

```python

import os
import aspose.pdf as ap

def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```
