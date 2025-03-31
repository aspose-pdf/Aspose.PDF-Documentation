---
title: PDF에서 썸네일 이미지 생성
linktitle: 썸네일 이미지 생성
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /ko/net/generate-thumbnail-images-from-pdf-documents/
description: 이 섹션에서는 PDF 문서에서 썸네일 이미지를 생성하는 방법을 설명합니다.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "이 새로운 기능은 사용자가 PDF 문서에서 직접 효율적으로 썸네일 이미지를 생성할 수 있도록 합니다. 이 기능은 PDF 페이지를 쉽게 공유할 수 있는 이미지 형식으로 변환하여 문서 관리를 향상시키고, 개발자와 사용자 모두의 워크플로를 간소화합니다. 다양한 이미지 형식을 지원하여 이 기능은 Adobe Acrobat과 같은 외부 소프트웨어 없이 PDF 콘텐츠를 시각화하는 과정을 단순화합니다.",
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
    "description": "이 섹션에서는 PDF 문서에서 썸네일 이미지를 생성하는 방법을 설명합니다."
}
</script>

{{% alert color="primary" %}}

Adobe Acrobat SDK는 Acrobat 기술과 상호 작용하는 소프트웨어를 개발하는 데 도움이 되는 도구 세트입니다. SDK에는 헤더 파일, 타입 라이브러리, 간단한 유틸리티, 샘플 코드 및 문서가 포함되어 있습니다.

Acrobat SDK를 사용하면 여러 가지 방법으로 Acrobat 및 Adobe Reader와 통합된 소프트웨어를 개발할 수 있습니다:

- **JavaScript** — Acrobat 또는 Adobe Reader의 기능을 확장하기 위해 개별 PDF 문서 또는 외부에서 스크립트를 작성합니다.
- **플러그인** — Acrobat 또는 Adobe Reader의 기능을 동적으로 연결하고 확장하는 플러그인을 생성합니다.
- **애플리케이션 간 통신** — Acrobat 기능을 제어하기 위해 애플리케이션 간 통신(IAC)을 사용하는 별도의 애플리케이션 프로세스를 작성합니다. DDE 및 OLE는 Microsoft® Windows®에서 지원되며, Mac OS®에서는 Apple 이벤트/AppleScript가 지원됩니다. UNIX®에서는 IAC를 사용할 수 없습니다.

Aspose.PDF for .NET는 Adobe Acrobat Automation에 대한 의존성을 없애는 많은 동일한 기능을 제공합니다. 이 문서에서는 먼저 Acrobat SDK를 사용하고 그 다음 Aspose.PDF를 사용하여 PDF 문서에서 썸네일 이미지를 생성하는 방법을 보여줍니다.

{{% /alert %}}

## Acrobat 애플리케이션 간 통신 API를 사용한 애플리케이션 개발

Acrobat API는 Acrobat 애플리케이션 간 통신(IAC) 객체를 사용하는 두 개의 뚜렷한 레이어로 구성되어 있다고 생각할 수 있습니다:

- Acrobat 애플리케이션(AV) 레이어. AV 레이어는 문서가 어떻게 표시되는지를 제어할 수 있게 해줍니다. 예를 들어, 문서 객체의 뷰는 Acrobat과 연결된 레이어에 존재합니다.
- 휴대용 문서(PD) 레이어. PD 레이어는 페이지와 같은 문서 내의 정보에 접근할 수 있게 해줍니다. PD 레이어에서 PDF 문서의 기본 조작을 수행할 수 있으며, 페이지를 삭제, 이동 또는 교체하거나 주석 속성을 변경할 수 있습니다. 또한 PDF 페이지를 인쇄하고, 텍스트를 선택하고, 조작된 텍스트에 접근하며, 썸네일을 생성하거나 삭제할 수 있습니다.

우리의 의도는 PDF 페이지를 썸네일 이미지로 변환하는 것이므로 IAC에 더 집중하고 있습니다. IAC API에는 PDDoc, PDPage, PDAnnot 등과 같은 객체가 포함되어 있어 사용자가 휴대용 문서(PD) 레이어를 다룰 수 있게 해줍니다. 다음 코드 샘플은 폴더를 스캔하고 PDF 페이지를 썸네일 이미지로 변환합니다. Acrobat SDK를 사용하면 PDF 메타데이터를 읽고 문서의 페이지 수를 가져올 수도 있습니다.

### Acrobat 접근법

각 문서에 대한 썸네일 이미지를 생성하기 위해 Adobe Acrobat 7.0 SDK와 Microsoft .NET 2.0 Framework를 사용했습니다.

[Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/)는 Adobe Acrobat의 전체 버전과 결합되어 COM 객체 라이브러리를 노출합니다(안타깝게도 무료 Adobe Reader는 COM 인터페이스를 노출하지 않습니다). 이러한 COM 객체를 COM Interop을 통해 사용하여 PDF 문서를 로드하고 첫 페이지를 가져와 클립보드에 렌더링합니다. 그런 다음 .NET Framework를 사용하여 이를 비트맵으로 복사하고 이미지를 스케일링 및 결합하여 결과를 GIF 또는 PNG 파일로 저장합니다.

Adobe Acrobat이 설치되면 regedit.exe를 사용하여 HKEY_CLASSES_ROOT에서 AcroExch.PDDoc이라는 항목을 찾습니다.

**AcroExch.PDDoc 항목을 보여주는 레지스트리**

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

## Aspose.PDF for .NET 접근법

Aspose.PDF for .NET는 PDF 문서를 다루는 데 광범위한 지원을 제공합니다. 또한 PDF 문서의 페이지를 다양한 이미지 형식으로 변환하는 기능을 지원합니다. 위에서 설명한 기능은 Aspose.PDF for .NET를 사용하여 쉽게 달성할 수 있습니다.

Aspose.PDF는 뚜렷한 이점이 있습니다:

- PDF 파일을 작업하기 위해 시스템에 Adobe Acrobat을 설치할 필요가 없습니다.
- Aspose.PDF for .NET는 Acrobat Automation에 비해 간단하고 이해하기 쉽습니다.

PDF 페이지를 JPEG로 변환해야 하는 경우, [Aspose.PDF.Devices](https://reference.aspose.com/pdf/ko/net/aspose.pdf.devices) 네임스페이스는 PDF 페이지를 JPEG 이미지로 렌더링하기 위한 [JpegDevice](https://reference.aspose.com/pdf/ko/net/aspose.pdf.devices/jpegdevice)라는 클래스를 제공합니다. 다음 코드 스니펫을 살펴보세요.

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

- PDF 문서에서 썸네일 이미지를 생성해 주신 CodeProject에 감사드립니다. [Generate Thumbnail Image from PDF document](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Acrobat SDK 참조를 제공해 주신 Acrobat에 감사드립니다. [Acrobat SDK reference](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

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