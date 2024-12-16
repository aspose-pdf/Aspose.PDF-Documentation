---
title: Извлечение информации о изображении и подписи
linktitle: Извлечение информации о изображении и подписи
type: docs
weight: 30
url: /ru/net/extract-image-and-signature-information/
description: Вы можете извлекать изображения из поля подписи и извлекать информацию о подписи, используя класс SignatureField с C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Извлечение информации о изображении и подписи",
    "alternativeHeadline": "Как извлечь изображение и подпись из PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, извлечение подписи",
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
    "url": "/net/extract-image-and-signature-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-signature-information/"
    },
    "dateModified": "2022-02-04",
    "description": "Вы можете извлекать изображения из поля подписи и извлекать информацию о подписи, используя класс SignatureField с C#."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Извлечение изображения из поля подписи

Aspose.PDF для .NET поддерживает функцию цифровой подписи PDF-файлов с использованием класса [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) и при подписании документа вы также можете установить изображение для SignatureAppearance. Теперь этот API также предоставляет возможность извлекать информацию о подписи, а также изображение, связанное с полем подписи.

Для извлечения информации о подписи мы ввели метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage) в класс SignatureField. Пожалуйста, ознакомьтесь со следующим фрагментом кода, который демонстрирует шаги по извлечению изображения из объекта SignatureField:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir+ @"ExtractingImage.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            string outFile = dataDir+ @"output_out.jpg";
            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    using (System.Drawing.Image image = Bitmap.FromStream(imageStream))
                    {
                        image.Save(outFile, System.Drawing.Imaging.ImageFormat.Jpeg);
                    }
                }
            }
        }
    }
}
```
### Замена изображения подписи

Иногда может возникнуть необходимость заменить только изображение уже существующего поля подписи в файле PDF. Для выполнения этой задачи сначала нам нужно искать поля формы в файле PDF, определять поля подписи, получать размеры (прямоугольные размеры) поля подписи, а затем штамповать изображение на тех же размерах.

## Извлечение информации о подписи

Aspose.PDF для .NET поддерживает функцию цифровой подписи файлов PDF с использованием класса SignatureField. В настоящее время мы также можем определять действительность сертификата, но мы не можем извлечь весь сертификат. Информация, которую можно извлечь, включает в себя открытый ключ, отпечаток пальца, издателя и т.д.

Для извлечения информации о подписи мы ввели метод [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) в класс [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield).
Для извлечения информации о подписи был введен метод [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) в класс [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir + "ExtractSignatureInfo.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream != null)
            {
                using (cerStream)
                {
                    byte[] bytes = new byte[cerStream.Length];
                    using (FileStream fs = new FileStream(dataDir + @"input.cer", FileMode.CreateNew))
                    {
                        cerStream.Read(bytes, 0, bytes.Length);
                        fs.Write(bytes, 0, bytes.Length);
                    }
                }
            }
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

