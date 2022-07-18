---
title: Manipulate PDF Document 
linktitle: Manipulate PDF Document
type: docs
weight: 30
url: /cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: This section explains about validation PDF Document for PDF A Standard, how to work with TOC, how to set PDF expiry date, and how to determine the Progress of PDF file generation.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Validate PDF Document for PDF A Standard (A 1A and A 1B)

To validate a PDF document for PDF/A-1a or PDF/A-1b compatibility, use the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c) method. This method allows you to specify the name of the file in which the result is to be saved and the required validation type [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) enumeration : PDF_A_1A or PDF_A_1B.

{{% alert color="primary" %}}

The output XML format is custom Aspose format. The XML contains a collection of tags with the name Problem; each tag contains the details of a particular problem. The Problem tag’s ObjectID attribute represents the ID of the particular object this problem is related to. The Clause attribute represents a corresponding rule in the PDF specification.

{{% /alert %}}

The following code snippet shows you how to validate PDF document for PDF/A-1A.

```cpp
void ExampleValidate01() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validate PDF for PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

The following code snippet shows you how to validate PDF document for PDF/A-1B.

```cpp
void ExampleValidate02() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validate PDF for PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## Working with TOC

### Add TOC to Existing PDF

Aspose.PDF API allows you to add a table of content either when creating a PDF, or to an existing file.

To add a TOC to an existing PDF file, use the [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) class in the Aspose.Pdf namespace. The Aspose.Pdf namespace allows you to create new and manipulates existing PDF files. To add a TOC to an existing PDF, use the Aspose.Pdf namespace.

The following code snippet shows how to create a table of contents inside an existing PDF file.

```cpp
void ExampleToc01() {
    // String for path names.
    String _dataDir("C:\\Samples\\");

    // String for file names
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Get access to first page of PDF file
    auto tocPage = document->get_Pages()->Insert(1);

    // Create object to represent TOC information
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Set the title for TOC
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // Create string objects which will be used as TOC elements
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"First page", 0);
    titles->SetValue(u"Second page", 1);
    titles->SetValue(u"Third page", 2);
    titles->SetValue(u"Fourth page", 3);

    for (int i = 0; i < 2; i++)
    {
        // Create Heading object
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // Specify the destination page for heading object

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // Destination page
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // Destination coordinate
        segment2->set_Text(titles[i]);

        // Add heading to page containing TOC
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // Save the updated document
    document->Save(_dataDir + outputFileName);
}
```

### Set different TabLeaderType for different TOC Levels

Aspose.PDF for C++ also allows setting different TabLeaderType for different TOC levels. You need to set LineDash property of FormatArray with the appropriate value of TabLeaderType. Next, you may add the list section to the collection of the section of the Pdf document. After, create a section in the Pdf document and save the PDF file.

```cpp
void ExampleToc02() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    //set LeaderType
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // Create object to represent TOC information
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Set the title for TOC
    tocInfo->set_Title(title);

    //Add the list section to the sections collection of the Pdf document
    tocPage->set_TocInfo(tocInfo);

    //Define the format of the four levels list by setting the left margins
    //and
    //text format settings of each level

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    //Create a section in the Pdf document
    auto page = document->get_Pages()->Add();

    //Add four headings in the section
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Sample Heading" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    //Add the heading into Table Of Contents.
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // save the Pdf
    document->Save(_dataDir + outputFileName);
}
```

### Hide Page Numbers in TOC

If you want to hide page numbers along with titles in a table of contents, you can use the [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) property of [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) Class as false.

Please check following code snippet to hide page numbers in the table of contents:

```cpp
void ExampleToc03() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // Create object to represent TOC information
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Set the title for TOC
    tocInfo->set_Title(title);

    //Add the list section to the sections collection of the Pdf document  
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    //Define the format of the four levels list by setting the left margins and
    //text format settings of each level

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    //Add four headings in the section
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"this is heading of level " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // save the Pdf
    document->Save(_dataDir + outputFileName);
}
```

## How to set PDF expiry date

We apply access privileges on PDF files so that a certain group of users can access particular features/objects of PDF documents. In order to restrict the PDF file access, we usually apply encryption and we may have a requirement to set PDF file expiration, so that the user accessing/viewing the document gets a valid prompt regarding PDF file expiry.

In order to accomplish the above stated requirement, we can use [JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/) object. Please check the following code snippet.

```cpp
void SetPDFexpiryDate() {

    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name. 
    String outputFileName("SetExpiryDate_out.pdf");

    // Instantiate Document object
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF file
    document->get_Pages()->Add();

    // Add text fragment to paragraphs collection of page object
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // Create JavaScript object to set PDF expiry date
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // Set JavaScript as PDF open action
    document->set_OpenAction(javaScript);

    // Save PDF Document
    document->Save(_dataDir + outputFileName);
}
```

## Determine Progress of PDF File Generation

A customer asked us to add a feature that allows developers to determine the progress of PDF file generation. Here’s the response to that request.

The field [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) of [DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) class allows you to determine how PDF generation is going.

The code snippets below shows how to use [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb).

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Event type: {0}, Value: {1}, MaxValue: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Open document
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## Flatten Fillable PDF in C++

PDF documents often include forms with interactive fillable widgets such as radio buttons, checkboxes, text boxes, lists, etc. To make it uneditable for various application purposes, we need to flatten the PDF file.
Aspose.PDF for C++ provides the function to flatten your PDF in C++ with just few line of code:

```cpp
void FlattenFillablePDF() {
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Flatten Flatten Fillable PDF 
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // Save the updated document
    document->Save(_dataDir + outputFileName);
}
```
