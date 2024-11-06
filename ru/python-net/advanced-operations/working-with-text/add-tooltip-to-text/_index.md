---
title: PDF Tooltip с использованием Python
linktitle: PDF Tooltip
type: docs
weight: 20
url: ru/python-net/pdf-tooltip/
description: Узнайте, как добавить всплывающую подсказку к текстовому фрагменту в PDF с использованием Python и Aspose.PDF
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip с использованием Python",
    "alternativeHeadline": "Добавьте всплывающую подсказку в PDF к тексту",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, python, добавить всплывающую подсказку в pdf",
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
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "Узнайте, как добавить всплывающую подсказку к текстовому фрагменту в PDF с использованием Python и Aspose.PDF"
}
</script>


## Добавление всплывающей подсказки к найденному тексту путем добавления невидимой кнопки

Этот код демонстрирует, как добавить всплывающие подсказки к определенным фрагментам текста в PDF-документе с использованием Aspose.PDF. Всплывающие подсказки отображаются, когда курсор мыши находится над соответствующим текстом.

Следующий фрагмент кода покажет вам, как реализовать эту функциональность:

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Переместите курсор мыши сюда, чтобы отобразить всплывающую подсказку")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "Переместите курсор мыши сюда, чтобы отобразить очень длинную всплывающую подсказку"
        )
    )
    document.save(output_pdf)

    # Открыть документ с текстом
    document = ap.Document(output_pdf)
    # Создать объект TextAbsorber, чтобы найти все фразы, соответствующие регулярному выражению
    absorber = ap.text.TextFragmentAbsorber(
        "Переместите курсор мыши сюда, чтобы отобразить всплывающую подсказку"
    )
    # Применить абсорбер к страницам документа
    document.pages.accept(absorber)
    # Получить извлеченные текстовые фрагменты
    text_fragments = absorber.text_fragments

    # Перебрать фрагменты
    for fragment in text_fragments:
        # Создать невидимую кнопку на позиции текстового фрагмента
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # alternate_name будет отображаться как всплывающая подсказка приложением просмотра
        field.alternate_name = "Подсказка для текста."
        # Добавить поле кнопки в документ
        document.form.add(field)

    # Далее будет пример очень длинной всплывающей подсказки
    absorber = ap.text.TextFragmentAbsorber(
        "Переместите курсор мыши сюда, чтобы отобразить очень длинную всплывающую подсказку"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Установить очень длинный текст
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # Сохранить документ
    document.save(output_pdf)
```


## Создание скрытого текстового блока и его отображение при наведении мыши

Этот фрагмент кода на Python показывает, как добавить всплывающий текст в PDF-документ, который появляется при наведении курсора мыши на определенную область.

Сначала создается новый PDF-документ, и в него добавляется абзац с текстом "Переместите курсор мыши сюда, чтобы отобразить всплывающий текст". Затем документ сохраняется.

Далее, сохраненный документ снова открывается, и создается объект TextAbsorber для поиска ранее добавленного текстового фрагмента. Этот текстовый фрагмент затем используется для определения позиции и характеристик всплывающего текстового поля.

Создается объект TextBoxField для представления всплывающего текстового поля, и его свойства, такие как позиция, значение, статус только для чтения и видимость, устанавливаются соответствующим образом. Кроме того, полю присваиваются уникальное имя и характеристики внешнего вида.

Всплывающее текстовое поле добавляется в форму документа, и на позиции исходного текстового фрагмента создается невидимое кнопочное поле.
 HideAction события назначены полю кнопки, указывая, что плавающее текстовое поле должно появляться, когда курсор мыши входит в его окрестность, и исчезать, когда курсор выходит.

Наконец, поле кнопки добавляется в форму документа, и измененный документ сохраняется.

Этот фрагмент кода предоставляет метод для создания интерактивных плавающих текстовых элементов в PDF-документе с использованием Aspose.PDF для Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Переместите курсор мыши сюда, чтобы отобразить плавающий текст")
    )
    document.save(output_pdf)

    # Открыть документ с текстом
    document = ap.Document(output_pdf)
    # Создать объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
    absorber = ap.text.TextFragmentAbsorber(
        "Переместите курсор мыши сюда, чтобы отобразить плавающий текст"
    )
    # Применить абсорбер для страниц документа
    document.pages.accept(absorber)
    # Получить первый извлеченный фрагмент текста
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # Создать скрытое текстовое поле для плавающего текста в указанном прямоугольнике страницы
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # Установить текст для отображения в качестве значения поля
    floating_field.value = 'Это "плавающее текстовое поле".'
    # Мы рекомендуем сделать поле "только для чтения" для этого сценария
    floating_field.read_only = True
    # Установить флаг "скрыто", чтобы сделать поле невидимым при открытии документа
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # Установка уникального имени поля не обязательна, но разрешена
    floating_field.partial_name = "FloatingField_1"

    # Установка характеристик внешнего вида поля не обязательна, но улучшает его
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # Добавить текстовое поле в документ
    document.form.add(floating_field)
    # Создать невидимую кнопку на позиции текстового фрагмента
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # Создать новое действие скрытия для указанного поля (аннотации) и флаг невидимости.
    # (Вы также можете ссылаться на плавающее поле по имени, если вы указали его выше.)
    # Добавить действия при входе/выходе курсора на невидимое поле кнопки

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # Добавить поле кнопки в документ
    document.form.add(button_field)

    # Сохранить документ
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET Библиотека",
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
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>