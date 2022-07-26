---
title: Convert PDF file to HTML format 
linktitle: Convert PDF file to HTML format
type: docs
weight: 50
url: /cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: This topic show you how to Aspose.PDF allows to convert PDF file to HTML format with C++ library.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** provides many features for converting various file formats into PDF documents and converting PDF files into various output formats. This article discusses how to convert a PDF file into <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for C++ provides the capability to convert HTML files into PDF format using the InLineHtml approach. We have had many requests for functionality that converts a PDF file into HTML format and have provided this feature. Please note that this feature also supports XHTML 1.0.

**Aspose.PDF for C++** support the features  to convert a PDF file into HTML. The main tasks you can accomplish with the Aspose.PDF library are listed:

- сonvert PDF to HTML;
- splitting Output to Multi-page HTML;
- specify Folder for Storing SVG Files;
- compressing SVG Images During Conversion;
- specifying the Images Folder;
- create Subsequent Files with Body Contents Only;
- transparent Text rendering;
- PDF document layers rendering.

Aspose.PDF for C++ provides a two-line code for transforming a source PDF file to HTML. The `SaveFormat enumeration` contains the value Html which lets you save the source file to HTML. The following code snippet shows the process of converting a PDF file into HTML.

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Save the output in HTML format
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Try to convert PDF to HTML online**

Aspose.PDF for C++ presents you online free application ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## Splitting Output to Multi-page HTML

When converting large PDF file with several pages to HTML format, the output appears as a single HTML page. It can end up being very long. To control page size, it is possible to split the output into several pages during PDF to HTML conversion. Please try using the following code snippet.

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // Specify to split the output into multiple pages
    htmlOptions->set_SplitIntoPages(true);

    try {
    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Specify Folder for Storing SVG Files

During PDF to HTML conversion, it is possible to specify the folder that SVG images should be saved to. Use the [`HtmlSaveOption class`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`SpecialFolderForSvgImages property`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f) to specify a special SVG image directory. This property gets or sets the path to the directory to which SVG images must be saved to when encountered during conversion. If the parameter is empty or null, then any SVG files are saved together with other image files.

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Specify the folder where SVG images are saved during PDF to HTML conversion
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Compressing SVG Images During Conversion

To compress SVG images during PDF to HTML conversion, please try using the following code:

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Specify the folder where SVG images are saved during PDF to HTML conversion
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Specifying the Images Folder

We can also specify the folder that images will be saved to during PDF to HTML conversion:

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Specify the folder where All images are saved during PDF to HTML conversion
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Create Subsequent Files with Body Contents Only

Recently, we were asked to introduce a feature where PDF files are converted to HTML and the user can get only the contents of the `<body>` tag for each page. This would produce one file with CSS, `<html>`, `<head>` details and all pages in other files just with `<body>` contents.

To meet this requirement, a new property, HtmlMarkupGenerationMode, was introduced to the [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) class.

With the following simple code snippet, you can split the output HTML into pages. In the output pages, all HTML objects must go exactly where they go now (fonts processing and output, CSS creation and output, images creation and output), except that the output HTML will contain contents currently placed inside thetags (now “body” tags will be omitted). However, when using this approach, the link to the CSS is the responsibility of your code, because things like will be stripped out. For this purpose, you may read the CSS via File.ReadAllText() and send it via AJAX to to a web page where it will be applied by jQuery.

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Transparent Text rendering

In case the source/input PDF file contains transparent texts shadowed by foreground images, then there might be text rendering issues. So in order to cater such scenarios, [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) and SaveTransparentTexts properties can be used.

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF document layers rendering

We can render PDF document layers in separate layer type element during PDF to HTML conversion:

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate HTML Save Option object
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Specify to render PDF document layers separately in output HTML
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // Save the output in HTML format
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
