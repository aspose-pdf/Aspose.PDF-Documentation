---
title: Простая замена текста
type: docs
weight: 40
url: /python-net/replace-text-simple/
description: В этом примере все вхождения "33" заменяются на "XXXIII " во всём документе. Это демонстрирует простую замену строк без пользовательского форматирования или регулярных выражений.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Замена текста в PDF с использованием PdfContentEditor в Python
Abstract: В этом примере демонстрируется, как заменить текст по всему PDF‑документу, используя Aspose.PDF for Python через Facades API. Он заменяет все вхождения указанной строки новым текстом.
---

Простая замена текста полезна при обновлении повторяющихся значений в документе. С [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете определить область замены и заменить текст глобально на всех страницах.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Настройте область замены для всех вхождений.
1. Замените целевой текст.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```
