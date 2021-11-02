---
title: Convert Text to PDF 
linktitle: Convert Text to PDF
type: docs
weight: 300
url: /cpp/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for C++ allows you to convert plain text file to PDF or to convert pre-formatted text file to PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** support the feature converting plain text and pre-formatted text file to PDF format.

Converting text to PDF means adding text fragments to the PDF page. As for text files, we are dealing with 2 types of text: pre-formatting (for example, 25 lines with 80 characters per line) and non-formatted text (plain text). Depending on our needs, we can control this addition ourselves or entrust it to the library's algorithms.

## Live Example

Aspose.PDF for C++ presents you online free application ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), where you may try to investigate the functionality and quality it works.

[![How to convert Text to PDF](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)

## Convert plain text file to PDF

In case of the plain text file, we can use the following technique:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. Read the source text file using [TextReader](https://apireference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)
1. Instantiate [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) Object.
1. Add a [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) to pages collection of document.
1. Create a new object of TextFragment and pass TextReader object to its constructor.
1. Add a new text paragraph in paragraphs collection and pass the TextFragment object.
1. Load and [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) the input file.

```cpp
void ConvertTextToPDF() {
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

## Convert pre-formatted text file to PDF

Converting pre-formatted text is like plain text but you need to make some additional actions such as setting margins, font type and size. Obviously that font should be monospace (for example Courier New).

Follow these steps to convert pre-formatted text to PDF with C++:

1. Instantiate a Document object by calling its empty constructor.
1. Set left and right margins for better presentation.
1. Instantiate [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object and add a new page in Pages collection.
1. Load and [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) the input image file.

```cpp
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
