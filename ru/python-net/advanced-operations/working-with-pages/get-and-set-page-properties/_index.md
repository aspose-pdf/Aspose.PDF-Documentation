---
title: Получение и Установка Свойств Страницы с использованием Python
linktitle: Получение и Установка Свойств Страницы
type: docs
weight: 90
url: ru/python-net/get-and-set-page-properties/
description: Этот раздел показывает, как получить количество страниц в PDF файле, получить информацию о свойствах страниц PDF, таких как цвет, и установить свойства страницы.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Получение и Установка Свойств Страницы с использованием Python",
    "alternativeHeadline": "Получение и Установка Свойств Страниц PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, python, получение свойств страницы, установка свойств страницы",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
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
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF for Python via .NET позволяет читать и задавать свойства страниц в PDF-файле в ваших Python приложениях. Этот раздел показывает, как получить количество страниц в PDF-файле, получить информацию о свойствах страниц PDF, таких как цвет, и задать свойства страниц. Примеры приведены на Python.

## Получение количества страниц в PDF-файле

При работе с документами часто необходимо знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

Чтобы получить количество страниц в PDF-файле:

1. Откройте PDF-файл, используя класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Затем используйте свойство Count коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (из объекта Document), чтобы получить общее количество страниц в документе.

Следующий фрагмент кода показывает, как получить количество страниц PDF-файла.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Получить количество страниц
    print("Количество страниц:", str(len(document.pages)))
```


### Получение количества страниц без сохранения документа

Иногда мы создаем PDF файлы на лету, и во время создания PDF файла может возникнуть необходимость (создание оглавления и т.д.) получить количество страниц PDF файла без сохранения файла на системе или потоке. Чтобы удовлетворить это требование, в классе Document был введен метод [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода, который показывает шаги для получения количества страниц без сохранения документа.

```python

    import aspose.pdf as ap

    # Создать экземпляр Document
    document = ap.Document()
    # Добавить страницу в коллекцию страниц PDF файла
    page = document.pages.add()
    # Создать экземпляр цикла
    for i in range(0, 300):
        # Добавить TextFragment в коллекцию абзацев объекта страницы
        page.paragraphs.add(ap.text.TextFragment("Тест количества страниц"))
    # Обработать абзацы в PDF файле для получения точного количества страниц
    document.process_paragraphs()
    # Вывести количество страниц в документе
    print("Количество страниц в документе =", str(len(document.pages)))
```


## Получение Свойств Страницы

Каждая страница в PDF-файле имеет ряд свойств, таких как ширина, высота, bleed-, crop- и trimbox. Aspose.PDF позволяет получить доступ к этим свойствам.

### **Понимание Свойств Страницы: Разница между Artbox, BleedBox, CropBox, MediaBox, TrimBox и Свойством Rect**

- **Media box**: Media box является самым большим прямоугольником страницы. Он соответствует размеру страницы (например, A4, A5, US Letter и т.д.), выбранному при печати документа в PostScript или PDF. Другими словами, media box определяет физический размер носителя, на котором PDF-документ отображается или печатается.
- **Bleed box**: Если у документа есть вылет, у PDF также будет bleed box.
 Bleed — это количество цвета (или изображения), которое выходит за край страницы. Это используется для того, чтобы при печати и обрезке документа до нужного размера («подрезка») чернила доходили до края страницы. Даже если страница будет обрезана неточно — слегка не по меткам обрезки — на странице не появятся белые края.
- **Trim box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **Art box**: Art box — это рамка, нарисованная вокруг фактического содержимого страниц в ваших документах. Эта рамка используется при импорте PDF-документов в другие приложения.
- **Crop box**: Crop box — это размер «страницы», при котором ваш PDF-документ отображается в Adobe Acrobat. В нормальном режиме отображения в Adobe Acrobat отображается только содержимое рамки Crop box.
  Для подробного описания этих свойств прочитайте спецификацию Adobe.Pdf, в частности, раздел 10.10.1 Page Boundaries.
- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox. Картинка ниже иллюстрирует эти свойства.

Для получения дополнительной информации, пожалуйста, посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Доступ к свойствам страницы**

Класс [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) предоставляет все свойства, связанные с конкретной страницей PDF. Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Оттуда можно получить доступ либо к отдельным объектам Page, используя их индекс, либо пройтись по коллекции с помощью цикла foreach, чтобы получить все страницы. Как только доступ к отдельной странице получен, мы можем получить ее свойства. Следующий фрагмент кода показывает, как получить свойства страницы.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    # Получить конкретную страницу
    page = document.pages[1]
    # Получить свойства страницы
    print(
        "ArtBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("Номер страницы :", page.number)
    print("Поворот :", page.rotate)
```

## Получение Конкретной Страницы PDF Файла

Aspose.PDF для Python позволяет [разделить PDF на отдельные страницы](/pdf/python-net/split-pdf-document/) и сохранить их как PDF файлы. Получение определённой страницы в PDF файле и её сохранение как нового PDF - это очень похожая операция: откройте исходный документ, получите доступ к странице, создайте новый документ и добавьте туда страницу.

[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection) объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) содержит страницы в PDF файле. Чтобы получить конкретную страницу из этой коллекции:

1. Укажите индекс страницы, используя свойство Pages.
1. Создайте новый объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Добавьте объект [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) к новому объекту Document.
1. Сохраните результат, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий код показывает, как получить конкретную страницу из PDF файла и сохранить её как новый файл.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Получить конкретную страницу
    page = document.pages[2]

    # Сохранить страницу как PDF файл
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## Определение цвета страницы

Класс [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) предоставляет свойства, связанные с конкретной страницей в PDF-документе, включая тип цвета - RGB, черно-белый, градации серого или не определен - который использует страница.

Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
 The [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) свойство указывает цвет элементов на странице. Чтобы получить или определить информацию о цвете для конкретной страницы PDF, используйте свойство [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) объекта [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).

Следующий фрагмент кода показывает, как перебрать отдельные страницы PDF-файла, чтобы получить информацию о цвете.

```python

    import aspose.pdf as ap

    # Открыть исходный PDF файл
    document = ap.Document(input_pdf)
    # Перебрать все страницы PDF-файла
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # Получить информацию о типе цвета для конкретной страницы PDF
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("Страница # " + str(page_number) + " черно-белая.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("Страница # " + str(page_number) + " в градациях серого.")

        if page_color_type == ap.ColorType.RGB:
            print("Страница # " + str(page_number) + " RGB.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("Цвет страницы # " + str(page_number) + " не определен.")
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET библиотека",
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
    "applicationCategory": "Библиотека для манипуляции с PDF для Python",
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