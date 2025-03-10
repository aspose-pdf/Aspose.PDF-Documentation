---
title: Объединение PDF документов в C#
linktitle: Объединение PDF документов
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/concatenate-pdf-documents/
description: Этот раздел объясняет, как объединить PDF документы с помощью Aspose.PDF Facades, используя класс PdfFileEditor.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Concatenate PDF documents in C#",
    "alternativeHeadline": "Effortlessly Merge PDF Files in C#",
    "abstract": "Функциональность в Aspose.PDF for .NET позволяет разработчикам эффективно объединять несколько PDF документов, используя класс PdfFileEditor в C#. Эта функция поддерживает объединение файлов через пути к файлам и MemoryStreams, создание уникальных имен полей в PDF формах и даже генерацию оглавления в итоговом документе, предоставляя упрощенное решение для управления документами и интеграции.",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## **Обзор**

Эта статья объясняет, как объединить, комбинировать или конкатенировать различные PDF файлы в один PDF с использованием C#. Она охватывает такие темы, как:

- [C# Объединение PDF файлов](#concatenate-pdf-files-using-file-paths)
- [C# Комбинирование PDF файлов](#concatenate-pdf-files-using-file-paths)
- [C# Объединение нескольких PDF файлов в один PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Комбинирование нескольких PDF файлов в один PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Объединение всех PDF файлов в папке](#concatenating-all-pdf-files-in-particular-folder)
- [C# Комбинирование всех PDF файлов в папке](#concatenating-all-pdf-files-in-particular-folder)
- [C# Объединение PDF файлов с использованием путей к файлам](#concatenate-pdf-files-using-file-paths)
- [C# Комбинирование PDF файлов с использованием потоков](#concatenate-array-of-pdf-files-using-streams)
- [C# Конкатенация всех PDF файлов в папке](#concatenate-pdf-files-in-folder)

## Объединение PDF файлов с использованием путей к файлам

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) — это класс в [пространстве имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades), который позволяет вам объединять несколько PDF файлов. Вы можете объединять файлы не только с использованием FileStreams, но и с использованием MemoryStreams. В этой статье будет объяснен процесс объединения файлов с использованием MemoryStreams, а затем показан с помощью фрагмента кода.

Метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) может быть использован для объединения двух PDF файлов. Метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) позволяет передавать три параметра: первый входной PDF, второй входной PDF и выходной PDF. Итоговый выходной PDF содержит оба входных PDF файла.

Следующий фрагмент кода на C# показывает, как объединить PDF файлы с использованием путей к файлам.

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

В некоторых случаях, когда есть много оглавлений, пользователи могут отключить их, установив CopyOutlines в false, и улучшить производительность объединения.

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

## Объединение нескольких PDF файлов с использованием MemoryStreams

Метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) принимает исходные PDF файлы и целевой PDF файл в качестве параметров. Эти параметры могут быть либо путями к PDF файлам на диске, либо они могут быть MemoryStreams. Теперь, для этого примера, мы сначала создадим два файловых потока для чтения PDF файлов с диска. Затем мы преобразуем эти файлы в массивы байтов. Эти массивы байтов PDF файлов будут преобразованы в MemoryStreams. Как только мы получим MemoryStreams из PDF файлов, мы сможем передать их в метод объединения и объединить в один выходной файл.

Следующий фрагмент кода на C# показывает, как объединить несколько PDF файлов с использованием MemoryStreams:

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

## Объединение массива PDF файлов с использованием путей к файлам

Если вы хотите объединить несколько PDF файлов, вы можете использовать перегрузку метода [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index), которая позволяет передавать массив PDF файлов. Итоговый выход сохраняется как объединенный файл, созданный из всех файлов в массиве. Следующий фрагмент кода на C# показывает, как объединить массив PDF файлов с использованием путей к файлам.

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

## Объединение массива PDF файлов с использованием потоков

Объединение массива PDF файлов не ограничивается только файлами, находящимися на диске. Вы также можете объединить массив PDF файлов из потоков. Если вы хотите объединить несколько PDF файлов, вы можете использовать соответствующую перегрузку метода [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Сначала вам нужно создать массив входных потоков и один поток для выходного PDF, а затем вызвать метод [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Выход будет сохранен в выходном потоке. Следующий фрагмент кода на C# показывает, как объединить массив PDF файлов с использованием потоков.

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

## Объединение всех PDF файлов в определенной папке

Вы даже можете прочитать все PDF файлы в определенной папке во время выполнения и объединить их, даже не зная имена файлов. Просто укажите путь к директории, которая содержит PDF документы, которые вы хотите объединить.

Пожалуйста, попробуйте использовать следующий фрагмент кода на C#, чтобы достичь этой функциональности.

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

## Объединение PDF форм и сохранение уникальных имен полей

Класс [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) в [пространстве имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) предлагает возможность объединять PDF файлы. Теперь, если PDF файлы, которые нужно объединить, имеют поля формы с одинаковыми именами полей, Aspose.PDF предоставляет возможность сохранить поля в результирующем PDF файле уникальными, а также вы можете указать суффикс, чтобы сделать имена полей уникальными. Свойство [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) как true сделает имена полей уникальными, когда PDF формы объединяются. Также свойство [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) класса PdfFileEditor может быть использовано для указания пользовательского формата суффикса, который добавляется к имени поля, чтобы сделать его уникальным при объединении форм. Эта строка должна содержать подстроку `%NUM%`, которая будет заменена числами в результирующем файле.

Пожалуйста, посмотрите следующий простой фрагмент кода, чтобы достичь этой функциональности.

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

## Объединение PDF файлов и создание оглавления

## Объединение PDF файлов

Пожалуйста, ознакомьтесь со следующим фрагментом кода для информации о том, как объединить PDF файлы.

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

### Вставка пустой страницы

После того, как PDF файлы были объединены, мы можем вставить пустую страницу в начале документа, на которой мы можем создать оглавление. Для выполнения этого требования мы можем загрузить объединенный файл в объект **Document** и вызвать метод Page.Insert(...), чтобы вставить пустую страницу.

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

### Добавление текстовых штампов

Для создания оглавления нам нужно добавить текстовые штампы на первой странице, используя [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp) объекты. Класс Stamp предоставляет метод `BindLogo(...)` для добавления [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext), и мы также можем указать местоположение для добавления этих текстовых штампов, используя метод `SetOrigin(..)`. В этой статье мы объединяем два PDF файла, поэтому нам нужно создать два объекта текстового штампа, указывающих на эти отдельные документы.

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

### Создание локальных ссылок

Теперь нам нужно добавить ссылки на страницы внутри объединенного файла. Для выполнения этого требования мы можем использовать метод `CreateLocalLink(..)` класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). В следующем фрагменте кода мы передали Transparent в качестве 4-го аргумента, чтобы прямоугольник вокруг ссылки не был виден.

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

### Полный код

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

## Объединение PDF файлов в папке

Класс [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) в пространстве имен Aspose.Pdf.Facades предлагает вам возможность объединять PDF файлы. Вы даже можете прочитать все PDF файлы в определенной папке во время выполнения и объединить их, даже не зная имена файлов. Просто укажите путь к директории, которая содержит PDF документы, которые вы хотите объединить.

Пожалуйста, попробуйте использовать следующий фрагмент кода на C#, чтобы достичь этой функциональности от Aspose.PDF:

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