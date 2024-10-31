---
title: Добавление текстовых штампов в PDF с помощью Python
linktitle: Текстовые штампы в PDF файле
type: docs
weight: 20
url: /python-net/text-stamps-in-the-pdf-file/
description: Добавьте текстовый штамп в PDF документ с использованием класса TextStamp из библиотеки Aspose.PDF для Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление текстовых штампов в PDF Python",
    "alternativeHeadline": "Добавление текстовых штампов в PDF Python",
    "author": {
        "@type": "Person",
        "name":"Андрий Андруховский",
        "givenName": "Андрий",
        "familyName": "Андруховский",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, генерация документов",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "Добавьте текстовый штамп в PDF документ с использованием класса TextStamp из библиотеки Aspose.PDF для Python."
}
</script>


## Добавление текстового штампа с помощью Python

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) для добавления текстового штампа в PDF файл. Класс [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для того чтобы добавить текстовый штамп, вам нужно создать объект Document и объект TextStamp с использованием необходимых свойств. После этого вы можете вызвать метод [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) страницы для добавления штампа в PDF. Следующий фрагмент кода показывает, как добавить текстовый штамп в PDF файл.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Создать текстовый штамп
    text_stamp = ap.TextStamp("Sample Stamp")
    # Установить, является ли штамп фоном
    text_stamp.background = True
    # Установить начальную точку
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Повернуть штамп
    text_stamp.rotate = ap.Rotation.ON90
    # Установить свойства текста
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # Добавить штамп на конкретную страницу
    document.pages[1].add_stamp(text_stamp)

    # Сохранить выходной документ
    document.save(output_pdf)
```


## Определение выравнивания для объекта TextStamp

Добавление водяных знаков в PDF документы является одной из часто требуемых функций, и Aspose.PDF для Python полностью способен добавлять как изображение, так и текстовые водяные знаки. У нас есть класс под названием [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/), который предоставляет возможность добавлять текстовые штампы в PDF файл. Недавно возникла необходимость поддерживать функцию указания выравнивания текста при использовании объекта TextStamp. Поэтому, чтобы удовлетворить это требование, мы ввели свойство [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) в классе [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/). Используя это свойство, мы можем указать [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) выравнивание текста.

Следующие фрагменты кода показывают пример того, как загрузить существующий PDF документ и добавить в него TextStamp.

```python

    import aspose.pdf as ap

    # Создать объект Document с входным файлом
    doc = ap.Document(input_pdf)
    # Создать объект FormattedText с примером строки
    text = ap.facades.FormattedText("This")
    # Добавить новую строку текста в FormattedText
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # Создать объект TextStamp с использованием FormattedText
    stamp = ap.TextStamp(text)
    # Указать горизонтальное выравнивание текстового штампа как центрированное
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Указать вертикальное выравнивание текстового штампа как центрированное
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # Указать горизонтальное выравнивание текста для TextStamp как центрированное
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # Установить верхнее поле для объекта штампа
    stamp.top_margin = 20
    # Добавить объект штампа на первую страницу документа
    doc.pages[1].add_stamp(stamp)

    # Сохранить обновленный документ
    doc.save(output_pdf)
```


## Заливка Обводка Текста как Штамп в PDF Файл

Мы реализовали установку режима рендеринга для сценариев добавления и редактирования текста. Чтобы отобразить текст с обводкой, создайте объект TextState для передачи расширенных свойств. Установите цвет для обводки. Затем установите режим рендеринга текста. Следующим шагом свяжите TextState и добавьте Штамп.

Следующий фрагмент кода демонстрирует добавление Заливки Обводки Текста:

```python

    import aspose.pdf as ap

    # Создайте объект TextState для передачи расширенных свойств
    ts = ap.text.TextState()
    # Установите цвет для обводки
    ts.stroking_color = ap.Color.gray
    # Установите режим рендеринга текста
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # Загрузите входной PDF документ
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAID IN FULL",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # Свяжите TextState
    stamp.bind_text_state(ts)
    # Установите X,Y координаты
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # Добавьте Штамп
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипуляции PDF для Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>