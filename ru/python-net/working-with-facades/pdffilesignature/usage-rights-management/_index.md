---
title: Управление правами использования
linktitle: Управление правами использования
type: docs
weight: 100
url: /ru/python-net/usage-rights-management/
description: Узнайте, как обнаруживать и удалять права использования из PDF‑документов с помощью PdfFileSignature в Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление прав использования PDF в Python
Abstract: В этой статье объясняется, как проверять и удалять права использования из PDF‑документов с помощью Aspose.PDF for Python via .NET. Показано, как проверить, содержит ли PDF права использования, и как сохранить новую версию документа после их удаления.
---

Aspose.PDF for Python via .NET предоставляет [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) фасад для работы с подписанными PDF и связанными настройками прав использования. В некоторых рабочих процессах вам может потребоваться проверить, содержит ли документ права использования, и удалить их перед сохранением обновлённой версии файла.

Этот пример демонстрирует одну распространённую задачу управления правами использования:

1. Проверьте, содержит ли PDF права использования.
1. Удалите права использования из документа.
1. Сохраните обновлённый PDF‑файл.

## Проверьте, содержит ли PDF права использования

Перед удалением прав использования пример проверяет текущее состояние документа, вызывая `contains_usage_rights()`. Это позволяет вам подтвердить, присутствуют ли права использования, прежде чем вносить изменения.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## Удалить права использования из PDF

Используйте `remove_usage_rights()` когда документ больше не должен сохранять свои текущие настройки прав использования. Пример проверяет начальное состояние, удаляет права и сохраняет обновлённый PDF в новый файл.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

