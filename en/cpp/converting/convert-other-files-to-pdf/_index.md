---
title: Convert other file formats to PDF in C++
linktitle: Convert other file formats to PDF
type: docs
weight: 80
url: /cpp/convert-other-files-to-pdf/
description: Convert text, LaTeX, Markdown, PostScript, XPS, and XML with XSL-FO stylesheets to PDF using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generate PDFs from Text, LaTeX, Markdown, and XPS in C++
Abstract: Learn how to create PDFs from plain or preformatted text, LaTeX, Markdown, PostScript, XPS, and XML with Aspose.PDF for C++. The examples cover page breaks, custom PostScript font folders, and XML conversion with an XSL-FO stylesheet.
---

Create PDF documents from text, markup, and page-description formats with Aspose.PDF for C++. Use format-specific load options for LaTeX, Markdown, PostScript, XPS, and XML with an XSL-FO stylesheet, or build PDF paragraphs from text files.

## Convert plain text to PDF

Read an entire text file and place its contents in a PDF text fragment.

1. Read the input file with System::IO::File::ReadAllText().
1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) containing the text.
1. Add the fragment to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertTextToPDF(String path_infile, String path_outfile)
{
    String content = System::IO::File::ReadAllText(path_infile);
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto text = MakeObject<TextFragment>(content);
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);
    document->Save(path_outfile);
}
```

## Convert preformatted text with page breaks

Process a text file line by line using a monospaced font and explicit form-feed markers.

Ensure Courier New is available. A line starting with a form feed is treated as a page-break marker; any other text on that line is not added. At such a marker, processing stops if the page count is already greater than 3.

1. Read the input file with System::IO::File::ReadAllLines().
1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Set left and right margins and configure a 12-point Courier New font through [PageInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/pageinfo/).
1. Iterate through the lines and check for a leading form-feed character.
1. Add a page and reapply formatting when a form-feed marker is found, subject to the source's page-count guard.
1. For other lines, add a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) to the page.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertTextPreformattedToPdf(String path_infile, String path_outfile)
{
    // Read the text file as array of string
    auto lines = System::IO::File::ReadAllLines(path_infile);

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
    document->Save(path_outfile);
}
```

## Convert LaTeX to PDF

Load the LaTeX source with format-specific options and save it as PDF.

1. Create [TeXLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/texloadoptions/).
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the input file path and the load options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/TeXLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertLaTeXtoPDF(String path_infile, String path_outfile)
{
    auto options = MakeObject<TeXLoadOptions>();
    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);
}
```

## Convert Markdown to PDF

Load the Markdown source with format-specific options and save it as PDF.

1. Create [MdLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/mdloadoptions/).
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the input file path and the load options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/MdLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertMarkdownToPDF(String path_infile, String path_outfile)
{
    auto options = MakeObject<MdLoadOptions>();
    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);
}
```

## Convert PostScript to PDF

Load the PostScript source with format-specific options and save it as PDF.

1. Create [PsLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/psloadoptions/).
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the input file path and the load options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PsLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertPostscriptToPDF(String path_infile, String path_outfile)
{
    auto options = MakeObject<PsLoadOptions>();
    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);
}
```

## Convert PostScript with custom font folders

Provide font search folders when loading a PostScript file.

Replace the sample Windows folder paths with directories available on your system. The source file name and function retain the spelling avdanced from the supplied example.

1. Create [PsLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/psloadoptions/).
1. Create an array containing the font folder paths.
1. Assign the array to FontsFolders.
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) from the input path and options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PsLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertPostscriptToPDFAvdanced(String path_infile, String path_outfile)
{
    auto options = MakeObject<PsLoadOptions>();
    auto folders = MakeArray<String>({ String(u"E:\\Samples\\Conversion\\Fonts"), String(u"C:\\tmp\\") });

    options->set_FontsFolders(folders);

    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);
}
```

## Convert XPS to PDF

Load the XPS source with format-specific options and save it as PDF.

1. Create [XpsLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/xpsloadoptions/).
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the input file path and the load options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/XpsLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertXPStoPDF(String path_infile, String path_outfile)
{
    auto options = MakeObject<XpsLoadOptions>();    
    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);        
}
```

## Convert XML with an XSL-FO stylesheet

Load XML with a companion XSLT stylesheet through XslFoLoadOptions.

Supply both the XML and its corresponding XSLT file. The path substitution expects lowercase .xml; parsing errors are configured to raise an exception immediately.

1. Derive the stylesheet path by replacing .xml in the input path with .xslt.
1. Create [XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/xslfoloadoptions/) with the stylesheet path.
1. Set ParsingErrorsHandlingType to ThrowExceptionImmediately.
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) from the XML path and options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/XslFoLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertXSLFO_to_PDF(String path_infile, String path_outfile)
{
    String infilenameXSL = path_infile.Replace(u".xml", u".xslt");        
    // Instantiate XslFoLoadOption object
    auto options = MakeObject<XslFoLoadOptions>(infilenameXSL);

    // Set error handling strategy
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Create Document object
    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);
}
```
