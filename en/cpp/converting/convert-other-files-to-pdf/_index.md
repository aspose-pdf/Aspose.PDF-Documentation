---
title: Convert other file formats to PDF
linktitle: Convert other file formats to PDF
type: docs
weight: 80
url: /cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Learn how to convert a variety of file formats, including Word and Excel, into PDF format using Aspose.PDF in C++.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Convert EPUB to PDF

**Aspose.PDF for C++** allows you simply convert EPUB files to PDF format.

<abbr title="electronic publication">EPUB</abbr> (short for electronic publication) is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub. EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device.

EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.The version EPUB 3 is also endorsed by the Book Industry Study Group (BISG), a leading book trade association for standardized best practices, research, information and events, for packaging of content.

Conversion steps:

1. Create a [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. Create an instance of [EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)class.
1. Create an instance of [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class with mention source filename and options.
1. Load and [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) the input file.

Next following code snippet show you how to convert EPUB files to PDF format with C++.

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```

{{% alert color="success" %}}
**Try to convert EPUB to PDF online**

Aspose.PDF for C++ presents you online free application ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Convert Text to PDF

**Aspose.PDF for C++** support the feature converting plain text and pre-formatted text file to PDF format.

Converting text to PDF means adding text fragments to the PDF page. As for text files, we are dealing with 2 types of text: pre-formatting (for example, 25 lines with 80 characters per line) and non-formatted text (plain text). Depending on our needs, we can control this addition ourselves or entrust it to the library's algorithms.

### Convert plain text file to PDF

In case of the plain text file, we can use the following technique:

1. Create a [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. Read the source text file using [TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)
1. Instantiate [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) Object.
1. Add a [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) to pages collection of document.
1. Create a new object of TextFragment and pass TextReader object to its constructor.
1. Add a new text paragraph in paragraphs collection and pass the TextFragment object.
1. Load and [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) the input file.

```cpp
void ConvertTextToPDF()
{
    std::clog << "Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // Read the source text file
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // Instantiate a Document object by calling its empty constructor
    auto document = MakeObject<Document>();

    // Add a new page in Pages collection of Document
    auto page = document->get_Pages()->Add();

    // Create an instance of TextFragmet and pass the text from reader object to its constructor as argument
    auto text = MakeObject<TextFragment>(content);

    // Add a new text paragraph in paragraphs collection and pass the TextFragment object
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Save resultant PDF file
    document->Save(_dataDir + outfilename);
    std::clog << "Text to PDF convert: End" << std::endl;
}
```

### Convert pre-formatted text file to PDF

Converting pre-formatted text is like plain text but you need to make some additional actions such as setting margins, font type and size. Obviously that font should be monospace (for example Courier New).

Follow these steps to convert pre-formatted text to PDF with C++:

1. Instantiate a Document object by calling its empty constructor.
1. Set left and right margins for better presentation.
1. Instantiate [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object and add a new page in Pages collection.
1. Load and [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) the input image file.

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Performatted Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // Read the text file as array of string
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // Instantiate a Document object by calling its empty constructor
    auto document = MakeObject<Document>();

    // Add a new page in Pages collection of Document
    auto page = document->get_Pages()->Add();

    // Set left and right margins for better presentation
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // check if line contains "form feed" character
        // see https://en.wikipedia.org/wiki/Page_break
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // Set left and right margins for better presentation
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // Create an instance of TextFragment and
        // pass the line to its constructor as argument
        auto text = MakeObject<TextFragment>(line);

        // Add a new text paragraph in paragraphs collection and pass the TextFragment object
        page->get_Paragraphs()->Add(text);
        }
    }

    // Save resultant PDF file
    document->Save(_dataDir + outfilename);
    std::clog << "Performatted Text to PDF convert: End" << std::endl;
}
```

{{% alert color="success" %}}
**Try to convert TEXT to PDF online**

Aspose.PDF for C++ presents you online free application ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion TEXT to PDF with Free App](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## Convert XPS to PDF

**Aspose.PDF for C++** support feature converting <abbr title="XML Paper Specification">XPS</abbr> files to PDF format. Check this article to resolve your tasks.

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into its Windows operating system.

{{% alert color="primary" %}}

The file format is basically a zipped XML file which is primarily used for distribution and storage. It's very difficult to edit and mostly implemented by Microsoft.

{{% /alert %}}

In order to convert XPS to PDF with Aspose.PDF for C++, we have introduced a class named [XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) which is used to initialize a [LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) object. Later, this object is passed as an argument during the Document object initialization and it helps the PDF rendering engine to determine the source document's input format.

The following code snippet shows the process of converting XPS file into PDF format with C++.

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Try to convert XPS format to PDF online**

Aspose.PDF for C++ presents you online free application ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Convert XML to PDF

The XML format used to store structured data. There are several ways to convert <abbr title="Extensible Markup Language">XML</abbr> to PDF in Aspose.PDF.

## Convert XSL-FO to PDF

1. Create a [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. Instantiate [XslFoLoadOption object](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Set error handling strategy.
1. Instantiate [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) Object.
1. [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) the input image file.

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

     String outfilename("XMLFOtoPDF.pdf");
    // Instantiate XslFoLoadOption object
    auto options = new XslFoLoadOptions(infilenameXSL);
    // Set error handling strategy
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Create Document object
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**Try to convert XML to PDF online**

Aspose.PDF for C++ presents you online free application ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

