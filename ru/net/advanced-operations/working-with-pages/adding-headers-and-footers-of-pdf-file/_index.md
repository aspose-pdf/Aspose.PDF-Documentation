---
title: Добавление верхнего и нижнего колонтитулов в PDF
linktitle: Добавление верхнего и нижнего колонтитулов в PDF
type: docs
weight: 70
url: /ru/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF для .NET позволяет добавлять верхние и нижние колонтитулы в ваш PDF-файл с использованием класса TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление верхнего и нижнего колонтитулов в PDF",
    "alternativeHeadline": "Как добавить верхний и нижний колонтитулы в файл PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, добавление верхнего колонтитула, добавление нижнего колонтитула в pdf",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET позволяет добавлять верхние и нижние колонтитулы в ваш PDF-файл с использованием класса TextStamp."
}
</script>
**Aspose.PDF для .NET** позволяет добавлять заголовок и нижний колонтитул в ваш существующий PDF файл. Вы можете добавлять изображения или текст в документ PDF. Также попробуйте добавить разные заголовки в один PDF файл с помощью C#.

Приведенный ниже фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавление текста в заголовок PDF файла

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) для добавления текста в заголовок PDF файла. Класс TextStamp предоставляет свойства, необходимые для создания текстовой печати, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для добавления текста в заголовок вам нужно создать объект Document и объект TextStamp с использованием необходимых свойств. После этого вы можете вызвать метод AddStamp страницы для добавления текста в заголовок PDF.

Вам нужно установить свойство TopMargin таким образом, чтобы оно корректировало текст в области заголовка вашего PDF. Вам также нужно установить HorizontalAlignment в значение Center и VerticalAlignment в значение Top.

Приведенный ниже фрагмент кода показывает, как добавить текст в заголовок PDF файла с помощью C#.
Следующий фрагмент кода показывает, как добавить текст в заголовок файла PDF с использованием C#.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// Создать заголовок
TextStamp textStamp = new TextStamp("Текст заголовка");
// Установить свойства штампа
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// Добавить заголовок на все страницы
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Сохранить обновленный документ
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## Добавление текста в нижний колонтитул файла PDF

Вы можете использовать класс TextStamp для добавления текста в нижний колонтитул файла PDF.
Вы можете использовать класс TextStamp для добавления текста в нижний колонтитул PDF файла.

{{% alert color="primary" %}}

Вам нужно установить свойство Bottom Margin таким образом, чтобы текст корректировался в области нижнего колонтитула вашего PDF. Также необходимо установить HorizontalAlignment в значение Center и VerticalAlignment в значение Bottom

{{% /alert %}}

Следующий фрагмент кода показывает, как добавить текст в нижний колонтитул PDF файла на C#.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// Создать колонтитул
TextStamp textStamp = new TextStamp("Текст колонтитула");
// Установить свойства штампа
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Добавить колонтитул на все страницы
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Сохранить выходной файл
doc.Save(dataDir + "TextinFooter_out.pdf");
```
## Добавление изображения в заголовок PDF-файла

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) для добавления изображения в заголовок PDF-файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Чтобы добавить изображение в заголовок, вам нужно создать объект Document и объект Image Stamp с необходимыми свойствами. После этого вы можете вызвать метод [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) страницы, чтобы добавить изображение в заголовок PDF.

{{% alert color="primary" %}}

Вам нужно установить свойство TopMargin таким образом, чтобы оно регулировало изображение в области заголовка вашего PDF. Также необходимо установить HorizontalAlignment в значение Center и VerticalAlignment в значение Top.

{{% /alert %}}

Следующий фрагмент кода показывает, как добавить изображение в заголовок PDF-файла на C#.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// Создать заголовок
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Установить свойства штампа
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// Добавить заголовок на все страницы
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Сохранить выходной файл
doc.Save(dataDir + "ImageinHeader_out.pdf");
```
## Добавление изображения в нижний колонтитул PDF-файла

Вы можете использовать класс Image Stamp для добавления изображения в нижний колонтитул PDF-файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для добавления изображения в нижний колонтитул необходимо создать объект Document и объект Image Stamp с использованием необходимых свойств. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить изображение в нижний колонтитул PDF.

{{% alert color="primary" %}}

Вам необходимо установить свойство [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin), чтобы оно подстроило изображение в области нижнего колонтитула вашего PDF. Также необходимо установить [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) в значение `Center` и [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) в значение `Bottom`.

{{% /alert %}}

Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF-файла с помощью C#.
Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF-файла на C#.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// Создать нижний колонтитул
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Установить свойства печати
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Добавить нижний колонтитул на все страницы
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Сохранить выходной файл
doc.Save(dataDir + "ImageInFooter_out.pdf");
```

## Добавление разных заголовков в один PDF-файл

Мы знаем, что можем добавить TextStamp в раздел заголовка/нижнего колонтитула документа, используя свойства TopMargin или Bottom Margin, но иногда у нас может возникнуть необходимость добавить несколько заголовков/нижних колонтитулов в один PDF-документ.
Мы знаем, что можем добавить TextStamp в раздел Заголовок/Нижний колонтитул документа, используя свойства TopMargin или Bottom Margin, но иногда у нас может возникнуть потребность добавить несколько заголовков/нижних колонтитулов в один PDF-документ.

Для выполнения этого требования мы создадим отдельные объекты TextStamp (количество объектов зависит от необходимого количества Заголовков/Нижних колонтитулов) и добавим их в PDF-документ. Мы также можем указать различную информацию о форматировании для каждого объекта штампа. В следующем примере мы создали объект Document и три объекта TextStamp, а затем использовали метод [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) страницы для добавления текста в раздел заголовка PDF. Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF-файла с Aspose.PDF для .NET.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть исходный документ
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// Создать три штампа
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("Header 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("Header 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("Header 3");

// Установить выравнивание штампа (разместить штамп в верхней части страницы, горизонтально по центру)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Указать стиль шрифта как Жирный
stamp1.TextState.FontStyle = FontStyles.Bold;
// Установить информацию о цвете переднего плана текста как красный
stamp1.TextState.ForegroundColor = Color.Red;
// Указать размер шрифта как 14
stamp1.TextState.FontSize = 14;

// Теперь нам нужно установить вертикальное выравнивание 2-го объекта штампа как Верх
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Установить информацию о горизонтальном выравнивании для штампа как Центрированный
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Установить коэффициент масштабирования для объекта штампа
stamp2.Zoom = 10;

// Установить форматирование 3-го объекта штампа
// Указать информацию о вертикальном выравнивании для объекта штампа как ВЕРХ
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Установить информацию о горизонтальном выравнивании для объекта штампа как Центрированный
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Установить угол поворота для объекта штампа
stamp3.RotateAngle = 35;
// Установить розовый как цвет фона для штампа
stamp3.TextState.BackgroundColor = Color.Pink;
// Изменить информацию о шрифте для штампа на Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// Первый штамп добавлен на первую страницу;
doc.Pages[1].AddStamp(stamp1);
// Второй штамп добавлен на вторую страницу;
doc.Pages[2].AddStamp(stamp2);
// Третий штамп добавлен на третью страницу.
doc.Pages[3].AddStamp(stamp3);
// Сохранить обновленный документ
doc.Save(dataDir + "MultiHeader_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
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
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
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
```

