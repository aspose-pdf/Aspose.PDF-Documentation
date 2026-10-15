---
title: Work with PDF file metadata in C++
linktitle: PDF File Metadata
type: docs
weight: 200
url: /cpp/pdf-file-metadata/
description: Read and update PDF document information, register XMP namespace prefixes, and set XMP values using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get and Set PDF Document Properties and XMP Metadata in C++
Abstract: Learn how to read and update author, title, keywords, dates, and other PDF information fields with Aspose.PDF for C++. The examples also register an XMP namespace prefix and add timestamp and string values through XmpValue.
---

This page covers the four supplied examples for reading file information, updating standard properties, registering an XMP namespace prefix, and adding XMP values.

Use [DocumentInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/documentinfo/) for fields such as author, title, subject, keywords, and dates. Use [Metadata](https://reference.aspose.com/pdf/cpp/aspose.pdf/metadata/) for XMP properties and wrap C++ values in [XmpValue](https://reference.aspose.com/pdf/cpp/aspose.pdf/xmpvalue/).

Configure your project to include and link Aspose.PDF for C++, supply an input PDF, and create output directories before calling the examples. The snippets omit the project-specific pdf-file-metadata.h include. The reading function prints information without saving a file; each writing function accepts its own output path.

## Get PDF file information

Read standard document information and print the values without modifying the PDF.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Access its [DocumentInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/documentinfo/) through get_Info().
1. Read Author, CreationDate, Keywords, ModDate, Subject, and Title.
1. Print the values to the console.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocumentInfo.h>

using namespace System;
using namespace Aspose::Pdf;

void GetPdfFileInformation(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto docInfo = document->get_Info();

    std::cout << "Author: " << docInfo->get_Author() << std::endl;
    std::cout << "Creation Date: " << docInfo->get_CreationDate().ToString() << std::endl;
    std::cout << "Keywords: " << docInfo->get_Keywords() << std::endl;
    std::cout << "Modify Date: " << docInfo->get_ModDate().ToString() << std::endl;
    std::cout << "Subject: " << docInfo->get_Subject() << std::endl;
    std::cout << "Title: " << docInfo->get_Title() << std::endl;
}
```

## Set XMP metadata with a namespace prefix

Register the xmp prefix for the Adobe XMP namespace and add a modification timestamp.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Access [Metadata](https://reference.aspose.com/pdf/cpp/aspose.pdf/metadata/) and call [RegisterNamespaceUri()](https://reference.aspose.com/pdf/cpp/aspose.pdf/metadata/) with the xmp prefix and namespace URI.
1. Get the current [DateTimeOffset](https://reference.aspose.com/pdf/cpp/system/datetimeoffset/) and format it with the round-trip o format.
1. Wrap the formatted timestamp in [XmpValue](https://reference.aspose.com/pdf/cpp/aspose.pdf/xmpvalue/) and call [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/metadata/) for xmp:ModifyDate.
1. Save the updated PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <iostream>
#include <system/date_time_offset.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Metadata.h>
#include <Aspose.PDF.Cpp/Data/XMP/XmpValue.h>

using namespace System;
using namespace Aspose::Pdf;

void SetPrefixMetadata(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http://ns.adobe.com/xap/1.0/");
    document->get_Metadata()->Add(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTimeOffset::get_Now().ToString(u"o")));
    document->Save(outputFile);

    std::cout << "Prefix metadata saved to " << outputFile << std::endl;
}
```

## Set PDF file information

Update the document information fields and save a separate output PDF.

The example assigns the current time to both CreationDate and ModDate, replacing any existing creation date. Adapt those assignments if you need to retain the original date.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and access its [DocumentInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/documentinfo/).
1. Get the current time with [DateTime::get_Now()](https://reference.aspose.com/pdf/cpp/system/datetime/).
1. Set Author, CreationDate, Keywords, ModDate, Subject, and Title.
1. Set Producer and Creator.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/) and print the output path.

```cpp
#include <iostream>
#include <system/date_time.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DocumentInfo.h>

using namespace System;
using namespace Aspose::Pdf;

void SetFileInformation(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto docInfo = document->get_Info();
    auto now = DateTime::get_Now();

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(now);
    docInfo->set_Keywords(u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate(now);
    docInfo->set_Subject(u"PDF Information");
    docInfo->set_Title(u"Setting PDF Document Information");
    docInfo->set_Producer(u"Custom producer");
    docInfo->set_Creator(u"Custom creator");
    document->Save(outputFile);

    std::cout << "File information saved to " << outputFile << std::endl;
}
```

## Set XMP property values

Add the sample creation date, nickname, and custom property to the PDF metadata.

The example retains the supplied xmp:CustomProperty name. Treat it as sample application data rather than a standard XMP property.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Access [Metadata](https://reference.aspose.com/pdf/cpp/aspose.pdf/metadata/) through get_Metadata().
1. Wrap the current [DateTimeOffset](https://reference.aspose.com/pdf/cpp/system/datetimeoffset/) round-trip string in [XmpValue](https://reference.aspose.com/pdf/cpp/aspose.pdf/xmpvalue/) and add xmp:CreateDate.
1. Add xmp:Nickname and xmp:CustomProperty using [XmpValue](https://reference.aspose.com/pdf/cpp/aspose.pdf/xmpvalue/) strings.
1. Save the updated PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/) and print the output path.

```cpp
#include <iostream>
#include <system/date_time_offset.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Metadata.h>
#include <Aspose.PDF.Cpp/Data/XMP/XmpValue.h>

using namespace System;
using namespace Aspose::Pdf;

void SetXmpMetadata(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->get_Metadata()->Add(u"xmp:CreateDate", MakeObject<XmpValue>(DateTimeOffset::get_Now().ToString(u"o")));
    document->get_Metadata()->Add(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    document->get_Metadata()->Add(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));
    document->Save(outputFile);

    std::cout << "XMP metadata saved to " << outputFile << std::endl;
}
```
