---
title: Добавить действие закладки
type: docs
weight: 10
url: /python-net/add-bookmark-action/
description: В этом примере привязывается входной PDF, создаётся закладка с меткой "PdfContentEditor Bookmark", которая переходит к странице 1, и сохраняется обновлённый документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать закладку с действием навигации в PDF с помощью Python
Abstract: В этом примере демонстрируется, как добавить закладку с действием навигации в PDF‑документ с использованием Aspose.PDF for Python via the Facades API. Показано, как настроить текст закладки, её внешний вид и действие, которое перенаправляет пользователей на определённую страницу.
---

Закладки обеспечивают быстрый переход внутри PDF‑документов. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете программно создавать закладки и назначать действия, такие как переход к странице. Вы также можете настраивать внешний вид закладки, включая цвет и варианты стиля, такие как полужирный или курсив.

1. Создайте объект PdfContentEditor.
1. Привяжите входной PDF.
1. Определите свойства закладки.
1. Назначьте действие закладки.
1. Сохраните обновлённый Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```