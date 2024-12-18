---
title: Получение и установка свойств страницы
type: docs
url: /ru/net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Получение и установка свойств страницы",
    "alternativeHeadline": "Получение и задание свойств страницы PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, получение свойств страницы, задание свойств страницы",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
Aspose.PDF для .NET позволяет читать и устанавливать свойства страниц в PDF-файле в ваших .NET приложениях. В этом разделе показано, как получить количество страниц в PDF-файле, получить информацию о свойствах страницы PDF, таких как цвет, и установить свойства страницы. Приведенные примеры написаны на C#, но вы можете использовать любой .NET язык, такой как VB.NET, для достижения того же.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Получить количество страниц в PDF-файле

При работе с документами часто хочется знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

Чтобы получить количество страниц в PDF-файле:

1. Откройте PDF-файл с помощью класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Затем используйте свойство Count коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (из объекта Document) для получения общего количества страниц в документе.

Следующий фрагмент кода показывает, как получить количество страниц PDF-файла.
Следующий фрагмент кода показывает, как получить количество страниц PDF-файла.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetNumberofPages-GetNumberofPages.cs" >}}

### Получение количества страниц без сохранения документа

Иногда мы генерируем PDF-файлы на лету и в процессе создания PDF-файла может возникнуть необходимость (создание содержания и т.д.) узнать количество страниц PDF-файла без сохранения файла на системе или потоке. Для удовлетворения этой потребности в классе Document был введен метод [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs). Пожалуйста, ознакомьтесь со следующим фрагментом кода, который показывает шаги получения количества страниц без сохранения документа.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetPageCount-GetPageCount.cs" >}}

## Получение свойств страницы

Каждая страница в PDF-файле имеет ряд свойств, таких как ширина, высота, поля обрезки, области обрезки и подрезки.
Каждая страница в файле PDF имеет ряд свойств, таких как ширина, высота, поля обрезки, кадрирования и обрезки.

### **Понимание свойств страницы: различие между Artbox, BleedBox, CropBox, MediaBox, TrimBox и свойством Rect**

- **Media box**: Media box является самой большой коробкой страницы. Он соответствует размеру страницы (например, A4, A5, US Letter и т.д.), выбранному при печати документа в PostScript или PDF. Другими словами, media box определяет физический размер носителя, на котором отображается или печатается документ PDF.
- **Bleed box**: Если документ содержит область обрезки, то в PDF также будет присутствовать bleed box. Область обрезки — это количество цвета (или изображения), выходящее за край страницы. Это используется для того, чтобы убедиться, что когда документ будет напечатан и обрезан до нужного размера («подрезка»), краска будет доходить до края страницы. Даже если страница будет обрезана немного не по меткам обрезки - белые края не появятся на странице.
- **Trim box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **Trim box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **Art box**: Art box — это рамка, нарисованная вокруг фактического содержимого страниц в ваших документах. Эта рамка используется при импорте PDF-документов в другие приложения.
- **Crop box**: Crop box — это размер «страницы», при котором ваш PDF-документ отображается в Adobe Acrobat. В обычном виде отображается только содержимое crop box в Adobe Acrobat.
  Для подробных описаний этих свойств ознакомьтесь со спецификацией Adobe.Pdf, особенно 10.10.1 Границы страницы.
- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox. Ниже приведена иллюстрация этих свойств.

Для дополнительной информации, пожалуйста, посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Доступ к свойствам страницы**

Класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) предоставляет все свойства, связанные с конкретной страницей PDF.
Класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) предоставляет все свойства, связанные с конкретной страницей PDF.

Оттуда можно получить доступ к отдельным объектам Page, используя их индекс, или перебирать коллекцию с помощью цикла foreach, чтобы получить все страницы. Как только отдельная страница становится доступной, мы можем получить ее свойства. Следующий фрагмент кода показывает, как получить свойства страницы.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## Получить конкретную страницу PDF-файла

Aspose.PDF позволяет [разделить PDF на отдельные страницы](/pdf/ru/net/split-pdf-document/) и сохранить их как файлы PDF. Получение указанной страницы в PDF-файле и сохранение ее как нового PDF происходит очень похожим образом: открыть исходный документ, получить доступ к странице, создать новый документ и добавить на него страницу.

Объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) хранит страницы в файле PDF через [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
[Объект Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) содержит в себе [коллекцию страниц PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), которая включает все страницы PDF файла.

1. Укажите индекс страницы, используя свойство Pages.
1. Создайте новый объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Добавьте объект [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) в новый объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Сохраните результат, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Ниже представлен фрагмент кода, который показывает, как получить конкретную страницу из PDF файла и сохранить её как новый файл.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## Определение цвета страницы

Класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) предоставляет свойства, связанные с конкретной страницей в документе PDF, включая тип цвета - RGB, черно-белый, оттенки серого или неопределенный.
Класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) предоставляет свойства, связанные с конкретной страницей в PDF-документе, включая тип цвета - RGB, черно-белый, оттенки серого или неопределенный - который используется на странице.

Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). Свойство ColorType определяет цвет элементов на странице. Чтобы получить или определить информацию о цвете для конкретной страницы PDF, используйте свойство [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

Следующий фрагмент кода показывает, как перебирать отдельные страницы PDF-файла для получения информации о цвете.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


