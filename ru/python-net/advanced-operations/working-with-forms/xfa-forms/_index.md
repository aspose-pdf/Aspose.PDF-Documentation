---
title: Работа с XFA-формами
linktitle: XFA-формы
type: docs
weight: 20
url: /python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API позволяет работать с полями XFA и XFA Acroform в PDF-документе.
lastmod: "2025-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Преобразовать XFA‑в‑Acroform

{{% alert color="primary" %}}

Попробовать онлайн
Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Следующий фрагмент кода демонстрирует, как преобразовать динамическую форму XFA (XML Forms Architecture) в стандартный AcroForm.

**Ключевые шаги включают:**

1. Загрузка входного PDF‑документа.
1. Изменение типа формы на STANDARD.
1. Сохранение преобразованного PDF в новый файл.

Это преобразование обеспечивает лучшую совместимость и единообразную обработку форм во всех различных PDF‑просмотрщиках и приложениях.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## Использование IgnoreNeedsRendering

В этом примере демонстрируется, как преобразовать динамическую форму XFA в стандартную AcroForm с помощью Aspose.PDF for Python. Код проверяет, содержит ли входной PDF форму XFA, и при необходимости переопределяет рендеринг. Затем он устанавливает тип формы в STANDARD и сохраняет обновлённый PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
