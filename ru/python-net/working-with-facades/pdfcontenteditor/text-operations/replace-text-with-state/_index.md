---
title: Заменить текст с использованием state
linktitle: Заменить текст с использованием state
type: docs
weight: 50
url: /ru/python-net/replace-text-with-state/
description: В этом примере все вхождения "software" заменяются на "SOFTWARE" и форматируются синим цветом размером шрифта 14.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Заменить текст с пользовательским форматированием в PDF с помощью PdfContentEditor на Python
Abstract: Этот пример демонстрирует, как заменить текст в PDF‑документе, применяя пользовательское форматирование с помощью Aspose.PDF for Python через Facades API. Показано, как управлять цветом текста и размером шрифта при замене.
---

При обновлении текста в PDF вы можете захотеть, чтобы заменяемый контент выделялся. Используя объект TextState, можно задать стиль, например цвет и размер шрифта, а затем применить его ко всему замененному тексту.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  экземпляр.
1. Привяжите входной PDF‑документ.
1. Определите TextState с пользовательским форматированием.
1. Настройте область замены.
1. Замените текст по всему документу.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```

