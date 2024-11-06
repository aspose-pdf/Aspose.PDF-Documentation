---
title: Добавление заголовка и колонтитула в PDF с использованием Python
linktitle: Добавление заголовка и колонтитула в PDF
type: docs
weight: 50
url: ru/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF для Python через .NET позволяет добавлять заголовки и колонтитулы в ваш PDF файл с использованием класса TextStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление заголовка и колонтитула в PDF с использованием Python",
    "alternativeHeadline": "Как добавить заголовок и колонтитул в PDF файл",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, добавление заголовка, добавление колонтитула в pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для Python через .NET позволяет добавлять заголовки и колонтитулы в ваш PDF файл с использованием класса TextStamp."
}
</script>


**Aspose.PDF для Python через .NET** позволяет добавлять заголовок и нижний колонтитул в ваш существующий PDF-файл. Вы можете добавлять изображения или текст в PDF-документ. Также попробуйте добавить разные заголовки в один PDF-файл с помощью Python.

## Добавление текста в заголовок PDF-файла

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/), чтобы добавить текст в заголовок PDF-файла. Класс TextStamp предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить текст в заголовок, вам нужно создать объект Document и объект TextStamp, используя необходимые свойства. После этого вы можете вызвать метод 'add_stamp' страницы, чтобы добавить текст в заголовок PDF.

Вам необходимо установить свойство [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) таким образом, чтобы оно корректировало текст в области заголовка вашего PDF. Вам также нужно установить 'horizontal_alignment' на Center и 'vertical_alignment' на Top.

В следующем фрагменте кода показано, как добавить текст в заголовок PDF-файла с помощью Python:

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Создать заголовок
    textStamp = ap.TextStamp("Header Text")
    # Установить свойства штампа
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Добавить заголовок на все страницы
    for page in document.pages:
        page.add_stamp(textStamp)

    # Сохранить обновленный документ
    document.save(output_pdf)
```

## Добавление текста в нижний колонтитул PDF файла

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) для добавления текста в нижний колонтитул PDF файла.
 class TextStamp предоставляет свойства, необходимые для создания текстовой печати, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для того чтобы добавить текст в нижний колонтитул, вам нужно создать объект Document и объект TextStamp, используя необходимые свойства. После этого вы можете вызвать метод 'add_stamp' страницы, чтобы добавить текст в нижний колонтитул PDF.

Следующий фрагмент кода показывает, как добавить текст в нижний колонтитул PDF файла с помощью Python:

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Создать нижний колонтитул
    textStamp = ap.TextStamp("Footer Text")
    # Установить свойства печати
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Добавить нижний колонтитул на все страницы
    for page in document.pages:
        page.add_stamp(textStamp)

    # Сохранить обновленный PDF файл
    document.save(output_pdf)
```

## Добавление изображения в верхний колонтитул PDF файла

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/), чтобы добавить изображение в верхний колонтитул PDF файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для того чтобы добавить изображение в заголовок, вам нужно создать объект Document и объект Image Stamp, используя необходимые свойства. После этого вы можете вызвать метод 'add_stamp' страницы, чтобы добавить изображение в заголовок PDF.

Следующий фрагмент кода показывает, как добавить изображение в заголовок PDF файла с помощью Python:

```python 

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Создать заголовок
    image_stamp = ap.ImageStamp(input_image)
    # Установить свойства штампа
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Добавить заголовок на все страницы
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Сохранить обновленный документ
    document.save(output_pdf)
```

## Добавление изображения в нижний колонтитул PDF файла

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) для добавления изображения в нижний колонтитул PDF файла. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) класс предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить изображение в нижний колонтитул, вам нужно создать объект Document и объект ImageStamp с использованием необходимых свойств. После этого вы можете вызвать метод 'add_stamp' страницы, чтобы добавить изображение в нижний колонтитул PDF.

Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF файла с помощью Python:

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Создать нижний колонтитул
    image_stamp = ap.ImageStamp(input_image)
    # Установить свойства штампа
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Добавить нижний колонтитул на все страницы
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Сохранить обновленный PDF файл
    document.save(output_pdf)
```

## Добавление разных заголовков в один PDF файл

Мы знаем, что можем добавить TextStamp в раздел Заголовок/Нижний колонтитул документа, используя свойства [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) или [bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties), но иногда может возникнуть необходимость добавить несколько заголовков/нижних колонтитулов в одном PDF документе. **Aspose.PDF for Python via .NET** объясняет, как это сделать.

Чтобы выполнить это требование, мы создадим отдельные объекты TextStamp (количество объектов зависит от количества требуемых Заголовков/Нижних колонтитулов) и добавим их в PDF документ.
 Мы также можем указать различную информацию о форматировании для отдельного объекта штампа. В следующем примере мы создали объект Document и три объекта TextStamp, а затем использовали метод 'add_stamp' класса Page, чтобы добавить текст в разделе заголовка PDF. Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF-файла с помощью Aspose.PDF для Python:

```python

    import aspose.pdf as ap

    # Создаем три штампа
    stamp1 = ap.TextStamp("Заголовок 1")
    stamp2 = ap.TextStamp("Заголовок 2")
    stamp3 = ap.TextStamp("Заголовок 3")

    # Устанавливаем выравнивание штампа (размещаем штамп вверху страницы, по центру по горизонтали)
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Указываем стиль шрифта как Жирный
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # Устанавливаем цвет текста как красный
    stamp1.text_state.foreground_color = ap.Color.red
    # Указываем размер шрифта как 14
    stamp1.text_state.font_size = 14

    # Теперь нам нужно установить вертикальное выравнивание второго объекта штампа как Вверх
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # Устанавливаем информацию о горизонтальном выравнивании штампа как по центру
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Устанавливаем коэффициент увеличения для объекта штампа
    stamp2.zoom = 10

    # Устанавливаем форматирование третьего объекта штампа
    # Указываем информацию о вертикальном выравнивании для объекта штампа как Вверх
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # Устанавливаем информацию о горизонтальном выравнивании для объекта штампа как по центру
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Устанавливаем угол поворота для объекта штампа
    stamp3.rotate_angle = 35
    # Устанавливаем розовый цвет как цвет фона для штампа
    stamp3.text_state.background_color = ap.Color.pink
    # Изменяем шрифт для штампа на Verdana
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # Первый штамп добавляется на первую страницу;
    document.pages[1].add_stamp(stamp1)
    # Второй штамп добавляется на вторую страницу;
    document.pages[2].add_stamp(stamp2)
    # Третий штамп добавляется на третью страницу.
    document.pages[3].add_stamp(stamp3)

    # Сохраняем обновленный документ
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET библиотеку",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для Python",
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