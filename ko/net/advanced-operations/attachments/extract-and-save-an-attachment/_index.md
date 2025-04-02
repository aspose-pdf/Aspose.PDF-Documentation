---
title: 첨부 파일 추출 및 저장
linktitle: 첨부 파일 추출 및 저장
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/extract-and-save-an-attachment/
description: Aspose.PDF for .NET은 PDF 문서에서 모든 첨부 파일을 가져올 수 있게 해줍니다. 또한, 문서에서 개별 첨부 파일을 가져올 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract and Save an Attachment",
    "alternativeHeadline": "Extract Attachments from PDF Documents with Ease",
    "abstract": "Aspose.PDF for .NET은 사용자가 PDF 문서에서 첨부 파일을 원활하게 추출하고 저장할 수 있는 강력한 기능을 소개합니다. 이 기능은 모든 내장 파일 또는 특정 첨부 파일을 검색할 수 있게 하여 PDF 파일을 다루는 개발자의 문서 관리 및 접근성을 향상시킵니다. 이 혁신적인 도구를 사용하여 첨부 파일을 손쉽게 처리하여 PDF 워크플로를 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract attachments, save attachments, Aspose.PDF for .NET, PDF document, individual attachment, embedded files collection, FileSpecification object, PDF manipulation, document instance, get all attachments",
    "wordcount": "1149",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2025-04-02",
    "description": "Aspose.PDF for .NET은 PDF 문서에서 모든 첨부 파일을 가져올 수 있게 해줍니다. 또한, 문서에서 개별 첨부 파일을 가져올 수 있습니다."
}
</script>

## 모든 첨부 파일 가져오기

Aspose.PDF를 사용하면 PDF 문서에서 모든 첨부 파일을 가져올 수 있습니다. 이는 PDF와 별도로 문서를 저장하려는 경우나 PDF에서 첨부 파일을 제거해야 할 때 유용합니다.

