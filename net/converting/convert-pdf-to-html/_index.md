---
title: Convert PDF to HTML
type: docs
weight: 280
url: /net/convert-pdf-to-html/
---
# Convert PDF to HTML

Aspose.PDF for .NET provides many features for converting various file formats into PDF documents and converting PDF files into various output formats. This article discusses how to convert a PDF file into HTML. Aspose.PDF for .NET provides the capability to convert HTML files into PDF format using the InLineHtml approach. We have had many requests for functionality that converts a PDF file into HTML format and have provided this feature. Please note that this feature also supports XHTML 1.0.


- Convert PDF to HTML
- Splitting Output to Multi-page HTML
- Specify Folder for Storing SVG Files
- Compressing SVG Images During Conversion
- Specifying the Images Folder
- Create Subsequent Files with Body Contents Only
- Transparent Text rendering
- PDF document layers rendering

## Convert PDF to HTML

>Try online: You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-html](https://products.aspose.app/pdf/conversion/pdf-to-html)

Aspose.PDF for .NET provides a two-line code for transforming a source PDF file to HTML. The SaveFormat enumeration contains the value .Html which lets you save the source file to HTML. The following code snippet shows the process of converting a PDF file into HTML.

```// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Open the source PDF document
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Save the file into MS document format
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```
## Splitting Output to Multi-page HTML
When converting large PDF file with several pages to HTML format, the output appears as a single HTML page. It can end up being very long. To control page size, it is possible to split the output into several pages during PDF to HTML conversion. Please try using the following code snippet.

```// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Open the source PDF document
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Instantiate HTML SaveOptions object
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Specify to split the output into multiple pages
htmlOptions.SplitIntoPages = true;

// Save the document
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

## Specify Folder for Storing SVG Files
During PDF to HTML conversion, it is possible to specify the folder that SVG images should be saved to. Use the HtmlSaveOption class' SpecialFolderForSvgImages property to specify a special SVG image directory. This property gets or sets the path to the directory to which SVG images must be saved to when encountered during conversion. If the parameter is empty or null, then any SVG files are saved together with other image files.

```csharp
// Load the PDF file
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// Instantiate HTML save options object
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Specify the folder where SVG images are saved during PDF to HTML conversion
newOptions.SpecialFolderForSvgImages = dataDir;

// Save the output file
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

## Compressing SVG Images During Conversion
To compress SVG images during PDF to HTML conversion, please try using the following code:

```// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Create HtmlSaveOption with tested feature
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Compress the SVG images if there are any
newOptions.CompressSvgGraphicsIfAny = true;
```
## Specifying the Images Folder
We can also specify the folder that images will be saved to during PDF to HTML conversion:

```// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Create HtmlSaveOption with tested feature
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Specify the separate folder to save images
newOptions.SpecialFolderForAllImages = dataDir;
```

## Create Subsequent Files with Body Contents Only

Recently, we were asked to introduce a feature where PDF files are converted to HTML and the user can get only the contents of the `<body>` tag for each page. This would produce one file with CSS, `<html>`, `<head>` details and all pages in other files just with `<body>` contents.

To meet this requirement, a new property, HtmlMarkupGenerationMode, was introduced to the HtmlSaveOptions class.

With the following simple code snippet, you can split the output HTML into pages. In the output pages, all HTML objects must go exactly where they go now (fonts processing and output, CSS creation and output, images creation and output), except that the output HTML will contain contents currently placed inside thetags (now “body” tags will be omitted). However, when using this approach, the link to the CSS is the responsibility of your code, because things like will be stripped out. For this purpose, you may read the CSS via File.ReadAllText() and send it via AJAX to to a web page where it will be applied by jQuery.

```// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
            
HtmlSaveOptions options = new HtmlSaveOptions();
// This is the tested setting
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```
## Transparent Text rendering

In case the source/input PDF file contains transparent texts shadowed by foreground images, then there might be text rendering issues. So in order to cater such scenarios, SaveShadowedTextsAsTransparentTexts and SaveTransparentTexts properties can be used.

```// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
## PDF document layers rendering
We can render PDF document layers in separate layer type element during PDF to HTML conversion:

```// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// Instantiate HTML SaveOptions object
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Specify to render PDF document layers separately in output HTML
htmlOptions.ConvertMarkedContentToLayers = true;

// Save the document
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```