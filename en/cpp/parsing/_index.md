---
title: Parse PDF documents
linktitle: Parse PDF documents
type: docs
weight: 80
url: /cpp/parsing/
description: Extract text, images, font information, tables, AcroForm values, and vector graphics from PDF documents in C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Parse PDF documents with Aspose.PDF for C++ to read text, image resources, font information, table data, form values, and vector graphics. The examples in this section demonstrate extraction and inspection tasks for these types of content.

- [Extract Text from PDF](/pdf/cpp/extract-text-from-pdf/) — Extract text from documents, pages, regions, and annotations.
- [Extract Images from PDF](/pdf/cpp/extract-images-from-the-pdf-file/) — Save an embedded image resource from a PDF page as JPEG using Aspose.PDF for C++.
- [Extract Fonts from PDF](/pdf/cpp/extract-fonts-from-pdf/) — List the names of fonts used in a PDF document with Aspose.PDF for C++.
- [Extract Data from Table](/pdf/cpp/extract-data-from-table-in-pdf/) — Read detected PDF tables, filter them by a marked region, or convert the document to Excel with Aspose.PDF for C++.
- [Extract Data from AcroForm](/pdf/cpp/extract-data-from-acroform/) — Read PDF form fields and export values to XML, FDF, XFDF, or a JSON-style file using Aspose.PDF for C++.
- [Extract Vector Data from PDF](/pdf/cpp/extract-vector-data-from-pdf/) — Inspect vector graphics properties and export page or element graphics to SVG with Aspose.PDF for C++.

## Use the parsing examples

Configure your project to include and link Aspose.PDF for C++ before calling the helper functions. Supply existing input PDFs, valid page and resource indices, and writable output paths. Some examples inspect only the first page or one selected resource; their accompanying steps describe that scope.

The snippets retain the supplied example implementations and omit the project-specific parsing.h include. Add the required SDK headers and namespace declarations to your project. The paragraph geometry example remains commented out as in the supplied source.

Most examples open a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and use an absorber or a resource collection to inspect its content. Follow the API links in each procedure for class and method details.
