---
title: Извлечение информации об изображении и подписи
linktitle: Извлечение информации об изображении и подписи
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/extract-image-and-signature-information/
description: Вы можете извлечь изображения из поля подписи и информацию о подписи с помощью класса SignatureField на C#.
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Image and Signature Information",
    "alternativeHeadline": "Extract PDF signature images and certificate details",
    "abstract": "Новый функционал Aspose.PDF для .NET извлекает изображения и подробную информацию из полей подписи PDF. Используя C#, разработчики могут получить изображения подписей и данные сертификатов, включая открытый ключ, отпечаток и сведения о выдавшем, расширяя возможности работы с PDF. Это улучшает проверку и управление цифровыми подписями в приложениях",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract Image, SignatureField class, ExtractImage method, ExtractCertificate method, C#, Aspose.PDF for .NET, PDF Signature, digital signature, signature information",
    "wordcount": "834",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/extract-image-and-signature-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-signature-information/"
    },
    "dateModified": "2025-04-11",
    "description": "Вы можете извлекать изображения из поля подписи и извлекать информацию о подписи, используя класс SignatureField с C#."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Извлечение изображения из поля подписи

Aspose.PDF for .NET поддерживает возможность цифровой подписи PDF файлов с использованием класса [SignatureField](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/signaturefield), и при подписании документа вы также можете установить изображение для `SignatureAppearance`. Теперь этот API также предоставляет возможность извлекать информацию о подписи, а также изображение, связанное с полем подписи.

Чтобы извлечь информацию о подписи, мы представили метод [ExtractImage](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/signaturefield/methods/extractimage) в классе SignatureField. Пожалуйста, посмотрите следующий фрагмент кода, который демонстрирует шаги для извлечения изображения из объекта `SignatureField`:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractingImage.pdf"))
    {
        // Searching for signature fields
        foreach (var field in document.Form)
        {
            var sf = field as Aspose.Pdf.Forms.SignatureField;
            if (sf == null)
            {
                continue;
            }

            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    continue;
                }

                using (System.Drawing.Image image = System.Drawing.Bitmap.FromStream(imageStream))
                {
                    // Save the image
                    image.Save(dataDir + "output_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
                }
            }
        }
    }
}
```

## Извлечение информации о подписи

Aspose.PDF for .NET поддерживает возможность цифровой подписи PDF файлов с использованием класса SignatureField. В настоящее время мы также можем определить действительность сертификата, но не можем извлечь весь сертификат. Информация, которую можно извлечь, включает открытый ключ, отпечаток, выпускателя и т.д.

Чтобы извлечь информацию о подписи, мы представили метод [ExtractCertificate](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) в классе [SignatureField](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/signaturefield). Пожалуйста, посмотрите следующий фрагмент кода, который демонстрирует шаги для извлечения сертификата из объекта SignatureField:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractCertificate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractSignatureInfo.pdf"))
    {
        // Searching for signature fields
        foreach (var field in document.Form)
        {
            var sf = field as Aspose.Pdf.Forms.SignatureField;
            if (sf == null)
            {
                continue;
            }
            // Extract certificate
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream == null)
            {
                continue;
            }
            // Save certificate
            using (cerStream)
            {
                byte[] bytes = new byte[cerStream.Length];
                using (FileStream fs = new FileStream(dataDir + "input.cer", FileMode.CreateNew))
                {
                    cerStream.Read(bytes, 0, bytes.Length);
                    fs.Write(bytes, 0, bytes.Length);
                }
            }
        }
    }
}
```

Вы можете получить информацию о алгоритмах подписи документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void GetSignaturesInfo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = signature.GetSignatureNames();
            var signaturesInfoList =  signature.GetSignaturesInfo();
            foreach (var sigInfo in signaturesInfoList)
            {
                Console.WriteLine(sigInfo.DigestHashAlgorithm);
                Console.WriteLine(sigInfo.AlgorithmType);
                Console.WriteLine(sigInfo.CryptographicStandard);
                Console.WriteLine(sigInfo.SignatureName);
            }
        }
    }
}
```

Пример вывода для приведенного выше примера:
```
Sha256
Rsa
Pkcs7
Signature1
```

## Проверка подписей на компрометацию

Вы можете использовать класс **SignaturesCompromiseDetector** для проверки цифровых подписей на компрометацию. Вызовите метод **Check()**, чтобы проверить подписи документа. Если компрометация подписей не обнаружена, метод вернет true. Если метод возвращает false, вы можете проверить, есть ли компрометированные подписи, используя свойство **HasCompromisedSignatures**, и получить список компрометированных подписей через свойство **CompromisedSignatures**.

Чтобы проверить, охватывают ли существующие подписи весь документ, используйте свойство **SignaturesCoverage**. Это свойство может иметь следующие значения:
- **Неопределено** – если одна из подписей явно скомпрометирована или проверка покрытия не удалась.
- **Полностью подписано** – если подписи охватывают весь документ.
- **Частично подписано** – если подписи не охватывают весь документ и есть неподписанный контент.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Check(string pdfFile)
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(pdfFile))
    {   
        // Create the compromise detector instance
        var detector = new Aspose.Pdf.SignaturesCompromiseDetector(document);
        CompromiseCheckResult result;
    
        // Check for compromise
        if (detector.Check(out result))
        {
            Console.WriteLine("No signature compromise detected");
            return;
        }
         
        // Get information about compromised signatures
        if (result.HasCompromisedSignatures)
        {
            Console.WriteLine($"Count of compromised signatures: {result.CompromisedSignatures.Count}");
            foreach (var signatureName in result.CompromisedSignatures)
            {
                Console.WriteLine($"Signature name: {signatureName.FullName}");
            }
        }
         
        // Get info about signatures coverage
        Console.WriteLine(result.SignaturesCoverage);   
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Check(string pdfFile)
{
    // Open PDF document
    using var document = new Aspose.Pdf.Document(pdfFile);
    // Create the compromise detector instance
    var detector = new Aspose.Pdf.SignaturesCompromiseDetector(document);

    // Check for compromise
    if (detector.Check(out var result))
    {
        Console.WriteLine("No signature compromise detected");
        return;
    }
         
    // Get information about compromised signatures
    if (result.HasCompromisedSignatures)
    {
        Console.WriteLine($"Count of compromised signatures: {result.CompromisedSignatures.Count}");
        foreach (var signatureName in result.CompromisedSignatures)
        {
            Console.WriteLine($"Signature name: {signatureName.FullName}");
        }
    }
         
    // Get info about signatures coverage
    Console.WriteLine(result.SignaturesCoverage);
}
```
{{< /tab >}}
{{< /tabs >}}

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