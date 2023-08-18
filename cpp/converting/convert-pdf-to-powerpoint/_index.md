---
title: Convert PDF to Microsoft PowerPoint in C++
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF allows you to convert PDF to PowerPoint format using C++. There is a possibility to convert PDF to PPTX with Slides as Images.
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Overview

This article explains how to **convert PDF to PowerPoint formats using C++**. It covers the following topics.

_Format_: **PPTX**
- [C++ PDF to PPTX](#cpp-pdf-to-pptx)
- [C++ Convert PDF to PPTX](#cpp-pdf-to-pptx)
- [C++ How to convert PDF file to PPTX](#cpp-pdf-to-pptx)

_Format_: **Microsoft PowerPoint PPTX format**
- [C++ PDF to PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Convert PDF to PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ How to convert PDF file to PowerPoint](#cpp-pdf-to-powerpoint-pptx)

Other topics covered by this article.
- [See Also](#see-also)

## C++ PDF to PowerPoint Conversions

**Aspose.PDF for C++** lets you track the progress of PDF to PPTX conversion.

During PDF to <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> conversion, the text is rendered as Text where you can select/update it. Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named [`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). An object of the PptxSaveOptions class is passed as a second argument to the [`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) method. The following code snippet shows the process for converting PDF files into PPTX format.

## Simple conversion PDF to PPTX with Aspose.PDF for C++

In order to convert PDF to PPTX, Aspose.PDF for C++ advice to use the following code steps.

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>Steps: Convert PDF to PPTX in C++</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>Steps: Convert PDF to PowerPoint PPTX format in C++</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class.
2. Create an instance of [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class.
3. Use the **Save** method of the **Document** object to _save the PDF as PPTX_.

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Save the output in PPTX format
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF to PPTX with Slides as Images

In case if you need to convert a searchable PDF to PPTX as images instead of selectable text, Aspose.PDF provides such a feature via [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class. To achieve this, set property [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) of [PptxSaveOptios](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class to 'true' as shown in the following code sample.

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // Save the output in PPTX format
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Progress Detail of PPTX Conversion

Aspose.PDF for C++ lets you track the progress of PDF to PPTX conversion. The [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class provides [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) property that can be specified to a custom method for tracking the progress of conversion as shown in the following code sample.

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //Specify Custom Progress Handler
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // Save the output in PPTX format
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

Following is the custom method for displaying progress conversion.

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Conversion progress : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Result page's " << eventInfo->Value << " of " << eventInfo->MaxValue << " layout created." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Result page's " << eventInfo->Value << " of " << eventInfo->MaxValue << " exported." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Source page " << eventInfo->Value << " of " << eventInfo->MaxValue << " analyzed." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF for C++ presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## See Also

This article also covers these topics. The codes are same as above.

_Format_: **PowerPoint**
- [C++ PDF to PowerPoint Code](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint Programmatically](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint Library](#cpp-pdf-to-powerpoint-pptx)
- [C++ Save PDF as PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Generate PowerPoint from PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Create PowerPoint from PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint Converter](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Microsoft PowerPoint PPTX format**
- [C++ PDF to PowerPoint PPTX Code](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint PPTX API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint PPTX Programmatically](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint PPTX Library](#cpp-pdf-to-powerpoint-pptx)
- [C++ Save PDF as PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ Generate PowerPoint PPTX from PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Create PowerPoint PPTX from PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint PPTX Converter](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF to PPTX Code](#cpp-pdf-to-pptx)
- [C++ PDF to PPTX API](#cpp-pdf-to-pptx)
- [C++ PDF to PPTX Programmatically](#cpp-pdf-to-pptx)
- [C++ PDF to PPTX Library](#cpp-pdf-to-pptx)
- [C++ Save PDF as PPTX](#cpp-pdf-to-pptx)
- [C++ Generate PPTX from PDF](#cpp-pdf-to-pptx)
- [C++ Create PPTX from PDF](#cpp-pdf-to-pptx)
- [C++ PDF to PPTX Converter](#cpp-pdf-to-pptx)
