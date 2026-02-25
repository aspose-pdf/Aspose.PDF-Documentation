---
title: Работа с XFA-формами
linktitle: XFA-формы
type: docs
weight: 20
url: /ru/python-net/xfa-forms/
description: Aspose.PDF для Python через .NET API позволяет работать с полями XFA и XFA Acroform в PDF‑документе.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Конвертация XFA в Acroform

{{% alert color="primary" %}}

Попробовать онлайн
Вы можете проверить качество конвертации Aspose.PDF и посмотреть результаты онлайн по этой ссылке: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Следующий фрагмент кода демонстрирует, как преобразовать динамическую форму XFA (XML Forms Architecture) в стандартный AcroForm.

**Ключевые шаги включают:**

1. Загрузка входного PDF‑документа.
1. Изменение типа формы на STANDARD.
1. Сохранение преобразованного PDF в новый файл.

Эта конвертация обеспечивает лучшую совместимость и единообразную работу с формами в разных PDF‑просмотрщиках и приложениях.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## Использование IgnoreNeedsRendering

В этом примере демонстрируется, как с помощью Aspose.PDF для Python преобразовать динамическую форму XFA в стандартный AcroForm. Код проверяет, содержит ли входной PDF форму XFA, и при необходимости переопределяет рендеринг. Затем он устанавливает тип формы в STANDARD и сохраняет обновлённый PDF.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```

