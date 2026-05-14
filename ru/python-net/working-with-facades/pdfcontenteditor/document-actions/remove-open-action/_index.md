---
title: Удалить действие при открытии
linktitle: Удалить действие при открытии
type: docs
weight: 30
url: /ru/python-net/remove-open-action/
description: В этом примере загружается существующий PDF, удаляется действие при открытии и сохраняется очищенный документ.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить действие открытия документа из PDF с использованием Python
Abstract: В этом примере демонстрируется, как удалить действие открытия документа из PDF с использованием Aspose.PDF for Python via the Facades API. Показано, как привязать PDF, очистить действие при открытии и сохранить обновлённый документ.
---

PDF‑документы могут содержать действия, которые автоматически выполняются при открытии файла, такие как JavaScript‑оповещения, команды навигации или другие поведения. В некоторых сценариях может потребоваться удалить эти действия по соображениям безопасности, соответствия требованиям или удобства пользователя.

С помощью PdfContentEditor вы можете легко удалить действие открытия документа и обеспечить, чтобы PDF открывался без выполнения какого-либо автоматического поведения.

1. Создайте объект PdfContentEditor.
1. Привяжите входной PDF.
1. Удалите действие открытия документа.
1. Сохраните обновлённый Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```

