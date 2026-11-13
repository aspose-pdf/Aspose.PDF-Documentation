---
title: Manage PDF XMP metadata in C++
linktitle: PdfXmpMetadata Class
type: docs
weight: 130
url: /cpp/pdfxmpmetadata-class/
description: Add, update, remove, and read XMP properties and register a custom metadata namespace using Aspose.PDF for C++.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read and Customize PDF XMP Properties in C++
Abstract: Use PdfXmpMetadata to write standard and custom XMP properties and register a namespace. A companion example reads the expected properties and writes a text report.
---

Use [PdfXmpMetadata](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/) to add, update, remove, and read XMP properties and register a custom metadata namespace.

The read example expects the standard and custom keys written by AddXmpMetadata. Its outputFile is a text report rather than a modified PDF.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## PdfXmpMetadata workflows

- [Add XMP metadata](#add-xmp-metadata)
- [Get XMP metadata](#get-xmp-metadata)

## Add XMP metadata

Set standard timestamps and creator tool, remove ModifyDate, and register and update a custom property.

1. Create [PdfXmpMetadata](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Add the XMP property with [PdfXmpMetadata::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/add/).
1. Remove the XMP property with [PdfXmpMetadata::Remove()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/remove/).
1. Register the custom namespace with [PdfXmpMetadata::RegisterNamespaceURI()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/registernamespaceuri/).
1. Update the metadata value with [PdfXmpMetadata::idx_set()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/idx_set/).
1. Save the resulting PDF with [PdfXmpMetadata](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Data/XMP/XmpValue.h>
#include <Aspose.PDF.Cpp/Facades/DefaultMetadataProperties.h>
#include <Aspose.PDF.Cpp/Facades/PdfXmpMetadata.h>
#include <system/date_time_offset.h>
#include <system/string.h>

namespace Facades::Examples::PDF_XmpMetaData
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void AddXmpMetadata(String inputFile, String outputFile)
	{
		auto xmp = MakeObject<PdfXmpMetadata>();
		xmp->BindPdf(inputFile);
		auto timestamp = MakeObject<XmpValue>(DateTimeOffset::get_UtcNow().ToString(u"o"));
		xmp->Add(DefaultMetadataProperties::CreateDate, timestamp);
		xmp->Add(DefaultMetadataProperties::MetadataDate, timestamp);
		xmp->Add(DefaultMetadataProperties::CreatorTool, MakeObject<XmpValue>(u"Creator tool name"));
		xmp->Remove(DefaultMetadataProperties::ModifyDate);
		xmp->RegisterNamespaceURI(u"customNamespace", u"http://www.customNameSpaces.com/ns/");
		xmp->Add(u"customNamespace:UserPropertyName", MakeObject<XmpValue>(u"UserPropertyValue"));
		xmp->idx_set(u"customNamespace:UserPropertyName", MakeObject<XmpValue>(u"UserPropertyValue2"));
		xmp->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_XmpMetaData
```

## Get XMP metadata

Read expected standard and custom XMP keys, print them, and write a text report.

1. Create [PdfXmpMetadata](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read the metadata value with [PdfXmpMetadata::idx_get()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfxmpmetadata/idx_get/).
1. Write the collected values to the output text file.

```cpp
#include <Aspose.PDF.Cpp/Data/XMP/XmpValue.h>
#include <Aspose.PDF.Cpp/Facades/DefaultMetadataProperties.h>
#include <Aspose.PDF.Cpp/Facades/PdfXmpMetadata.h>
#include <iostream>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_XmpMetaData
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void GetXmpMetadata(String inputFile, String outputFile)
{
    auto xmp = MakeObject<PdfXmpMetadata>();
    xmp->BindPdf(inputFile);
    String report;
    for (auto key : {DefaultMetadataProperties::CreateDate, DefaultMetadataProperties::MetadataDate,
                     DefaultMetadataProperties::CreatorTool})
        report += xmp->idx_get(key)->ToString() + u"\n";
    report += xmp->idx_get(u"customNamespace:UserPropertyName")->ToString() + u"\n";
    std::cout << report << std::endl;
    System::IO::File::WriteAllText(outputFile, report);
}
} // namespace Facades::Examples::PDF_XmpMetaData
```
