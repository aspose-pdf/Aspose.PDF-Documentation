---
title: Работа с портфолио в PDF
linktitle: Портфолио
type: docs
weight: 40
url: /ru/net/portfolio/
description: Как создать PDF портфолио с помощью C#. Вы должны использовать файл Microsoft Excel, документ Word и файл изображения для создания PDF портфолио.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с портфолио в PDF",
    "alternativeHeadline": "Создание портфолио в документе PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, портфолио",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "Как создать PDF портфолио с помощью C#. Вы должны использовать файл Microsoft Excel, документ Word и файл изображения для создания PDF портфолио."
}
</script>
## Как создать портфолио PDF

Aspose.PDF позволяет создавать документы портфолио PDF с использованием класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Добавьте файл в объект Document.Collection после его получения с помощью класса [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Когда файлы будут добавлены, используйте метод Save класса Document для сохранения документа портфолио.

Следующий пример использует файл Microsoft Excel, документ Word и файл изображения для создания портфолио PDF.

Код ниже приводит к следующему портфолио.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

### Портфолио PDF, созданное с помощью Aspose.PDF

![Портфолио PDF, созданное с помощью Aspose.PDF для .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Создать объект Document
Document doc = new Document();

// Создать объект коллекции документов
doc.Collection = new Collection();

// Получить файлы для добавления в портфолио
FileSpecification excel = new FileSpecification( dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification( dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// Описать файлы
excel.Description = "Файл Excel";
word.Description = "Файл Word";
image.Description = "Файл изображения";

// Добавить файлы в коллекцию документов
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// Сохранить документ портфолио
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## Извлечение файлов из портфолио PDF

Портфолио PDF позволяет объединять содержимое из различных источников (например, PDF, Word, Excel, JPEG файлы) в один единый контейнер. Оригинальные файлы сохраняют свою индивидуальность, но собираются в файл портфолио PDF. Пользователи могут открывать, читать, редактировать и форматировать каждый компонентный файл независимо от других файлов компонентов.

Aspose.PDF позволяет создавать документы портфолио PDF с использованием класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Также предлагается возможность извлечения файлов из портфолио PDF.

Следующий фрагмент кода показывает вам шаги по извлечению файлов из портфолио PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Загрузка исходного PDF портфолио
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// Получение коллекции встроенных файлов
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// Итерация по отдельным файлам портфолио
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // Получение вложения и запись в файл или поток
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // Сохранение извлеченного файла в какое-либо место
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // Закрытие объекта потока
    fileStream.Close();
}
```
![Извлечь файлы из портфолио PDF](working-with-pdf-portfolio_2.jpg)

## Удаление файлов из портфолио PDF

Чтобы удалить файлы из портфолио PDF, используйте следующие строки кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Загрузка исходного портфолио PDF
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
```

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


