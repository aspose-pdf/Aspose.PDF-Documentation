---
title: Convert PDF to text 
linktitle: Convert PDF to text
type: docs
weight: 120
url: /cpp/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: With Aspose.PDF for C++ you can convert a whole PDF document to a text file or convert only a PDF page to a text file.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** support converting whole PDF document and single page to a Text file.

## Convert whole PDF document to Text file

You can convert PDF document to TXT file using 'TextAbsorber' class.

The following code snippet explains how to extract the texts from the all pages.

```cpp
void ConvertPDFDocToTXT()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.pdf");
 // String for output file name
 String outfilename("input_Text_Extracted_out.txt");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 auto ta = MakeObject<TextAbsorber>();
 ta->Visit(document);
 // Save the extracted text in text file
 System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), where you may try to investigate the functionality and quality it works.

[![Convert PDF to Text file](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)

## Convert PDF page to text file

You can convert PDF document to TXT file with Aspose.PDF for C++. You should use  `TextAbsorber` class for resolve this task.

The following code snippet explains how to extract the texts from the particular pages.

```cpp
void ConvertPDFPagestoTXT()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample-4pages.pdf");
 // String for output file name
 String outfilename("sample-4pages_out.txt");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 auto ta = MakeObject<TextAbsorber>();

 auto pages = { 1, 3, 4 };
 try {
  for (auto page : pages)
  {
   ta->Visit(document->get_Pages()->idx_get(page));
  }
  // Save the extracted text in text file
  auto text = ta->get_Text();
  System::IO::File::WriteAllText(_dataDir + outfilename, text);
 }
 catch (Exception ex) {
  std::cerr << ex->get_Message() << std::endl;
 }
 std::clog << __func__ << ": Finish" << std::endl;
}
```
