---
title: Извлечение векторных данных из PDF-файла с помощью Python
linktitle: Извлечение векторных данных из PDF
type: docs
weight: 80
url: /ru/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF упрощает извлечение векторных данных из PDF-файла. Вы можете получать векторные данные (path, polygon, polyline), такие как позиция, цвет, толщина линии и другие параметры.
lastmod: "2026-04-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение доступа к векторным данным PDF-документа

Используйте [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/), чтобы анализировать элементы векторной графики на странице [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). После обработки целевой страницы переберите извлечённые элементы, чтобы изучить такие свойства, как границы прямоугольника, позиции и операторы рисования.

1. Откройте исходный PDF как `Document`.
1. Создайте экземпляр `GraphicsAbsorber`.
1. Вызовите `gr_absorber.visit(page)` для целевой страницы.
1. Получите извлечённые элементы из `gr_absorber.elements`.
1. Переберите элементы и запишите их свойства в выходной файл.

```python
import aspose.pdf as ap


def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])

        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(
                    f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
                )
    finally:
        document.close()
```

## Сохранение векторной графики со страницы в SVG-файл

Экспортируйте векторную графику со страницы PDF в SVG, чтобы сохранить масштабируемые контуры и фигуры вне исходного PDF. Этот метод полезен для повторного использования векторных иллюстраций в веб-, дизайнерских или издательских процессах.

1. Загрузите PDF-документ.
1. Получите доступ к целевой странице.
1. Вызовите `page.try_save_vector_graphics()`, чтобы экспортировать векторные контуры страницы в SVG.
1. Закройте документ.

```python
import aspose.pdf as ap


def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### Извлечение каждого подпути в отдельный SVG

Когда страница содержит несколько независимых векторных путей, используйте [SvgExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) вместе с [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/), чтобы записать каждый подпуть в отдельный SVG-файл.

1. Загрузите PDF.
1. Создайте `SvgExtractionOptions` и настройте `extract_every_subpath_to_svg`.
1. Получите доступ к первой странице документа.
1. Создайте экземпляр `SvgExtractor`, передав параметры.
1. Вызовите `extractor.extract()`, чтобы записать отдельные SVG-файлы для каждого векторного подпути.
1. Закройте документ.

```python
import aspose.pdf as ap


def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True

        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### Извлечение списка элементов в одно изображение

Извлеките несколько векторных элементов со страницы PDF и сохраните их как одно объединённое SVG-изображение. Это полезно, когда нужно сохранить визуальную связь между сгруппированными фигурами, диаграммами или фрагментами рисунка.

1. Откройте PDF с помощью [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Выберите страницу и подготовьте список векторных элементов.
1. Используйте [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/), чтобы объединить эти элементы в один SVG.
1. Сохраните выходной файл.

```python
import aspose.pdf as ap


def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### Извлечение одного элемента

Извлеките один конкретный векторный элемент из PDF и сохраните его как отдельный SVG-файл. Это полезно для изоляции логотипов, значков или отдельных фигур из более сложных векторных страниц.

1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/), чтобы захватить векторные данные.
1. Обработайте выбранную страницу, чтобы собрать её векторные элементы.
1. Выберите целевой элемент, например [XFormPlacement](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. Сохраните этот отдельный элемент в SVG-файл.

```python
import aspose.pdf as ap


def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```
