---
title: Work with PDF pages in C++
linktitle: Working with Pages
type: docs
weight: 20
url: /cpp/working-with-pages/
description: Add, delete, extract, move, resize, crop, rotate, and stamp PDF pages and configure headers and footers using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Add, delete, extract, move, resize, crop, rotate, and stamp PDF pages and configure headers and footers using Aspose.PDF for C++.

- [Add Pages](/pdf/cpp/add-pages/) — Add blank pages, insert a page at a specific position, or copy a page from another PDF using Aspose.PDF for C++.
- [Add Headers and Footers](/pdf/cpp/add-headers-and-footers-of-pdf-file/) — Add text, images, HTML, LaTeX, tables, and page-number placeholders to PDF headers and footers using Aspose.PDF for C++.
- [Change Page Size](/pdf/cpp/change-page-size/) — Read PDF page dimensions, compare rectangles with and without rotation, and set a page size using Aspose.PDF for C++.
- [Crop Pages](/pdf/cpp/crop-pages/) — Change PDF page boxes or crop the first page to its first detected image placement using Aspose.PDF for C++.
- [Delete Pages](/pdf/cpp/delete-pages/) — Remove one page or a selected set of pages from a PDF document using Aspose.PDF for C++.
- [Extract Pages](/pdf/cpp/extract-pages/) — Copy selected PDF pages into a new document while retaining the input file using Aspose.PDF for C++.
- [Get and Set Page Properties](/pdf/cpp/get-and-set-page-properties/) — Inspect page counts, page boxes, rotation, and color types, and calculate a generated document's page count before saving with Aspose.PDF for C++.
- [Move Pages](/pdf/cpp/move-pages/) — Move pages to a new PDF or move a page to the end of its original document using Aspose.PDF for C++.
- [Rotate Pages](/pdf/cpp/rotate-pages/) — Set the rotation of every PDF page to 90 degrees using Aspose.PDF for C++.
- [Stamping](/pdf/cpp/stamping/) — Add image, text, page-number, and PDF-page stamps.

## Use the page examples

Configure your project to include and link Aspose.PDF for C++. Pass existing input PDFs and create output directories before calling the examples. Page numbers are one-based; several examples require two, three, or four pages. Supply image files and make Arial available for examples that use them.

The snippets omit the project-specific working-with-pages.h include. Add the required SDK headers and standard C++ headers to your project. Each source filename identifies the corresponding helper function. The examples that move pages between documents save the destination and the modified source to separate output files.

Use [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) to open the PDF, [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) to manage pages, and [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) to inspect or change individual page properties. Save edited documents with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

