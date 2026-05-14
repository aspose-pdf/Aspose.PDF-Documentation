---
title: Удалить вложения
type: docs
weight: 50
url: /python-net/remove-attachments/
description: В этом примере происходит привязка входного PDF, удаляются все вложения и сохраняется изменённый PDF без встроенных файлов.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить все вложения из PDF с использованием Python
Abstract: В этом примере показано, как удалить все вложения файлов из PDF‑документа с использованием Aspose.PDF for Python via the Facades API. Он демонстрирует, как привязать PDF, удалить встроенные вложения и сохранить обновлённый документ.
---

PDF‑файлы могут содержать вложения, такие как документы, изображения или другие файлы. Существуют ситуации, когда необходимо очистить PDF от всех вложений в целях безопасности, конфиденциальности или распространения. Используя [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете программно удалить все встроенные вложения в документе.

1. Создайте объект PdfContentEditor. 
1. Привяжите входной PDF.
1. Удалите все вложения.
1. Сохраните обновлённый Document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```
