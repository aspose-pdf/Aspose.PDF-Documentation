---
title: Замена текста с использованием RegEx
linktitle: Замена текста с использованием RegEx
type: docs
weight: 30
url: /python-net/replace-text-regex/
description: В этом примере все четырёхзначные числа в документе заменяются плейсхолдером "[NUMBER]". Это полезно для маскирования конфиденциальных данных, нормализации содержимого или анонимизации документов.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Замена текста с помощью регулярных выражений с PdfContentEditor в Python
Abstract: Этот пример демонстрирует, как заменить текст в PDF с помощью регулярных выражений, используя Aspose.PDF for Python через Facades API. Он показывает, как искать шаблоны и заменять все совпадения по всему документу.
---

Регулярные выражения позволяют гибко заменять текст на основе шаблонов, а не фиксированных строк. Включив поддержку regex в 'replace_text_strategy', вы можете сопоставлять динамичное содержимое, такое как числа, даты или отформатированные строки.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑документ.
1. Настройте стратегию замены для использования regex.
1. Заменить совпадающие шаблоны во всем документе.
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```
