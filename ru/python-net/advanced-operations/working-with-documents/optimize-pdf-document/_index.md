---
title: Оптимизация, Сжатие или Уменьшение размера PDF в Python
linktitle: Оптимизация PDF
type: docs
weight: 30
url: ru/python-net/optimize-pdf/
keywords: "оптимизация pdf python"
description: Оптимизация PDF файла, сжатие всех изображений, уменьшение размера PDF, удаление встроенных шрифтов, удаление неиспользуемых объектов с помощью Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Оптимизация PDF с использованием Python",
    "alternativeHeadline": "Как оптимизировать PDF с помощью Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, python, оптимизация pdf",
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
    "url": "/python-net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Оптимизация PDF файла, сжатие всех изображений, уменьшение размера PDF, удаление встроенных шрифтов, удаление неиспользуемых объектов с помощью Python."
}
</script>


Документ PDF может иногда содержать дополнительные данные. Уменьшение размера PDF-файла поможет вам оптимизировать передачу данных по сети и хранение. Это особенно удобно для публикации на веб-страницах, обмена в социальных сетях, отправки по электронной почте или архивирования в хранилище. Мы можем использовать несколько техник для оптимизации PDF:

- Оптимизация содержимого страниц для просмотра в Интернете
- Уменьшение или сжатие всех изображений
- Включение повторного использования содержимого страниц
- Объединение дублирующихся потоков
- Исключение встроенных шрифтов
- Удаление неиспользуемых объектов
- Удаление сглаживания полей формы
- Удаление или сглаживание аннотаций

{{% alert color="primary" %}}

 Подробное объяснение методов оптимизации можно найти на странице Обзор методов оптимизации.

{{% /alert %}}

## Оптимизация PDF-документа для Интернета

Оптимизация или линеаризация для Интернета относится к процессу подготовки PDF-файла для онлайн-просмотра с использованием веб-браузера. Чтобы оптимизировать файл для веб-отображения:

