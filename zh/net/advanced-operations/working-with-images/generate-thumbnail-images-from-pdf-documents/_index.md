---
title: 从PDF生成缩略图
linktitle: 生成缩略图
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /zh/net/generate-thumbnail-images-from-pdf-documents/
description: 本节描述如何从PDF文档生成缩略图
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "此新功能允许用户直接从PDF文档高效生成缩略图。此功能通过将PDF页面转换为易于共享的图像格式，增强了文档管理，简化了开发人员和用户的工作流程。支持多种图像格式，此功能简化了可视化PDF内容的过程，无需使用Adobe Acrobat等外部软件。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Generate Thumbnail Images, PDF documents, Aspose.PDF for .NET, Acrobat SDK, image formats, PDF Manipulation Library, JavaScript, interapplication communication, thumbnail images, JPEG conversion",
    "wordcount": "767",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "本节描述如何从PDF文档生成缩略图"
}
</script>

{{% alert color="primary" %}}

Adobe Acrobat SDK是一组工具，帮助您开发与Acrobat技术交互的软件。SDK包含头文件、类型库、简单实用程序、示例代码和文档。

使用Acrobat SDK，您可以以多种方式开发与Acrobat和Adobe Reader集成的软件：

- **JavaScript** — 编写脚本，无论是在单个PDF文档中还是外部，以扩展Acrobat或Adobe Reader的功能。
- **插件** — 创建动态链接的插件，扩展Acrobat或Adobe Reader的功能。
- **应用程序间通信** — 编写一个单独的应用程序进程，使用应用程序间通信（IAC）控制Acrobat功能。DDE和OLE在Microsoft® Windows®上受支持，而Mac OS®上支持Apple事件/AppleScript。IAC在UNIX®上不可用。

Aspose.PDF for .NET提供了许多相同的功能，使您不再依赖Adobe Acrobat自动化。本文展示了如何使用Acrobat SDK和Aspose.PDF从PDF文档生成缩略图。

{{% /alert %}}

## 使用Acrobat应用程序间通信API开发应用程序

将Acrobat API视为具有两个不同层次的对象，使用Acrobat应用程序间通信（IAC）对象：

- Acrobat应用程序（AV）层。AV层允许您控制文档的查看方式。例如，文档对象的视图位于与Acrobat相关联的层中。
- 可移植文档（PD）层。PD层提供对文档内信息的访问，例如页面。从PD层，您可以执行PDF文档的基本操作，例如删除、移动或替换页面，以及更改注释属性。您还可以打印PDF页面、选择文本、访问操作过的文本，并创建或删除缩略图。

由于我们的目的是将PDF页面转换为缩略图，因此我们更关注IAC。IAC API包含诸如PDDoc、PDPage、PDAnnot等对象，使用户能够处理可移植文档（PD）层。以下代码示例扫描一个文件夹并将PDF页面转换为缩略图。使用Acrobat SDK，我们还可以读取PDF元数据并检索文档中的页面数量。

### Acrobat方法

为了为每个文档生成缩略图，我们使用了Adobe Acrobat 7.0 SDK和Microsoft .NET 2.0框架。

[Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/)结合完整版本的Adobe Acrobat，公开了一个COM对象库（可惜免费的Adobe Reader不公开COM接口），可用于操作和访问PDF信息。通过COM Interop使用这些COM对象，加载PDF文档，获取第一页并将该页面渲染到剪贴板。然后，使用.NET框架，将其复制到位图，缩放并合并图像，并将结果保存为GIF或PNG文件。

安装Adobe Acrobat后，使用regedit.exe并在HKEY_CLASSES_ROOT下查找名为AcroExch.PDDoc的条目。

