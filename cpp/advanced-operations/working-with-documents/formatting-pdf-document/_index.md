---
title: Formatting PDF Document using C++
linktitle: Formatting PDF Document
type: docs
weight: 20
url: /cpp/formatting-pdf-document/
description: Create and format the PDF Document with Aspose.PDF for C++. Use the next code snippet to resolve your tasks.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Formatting PDF Document

### Get Document Window and Page Display Properties

This topic helps you understand how to get properties of the document window, viewer application, and how pages are displayed. To set these properties, open the PDF file using the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class. Now you can set the properties of the Document object, such as:

- CenterWindow – Center the document window on the screen. Default: false.
- Direction – Reading order. This determines how pages are laid out when displayed side by side. Default: left to right.
- DisplayDocTitle – Display the document title in the document window title bar. Default: false (the title is displayed).
- HideMenuBar – Hide or display the document window’s menu bar. Default: false (menu bar is displayed).
- HideToolBar – Hide or display the document window’s toolbar. Default: false (toolbar is displayed).
- HideWindowUI – Hide or display document window elements like scroll bars. Default: false (UI elements are displayed).
- NonFullScreenPageMode – How the document when it’s not displayed in full-page mode.
- PageLayout – The page layout.
- PageMode – How the document is displayed when first opened. The options are show thumbnails, full-screen, show attachment panel.

