---
title: Convert PDF to EPUB 
linktitle: Convert PDF to EPUB
type: docs
weight: 170
url: /cpp/convert-pdf-to-epub/
lastmod: "2021-06-05"
description: Aspose.PDF for C++ supports the feature to convert PDF documents to EPUB format. You may try using the code snippet to accomplish this requirement.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), where you may try to investigate the functionality and quality it works.

[![PDF to EPUB](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)

<abbr title="Electronic Publication">EPUB</abbr> (short for Electronic Publication) is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub.
EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device. EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.

Aspose.PDF for C++ also supports the feature to convert PDF documents to EPUB format. Aspose.PDF for C++ has a class named EpubSaveOptions which can be used as the second argument to [`Document.Save(..)`](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) method, to generate an EPUB file.
Please try using the following code snippet to accomplish this requirement with C++.

```cpp
void ConvertPDFtoEPUB()
{
	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Conversion\\");

	// String for input file name
	String infilename("sample.pdf");
	// String for output file name
	String outfilename("PDFToEPUB_out.epub");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	// Save PDF file into EPUB format
	document->Save(_dataDir + outfilename, SaveFormat::Epub);
	std::clog << __func__ << ": Finish" << std::endl;
}
```