**注册表显示AcroExch.PDDDoc条目**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // Acrobat objects
    Acrobat.CAcroPDDoc pdfDoc;
    Acrobat.CAcroPDPage pdfPage;
    Acrobat.CAcroRect pdfRect;
    Acrobat.CAcroPoint pdfPoint;

    AppSettingsReader appSettings = new AppSettingsReader();
    string pdfInputPath = appSettings.GetValue("pdfInputPath", typeof(string)).ToString();
    string pngOutputPath = appSettings.GetValue("pngOutputPath", typeof(string)).ToString();
    string templatePortraitFile = Application.StartupPath + @"\pdftemplate_portrait.gif";
    string templateLandscapeFile = Application.StartupPath + @"\pdftemplate_landscape.gif";

    // Get list of files to process from the input path
    string[] files = Directory.GetFiles(pdfInputPath, "*.pdf");

    for (int n = 0; n < files.Length; n++)
    {
        string inputFile = files[n];
        string outputFile = Path.Combine(pngOutputPath, Path.GetFileNameWithoutExtension(inputFile) + ".png");

        // Create PDF document
        pdfDoc = (Acrobat.CAcroPDDoc)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.PDDoc", "");

        if (pdfDoc.Open(inputFile) == 0)
        {
            throw new FileNotFoundException($"Unable to open PDF file: {inputFile}");
        }

        int pageCount = pdfDoc.GetNumPages();
        pdfPage = (Acrobat.CAcroPDPage)pdfDoc.AcquirePage(0);
        pdfPoint = (Acrobat.CAcroPoint)pdfPage.GetSize();

        pdfRect = (Acrobat.CAcroRect)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.Rect", "");
        pdfRect.Left = 0;
        pdfRect.right = pdfPoint.x;
        pdfRect.Top = 0;
        pdfRect.bottom = pdfPoint.y;

        pdfPage.CopyToClipboard(pdfRect, 0, 0, 100);
        IDataObject clipboardData = Clipboard.GetDataObject();

        if (clipboardData.GetDataPresent(DataFormats.Bitmap))
        {
            Bitmap pdfBitmap = (Bitmap)clipboardData.GetData(DataFormats.Bitmap);

            int thumbnailWidth = 45;
            int thumbnailHeight = 59;
            string templateFile = pdfPoint.x < pdfPoint.y ? templatePortraitFile : templateLandscapeFile;

            if (pdfPoint.x > pdfPoint.y)
            {
                // Swap width and height for landscape orientation
                (thumbnailWidth, thumbnailHeight) = (thumbnailHeight, thumbnailWidth);
            }

            Bitmap templateBitmap = new Bitmap(templateFile);
            Image pdfImage = pdfBitmap.GetThumbnailImage(thumbnailWidth, thumbnailHeight, null, IntPtr.Zero);

            Bitmap thumbnailBitmap = new Bitmap(thumbnailWidth + 7, thumbnailHeight + 7, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

            templateBitmap.MakeTransparent();

            using (Graphics thumbnailGraphics = Graphics.FromImage(thumbnailBitmap))
            {
                thumbnailGraphics.DrawImage(pdfImage, 2, 2, thumbnailWidth, thumbnailHeight);
                thumbnailGraphics.DrawImage(templateBitmap, 0, 0);
                thumbnailBitmap.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
            }

            Console.WriteLine("Generated thumbnail: {0}", outputFile);

            pdfDoc.Close();
            Marshal.ReleaseComObject(pdfPage);
            Marshal.ReleaseComObject(pdfRect);
            Marshal.ReleaseComObject(pdfDoc);
        }
    }
}
```

## Aspose.PDF for .NET方法

Aspose.PDF for .NET提供了广泛支持以处理PDF文档。它还支持将PDF文档的页面转换为多种图像格式的能力。上述功能可以轻松地使用Aspose.PDF for .NET实现。

Aspose.PDF具有明显的优势：

- 您不需要在系统上安装Adobe Acrobat即可处理PDF文件。
- 使用Aspose.PDF for .NET相较于Acrobat自动化更简单易懂。

如果我们需要将PDF页面转换为JPEG，[Aspose.PDF.Devices](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices)命名空间提供了一个名为[JpegDevice](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/jpegdevice)的类，用于将PDF页面渲染为JPEG图像。请查看以下代码片段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Retrieve names of all the PDF files in a particular directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

    // Iterate through all the files entries in array
    for (int counter = 0; counter < fileEntries.Length; counter++)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(fileEntries[counter]))
        {
            for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
            {
                using (FileStream imageStream = new FileStream(dataDir + @"\Thumbanils" + counter.ToString() + "_" + pageCount + ".jpg", FileMode.Create))
                {
                    var resolution = new Aspose.Pdf.Devices.Resolution(300);
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(45, 59, resolution, 100);
                    // Convert a particular page and save the image to stream
                    jpegDevice.Process(document.Pages[pageCount], imageStream);
                }
            }
        }
    }
}
```

{{% alert color="primary" %}}

- 感谢CodeProject提供的[从PDF文档生成缩略图](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents)。
- 感谢Acrobat提供的[Acrobat SDK参考](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html)。

{{% /alert %}}

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