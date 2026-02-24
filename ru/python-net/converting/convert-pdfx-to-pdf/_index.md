---
title: Преобразование PDF/x в форматы PDF на Python
linktitle: Преобразовать PDF/x в форматы PDF
type: docs
weight: 120
url: /ru/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: В этом материале показано, как преобразовать PDF/x в форматы PDF с использованием Aspose.PDF for Python через .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как преобразовать PDF/x в форматы PDF
Abstract: Статья предоставляет всестороннее руководство по преобразованию PDF/UA и PDF/A в файл PDF с использованием Aspose.PDF for Python.
---

**PDF/x в формат PDF означает возможность преобразовать PDF/UA и PDF/A в файл PDF.**

## Преобразовать PDF/A в PDF

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Вызовите 'remove_pdfa_compliance()', чтобы удалить все настройки соответствия и метаданные, связанные с PDF/A.
1. Сохраните полученный PDF по указанному пути вывода.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Удаление соответствия PDF/UA

Эта функция демонстрирует двухэтапный процесс преобразования: сначала удаляется соответствие PDF/UA (Universal Accessibility), затем полученный PDF преобразуется в формат PDF/A-1B с автоматической разметкой для доступности и семантической структуры.

1. Загрузите PDF‑документ, используя 'ap.Document()'.
1. Вызовите 'document.remove_pdfa_compliance()', чтобы удалить любые ограничения или настройки соответствия PDF/A.
1. Сохраните измененный PDF в 'path_outfile'.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
