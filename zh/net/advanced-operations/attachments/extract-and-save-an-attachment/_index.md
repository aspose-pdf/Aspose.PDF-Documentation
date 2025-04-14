---
title: 提取并保存附件
linktitle: 提取并保存附件
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/extract-and-save-an-attachment/
description: Aspose.PDF for .NET 允许您从 PDF 文档中获取所有附件。此外，您还可以从文档中获取单个附件。
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
    "abstract": "Aspose.PDF for .NET 引入了一项强大的功能，使用户能够无缝提取和保存 PDF 文档中的附件。此功能允许检索所有嵌入文件或特定附件，增强了处理 PDF 文件的开发人员的文档管理和可访问性。通过轻松处理附件来优化您的 PDF 工作流程，使用这个创新工具",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract attachments, save attachments, Aspose.PDF for .NET, PDF document, individual attachment, embedded files collection, FileSpecification object, PDF manipulation, document instance, get all attachments",
    "wordcount": "1077",
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
    "description": "Aspose.PDF for .NET 允许您从 PDF 文档中获取所有附件。此外，您还可以从文档中获取单个附件。"
}
</script>

## 获取所有附件

使用 Aspose.PDF，可以从 PDF 文档中获取所有附件。这在您想要将文档单独保存到 PDF 中，或者需要从 PDF 中删除附件时非常有用。

要从 PDF 文件中获取所有附件：

1. 遍历 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象的 [EmbeddedFiles](https://reference.aspose.com/pdf/zh/net/aspose.pdf/embeddedfilecollection) 集合。 [EmbeddedFiles](https://reference.aspose.com/pdf/zh/net/aspose.pdf/embeddedfilecollection) 集合包含所有附件。此集合的每个元素代表一个 [FileSpecification](https://reference.aspose.com/pdf/zh/net/aspose.pdf/filespecification) 对象。通过 [EmbeddedFiles](https://reference.aspose.com/pdf/zh/net/aspose.pdf/embeddedfilecollection) 集合的 foreach 循环的每次迭代返回一个 [FileSpecification](https://reference.aspose.com/pdf/zh/net/aspose.pdf/filespecification) 对象。
1. 一旦对象可用，检索附加文件的所有属性或文件本身。

以下代码片段展示了如何从 PDF 文档中获取所有附件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

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


## 获取单个附件

为了获取单个附件，我们可以指定 Document 实例的 `EmbeddedFiles` 对象中的附件索引。请尝试使用以下代码片段。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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


## 获取包含在 FileAttachmentAnnotation 对象中的附件

除了 Document 对象的 EmbeddedFiles 集合外，附件还可以包含在 FileAttachmentAnnotation 对象中。以下是查看此类附件的数量和详细信息的代码。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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