---
title: Конвертировать PDF/A и PDF/UA в PDF на Python
linktitle: Конвертировать PDF/A и PDF/UA в PDF
type: docs
weight: 120
url: /python-net/convert-pdf_x-to-pdf/
lastmod: "2026-04-14"
description: Узнайте, как удалить соответствие PDF/A и PDF/UA из PDF‑файлов в Python с помощью Aspose.PDF for Python via .NET и сохранить их как стандартные PDF‑документы.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF/A и PDF/UA в стандартный PDF на Python
Abstract: В этой статье объясняется, как удалить соответствие PDF/A и PDF/UA из PDF‑документов, основанных на стандартах, с использованием Aspose.PDF for Python via .NET. Описываются сценарии, когда вам может понадобиться стандартный PDF вместо архивного или ограниченного доступностью файла, а также показывается, как сохранить результат после удаления метаданных и ограничений соответствия.
---

Используйте эту страницу, когда необходимо конвертировать PDF, основанный на стандартах, такой как PDF/A или PDF/UA, обратно в обычный PDF‑документ для последующего редактирования, обработки или распространения.

PDF-файлы, соответствующие стандартам, полезны для архивирования, печати и процессов обеспечения доступности, но в некоторых случаях может потребоваться удалить это соответствие перед интеграцией файла в другие системы или конвейеры. Aspose.PDF for Python via .NET позволяет сделать это программно, а затем сохранить результат как стандартный PDF‑файл.

## Конвертировать PDF/A в PDF

В этом примере удаляются метаданные и ограничения соответствия PDF/A из PDF, чтобы документ можно было снова сохранить как обычный PDF‑файл.

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Вызовите 'remove_pdfa_compliance()', чтобы удалить все настройки соответствия и метаданные, связанные с PDF/A.
1. Сохраните полученный PDF в указанный путь вывода.

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

Этот пример демонстрирует, как удалить соответствие, связанное с PDF/UA, чтобы документ можно было сохранить как обычный PDF для рабочих процессов, не связанных с доступностью.

1. Загрузите PDF‑документ, используя 'ap.Document()'.
1. Вызовите 'document.remove_pdfa_compliance()', чтобы удалить любые ограничения PDF/A или настройки соответствия.
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

## Когда использовать этот рабочий процесс

- Удалите настройки соответствия перед отправкой документа в цепочку инструментов, не требующую ограничений PDF/A или PDF/UA.
- Упростите последующую обработку документов, когда архивные или метаданные доступности более не требуются.
- Нормализуйте входные PDF перед их экспортом в другие форматы.

## Связанные преобразования

- [Преобразовать PDF в PDF/A, PDF/E и PDF/X](/pdf/ru/python-net/convert-pdf-to-pdf_x/) если вам нужен обратный рабочий процесс и вы хотите создавать PDF, соответствующие стандартам.
- [Преобразовать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) для вывода редактируемого документа после снятия ограничений соответствия.
- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для вывода, совместимого с браузером, из стандартных PDF‑файлов.