PDF 파일에서 모든 첨부 파일을 가져오려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션을 반복합니다. [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션에는 모든 첨부 파일이 포함되어 있습니다. 이 컬렉션의 각 요소는 [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 객체를 나타냅니다. [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션을 통해 foreach 루프의 각 반복은 [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 객체를 반환합니다.
1. 객체가 준비되면 첨부된 파일의 속성 또는 파일 자체를 검색합니다.

다음 코드 조각은 PDF 문서에서 모든 첨부 파일을 가져오는 방법을 보여줍니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        // Get embedded files collection
        Aspose.Pdf.EmbeddedFileCollection embeddedFiles = document.EmbeddedFiles;

        // Get count of the embedded files
        Console.WriteLine("Total files : {0}", embeddedFiles.Count);

        int count = 1;

        // Loop through the collection to get all the attachments
        foreach (Aspose.Pdf.FileSpecification fileSpecification in embeddedFiles)
        {
            Console.WriteLine("Name: {0}", fileSpecification.Name);
            Console.WriteLine("Description: {0}",
            fileSpecification.Description);
            Console.WriteLine("Mime Type: {0}", fileSpecification.MIMEType);

            // Check if parameter object contains the parameters
            if (fileSpecification.Params != null)
            {
                Console.WriteLine("CheckSum: {0}",
                fileSpecification.Params.CheckSum);
                Console.WriteLine("Creation Date: {0}",
                fileSpecification.Params.CreationDate);
                Console.WriteLine("Modification Date: {0}",
                fileSpecification.Params.ModDate);
                Console.WriteLine("Size: {0}", fileSpecification.Params.Size);
            }

            // Get the attachment and write to file or stream
            var fileContent = new byte[fileSpecification.Contents.Length];
            fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
            using (var fileStream = new FileStream(dataDir + count + "_out" + ".txt", FileMode.Create))
            {
                fileStream.Write(fileContent, 0, fileContent.Length);
            }
            count += 1;
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf");

    // Get embedded files collection
    Aspose.Pdf.EmbeddedFileCollection embeddedFiles = document.EmbeddedFiles;

    // Get count of the embedded files
    Console.WriteLine("Total files : {0}", embeddedFiles.Count);

    int count = 1;

    // Loop through the collection to get all the attachments
    foreach (Aspose.Pdf.FileSpecification fileSpecification in embeddedFiles)
    {
        Console.WriteLine("Name: {0}", fileSpecification.Name);
        Console.WriteLine("Description: {0}",
        fileSpecification.Description);
        Console.WriteLine("Mime Type: {0}", fileSpecification.MIMEType);

        // Check if parameter object contains the parameters
        if (fileSpecification.Params != null)
        {
            Console.WriteLine("CheckSum: {0}",
            fileSpecification.Params.CheckSum);
            Console.WriteLine("Creation Date: {0}",
            fileSpecification.Params.CreationDate);
            Console.WriteLine("Modification Date: {0}",
            fileSpecification.Params.ModDate);
            Console.WriteLine("Size: {0}", fileSpecification.Params.Size);
        }

        // Get the attachment and write to file or stream
        var fileContent = new byte[fileSpecification.Contents.Length];
        fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
        using var fileStream = new FileStream(dataDir + count + "_out" + ".txt", FileMode.Create);
        fileStream.Write(fileContent, 0, fileContent.Length);

        count += 1;
    }
}
```
{{< /tab >}}
{{< /tabs >}}


## 개별 첨부 파일 가져오기

개별 첨부 파일을 가져오려면 Document 인스턴스의 `EmbeddedFiles` 객체에서 첨부 파일의 인덱스를 지정할 수 있습니다. 다음 코드 조각을 사용해 보세요.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetIndividualAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetIndividualAttachment.pdf"))
    {
        // Get particular embedded file
        Aspose.Pdf.FileSpecification fileSpecification = document.EmbeddedFiles[1];

        // Get the file properties
        Console.WriteLine("Name: {0}", fileSpecification.Name);
        Console.WriteLine("Description: {0}", fileSpecification.Description);
        Console.WriteLine("Mime Type: {0}", fileSpecification.MIMEType);

        // Check if parameter object contains the parameters
        if (fileSpecification.Params != null)
        {
            Console.WriteLine("CheckSum: {0}",
            fileSpecification.Params.CheckSum);
            Console.WriteLine("Creation Date: {0}",
            fileSpecification.Params.CreationDate);
            Console.WriteLine("Modification Date: {0}",
            fileSpecification.Params.ModDate);
            Console.WriteLine("Size: {0}", fileSpecification.Params.Size);
        }

        // Get the attachment and write to file or stream
        var fileContent = new byte[fileSpecification.Contents.Length];
        fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

        using (var fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create))
        {
            fileStream.Write(fileContent, 0, fileContent.Length);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetIndividualAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetIndividualAttachment.pdf");

    // Get particular embedded file
    Aspose.Pdf.FileSpecification fileSpecification = document.EmbeddedFiles[1];

    // Get the file properties
    Console.WriteLine("Name: {0}", fileSpecification.Name);
    Console.WriteLine("Description: {0}", fileSpecification.Description);
    Console.WriteLine("Mime Type: {0}", fileSpecification.MIMEType);

    // Check if parameter object contains the parameters
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("CheckSum: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("Creation Date: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("Modification Date: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("Size: {0}", fileSpecification.Params.Size);
    }

    // Get the attachment and write to file or stream
    var fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

    using var fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
}
```
{{< /tab >}}
{{< /tabs >}}


## FileAttachmentAnnotation 객체에 포함된 첨부 파일 가져오기

Document 객체의 EmbeddedFiles 컬렉션 외에도, 첨부 파일은 FileAttachmentAnnotation 객체에도 포함될 수 있습니다. 아래는 이러한 첨부 파일의 수와 세부 정보를 보는 코드입니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ViewAttachmentsInFileAttachmentAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        for (int i = 1; i <= document.Pages.Count; i++)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[i].Annotations)
            {
                var fileAttachmentAnnotation = annotation as Aspose.Pdf.Annotations.FileAttachmentAnnotation;
                if (fileAttachmentAnnotation != null)
                {
                    Aspose.Pdf.FileSpecification file = fileAttachmentAnnotation.File;
                    if (file != null && file.Name != null)
                    {
                        Console.WriteLine($"Name: {file.Name} on page {i}");
                    }
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ViewAttachmentsInFileAttachmentAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf");

    for (int i = 1; i <= document.Pages.Count; i++)
    {
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[i].Annotations)
        {
            var fileAttachmentAnnotation = annotation as Aspose.Pdf.Annotations.FileAttachmentAnnotation;
            if (fileAttachmentAnnotation != null)
            {
                Aspose.Pdf.FileSpecification file = fileAttachmentAnnotation.File;
                if (file != null && file.Name != null)
                {
                    Console.WriteLine($"Name: {file.Name} on page {i}");
                }
            }
        }
    }
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