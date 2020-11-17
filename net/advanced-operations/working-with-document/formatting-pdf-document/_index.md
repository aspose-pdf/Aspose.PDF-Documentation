---
title: Formatting PDF Document
type: docs
weight: 10
url: /net/formatting-pdf-document/
---
# Working with Document

## Create Document
Aspose.PDF for .NET API lets you create and read PDF files using C# and VB.NET. The API can be used in a variety of .NET applications including WinForms, ASP.NET, and several others. In this article, we are going to show how to use Aspose.PDF for .NET API to easily generate and read PDF files in .NET applications.

### How to Create PDF File using C#
To create a PDF file using C#, the following steps can be used.

1. Create an object of Document class
1. Add a Page object to the Pages collection of the Document object
1. Add TextFragment to Paragraphs collection of the page
1. Save the resultant PDF document
 ```
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Initialize document object
Document document = new Document();
// Add page
Page page = document.Pages.Add();
// Add text to new page
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// Save updated PDF
document.Save(dataDir + "HelloWorld_out.pdf");
```cshrap
## Formatting PDF Document

### Get Document Window and Page Display Properties 
This topic helps you understand how to get properties of the document window, viewer application, and how pages are displayed. To set these properties:

Open the PDF file using the Document class. Now, you can set the Document object’s properties, such as

- CenterWindow – Center the document window on the screen. Default: false.
- Direction – Reading order. This determines how pages are laid out when displayed side by side. Default: left to right.
- DisplayDocTitle – Display the document title in the document window title bar. Default: false (the title is displayed).
- HideMenuBar – Hide or display the document window’s menu bar. Default: false (menu bar is displayed).
- HideToolBar – Hide or display the document window’s toolbar. Default: false (toolbar is displayed).
- HideWindowUI – Hide or display document window elements like scroll bars. Default: false (UI elements are displayed).
- NonFullScreenPageMode – How the document when it’s not displayed in full-page mode.
- PageLayout – The page layout.
- PageMode – How the document is displayed when first opened. The options are show thumbnails, full-screen, show attachment panel.

The following code snippet shows you how to get the properties using Document class.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// Get different document properties
// Position of document's window - Default: false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);
   
// Predominant reading order; determins the position of page
// When displayed side by side - Default: L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);
            
// Whether window's title bar should display document title
// If false, title bar displays PDF file name - Default: false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);
            
// Whether to resize the document's window to fit the size of
// First displayed page - Default: false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);
            
// Whether to hide menu bar of the viewer application - Default: false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);
            
// Whether to hide tool bar of the viewer application - Default: false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);
            
// Whether to hide UI elements like scroll bars
// And leaving only the page contents displayed - Default: false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);
            
// Document's page mode. How to display document on exiting full-screen mode.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);
            
// The page layout i.e. single page, one column
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);
            
// How the document should display when opened
// I.e. show thumbnails, full-screen, show attachment panel
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### Set Document Window and Page Display Properties
This topic explains how to set the properties of the document window, viewer application, and page display. To set these different properties:

1. Open the PDF file using the Document class.
1. Set the Document object’s properties.
1. Save the updated PDF file using the Save method.

Properties available are:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Each is used and described in the code below. The following - code snippet shows you how to set the properties using the Document class.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// Set different document properties
// Sepcify to position document's window - Default: false
pdfDocument.CenterWindow = true;
            
// Predominant reading order; determins the position of page
// When displayed side by side - Default: L2R
pdfDocument.Direction = Direction.R2L;
            
// Specify whether window's title bar should display document title
// If false, title bar displays PDF file name - Default: false
pdfDocument.DisplayDocTitle = true;
            
// Specify whether to resize the document's window to fit the size of
// First displayed page - Default: false
pdfDocument.FitWindow = true;
            
// Specify whether to hide menu bar of the viewer application - Default: false
pdfDocument.HideMenubar = true;
            
// Specify whether to hide tool bar of the viewer application - Default: false
pdfDocument.HideToolBar = true;
            
// Specify whether to hide UI elements like scroll bars
// And leaving only the page contents displayed - Default: false
pdfDocument.HideWindowUI = true;
            
// Document's page mode. specify how to display document on exiting full-screen mode.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;
            
// Specify the page layout i.e. single page, one column
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;
            
