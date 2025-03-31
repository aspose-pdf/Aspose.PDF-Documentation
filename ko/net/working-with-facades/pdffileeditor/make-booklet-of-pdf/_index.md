---
title: PDF 북릿 만들기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ko/net/make-booklet-of-pdf/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF로 PDF 북릿을 만드는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make Booklet of PDF",
    "alternativeHeadline": "Create Booklets from PDFs with Enhanced Flexibility",
    "abstract": "Aspose.PDF의 PDF 북릿 만들기 기능은 사용자가 PdfFileEditor 클래스를 사용하여 PDF 파일에서 쉽게 북릿을 만들 수 있도록 합니다. 이 기능은 파일 경로와 스트림을 모두 지원하여 페이지 크기를 사용자 정의하고 출력 제어를 향상시키기 위해 왼쪽 및 오른쪽 페이지를 지정할 수 있습니다. 이 강력한 도구는 북릿 제작 프로세스를 간소화하여 PDF 조작을 위한 필수 리소스가 됩니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "946",
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
    "url": "/net/make-booklet-of-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-booklet-of-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 파일 경로를 사용하여 PDF 북릿 만들기

[MakeBooklet](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스를 사용하여 입력 PDF 파일의 북릿을 만들고 출력 PDF 파일로 저장할 수 있습니다. 이 오버로드는 파일 경로를 사용하여 북릿을 만들 수 있게 해줍니다. 다음 코드 스니펫은 파일 경로를 사용하여 북릿을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
}
```

## 페이지 크기 및 파일 경로를 사용하여 PDF 북릿 만들기

[MakeBooklet](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스를 사용하여 입력 PDF 파일의 북릿을 만들고 출력 PDF 파일로 저장할 수 있습니다. 이 오버로드는 파일 경로를 사용하여 북릿을 만들 수 있게 해줍니다. 또한 이 오버로드를 사용하여 출력 PDF 파일의 페이지 크기를 설정할 수 있습니다. 다음 코드 스니펫은 페이지 크기와 파일 경로를 사용하여 북릿을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPageSizeAndPaths_out.pdf", PageSize.A5);
}
```

## 페이지 크기, 지정된 왼쪽 및 오른쪽 페이지, 파일 경로를 사용하여 PDF 북릿 만들기

[MakeBooklet](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스를 사용하여 입력 PDF 파일의 북릿을 만들고 출력 PDF 파일로 저장할 수 있습니다. 이 오버로드는 파일 경로를 사용하여 북릿을 만들 수 있게 해줍니다. 또한 이 오버로드를 사용하여 출력 PDF 파일의 페이지 크기를 설정하고 왼쪽 및 오른쪽 측면에 대한 특정 페이지를 지정할 수 있습니다. 다음 코드 스니펫은 페이지 크기, 지정된 왼쪽 및 오른쪽 페이지 및 파일 경로를 사용하여 북릿을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", PageSize.A5, leftPages, rightPages);
}
```

## 지정된 왼쪽 및 오른쪽 페이지, 파일 경로를 사용하여 PDF 북릿 만들기

[MakeBooklet](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스를 사용하여 입력 PDF 파일의 북릿을 만들고 출력 PDF 파일로 저장할 수 있습니다. 이 오버로드는 파일 경로를 사용하여 북릿을 만들 수 있게 해줍니다. 또한 이 오버로드를 사용하여 출력 PDF 파일의 왼쪽 및 오른쪽 측면에 대한 특정 페이지를 지정할 수 있습니다. 다음 코드 스니펫은 지정된 왼쪽 및 오른쪽 페이지와 파일 경로를 사용하여 북릿을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", leftPages, rightPages);
}
```

## 스트림을 사용하여 PDF 북릿 만들기

[MakeBooklet](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스를 사용하여 입력 PDF 스트림의 북릿을 만들고 출력 PDF 스트림으로 저장할 수 있습니다. 이 오버로드는 파일 경로 대신 스트림을 사용하여 북릿을 만들 수 있게 해줍니다. 다음 코드 스니펫은 스트림을 사용하여 북릿을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream);
        }
    }
}
```

## 페이지 크기 및 스트림을 사용하여 PDF 북릿 만들기

[MakeBooklet](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스를 사용하여 입력 PDF 스트림의 북릿을 만들고 출력 PDF 스트림으로 저장할 수 있습니다. 이 오버로드는 파일 경로 대신 스트림을 사용하여 북릿을 만들 수 있게 해줍니다. 또한 이 오버로드를 사용하여 출력 PDF 스트림의 페이지 크기를 설정할 수 있습니다. 다음 코드 스니펫은 페이지 크기와 스트림을 사용하여 북릿을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5);
        }
    }
}
```

## 페이지 크기, 지정된 왼쪽 및 오른쪽 페이지, 스트림을 사용하여 PDF 북릿 만들기

[MakeBooklet](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스를 사용하여 입력 PDF 스트림의 북릿을 만들고 출력 PDF 스트림으로 저장할 수 있습니다. 이 오버로드는 파일 경로 대신 스트림을 사용하여 북릿을 만들 수 있게 해줍니다. 또한 이 오버로드를 사용하여 출력 PDF 파일의 페이지 크기를 설정하고 왼쪽 및 오른쪽 측면에 대한 특정 페이지를 지정할 수 있습니다. 다음 코드 스니펫은 페이지 크기, 지정된 왼쪽 및 오른쪽 페이지 및 스트림을 사용하여 북릿을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5, leftPages, rightPages);
        }
    }
}
```

## 지정된 왼쪽 및 오른쪽 페이지, 스트림을 사용하여 PDF 북릿 만들기

[MakeBooklet](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스를 사용하여 입력 PDF 스트림의 북릿을 만들고 출력 PDF 스트림으로 저장할 수 있습니다. 이 오버로드는 파일 경로 대신 스트림을 사용하여 북릿을 만들 수 있게 해줍니다. 또한 이 오버로드를 사용하여 출력 PDF 스트림의 왼쪽 및 오른쪽 측면에 대한 특정 페이지를 지정할 수 있습니다. 다음 코드 스니펫은 지정된 왼쪽 및 오른쪽 페이지와 스트림을 사용하여 북릿을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, leftPages, rightPages);
        }
    }
}
```