---
title: Липкие аннотации PDF с использованием Python
linktitle: липкая аннотация
type: docs
weight: 50
url: /ru/python-net/sticky-annotations/
description: Узнайте, как добавлять липкие аннотации в PDF‑документы с помощью Aspose.PDF в Python через .NET для комментариев и отзывов.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Руководство по работе с липкими аннотациями в PDF
Abstract: В этой статье представлено подробное руководство по управлению аннотациями‑водяными знаками в PDF‑документах с использованием библиотеки Aspose.PDF для Python. Описывается процесс добавления, получения и удаления аннотаций‑водяных знаков для обеспечения подлинности и брендинга документа. Аннотация‑водяной знак может использоваться для внедрения графики, такой как логотипы, фиксированного размера и позиции на странице. Руководство включает фрагменты кода, демонстрирующие, как добавить аннотацию‑водяной знак в определённое место с регулируемой непрозрачностью, а также как получать и удалять существующие аннотации‑водяные знаки. Примеры кода иллюстрируют использование библиотеки Aspose.PDF для программного манипулирования PDF‑документами, предлагая практический подход для разработчиков по интеграции функций водяного знака в их приложения.
---

## Добавить водяную аннотацию

Самой заметной и легко визуализируемой и передаваемой является аннотация‑водяной знак. Это лучший способ разместить в вашем PDF‑документе логотип или любой другой символ, подтверждающий его оригинальность.

Графическая аннотация‑водяной знак должна использоваться для представления графики, печатаемой фиксированного размера и положения на странице, независимо от размеров печатаемой страницы.

Вы можете добавить текст водяного знака, используя [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) в определённой позиции страницы PDF. Непрозрачность водяного знака также можно контролировать с помощью свойства [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties).

Пожалуйста, посмотрите следующий фрагмент кода для добавления WatermarkAnnotation.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## Получить водяную аннотацию

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## Удалить водяную аннотацию

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