// Specify how the document should display when opened
// I.e. show thumbnails, full-screen, show attachment panel
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// Save updated PDF file
pdfDocument.Save(dataDir);
```
### Embedding Fonts in an existing PDF file
PDF readers support [a core of 14 fonts](https://en.wikipedia.org/wiki/PDF#Text) so that documents can be displayed the same way regardless of the platform the document is displayed on. When a PDF contains a font that is not one of the 14 core fonts, embed the font to the PDF file to avoid font substitution.

Aspose.PDF for .NET supports font embedding in existing PDF files. You can embed a complete font or a subset of the font. To embed the font, open the PDF file using the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class. Then use the [Aspose.Pdf.Text.Font](https://apireference.aspose.com/pdf/net/aspose.pdf.text) class to embed the font into the PDF file. To embed the full font, use the Font class’ IsEmbeded property; to use a subset of the font, use the IsSubset property.

>A font subset embeds only the characters that are used and is useful where fonts are used for short sentences or slogans, for example where a corporate font is used for a logo, but not for the body text. Using a subset reduces the file size of the output PDF. However, if a custom font is used for the body text, embed it in its entirety.

The following code snippet shows how to embed a font in a PDF file.
### Embedding Standard Type 1 Fonts
Some PDF documents have fonts from a special Adobe font set. Fonts from this set are called “Standard Type 1 Fonts”. This set includes 14 fonts and embedding this type of fonts requires using of special flags i.e [Aspose.Pdf.Document.EmbedStandardFonts](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). Following is the code snippet which can be used to get a document with all fonts embedded including Standard Type 1 Fonts:
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Load an existing PDF Document
Document pdfDocument = new Document(dataDir + "input.pdf");
// Set EmbedStandardFonts property of document
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
            // Check if font is already embedded
            if (!pageFont.IsEmbedded)
            {
                pageFont.IsEmbedded = true;
            }
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### Embedding Fonts while creating PDF
If you need to use any font other than the 14 core fonts supported by Adobe Reader, you must embed the font description while generating the Pdf file. If font information is not embedded, Adobe Reader will take it from the Operating System if it’s installed over the system, or it will construct a substitute font according to the font descriptor in the Pdf.

>Please note the embedded font must be installed on the host machine i.e. in case of the following code ‘Univers Condensed’ font is installed over the system.

We use the property IsEmbedded of Font class to embed the font information into Pdf file. Setting the value of this property to ‘True’ will embed the complete font file into the Pdf, knowing the fact that it will increase the Pdf file size. Following is the code snippet that can be used to embed the font information into Pdf.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instantiate Pdf object by calling its empty constructor
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// Create a section in the Pdf object
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// Save PDF Document
doc.Save(dataDir);
```
### Set Default Font Name while Saving PDF
When a PDF document contains fonts, which are not available in the document itself and on the device, API replaces these fonts with the default font. When font is available (is installed on the device or is embedded into the document), output PDF should have the same font (should not be replaced with default font). The value of the default font should contain the name of the font (not the path to the font files). We have implemented a feature to set default font name while saving a document as PDF. Following code snippet can be used to set default font:
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Load an existing PDF document with missing font
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // Specify Default Font Name
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### Get All Fonts from PDF Document
In case you want to get all fonts from a PDF document, you can use FontUtilities.GetAllFonts() method provided in Document class. Please check following code snippet in order to get all fonts from an existing PDF document:
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```
### Get Warnings for Font Substitution
Aspose.PDF for .NET provides methods to get notifications about font substitution for handling font substitution cases. The code snippets below show how to use corresponding functionality.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```

 The *OnFontSubstitution* method is as listed below.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
oldFont.FontName, newFont.FontName));
```
### Improve Fonts Embedding using FontSubsetStrategy
The feature to embed the fonts as a subset can be accomplished by using the IsSubset property, but sometimes you want to reduce a fully embedded font set to only subsets that are used in the document. Aspose.Pdf.Document has property FontUtilities which includes method SubsetFonts(FontSubsetStrategy subsetStrategy). In the method SubsetFonts(), the parameter subsetStrategy helps to tune the subset strategy. FontSubsetStrategy supports two following variants of font subsetting.

- SubsetAllFonts - This will subset all fonts, used in a document.
- SubsetEmbeddedFontsOnly - This will subset only those fonts which are fully embedded into the document.

Following code snippet shows how to set FontSubsetStrategy:
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// All fonts will be embedded as subset into document in case of SubsetAllFonts.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```
### Get-Set Zoom Factor of PDF File
Sometimes, you want to determine what a PDF document’s current zoom factor is. With Aspose.Pdf, you can find out the current value as well as set one.

The [GoToAction](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) class’ Destination property allows you to get the zoom value associated with a PDF file. Similarly, it can be used to set a file’s zoom factor.

#### Set Zoom factor
The following code snippet shows how to set the zoom factor of a PDF file.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instantiate new Document object
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// Save the document
doc.Save(dataDir);
```
#### Get Zoom Factor
The following code snippet shows how to get a PDF file’s zoom factor.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instantiate new Document object
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// Create GoToAction object
GoToAction action = doc.OpenAction as GoToAction;
            
// Get the Zoom factor of PDF file
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // Document zoom value;
```
### Setting Print Dialog Preset Properties
Aspoose.PDF allows setting the Print Dialog Preset properties of a PDF document. It allows you to change the DuplexMode property for a PDF document which is set to simplex by default. This can be achieved using two different methodologies as shown below.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```
### Setting Print Dialog Preset Properties using PDF Content Editor
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("The file has duplex flip short edge");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
}
```
