---
title: Attach ZUGFeRD invoice XML to a PDF
linktitle: Attach ZUGFeRD to PDF
type: docs
weight: 10
url: /cpp/attach-zugferd/
description: Attach invoice XML to a PDF in C++, configure associated-file metadata, and convert the document to PDF/A-3A.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Attach Invoice XML with Associated-File Metadata in C++
Abstract: Learn how to embed an existing invoice XML file in a PDF with Aspose.PDF for C++. Configure the attachment MIME type and associated-file relationship, then convert the document to PDF/A-3A.
---

Embed an existing XML invoice in a PDF using Aspose.PDF for C++. The example sets the attachment MIME type and associated-file relationship, adds the XML to the document, and converts the result to PDF/A-3A.

## Attach invoice XML and convert to PDF/A-3A

Supply an existing PDF invoice and its XML data. Configure your project to include and link Aspose.PDF for C++, and create the output directory before running the function.

1. Open the source PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [FileSpecification](https://reference.aspose.com/pdf/cpp/aspose.pdf/filespecification/) with the XML file path and a description.
1. Set the MIME type to text/xml on the [FileSpecification](https://reference.aspose.com/pdf/cpp/aspose.pdf/filespecification/).
1. Set the [AFRelationship](https://reference.aspose.com/pdf/cpp/aspose.pdf/afrelationship/) to Alternative.
1. Add the attachment with [EmbeddedFileCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/embeddedfilecollection/add/) using the key factur.
1. Derive the conversion log path from the output file path.
1. Call [Document::Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/) with [PdfFormat](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfformat/) set to PDF_A_3A and [ConvertErrorAction](https://reference.aspose.com/pdf/cpp/aspose.pdf/converterroraction/) set to Delete.
1. Save the output PDF with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).


```cpp

#include <iostream>
#include <Aspose.PDF.Cpp/AFRelationship.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/EmbeddedFileCollection.h>
#include <Aspose.PDF.Cpp/FileSpecification.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/ConvertErrorAction.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>

using namespace System;
using namespace Aspose::Pdf;

void AttachInvoiceZugferdFormat(System::String inputFile, System::String invoiceFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    String description = u"Invoice metadata conforming to ZUGFeRD standard";
    auto fileSpecification = MakeObject<FileSpecification>(invoiceFile, description);

    fileSpecification->set_MIMEType(u"text/xml");
    fileSpecification->set_AFRelationship(AFRelationship::Alternative);
    document->get_EmbeddedFiles()->Add(u"factur", fileSpecification);

    String logPath = outputFile.Replace(u".pdf", u"_log.xml");
    document->Convert(logPath, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);
    document->Save(outputFile);

    std::cout << "ZUGFeRD invoice attached to " << outputFile << std::endl;
}
```


