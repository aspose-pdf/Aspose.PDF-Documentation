---
title: Удалить штамп по индексу
type: docs
weight: 50
url: /ru/python-net/delete-stamp-by-index/
description: В этом примере создаются две резиновые печати на странице 2. Затем печать можно удалить, указав её индекс.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить резиновую печать по индексу в PDF с использованием PdfContentEditor в Python
Abstract: В этом примере показано, как удалить аннотацию резиновой печати в PDF, используя её индекс с помощью Aspose.PDF for Python через Facades API. Он демонстрирует, как добавить несколько печатей, а затем удалить одну из них, исходя из их порядка на странице.
---

Когда на странице присутствует несколько резиновых печатей, вы можете удалить конкретную, используя её индекс. Метод delete_stamp() позволяет удалять аннотации в соответствии с их последовательностью, что полезно, если вы не отслеживаете идентификаторы печатей, а знаете их порядок.

1. Создайте [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) экземпляр.
1. Привяжите входной PDF‑файл к экземпляру PdfContentEditor, используя bind_pdf(infile).
1. Вызовите 'delete_stamp(1, [2, 3])', чтобы удалить штамп с индексом 1 со страниц 2 и 3.
1. Сохраните изменённый PDF‑документ в выходной файл, используя save(outfile).

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
