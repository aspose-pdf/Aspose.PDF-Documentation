---
title: Оптимизация, сжатие или уменьшение размера PDF в C#
linktitle: Оптимизация PDF
type: docs
weight: 30
url: /ru/net/optimize-pdf/
keywords: "optimize pdf c#"
description: Оптимизация файла PDF, сжатие всех изображений, уменьшение размера PDF, удаление встроенных шрифтов, удаление неиспользуемых объектов с помощью C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/changing-page-sizes-in-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Оптимизация PDF с использованием C#",
    "alternativeHeadline": "Как оптимизировать PDF с помощью .NET",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, c#, оптимизация pdf",
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
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "английский"
            }
        ]
    },
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Оптимизация файла PDF, сжатие всех изображений, уменьшение размера PDF, удаление встроенных шрифтов, удаление неиспользуемых объектов с помощью C#."
}
</script>
PDF-документ иногда может содержать дополнительные данные. Уменьшение размера файла PDF поможет оптимизировать передачу по сети и хранение. Это особенно удобно для публикации на веб-страницах, обмена в социальных сетях, отправки по электронной почте или архивирования на хранилищах. Мы можем использовать несколько методов для оптимизации PDF:

- Оптимизировать содержимое страницы для просмотра в интернете
- Сжать или уменьшить все изображения
- Включить повторное использование содержимого страницы
- Объединить дублирующиеся потоки
- Удалить встроенные шрифты
- Удалить неиспользуемые объекты
- Удалить поля форм, сделанные плоскими
- Удалить или сделать плоскими аннотации

{{% alert color="primary" %}}

 Подробное описание методов оптимизации можно найти на странице Обзор методов оптимизации.

{{% /alert %}}

## Оптимизация PDF-документа для веба

Оптимизация или линеаризация для веба относится к процессу подготовки файла PDF к просмотру в онлайн-режиме с использованием веб-браузера. Чтобы оптимизировать файл для отображения в вебе:

