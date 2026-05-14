---
title: Заменить текст на странице с помощью state
type: docs
weight: 20
url: /python-net/replace-text-on-page-with-state/
description: В этом примере все "software" на странице 1 заменяются на "SOFTWARE PAGE 1", используя красный текст с размером шрифта 12.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Заменить текст с пользовательским форматированием на конкретной странице с помощью PdfContentEditor в Python
Abstract: Этот пример демонстрирует, как заменить текст на определённой странице PDF, применяя пользовательское форматирование с использованием Aspose.PDF for Python через Facades API. Он показывает, как контролировать размер шрифта и цвет при замене текста.
---

Иногда замена текста в PDF также требует изменения форматирования, например цвета или размера шрифта. С помощью TextState вы можете определить свойства оформления и применить их во время замены. Это позволяет выделять изменённый текст или обеспечивать единообразное форматирование во всех документах.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Определите TextState с пользовательским форматированием.
1. Настройте стратегию замены.
1. Замените текст на конкретной странице.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```
