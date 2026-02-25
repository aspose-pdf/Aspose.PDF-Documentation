---
title: Извлечение векторных данных из PDF-файла с помощью Python
linktitle: Извлечение векторных данных из PDF
type: docs
weight: 80
url: /ru/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF упрощает извлечение векторных данных из PDF‑файла. Вы можете получить векторные данные (контур, полигон, полилинию), такие как положение, цвет, толщина линии и т.д.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Доступ к векторным данным из PDF‑документа

В следующем фрагменте кода используется класс GraphicsAbsorber, показывающий, как извлекать векторные графические элементы из конкретной страницы PDF‑документа и исследовать такие свойства, как границы прямоугольника, операторы и позиции.

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Инициализируйте экземпляр 'GraphicsAbsorber'.
1. Вызовите 'gr_absorber.visit()', чтобы просмотреть вторую страницу.
1. Получите извлечённые элементы через 'gr_absorber.elements'.
1. Пройдитесь по каждому элементу и запишите свойства — прямоугольник, позицию и количество операторов.
1. Запишите информацию в текстовый файл вывода.
1. Закройте документ, чтобы освободить ресурсы.

```python

import os
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
                f.write(f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n")
    finally:
        document.close()
```

## Сохранение векторной графики со страницы в SVG‑файл

Экспортируйте векторную графику со страницы PDF в SVG‑файл, сохраняя векторные формы и контуры:

1. Загрузите PDF‑документ.
1. Получите доступ к целевой странице().
1. Вызовите 'page.try_save_vector_graphics()', который экспортирует векторные пути страницы в SVG‑файл.
1. Закройте документ.

```python

import os
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

Извлеките каждый подпуть (компонент) векторной графики в отдельные SVG‑файлы, используя объект параметров извлечения.

1. Загрузите PDF.
1. Создайте 'SvgExtractionOptions' и установите 'extract_every_subpath_to_svg'.
1. Получите доступ к первой странице документа.
1. Создайте экземпляр 'SvgExtractor' с этими параметрами.
1. Вызовите 'extractor.extract()', чтобы вывести отдельные SVG‑файлы для каждого векторного подпути.
1. Закройте документ.

```python

import os
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

### Извлечение списка элементов в единое изображение

Извлеките несколько векторных элементов со страницы PDF и сохраните их как единое комбинированное SVG‑изображение с помощью Aspose.PDF для Python.
Это полезно, когда необходимо сохранить визуальную структуру сгруппированных фигур или чертежей, например диаграмм или экспортов CAD.

1. Откройте PDF, используя 'Document'.
1. Выберите страницу и подготовьте список векторных элементов.
1. Используйте 'SvgExtractor' для объединения этих элементов в один SVG.
1. Сохраните файл вывода.

```python

import os
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

### Извлечение отдельного элемента

Извлеките один конкретный векторный элемент из PDF и сохраните его в отдельный SVG‑файл.
Это полезно для изоляции и экспорта логотипов, значков или отдельных форм из сложных векторных PDF.

1. Создайте 'GraphicsAbsorber' для захвата векторных данных.
1. Посетите конкретную страницу, чтобы собрать её векторные элементы.
1. Выберите целевой элемент (например, 'XFormPlacement').
1. Сохраните этот отдельный элемент в SVG‑файл.

```python

import os
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
