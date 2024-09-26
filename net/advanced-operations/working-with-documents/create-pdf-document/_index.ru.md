---
title: Как создать PDF с помощью C#
linktitle: Создать PDF документ
type: docs
weight: 10
url: /net/create-pdf-document/
description: Создайте и отформатируйте PDF документ с помощью Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Как создать PDF с помощью C#",
    "alternativeHeadline": "Создать PDF документ с нуля",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, dotnet, создать PDF документ",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Создайте и отформатируйте PDF документ с помощью Aspose.PDF для .NET."
}
</script>
Мы всегда ищем способы создавать PDF-документы и работать с ними в проектах на C# более точно, аккуратно и эффективно. Наличие простых в использовании функций из библиотеки позволяет нам сосредоточиться больше на работе, а меньше на трудоемких деталях создания PDF, будь то в .NET.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Создание (или генерация) PDF документа на языке C#

API Aspose.PDF для .NET позволяет создавать и читать PDF-файлы с использованием C# и VB.NET. API может использоваться в различных приложениях .NET, включая WinForms, ASP.NET и многие другие. В этой статье мы покажем, как использовать API Aspose.PDF для .NET для легкого создания и чтения PDF-файлов в приложениях .NET.

### Как создать простой PDF файл

Для создания PDF файла на C# можно использовать следующие шаги.

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) в коллекцию [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) страницы
1. Сохраните результатирующий PDF документ

```csharp
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Инициализация объекта документа
Document document = new Document();
// Добавление страницы
Page page = document.Pages.Add();
// Добавление текста на новую страницу
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// Сохранение обновленного PDF
document.Save(dataDir + "HelloWorld_out.pdf");
```

### Как создать поисковый PDF документ

Aspose.PDF для .NET предоставляет возможность создавать и модифицировать существующие PDF документы.
Aspose.PDF для .NET предоставляет возможность создавать и манипулировать существующими PDF-документами.

Нижеуказанная логика позволяет распознавать текст в изображениях PDF. Для распознавания вы можете использовать внешнюю поддержку OCR, соответствующую стандарту HOCR. Для тестирования мы использовали бесплатный OCR Google tesseract. Поэтому первым делом вам нужно установить Tesseract-OCR на вашу систему, и у вас будет консольное приложение tesseract.

Ниже приведен полный код для выполнения этой задачи:

```csharp

using System;

namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments
{
    class ExampleCreateDocument
    {
        private const string _dataDir = "C:\\Samples";
        public static void CreateSearchableDocuments(string file)
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document(file);
            bool convertResult = false;
            try
            {
                convertResult = doc.Convert(CallBackGetHocr);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            doc.Save(file);
            doc.Dispose();
        }

        static string CallBackGetHocr(System.Drawing.Image img)
        {
            string tmpFile = System.IO.Path.GetTempFileName();
            try
            {
                System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(img);

                bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
                string inputFile = string.Concat('"', tmpFile, '"');
                string outputFile = string.Concat('"', tmpFile, '"');
                string arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
                string tesseractProcessName = @"C:\Program Files\Tesseract-OCR\Tesseract.exe";

                System.Diagnostics.ProcessStartInfo psi =
                    new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
                    {
                        UseShellExecute = true,
                        CreateNoWindow = true,
                        WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                        WorkingDirectory = System.IO.Path.GetDirectoryName(tesseractProcessName)
                    };

                System.Diagnostics.Process p = new System.Diagnostics.Process
                {
                    StartInfo = psi
                };
                p.Start();
                p.WaitForExit();

                System.IO.StreamReader streamReader = new System.IO.StreamReader(tmpFile + ".hocr");
                string text = streamReader.ReadToEnd();
                streamReader.Close();

                return text;
            }
            finally
            {
                if (System.IO.File.Exists(tmpFile))
                    System.IO.File.Delete(tmpFile);
                if (System.IO.File.Exists(tmpFile + ".hocr"))
                    System.IO.File.Delete(tmpFile + ".hocr");
            }
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Организация",
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
                "@type": "Контактная точка",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "Контактная точка",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "Контактная точка",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Предложение",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "Совокупный рейтинг",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

