---
title: Заменить текст на странице
type: docs
weight: 10
url: /python-net/replace-text-on-page/
description: В этом примере "PDF" заменяется на "Page 1 Replaced Text" с использованием указанного размера шрифта.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Заменить текст на конкретной странице с помощью PdfContentEditor в Python
Abstract: Этот пример демонстрирует, как заменить текст в PDF‑документе с использованием Aspose.PDF for Python через Facades API. Показано, как заменить первое вхождение текста на странице и сохранить обновлённый документ.
---

Замена текста является распространённым требованием при обновлении PDF‑документов. С помощью [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете искать определённый текст и заменять его новым содержимым. Свойство ‘replace_text_strategy’ позволяет контролировать, сколько вхождений будет заменено.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Настройте стратегию замены текста.
1. Замените целевой текст.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```
