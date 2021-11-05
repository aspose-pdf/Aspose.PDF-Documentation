---
title: Convert PDF to PPTX 
linktitle: Convert PDF to PowerPoint
type: docs
weight: 110
url: /cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF allows you to convert PDF to PowerPoint format using C++. One way there is a possibility to convert PDF to PPTX with Slides as Images.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** lets you track the progress of PDF to PPTX conversion.

During PDF to <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> conversion, the text is rendered as Text where you can select/update it. Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named [`PptxSaveOptions`](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). An object of the PptxSaveOptions class is passed as a second argument to the [`Document.Save(..) method`](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) method. The following code snippet shows the process for converting PDF files into PPTX format.

## Simple conversion PDF to PPTX using C# and Aspose.PDF C++

In order to convert PDF to PPTX, Aspose.PDF for C++ advice to use the following code steps.

1. Create an instance of [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class
1. Create an instance of [PptxSaveOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class
1. Use the Save method of the Document object to save the PDF as PPTX

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

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![PDF to PPTX](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

In case if you need to convert a searchable PDF to PPTX as images instead of selectable text, Aspose.PDF provides such a feature via [Aspose.Pdf.PptxSaveOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class. To achieve this, set property [SlidesAsImages](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) of [PptxSaveOptios](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class to 'true' as shown in the following code sample.

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

Aspose.PDF for C++ lets you track the progress of PDF to PPTX conversion. The [Aspose.Pdf.PptxSaveOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class provides [CustomProgressHandler](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) property that can be specified to a custom method for tracking the progress of conversion as shown in the following code sample.

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
