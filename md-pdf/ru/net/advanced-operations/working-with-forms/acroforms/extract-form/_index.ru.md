---
title: Извлечь AcroForm - Извлечение данных формы из PDF в C#
linktitle: Извлечь AcroForm
type: docs
weight: 30
url: /net/extract-form/
keywords: extract form data from pdf c#
description: Извлеките форму из вашего PDF-документа с помощью библиотеки Aspose.PDF для .NET. Получите значение из отдельного поля файла PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Извлечь AcroForm",
    "alternativeHeadline": "Как извлечь AcroForm из PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, извлечь acroform",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Извлеките форму из вашего PDF-документа с помощью библиотеки Aspose.PDF для .NET. Получите значение из отдельного поля файла PDF."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Извлечение данных из формы

### Получение значений из всех полей PDF документа

Чтобы получить значения из всех полей в PDF документе, вам нужно пройти через все поля формы, а затем получить значение с помощью свойства Value. Получите каждое поле из коллекции Form, в базовом типе поля, называемом Field, и получите доступ к его свойству Value.

Следующие фрагменты кода на C# показывают, как получить значения всех полей из PDF документа.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// Получить значения из всех полей
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("Имя поля : {0} ", formField.PartialName);
    Console.WriteLine("Значение : {0} ", formField.Value);
}
```
### Получение значения из отдельного поля PDF-документа

Свойство Value поля формы позволяет получить значение определенного поля. Чтобы получить значение, получите поле формы из коллекции Form объекта Document. В этом примере на C# выбирается [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) и извлекается его значение с использованием свойства Value.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// Получить поле
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// Получить значение поля
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

Для получения URL кнопки отправки используйте следующие строки кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated as SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### Получение полей формы из определенного региона PDF-файла

Иногда вы можете знать, где в документе находится поле формы, но не знать его имени. Например, если у вас есть только схема печатной формы. С Aspose.PDF для .NET это не проблема. Вы можете узнать, какие поля находятся в заданной области PDF-файла. Чтобы получить поля формы из определенного региона PDF-файла:

1. Откройте PDF-файл с помощью объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Получите форму из коллекции Forms документа.
1. Укажите прямоугольный регион и передайте его в метод GetFieldsInRect объекта Form. Возвращается коллекция Fields.
1. Используйте это для манипуляции с полями.

Следующий фрагмент кода на C# показывает, как получить поля формы в определенной прямоугольной области PDF-файла.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Открыть pdf файл
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// Создать объект прямоугольника, чтобы получить поля в этой области
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// Получить PDF форму
Aspose.Pdf.Forms.Form form = doc.Form;

// Получить поля в прямоугольной области
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// Отобразить имена полей и значения
foreach (Field field in fields)
{
    // Отобразить свойства размещения изображения для всех размещений
    Console.Out.WriteLine("Имя поля: " + field.FullName + "-" + "Значение поля: " + field.Value);
}
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
    "applicationCategory": "Библиотека для манипулирования PDF для .NET",
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

