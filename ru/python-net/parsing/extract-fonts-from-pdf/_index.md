---
title: Извлечение шрифтов из PDF с помощью Python
linktitle: Извлечение шрифтов из PDF
type: docs
weight: 30
url: /ru/python-net/extract-fonts-from-pdf/
description: Используйте библиотеку Aspose.PDF для Python, чтобы извлечь все встроенные шрифты из вашего PDF‑документа.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь шрифты из PDF с помощью Python
Abstract: Эта статья предоставляет рекомендации по извлечению всех шрифтов из PDF‑документа с использованием конкретного метода из библиотеки Aspose.PDF. В ней представляется метод `font_utilities.get_all_fonts()`, доступный в классе `Document`, который упрощает получение информации о шрифтах. В статье включён пример кода на Python, демонстрирующий процесс импорт необходимых модулей, открытие PDF‑документа и перебор шрифтов с выводом имени каждого шрифта. Такой подход полезен разработчикам, которым нужно анализировать или манипулировать данными шрифтов в PDF‑файлах.
---

Если вы хотите получить все шрифты из PDF‑документа, вы можете использовать метод 'font_utilities.get_all_fonts()', предоставленный в классе Document. Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы получить все шрифты из существующего PDF‑документа:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

