---
title: Добавить пользовательскую ссылку действия
linktitle: Добавить пользовательскую ссылку действия
type: docs
weight: 20
url: /python-net/add-custom-action-link/
description: В этом примере привязывается входной PDF, добавляется пользовательская ссылка действия на первой странице и сохраняется изменённый документ. Для простоты используется пустой список действий, но в реальных реализациях могут быть включены фактические действия.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить пользовательскую ссылку действия в PDF с использованием PdfContentEditor на Python
Abstract: Этот пример демонстрирует, как добавить пользовательскую ссылку действия в документ PDF с использованием Aspose.PDF for Python via the Facades API. Показано, как создать область, по которой можно кликнуть, на странице, назначить пользовательское действие и сохранить обновлённый документ.
---

Пользовательские ссылки действия позволяют определять интерактивные области в PDF, которые могут запускать определённые действия при щелчке, такие как выполнение скриптов, навигация по страницам или выполнение команд, специфичных для приложения. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете создать пользовательскую ссылку действия, указав страницу, прямоугольник, цвет и действия.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Определите прямоугольник для кликабельной ссылки.
1. Укажите номер страницы и цвет ссылки.
1. Назначьте пользовательские действия (пусто в этом примере).
1. Сохраните обновлённый PDF‑документ.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```