The following code snippet shows you how to get the properties using [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class.

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Get different document properties
    // Position of document's window - Default: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // Predominant reading order; determins the position of page
    // When displayed side by side - Default: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // Whether window's title bar should display document title
    // If false, title bar displays PDF file name - Default: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // Whether to resize the document's window to fit the size of
    // First displayed page - Default: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // Whether to hide menu bar of the viewer application - Default: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // Whether to hide tool bar of the viewer application - Default: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // Whether to hide UI elements like scroll bars
    // And leaving only the page contents displayed - Default: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // Document's page mode. How to display document on exiting full-screen mode.
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // The page layout i.e. single page, one column
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // How the document should display when opened
    // I.e. show thumbnails, full-screen, show attachment panel
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```

### Set Document Window and Page Display Properties

This topic explains how to set the properties of the document window, viewer application, and page display. To set these different properties:

1. Open the PDF file using the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class.
1. Set different document properties:

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

1. [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) the updated PDF file using the Save method.

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

Each is used and described in the code below. The following - code snippet shows you how to set the properties using the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class.

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Set different document properties
    // Sepcify to position document's window - Default: false
    document->set_CenterWindow(true);

    // Predominant reading order; determins the position of page
    // When displayed side by side - Default: L2R
    document->set_Direction(Direction::R2L);

    // Specify whether window's title bar should display document title
    // If false, title bar displays PDF file name - Default: false
    document->set_DisplayDocTitle(true);

    // Specify whether to resize the document's window to fit the size of
    // First displayed page - Default: false
    document->set_FitWindow(true);

    // Specify whether to hide menu bar of the viewer application - Default: false
    document->set_HideMenubar(true);

    // Specify whether to hide tool bar of the viewer application - Default: false
    document->set_HideToolBar(true);

    // Specify whether to hide UI elements like scroll bars
    // And leaving only the page contents displayed - Default: false
    document->set_HideWindowUI(true);

    // Document's page mode. specify how to display document on exiting full-screen mode.
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // Specify the page layout i.e. single page, one column
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // Specify how the document should display when opened
    // I.e. show thumbnails, full-screen, show attachment panel
    document->set_PageMode(PageMode::UseThumbs);

    // Save updated PDF file
    document->Save(_dataDir + outputFileName);
}
```

### Embedding Fonts in an existing PDF file

PDF readers support [a core of 14 fonts](https://en.wikipedia.org/wiki/PDF#Text) so that documents can be displayed the same way regardless of the platform the document is displayed on. When a PDF contains a font that is not one of the 14 core fonts, embed the font to the PDF file to avoid font substitution.

Aspose.PDF for C++ supports font embedding in existing PDF files. You can embed a complete font or a subset of the font. To embed the font, open the PDF file using the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class. Then use the [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font) class to embed the font into the PDF file. To embed the full font, use the Font class’ IsEmbeded property; to use a subset of the font, use the IsSubset property.

{{% alert color="primary" %}}

A font subset embeds only the characters that are used and is useful where fonts are used for short sentences or slogans, for example where a corporate font is used for a logo, but not for the body text. Using a subset reduces the file size of the output PDF. However, if a custom font is used for the body text, embed it in its entirety.

{{% /alert %}}

The following code snippet shows how to embed a font in a PDF file.

### Embedding Standard Type 1 Fonts

There are PDF documents that use fonts from a special set are called “Standard Type 1 Fonts”. This set includes 14 fonts and embedding this type of font requires using of special flags i.e [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6).

Following is the code snippet which can be used to get a document with all fonts embedded including Standard Type 1 Fonts:

```cpp
void EmbeddingStandardType1Fonts()
{

    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Set EmbedStandardFonts property of document
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // Check if font is already embedded
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```

### Embedding Fonts while creating PDF

If you need to use any font other than the 14 core fonts supported by Adobe Reader, you must embed the font description while generating the Pdf file. If font information is not embedded, Adobe Reader will take it from the Operating System if it’s installed over the system, or it will construct a substitute font according to the font descriptor in the Pdf.

>Please note the embedded font must be installed on the host machine i.e. in case of the following code ‘Univers Condensed’ font is installed over the system.

We use the property IsEmbedded of Font class to embed the font information into Pdf file. Setting the value of this property to ‘True’ will embed the complete font file into the Pdf, knowing the fact that it will increase the Pdf file size. Following is the code snippet that can be used to embed the font information into Pdf.

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Create a section in the Pdf object
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"This is a sample text using Custom font.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // Save PDF Document
    document->Save(_dataDir);
}
```

### Set Default Font Name while Saving PDF

When a PDF document contains fonts, which are not available in the document itself and on the device, API replaces these fonts with the default font. When the font is available (is installed on the device or is embedded into the document), the output PDF should have the same font (should not be replaced with the default font). The value of the default font should contain the name of the font (not the path to the font files). Apose.PDF for C++ implemented a feature to set the default font name while saving a document as a PDF. The following code snippet can be used to set the default font:

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // Specify Default Font Name
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### Get All Fonts from PDF Document

In case you want to get all fonts from a PDF document, you can use [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts() method provided in [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class.

Please check following code snippet in order to get all fonts from an existing PDF document:

```cpp
void GetAllFontsFromPDFdocument()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### Get Warnings for Font Substitution

Aspose.PDF for C++ provides methods to get notifications about font substitution for handling font substitution cases. The code snippets below show how to use corresponding functionality.

```cpp
void GetWarningsForFontSubstitution()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

The [OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) method is as listed below.

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Warning: Font " << font.get_FontName() 
            << " was substituted with another font -> " 
            << newFont.get_FontName() << std::endl;
}
```

### Improve Fonts Embedding using FontSubsetStrategy

The feature to embed the fonts as a subset can be accomplished by using the IsSubset property, but sometimes you want to reduce a fully embedded font set to only subsets that are used in the document. [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) has property [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/) which includes method SubsetFonts(FontSubsetStrategy subsetStrategy). In the method SubsetFonts(), the parameter subsetStrategy helps to tune the subset strategy. FontSubsetStrategy supports two following variants of font subsetting.

- SubsetAllFonts - This will subset all fonts, used in a document.
- SubsetEmbeddedFontsOnly - This will subset only those fonts which are fully embedded into the document.

Following code snippet shows how to set FontSubsetStrategy:

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("sample.pdf");
    // String for file name.
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // All fonts will be embedded as subset into document in case of SubsetAllFonts.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```

### Get-Set Zoom Factor of PDF File

Sometimes, you want to set PDF document’s zoom factor. With Aspose.PDF for C++, you can set the value of zoom factor by [set_OpenAction(…) method](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21) of Document class.

The [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) class Destination property allows you to get the zoom value associated with a PDF file. Similarly, it can be used to set a file’s zoom factor.

#### Set Zoom factor

The following code snippet shows how to set the zoom factor of a PDF file.

```cpp
void SetZoomFactor() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("sample.pdf");
    // String for file name.
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // Save the document
    document->Save(_dataDir + outputFileName);
}
```

#### Get Zoom Factor

Get zoom factor in your PDF file using Aspose.PDF for C++.

The following code snippet shows how to get a PDF file’s zoom factor:

```cpp
void GetZoomFactor() 
{
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Create GoToAction object
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // Get the Zoom factor of PDF file
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // Document zoom value;
}
```

### Setting Print Dialog Preset Properties

Aspoose.PDF for C++ allows setting the Print Dialog Preset properties of a PDF document. It allows you to change the DuplexMode property for a PDF document which is set to simplex by default. This can be achieved using two different methodologies as shown below.

```cpp
void SettingPrintDialogPresetProperties()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### Setting Print Dialog Preset Properties using PDF Content Editor

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "The file has duplex flip short edge" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```
