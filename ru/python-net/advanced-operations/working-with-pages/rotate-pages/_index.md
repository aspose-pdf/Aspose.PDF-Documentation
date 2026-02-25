---
title: Поворот страниц PDF с помощью Python
linktitle: Поворот страниц PDF
type: docs
weight: 110
url: /ru/python-net/rotate-pages/
description: В этой теме описывается, как программно повернуть ориентацию страниц в существующем PDF‑файле с помощью Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как повернуть страницы в PDF с помощью Python
Abstract: В этой статье представлено руководство о том, как программно обновлять или менять ориентацию страниц в существующем PDF‑файле с помощью Python. Используя Aspose.PDF для Python через .NET, пользователи могут легко переключаться между альбомной и книжной ориентациями, изменяя свойства MediaBox страницы. Статья содержит фрагмент кода на Python, демонстрирующий, как перебрать страницы PDF‑документа, изменить их размеры и положения MediaBox и при необходимости скорректировать CropBox. Кроме того, объясняется, как установить угол поворота страниц с помощью метода 'rotate' для достижения нужной ориентации. Процесс завершается сохранением обновлённого PDF‑файла.
---

В этой теме описывается, как программно обновлять или менять ориентацию страниц в существующем PDF‑файле с помощью Python.

## Смена ориентации страницы

Эта функция поворачивает каждую страницу PDF [`Документ`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) на 90 градусов по часовой стрелке с использованием Aspose.PDF для Python.
Это полезно для исправления проблем с ориентацией страниц, например сканированных документов, лежащих боком. Исходный PDF остаётся неизменным, а повернутая версия сохраняется как новый файл.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```