1. Откройте входной документ в объекте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Используйте метод [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. Сохраните оптимизированный документ, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий фрагмент кода показывает, как оптимизировать PDF-документ для веба.

```python 

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Оптимизировать для веба
    document.optimize()

    # Сохранить выходной документ
    document.save(output_pdf)
```

## Уменьшение размера PDF

Метод [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) позволяет уменьшить размер документа, удаляя ненужную информацию. По умолчанию этот метод работает следующим образом:

- Ресурсы, которые не используются на страницах документа, удаляются
- Одинаковые ресурсы объединяются в один объект

- Неиспользуемые объекты удаляются

Ниже приведен пример. Однако обратите внимание, что этот метод не может гарантировать уменьшение размера документа.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Оптимизировать PDF документ. Однако обратите внимание, что этот метод не может гарантировать уменьшение размера документа
    document.optimize_resources()
    # Сохранить обновленный документ
    document.save(output_pdf)
```

## Управление стратегией оптимизации

Мы также можем настроить стратегию оптимизации. В настоящее время метод [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) использует 5 техник. Эти техники могут быть применены с использованием метода OptimizeResources() с параметром [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### Уменьшение или сжатие всех изображений

У нас есть два способа работы с изображениями: уменьшить качество изображения и/или изменить их разрешение.
 В любом случае, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) следует применять. В следующем примере мы уменьшаем изображения, снижая качество изображения до 50.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Инициализация OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Установить опцию CompressImages
    optimizeOptions.image_compression_options.compress_images = True
    # Установить опцию ImageQuality
    optimizeOptions.image_compression_options.image_quality = 50
    # Оптимизация PDF документа с использованием OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Сохранение обновленного документа
    document.save(output_pdf)
```

### Удаление неиспользуемых объектов

PDF документ иногда содержит PDF объекты, которые не ссылаются ни на один другой объект в документе. Это может произойти, например, когда страница удаляется из дерева страниц документа, но сам объект страницы не удаляется. Удаление этих объектов не делает документ недействительным, а скорее уменьшает его размер.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Установить опцию RemoveUsedObject
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Оптимизировать PDF документ с использованием OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Сохранить обновленный документ
    document.save(output_pdf)
```

### Удаление неиспользуемых потоков

Иногда документ содержит неиспользуемые потоки ресурсов. These streams are not “unused objects” because they are referenced from a page resource dictionary. Thus, they are not removed with a “remove unused objects” method. But these streams are never used with the page contents. This may happen in cases when an image has been removed from the page but not from the page resources. Also, this situation often occurs when pages are extracted from the document and document pages have “common” resources, that is, the same Resources object. Page contents are analyzed in order to determine if a resource stream is used or not. Unused streams are removed. It sometimes decreases the document size. The use of this technique is similar to the previous step:

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Установить параметр RemoveUsedStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Оптимизировать PDF-документ с использованием OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Сохранить обновленный документ
    document.save(output_pdf)
```

### Связывание Дублирующих Потоков

Некоторые документы могут содержать несколько идентичных потоков ресурсов (например, изображения). Это может произойти, например, когда документ объединяется с самим собой. Выходной документ содержит две независимые копии одного и того же потока ресурсов. Мы анализируем все потоки ресурсов и сравниваем их. Если потоки дублируются, они объединяются, то есть остается только одна копия. Ссылки изменяются соответствующим образом, а копии объекта удаляются. В некоторых случаях это помогает уменьшить размер документа.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Установить опцию LinkDuplcateStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Оптимизировать PDF-документ, используя OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Сохранить обновленный документ
    document.save(output_pdf)
```

### Извлечение Встроенных Шрифтов

Если документ использует встроенные шрифты, это означает, что все данные шрифта хранятся в документе.
 Преимущество заключается в том, что документ можно просматривать независимо от того, установлен ли шрифт на компьютере пользователя или нет. Но внедрение шрифтов увеличивает размер документа. Метод удаления внедренных шрифтов удаляет все внедренные шрифты. Таким образом, размер документа уменьшается, но сам документ может стать нечитаемым, если нужный шрифт не установлен.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Установить опцию UnembedFonts
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Оптимизировать PDF документ с использованием OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Сохранить обновленный документ
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Исходный размер файла: {}. Уменьшенный размер файла: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Ресурсы оптимизации применяют эти методы к документу. Если любой из этих методов применяется, размер документа, скорее всего, уменьшится. Если ни один из этих методов не применяется, размер документа не изменится, что очевидно.

## Дополнительные способы уменьшения размера PDF документа

### Удаление или упрощение аннотаций

Аннотации могут быть удалены, когда они не нужны. Когда они необходимы, но не требуют дополнительного редактирования, их можно упростить. Оба этих метода уменьшат размер файла.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Упрощение аннотаций
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Сохранить обновленный документ
    document.save(output_pdf)
```

### Удаление полей формы

Если PDF документ содержит AcroForms, мы можем попробовать уменьшить размер файла, упрощая поля формы.

```python

    import aspose.pdf as ap

    # Загрузить исходную PDF форму
    doc = ap.Document(input_pdf)

    # Упрощение форм
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Сохранить обновленный документ
    doc.save(output_pdf)
```

### Преобразование PDF из цветового пространства RGB в градации серого

PDF файл состоит из текста, изображений, вложений, аннотаций, графиков и других объектов. Вы можете столкнуться с требованием преобразовать PDF из цветового пространства RGB в градации серого, чтобы ускорить печать этих PDF файлов. Кроме того, при преобразовании файла в градации серого уменьшается размер документа, но это также может привести к снижению качества документа. Эта функция в настоящее время поддерживается функцией Pre-Flight в Adobe Acrobat, но при автоматизации работы с документами, Aspose.PDF является идеальным решением для предоставления таких возможностей манипуляции с документами. Для выполнения этого требования можно использовать следующий фрагмент кода.

```python

    import aspose.pdf as ap

    # Загрузить исходный PDF файл
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Преобразовать изображение из цветового пространства RGB в градации серого
        strategy.convert(page)

    # Сохранить полученный файл
    document.save(output_pdf)
```


### FlateDecode Сжатие

Aspose.PDF для Python через .NET предоставляет поддержку сжатия FlateDecode для функциональности оптимизации PDF. Следующий фрагмент кода ниже показывает, как использовать опцию в оптимизации для сохранения изображений с **FlateDecode** сжатием:

```python

    import aspose.pdf as ap

    # Открыть документ
    doc = ap.Document(input_pdf)
    # Инициализировать OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # Чтобы оптимизировать изображение, используя FlateDecode Compression, установите параметры оптимизации на Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Установить параметры оптимизации
    doc.optimize_resources(optimizationOptions)
    # Сохранить документ
    doc.save(output_pdf)