1. Откройте исходный документ в объекте [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1.
1.
1. Сохраните оптимизированный документ с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий фрагмент кода показывает, как оптимизировать PDF документ для веба.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// Оптимизировать для веба
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// Сохранить выходной документ
pdfDocument.Save(dataDir);
```

## Уменьшение размера PDF

Метод [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) позволяет уменьшить размер документа, удалив ненужную информацию.
[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) метод позволяет уменьшить размер документа, удаляя ненужную информацию.

- Ресурсы, которые не используются на страницах документа, удаляются
- Одинаковые ресурсы объединяются в один объект
- Неиспользуемые объекты удаляются

Ниже приведен пример. Однако следует отметить, что этот метод не может гарантировать уменьшение размера документа.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Открыть документ
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// Оптимизировать PDF документ. Однако следует отметить, что этот метод не может гарантировать уменьшение размера документа
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```

## Управление стратегией оптимизации

Мы также можем настраивать стратегию оптимизации.
Мы также можем настроить стратегию оптимизации.

### Уменьшение или сжатие всех изображений

У нас есть два способа работы с изображениями: уменьшить качество изображения и/или изменить их разрешение. В любом случае должны быть применены [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions). В следующем примере мы уменьшаем изображения, снижая [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) до 50.

`ImageQuality` работает аналогично качеству JPEG, где значение 0 является наименьшим, а значение 100 — наивысшим.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Открыть документ
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Инициализировать OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Установить опцию CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Установить опцию ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// Оптимизировать PDF документ с использованием OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```
Еще один способ - изменить размер изображений с более низким разрешением. В этом случае мы должны установить ResizeImages в значение true и MaxResolution в соответствующее значение.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Инициализация времени
var time = DateTime.Now.Ticks;
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Открыть документ
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// Инициализация OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Установка опции CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Установка опции ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Установка опции ResizeImage
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// Установка опции MaxResolution
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// Оптимизация PDF документа с использованием OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// Сохранение обновленного документа
pdfDocument.Save(dataDir);
```
Еще одна важная проблема - время выполнения. Но и эту настройку мы можем контролировать. В настоящее время мы можем использовать два алгоритма - Стандартный и Быстрый. Для контроля времени выполнения мы должны установить свойство [Version](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). Следующий фрагмент демонстрирует алгоритм Быстрый:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Инициализация времени
var time = DateTime.Now.Ticks;
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Открыть документ
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Инициализация OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Установить опцию CompressImages
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Установить опцию ImageQuality
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Установить версию сжатия изображений на быструю
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// Оптимизировать PDF документ используя OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```
### Удаление неиспользуемых объектов

Документ PDF иногда содержит объекты PDF, на которые не ссылаются другие объекты документа. Это может произойти, например, когда страница удаляется из дерева страниц документа, но сам объект страницы не удаляется. Удаление этих объектов не делает документ недействительным, а скорее уменьшает его размер.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Открыть документ
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Установить опцию RemoveUsedObject
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// Оптимизировать документ PDF с использованием OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```

### Удаление неиспользуемых потоков

Иногда документ содержит неиспользуемые потоки ресурсов.
Иногда документ содержит неиспользуемые потоки ресурсов.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Открытие документа
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Установка опции RemoveUsedStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// Оптимизация PDF документа с использованием OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Сохранение обновленного документа
pdfDocument.Save(dataDir);
```

### Связывание дублирующихся потоков

Некоторые документы могут содержать несколько идентичных потоков ресурсов (например, изображений).
Некоторые документы могут содержать несколько одинаковых потоков ресурсов (например, изображений).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Открыть документ
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Установить опцию LinkDuplcateStreams
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplcateStreams = true
};
// Оптимизировать PDF документ с использованием OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```

Кроме того, мы можем использовать настройки [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).
Кроме того, мы можем использовать настройки [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Открыть документ
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Установить опцию AllowReusePageContent
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("Начало");
// Оптимизировать PDF документ с использованием OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Сохранить обновленный документ
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Завершено");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Размер исходного файла: {0}. Размер уменьшенного файла: {1}", fi1.Length, fi2.Length);
```
### Извлечение шрифтов

Если документ использует встроенные шрифты, это означает, что все данные о шрифтах хранятся в документе. Преимущество заключается в том, что документ можно просматривать независимо от того, установлен ли шрифт на машине пользователя или нет. Но встраивание шрифтов увеличивает размер документа. Метод извлечения шрифтов удаляет все встроенные шрифты. Таким образом, размер документа уменьшается, но сам документ может стать нечитаемым, если не установлен нужный шрифт.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Открыть документ
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Установить опцию UnembedFonts
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("Start");
// Оптимизировать PDF документ используя OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Сохранить обновленный документ
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Finished");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
```
Оптимизационные ресурсы применяют эти методы к документу. Если какой-либо из этих методов применяется, размер документа скорее всего уменьшится. Если ни один из методов не применяется, размер документа не изменится, что очевидно.

## Дополнительные способы уменьшения размера PDF-документа

### Удаление или сглаживание аннотаций

Аннотации можно удалить, когда они не нужны. Когда они нужны, но не требуют дополнительного редактирования, их можно сгладить. Обе эти техники помогут уменьшить размер файла.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Открыть документ
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Сглаживание аннотаций
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// Сохранить обновленный документ
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### Удаление полей формы

Если документ PDF содержит AcroForms, мы можем попытаться уменьшить размер файла, сделав поля форм плоскими.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Загрузка исходной PDF формы
Document doc = new Document(dataDir + "input.pdf");

// Сделать формы плоскими
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Сохранить обновленный документ
doc.Save(dataDir);
```

### Конвертация PDF из цветового пространства RGB в оттенки серого

Файл PDF включает Текст, Изображение, Вложение, Аннотации, Графики и другие объекты.
PDF-файл содержит текст, изображения, вложения, аннотации, графики и другие объекты.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Загрузка исходного PDF файла
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // Получение экземпляра конкретной страницы в PDF
        Page page = document.Pages[idxPage];
        // Конвертация изображений RGB в градации серого
        strategy.Convert(page);
    }
    // Сохранение результирующего файла
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### Компрессия FlateDecode

{{% alert color="primary" %}}

Эта функция поддерживается начиная с версии 18.12 или выше.

{{% /alert %}}

Aspose.PDF для .NET поддерживает компрессию FlateDecode для функциональности оптимизации PDF.
Aspose.PDF для .NET поддерживает компрессию FlateDecode для функциональности оптимизации PDF.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **Сохранение изображения в XImageCollection**

Aspose.PDF для .NET предоставляет возможность сохранять новые изображения в **XImageCollection** с компрессией FlateDecode. Для включения этой опции вы можете использовать флаг **ImageFilterType.Flate**. Следующий фрагмент кода показывает, как использовать эту функциональность:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

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

