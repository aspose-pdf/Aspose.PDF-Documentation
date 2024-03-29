---
title: Convert PDF to Microsoft Word Documents in C++
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for C++ library allows you to convert PDF to Word format using C++ with ease and full control. These formats include DOC and DOCX. Learn more how to tune up PDF to Microsoft Word documents conversion.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Overview

This article explains how to convert PDF to Microsoft Word Documents using C++. It covers these topics.

_Format_: **DOC**
- [C++ PDF to DOC](#cpp-pdf-to-doc)
- [C++ Convert PDF to DOC](#cpp-pdf-to-doc)
- [C++ How to convert PDF file to DOC](#cpp-pdf-to-doc)

_Format_: **DOCX**
- [C++ PDF to DOCX](#cpp-pdf-to-docx)
- [C++ Convert PDF to DOCX](#cpp-pdf-to-docx)
- [C++ How to convert PDF file to DOCX](#cpp-pdf-to-docx)

_Format_: **Microsoft Word DOC format**
- [C++ PDF to Word](#cpp-pdf-to-word-doc)
- [C++ Convert PDF to Word](#cpp-pdf-to-word-doc)
- [C++ How to convert PDF file to Word](#cpp-pdf-to-word-doc)

_Format_: **Microsoft Word DOCX format**
- [C++ PDF to Word](#cpp-pdf-to-word-docx)
- [C++ Convert PDF to Word](#cpp-pdf-to-word-docx)
- [C++ How to convert PDF file to Word](#cpp-pdf-to-word-docx)

Other topics covered by this article
- [See Also](#see-also)

## C++ PDF to Word Conversions

One of the most popular feature is PDF to Microsoft Word DOC conversion, which makes the content easy to manipulate. Aspose.PDF for C++ allows you to convert PDF files to DOC.

## Convert PDF to DOC (Word 97-2003) file

Convert PDF file to DOC format with ease and full control. Aspose.PDF for C++ is flexible and supports a wide variety of conversions. Converting pages from PDF documents to images, for example, is a very popular feature.

A conversion that many of our customers have requested is PDF to DOC: converting a PDF file to a Microsoft Word document. Customers want this because PDF files cannot easily be edited, whereas Word documents can. Some companies want their users to be able to manipulate text, tables and images in files that started as PDFs.

Keeping alive the tradition of making things simple and understandable, Aspose.PDF for C++ lets you transform a source PDF file into a DOC file with two lines of code. To accomplish this feature, we have introduced an enumeration named SaveFormat and its value .Doc lets you save the source file to Microsoft Word format.

The following C++ code snippet shows the process of converting a PDF file into DOC format.

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>Steps: Convert PDF to DOC in C++</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>Steps: Convert PDF to Microsoft Word DOC format in C++</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object with the source PDF document.
2. Save it to **SaveFormat::Doc** format by calling **Document->Save()** method.

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Save the file into MS document format
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

The following code snippet shows the process of converting PDF file into DOC Advanced version:

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // Set the recognition mode as Flow
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // Set the Horizontal proximity as 2.5
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // Enable the value to recognize bullets during conversion process
    saveOptions->set_RecognizeBullets(true);

    try {
        // Save the file into MS document format
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Try to convert PDF to DOC online**

Aspose.PDF for C++ presents you online free application ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), where you may try to investigate the functionality and quality it works.

[![Convert PDF to DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convert PDF to DOCX

Aspose.PDF for C++ API lets you read and convert PDF documents to DOCX using C++ language. DOCX is a well-known format for Microsoft Word documents whose structure was changed from plain binary to a combination of XML and binary files. Docx files can be opened with Word 2007 and lateral versions but not with the earlier versions of MS Word which support DOC file extensions.

The following C++ code snippet shows the process of converting a PDF file into DOCX format.

<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>Steps: Convert PDF to DOCX in C++</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>Steps: Convert PDF to Microsoft Word DOCX format in C++</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object with the source PDF document.
2. Save it to **SaveFormat::DocX** format by calling **Document->Save()** method.

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Save the file into MS document format
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

The [`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) class has a property named Format which provides the capability to specify the format of the resultant document, that is, DOC or DOCX. In order to convert a PDF file to DOCX format, please pass the Docx value from the DocSaveOptions.DocFormat enumeration.

Please take a look over the following code snippet which provides the capability to convert PDF file to DOCX format with C++.

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // Set other DocSaveOptions params
    // ...

    // Save the file into MS document format

    try {
        // Save the file into MS document format
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="warning" %}}
**Try to convert PDF to DOCX online**

Aspose.PDF for C++ presents you online free application ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Word Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## See Also

This article also covers these topics. The codes are same as above.

_Format_: **Microsoft Word DOC format**
- [C++ PDF to Word Code](#cpp-pdf-to-word-doc)
- [C++ PDF to Word API](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Programmatically](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Library](#cpp-pdf-to-word-doc)
- [C++ Save PDF as Word](#cpp-pdf-to-word-doc)
- [C++ Generate Word from PDF](#cpp-pdf-to-word-doc)
- [C++ Create Word from PDF](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Converter](#cpp-pdf-to-word-doc)

_Format_: **Microsoft Word DOCX format**
- [C++ PDF to Word Code](#cpp-pdf-to-word-docx)
- [C++ PDF to Word API](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Programmatically](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Library](#cpp-pdf-to-word-docx)
- [C++ Save PDF as Word](#cpp-pdf-to-word-docx)
- [C++ Generate Word from PDF](#cpp-pdf-to-word-docx)
- [C++ Create Word from PDF](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Converter](#cpp-pdf-to-word-docx)

_Format_: **DOC**
- [C++ PDF to DOC Code](#cpp-pdf-to-doc)
- [C++ PDF to DOC API](#cpp-pdf-to-doc)
- [C++ PDF to DOC Programmatically](#cpp-pdf-to-doc)
- [C++ PDF to DOC Library](#cpp-pdf-to-doc)
- [C++ Save PDF as DOC](#cpp-pdf-to-doc)
- [C++ Generate DOC from PDF](#cpp-pdf-to-doc)
- [C++ Create DOC from PDF](#cpp-pdf-to-doc)
- [C++ PDF to DOC Converter](#cpp-pdf-to-doc)

_Format_: **DOC**
- [C++ PDF to DOCX Code](#cpp-pdf-to-docx)
- [C++ PDF to DOCX API](#cpp-pdf-to-docx)
- [C++ PDF to DOCX Programmatically](#cpp-pdf-to-docx)
- [C++ PDF to DOCX Library](#cpp-pdf-to-docx)
- [C++ Save PDF as DOCX](#cpp-pdf-to-docx)
- [C++ Generate DOCX from PDF](#cpp-pdf-to-docx)
- [C++ Create DOCX from PDF](#cpp-pdf-to-docx)
- [C++ PDF to DOCX Converter](#cpp-pdf-to-docx)
