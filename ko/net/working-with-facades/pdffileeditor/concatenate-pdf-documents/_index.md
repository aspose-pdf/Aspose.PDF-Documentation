---
title: C#에서 PDF 문서 연결하기
linktitle: PDF 문서 연결하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/concatenate-pdf-documents/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 문서를 연결하는 방법을 설명합니다.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Concatenate PDF documents in C#",
    "alternativeHeadline": "Effortlessly Merge PDF Files in C#",
    "abstract": "Aspose.PDF for .NET의 기능은 개발자가 C#에서 PdfFileEditor 클래스를 사용하여 여러 PDF 문서를 효율적으로 연결할 수 있도록 합니다. 이 기능은 파일 경로와 MemoryStreams를 통해 파일을 병합하고, PDF 양식에서 고유한 필드 이름을 생성하며, 최종 문서 내에서 목차를 생성하는 것을 지원하여 문서 관리 및 통합을 위한 간소화된 솔루션을 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1615",
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
    "url": "/net/concatenate-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/concatenate-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## **개요**

이 문서에서는 C#을 사용하여 서로 다른 PDF 파일을 단일 PDF로 병합, 결합 또는 연결하는 방법을 설명합니다. 다음과 같은 주제를 다룹니다.

- [C# PDF 파일 병합하기](#concatenate-pdf-files-using-file-paths)
- [C# PDF 파일 결합하기](#concatenate-pdf-files-using-file-paths)
- [C# 여러 PDF 파일을 하나의 PDF로 병합하기](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 여러 PDF 파일을 하나의 PDF로 결합하기](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 폴더 내 모든 PDF 파일 병합하기](#concatenating-all-pdf-files-in-particular-folder)
- [C# 폴더 내 모든 PDF 파일 결합하기](#concatenating-all-pdf-files-in-particular-folder)
- [C# 파일 경로를 사용하여 PDF 파일 병합하기](#concatenate-pdf-files-using-file-paths)
- [C# 스트림을 사용하여 PDF 파일 결합하기](#concatenate-array-of-pdf-files-using-streams)
- [C# 폴더 내 모든 PDF 파일 연결하기](#concatenate-pdf-files-in-folder)

## 파일 경로를 사용하여 PDF 파일 연결하기

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)는 여러 PDF 파일을 연결할 수 있는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 클래스입니다. 파일 스트림을 사용하여 파일을 연결할 수 있을 뿐만 아니라 메모리 스트림을 사용하여도 가능합니다. 이 문서에서는 메모리 스트림을 사용하여 파일을 연결하는 과정을 설명하고 코드 스니펫을 통해 보여줍니다.

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드를 사용하여 두 개의 PDF 파일을 연결할 수 있습니다. [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드는 세 개의 매개변수를 전달할 수 있습니다: 첫 번째 입력 PDF, 두 번째 입력 PDF 및 출력 PDF. 최종 출력 PDF에는 두 개의 입력 PDF 파일이 포함됩니다.

다음 C# 코드 스니펫은 파일 경로를 사용하여 PDF 파일을 연결하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Concatenate files
    pdfEditor.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths2.pdf", dataDir + "ConcatenateUsingPath_out.pdf");
}
```

일부 경우, 많은 개요가 있을 때 사용자는 CopyOutlines를 false로 설정하여 이를 비활성화하고 연결 성능을 향상시킬 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pfe = new Aspose.Pdf.Facades.PdfFileEditor();
    // Setting CopyOutlines to false
    pfe.CopyOutlines = false;
    // Concatenate files
    pfe.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled2.pdf", dataDir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf");
}
```

## 메모리 스트림을 사용하여 여러 PDF 파일 연결하기

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드는 소스 PDF 파일과 대상 PDF 파일을 매개변수로 사용합니다. 이 매개변수는 디스크의 PDF 파일 경로일 수도 있고 메모리 스트림일 수도 있습니다. 이제 이 예제에서는 먼저 두 개의 파일 스트림을 생성하여 디스크에서 PDF 파일을 읽습니다. 그런 다음 이 파일들을 바이트 배열로 변환합니다. PDF 파일의 바이트 배열은 메모리 스트림으로 변환됩니다. PDF 파일에서 메모리 스트림을 얻은 후, 이를 concatenate 메서드에 전달하여 단일 출력 파일로 병합할 수 있습니다.

다음 C# 코드 스니펫은 메모리 스트림을 사용하여 여러 PDF 파일을 연결하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateMultiplePdfFilesUsingMemoryStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    string document1Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams1.pdf";
    string document2Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams2.pdf";
    string resultPdfPath = dataDir + "concatenated_out.pdf";
    
    // Create two file streams to read PDF files
    using (var fs1 = new FileStream(document1Path, FileMode.Open, FileAccess.Read))
    {
        using (var fs2 = new FileStream(document2Path, FileMode.Open, FileAccess.Read))
        {
            // Create byte arrays to keep the contents of PDF files
            var buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            var buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            var i = 0;
            // Read PDF file contents into byte arrays
            i = fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            i = fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            using (var pdfStream = new MemoryStream())
            {
                using (var fileStream1 = new MemoryStream(buffer1))
                {
                    using (var fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to output MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        var data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        using (var output = new FileStream(resultPdfPath, FileMode.Create, FileAccess.Write))
                        {
                            // Write byte array contents in the output file stream
                            output.Write(data, 0, data.Length);
                        }
                    }
                }
            }
        }
    }
}
```

## 파일 경로를 사용하여 PDF 파일 배열 연결하기

여러 PDF 파일을 연결하려면 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드의 오버로드를 사용할 수 있으며, 이를 통해 PDF 파일 배열을 전달할 수 있습니다. 최종 출력은 배열의 모든 파일로부터 생성된 병합 파일로 저장됩니다. 다음 C# 코드 스니펫은 파일 경로를 사용하여 PDF 파일 배열을 연결하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of files
    var filesArray = new string[2];
    filesArray[0] = dataDir + "Concatenate1.pdf";
    filesArray[1] = dataDir + "Concatenate2.pdf";
    // Concatenate files
    pdfEditor.Concatenate(filesArray, dataDir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf");
}
```

## 스트림을 사용하여 PDF 파일 배열 연결하기

PDF 파일 배열을 연결하는 것은 디스크에 있는 파일로만 제한되지 않습니다. 스트림에서 PDF 파일 배열을 연결할 수도 있습니다. 여러 PDF 파일을 연결하려면 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드의 적절한 오버로드를 사용할 수 있습니다. 먼저 입력 스트림의 배열과 출력 PDF를 위한 하나의 스트림을 생성한 후 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드를 호출합니다. 출력은 출력 스트림에 저장됩니다. 다음 C# 코드 스니펫은 스트림을 사용하여 PDF 파일 배열을 연결하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    var document1Path = dataDir + "Concatenate1.pdf";
    var document2Path = dataDir + "Concatenate2.pdf";
    var resultPdfPath = dataDir + "ConcatenateArrayOfPdfUsingStreams_out.pdf";

    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Output stream
    using (var outputStream = new FileStream(resultPdfPath, FileMode.Create))
    {
        using (var stream1 = new FileStream(document1Path, FileMode.Open))
        {
            using (var stream2 = new FileStream(document2Path, FileMode.Open))
            {
                // Array of streams
                var inputStreams = new Stream[2];
                inputStreams[0] = stream1;
                inputStreams[1] = stream2;
                // Concatenate file
                pdfEditor.Concatenate(inputStreams, outputStream);
            }   
        }
    }
}
```

## 특정 폴더 내 모든 PDF 파일 연결하기

특정 폴더 내의 모든 PDF 파일을 런타임에 읽고 파일 이름을 알지 못한 채로 연결할 수도 있습니다. 연결하고자 하는 PDF 문서가 포함된 디렉토리의 경로를 제공하기만 하면 됩니다.

다음 C# 코드 스니펫을 사용하여 이 기능을 구현해 보십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatingAllPdfFilesInParticularFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    var fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    var resultPdfPath = dataDir + "ConcatenatingAllPdfFilesInParticularFolder_out.pdf";
    // Instantiate PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, resultPdfPath);
}
```

## PDF 양식 연결 및 필드 이름 고유하게 유지하기

[Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스는 PDF 파일을 연결할 수 있는 기능을 제공합니다. 이제 연결할 PDF 파일에 유사한 필드 이름을 가진 양식 필드가 있는 경우, Aspose.PDF는 결과 PDF 파일에서 필드를 고유하게 유지하는 기능을 제공하며, 필드 이름을 고유하게 만들기 위해 접미사를 지정할 수도 있습니다. [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)의 [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) 속성을 true로 설정하면 PDF 양식이 연결될 때 필드 이름이 고유하게 됩니다. 또한, [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) 속성을 사용하여 양식이 연결될 때 필드 이름을 고유하게 만들기 위해 추가되는 접미사의 사용자 정의 형식을 지정할 수 있습니다. 이 문자열은 결과 파일의 숫자로 대체될 `%NUM%` 하위 문자열을 포함해야 합니다.

다음 간단한 코드 스니펫을 참조하여 이 기능을 구현하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFormsAndKeepFieldsUnique()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique1.pdf";
    var inputFile2 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique2.pdf";
    var outFile = dataDir + "ConcatenatePDFForms_out.pdf";
    // Open PDF documents
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // To keep unique field Id for all the fields 
    fileEditor.KeepFieldsUnique = true;
    // Format of the suffix which is added to field name to make it unique when forms are concatenated.
    fileEditor.UniqueSuffix = "_%NUM%";
    // Concatenate the files into a resultant Pdf file
    fileEditor.Concatenate(inputFile1, inputFile2, outFile);
}
```

## PDF 파일 연결 및 목차 생성하기

## PDF 파일 연결하기

PDF 파일을 병합하는 방법에 대한 정보는 다음 코드 스니펫을 참조하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenateInput1.pdf";
    var inputFile2 = dataDir + "ConcatenateInput2.pdf";
    var outFile = dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf";
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    // Open PDF documents
    using (var outputStream = new FileStream(outFile, FileMode.Create))
    {
        using (var stream1 = new FileStream(inputFile1, FileMode.Open))
        {
            using (var stream2 = new FileStream(inputFile2, FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(stream1, stream2, outputStream);
            }
        }
    }
}
```

### 빈 페이지 삽입하기

PDF 파일이 병합된 후, 문서의 시작 부분에 빈 페이지를 삽입하여 목차를 생성할 수 있습니다. 이 요구 사항을 충족하기 위해 병합된 파일을 **Document** 객체에 로드하고 Page.Insert(...) 메서드를 호출하여 빈 페이지를 삽입해야 합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertBlankPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Insert a blank page at the beginning of concatenated file to display Table of Contents
    using (var document = new Aspose.Pdf.Document(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"))
    {
        // Insert a blank page in a PDF
        document.Pages.Insert(1);
    }
}
```

### 텍스트 스탬프 추가하기

목차를 생성하기 위해 첫 페이지에 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp) 객체를 사용하여 텍스트 스탬프를 추가해야 합니다. Stamp 클래스는 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)를 추가하기 위한 `BindLogo(...)` 메서드를 제공하며, `SetOrigin(..)` 메서드를 사용하여 이러한 텍스트 스탬프를 추가할 위치를 지정할 수 있습니다. 이 문서에서는 두 개의 PDF 파일을 연결하고 있으므로, 각 개별 문서를 가리키는 두 개의 텍스트 스탬프 객체를 생성해야 합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampForTableOfContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    var inputPdfFile = Path.Combine(dataDir, "ConcatenateInput1.pdf");
    // Set Text Stamp to display string Table Of Contents
    var stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent, Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(inputPdfFile).GetPageWidth(1) / 3, 700);
    // Set particular pages
    stamp.Pages = new[] { 1 };
}
```

### 로컬 링크 생성하기

이제 연결된 파일 내의 페이지로의 링크를 추가해야 합니다. 이 요구 사항을 충족하기 위해 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 `CreateLocalLink(..)` 메서드를 사용할 수 있습니다. 다음 코드 스니펫에서는 링크 주위의 사각형이 보이지 않도록 4번째 인수로 Transparent를 전달했습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLocalLinks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Now we need to add Heading for Table Of Contents and links for documents
    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
    // Bind PDF document
    contentEditor.BindPdf(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf");
    // Create link for first document
    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
}
```

### 전체 코드

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CompleteCode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create a MemoryStream object to hold the resultant PDf file
    using (var concatenatedStream = new MemoryStream())
    {
        using (var fs1 = new FileStream(dataDir + "ConcatenateInput1.pdf", FileMode.Open))
        {
            using (var fs2 = new FileStream(dataDir + "ConcatenateInput2.pdf", FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(fs1, fs2, concatenatedStream);
            }
        }

        using (var concatenatedPdfDocument = new Aspose.Pdf.Document(concatenatedStream))
        {
            // Insert a blank page at the beginning of concatenated file to display Table of Contents
            concatenatedPdfDocument.Pages.Insert(1);

            // Hold the result file with empty page added
            using (var documentWithBlankPage = new MemoryStream())
            {
                // Save PDF document
                concatenatedPdfDocument.Save(documentWithBlankPage);

                using (var documentWithTocHeading = new MemoryStream())
                {
                    // Add Table Of Contents logo as stamp to PDF file
                    var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp();
                    // Bind PDF document
                    fileStamp.BindPdf(documentWithBlankPage);

                    // Set Text Stamp to display string Table Of Contents
                    var stamp = new Aspose.Pdf.Facades.Stamp();
                    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(documentWithBlankPage).GetPageWidth(1) / 3, 700);
                    // Set particular pages
                    stamp.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(stamp);

                    // Create stamp text for first item in Table Of Contents
                    var document1Link = new Aspose.Pdf.Facades.Stamp();
                    document1Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("1 - Link to Document 1", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document1Link.SetOrigin(150, 650);
                    // Set particular pages on which stamp should be displayed
                    document1Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document1Link);

                    // Create stamp text for second item in Table Of Contents
                    var document2Link = new Aspose.Pdf.Facades.Stamp();
                    document2Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("2 - Link to Document 2", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document2Link.SetOrigin(150, 620);
                    // Set particular pages on which stamp should be displayed
                    document2Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document2Link);

                    // Save PDF document
                    fileStamp.Save(documentWithTocHeading);
                    fileStamp.Close();

                    // Now we need to add Heading for Table Of Contents and links for documents
                    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
                    // Bind PDF document
                    contentEditor.BindPdf(documentWithTocHeading);
                    // Create link for first document
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
                    // Create link for Second document
                    // We have used   new PdfFileInfo("d:/pdftest/Input1.pdf").NumberOfPages + 2   as PdfFileInfo.NumberOfPages(..) returns the page count for first document
                    // And 2 is because, second document will start at Input1+1 and 1 for the page containing Table Of Contents.
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 620, 100, 20),
                        new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "ConcatenateInput1.pdf").NumberOfPages + 2, 1, System.Drawing.Color.Transparent);
                    // Save PDF document
                    contentEditor.Save(dataDir + "Concatenated_Table_Of_Contents_out.pdf");
                }
            }
        }
    }
}
```

## 폴더 내 PDF 파일 연결하기

[Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스는 PDF 파일을 연결할 수 있는 기능을 제공합니다. 특정 폴더 내의 모든 PDF 파일을 런타임에 읽고 파일 이름을 알지 못한 채로 연결할 수도 있습니다. 연결하고자 하는 PDF 문서가 포함된 디렉토리의 경로를 제공하기만 하면 됩니다.

다음 C# 코드 스니펫을 사용하여 Aspose.PDF에서 이 기능을 구현해 보십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesInFolder()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, dataDir + "ConcatenatePdfFilesInFolder_out.pdf");
}
```