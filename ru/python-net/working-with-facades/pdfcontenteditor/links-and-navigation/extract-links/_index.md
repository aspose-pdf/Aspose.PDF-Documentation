---
title: Извлечение ссылок
type: docs
weight: 70
url: /python-net/extract-links/
description: В этом примере привязывается входной PDF, извлекаются все ссылки и выводятся их координаты и URI (если доступны).
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение ссылок из PDF с помощью PdfContentEditor в Python
Abstract: Этот пример демонстрирует, как извлечь все ссылки из PDF‑документа с использованием Aspose.PDF for Python via the Facades API. Он показывает, как идентифицировать и получить веб‑ссылки или другие интерактивные ссылки, встроенные в PDF.
---

PDF часто содержат интерактивные элементы, такие как веб‑ссылки, ссылки на документы и пользовательские действия. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), вы можете программно извлекать все аннотации ссылок из PDF. Это позволяет проверять или обрабатывать ссылки, например, для валидации URL‑адресов или анализа схем навигации в документе.

1. Создайте экземпляр PdfContentEditor.
1. Привяжите входной PDF‑документ.
1. Извлеките все ссылки, используя 'extract_link()'.
1. Перебирайте извлечённые ссылки.
1. Проверьте, является ли ссылка LinkAnnotation и является ли её действие GoToURIAction.
1. Выведите координаты прямоугольника и URI.
1. Отобразите сообщение, если ссылки не найдены.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```
