---
title: Импорт и экспорт аннотаций в формате XFDF
linktitle: Импорт и экспорт аннотаций в формате XFDF
type: docs
weight: 40
url: /ru/net/import-export-xfdf/
description: Вы можете импортировать и экспортировать аннотации в формате XFDF с использованием C# и библиотеки Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Импорт и экспорт аннотаций в формате XFDF",
    "alternativeHeadline": "Методы импорта и экспорта данных аннотаций в файлы XFDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, импорт экспорт в XFDF",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Вы можете импортировать и экспортировать аннотации в формате XFDF с использованием C# и библиотеки Aspose.PDF для .NET."
}
</script>
{{% alert color="primary" %}}

XFDF означает XML Forms Data Format. Это формат файла на основе XML. Этот формат файла используется для представления данных формы или аннотаций, содержащихся в форме PDF. XFDF может использоваться для различных целей, но в нашем случае он может использоваться либо для отправки, либо для получения данных формы или аннотаций на другие компьютеры или серверы и т. д., либо для архивации данных формы или аннотаций. В этой статье мы увидим, как Aspose.Pdf.Facades учел эту концепцию и как мы можем импортировать и экспортировать данные аннотаций в файл XFDF.

{{% /alert %}}

**Aspose.PDF для .NET** является функционально насыщенным компонентом, когда речь идет о редактировании документов PDF. Как мы знаем, XFDF является важным аспектом манипулирования формами PDF, пространство имен Aspose.Pdf.Facades в Aspose.PDF для .NET очень хорошо это учло и предоставило методы для импорта и экспорта данных аннотаций в файлы XFDF.

Класс [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) содержит два метода для работы с импортом и экспортом аннотаций в файл XFDF.
Класс [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) содержит два метода для работы с импортом и экспортом аннотаций в файл XFDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий фрагмент кода показывает, как экспортировать аннотации в файл XFDF:

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // Путь к каталогу документов.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// Импорт аннотаций из файла XFDF
        /// Файл XML Forms Data Format (XFDF), созданный приложением Adobe Acrobat для авторства PDF;
        /// содержит описания элементов форм страницы и их значений, таких как имена и значения текстовых полей;
        /// используется для сохранения данных формы, которые могут быть импортированы в документ PDF.
        /// Вы можете импортировать данные аннотации из файла XFDF в PDF, используя
        /// метод ImportAnnotationsFromXfdf в классе PdfAnnotationEditor.
        /// </summary>       

        public static void ExportAnnotationXFDF()
        {
            // Создаем объект PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // Привязываем PDF документ к редактору аннотаций
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));

            // Экспортируем аннотации
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
Следующий фрагмент кода описывает, как импортировать аннотации в файл XFDF:

```csharp
public static void ImportAnnotationXFDF()
{
    // Создать объект PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Создать новый PDF документ
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Импортировать аннотацию
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Сохранить выходной PDF
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Еще один способ экспорта/импорта аннотаций одновременно

В приведенном ниже коде метод ImportAnnotations позволяет импортировать аннотации непосредственно из другого PDF документа.

```csharp
        /// <summary>
        /// Метод ImportAnnotations позволяет импортировать аннотации непосредственно из другого PDF документа
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // Создать объект PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // Создать новый PDF документ
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // Редактор аннотаций позволяет импортировать аннотации из нескольких PDF документов,
            // но в этом примере мы используем только один.
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // Сохранить выходной PDF
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
        }
    }
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
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
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

