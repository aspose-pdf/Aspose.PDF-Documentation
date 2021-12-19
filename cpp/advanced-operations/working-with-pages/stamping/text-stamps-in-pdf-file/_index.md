---
title: Add Text stamps in PDF File
linktitle: Text stamps in PDF File
type: docs
weight: 20
url: /cpp/text-stamps-in-the-pdf-file/
description: Add a text stamp to a PDF file using the TextStamp class with C++.
lastmod: "2021-12-95"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Text Stamp with C++

You can use [TextStamp](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) class to add a text stamp in a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text stamp, you need to create a Document object and a TextStamp object using required properties. After that, you can call AddStamp method of the Page to add the stamp in the PDF. The following code snippet shows you how to add text stamp in the PDF file.

```cpp
void AddTextStampToPDFFile() {
   
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    
    // Create text stamp
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // Set whether stamp is background
    textStamp->set_Background(true);
    // Set origin
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // Rotate stamp
    textStamp->set_Rotate(Rotation::on90);

    // Set text properties
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // Add stamp to particular page
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // Save output document
    document->Save(_dataDir + outputFileName);
}
```

## Define alignment for TextStamp object

Adding watermarks to PDF documents is one of the frequent demanded features and Aspose.PDF for C++ is fully capable of adding Image as well as Text watermarks. We have a class named [TextStamp](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) which provides the feature to add text stamps over the PDF file. Recently there has been a requirement to support the feature to specify the alignment of text when using TextStamp object. So in order to fulfill this requirement, we have introduced TextAlignment property in TextStamp class. Using this property, we can specify the Horizontal text alignment.

The following code snippets shows an example on how to load an existing PDF document and add TextStamp over it.

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    
    // instantiate FormattedText object with sample string
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // add new text line to FormattedText
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // create TextStamp object using FormattedText
    auto stamp = MakeObject<TextStamp>(text);
    // specify the Horizontal Alignment of text stamp as Center aligned
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // specify the Vertical Alignment of text stamp as Center aligned
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // specify the Text Horizontal Alignment of TextStamp as Center aligned
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // set top margin for stamp object
    stamp->set_TopMargin(20);
    // add stamp to all pages of PDF file
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // save output document
    document->Save(_dataDir + outputFileName);
}
```

## Fill Stroke Text as Stamp in PDF File

We have implemented setting of rendering mode for text adding and editing scenarios. To render stroke text please create TextState object and set RenderingMode to TextRenderingMode.StrokeText and also select color for StrokingColor property. Later, bind TextState to the stamp using BindTextState() method.

Following code snippet demonstrates adding Fill Stroke Text:

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Create TextState object to transfer advanced properties
    auto ts = MakeObject<TextState>();

    // Set color for stroke
    ts->set_StrokingColor(Color::get_Gray());

    // Set text rendering mode
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // Load an input PDF document
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // Bind TextState
    stamp->BindTextState(ts);

    // Set X,Y origin
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // Add Stamp
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```
