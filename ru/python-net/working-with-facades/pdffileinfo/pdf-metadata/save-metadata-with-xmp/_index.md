---
title: Сохранить метаданные с помощью XMP
linktitle: Сохранить метаданные с помощью XMP
type: docs
weight: 30
url: /ru/python-net/save-metadata-with-xmp/
description: Сохранить метаданные PDF, используя XMP с Aspose.PDF for Python via .NET
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сохранение метаданных PDF с XMP с помощью Aspose.PDF for Python
Abstract: Это руководство демонстрирует, как сохранить метаданные PDF, используя XMP (Extensible Metadata Platform) с Aspose.PDF for Python via .NET. XMP гарантирует, что как стандартные, так и пользовательские метаданные встраиваются в стандартизированный формат XML внутри PDF, улучшая совместимость между приложениями и рабочими процессами.
---

Метаданные PDF могут храниться разными способами, и XMP является современным стандартизированным методом встраивания метаданных в файл PDF. Используя Aspose.PDF, вы можете обновлять стандартные поля, такие как Title, Subject, Keywords и Creator, а затем сохранять их в формате XMP, чтобы обеспечить более широкую совместимость и будущую защиту. Этот метод рекомендуется вместо устаревших способов хранения метаданных.

1. Загрузите PDF‑файл.
1. Установите стандартные поля метаданных.
1. Сохраните метаданные в формате XMP.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```

