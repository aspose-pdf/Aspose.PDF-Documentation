---
title: Save PDF document programmatically
linktitle: Save PDF
type: docs
weight: 30
url: /python-net/save-pdf-document/
description: Learn how to save PDF file in Python Aspose.PDF for Python via .NET library. Save PDF document to file system, to stream, and in Web applications.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to save PDF file in Aspose.PDF for Python
Abstract: The article provides guidance on saving PDF documents using the Aspose.PDF library in Python. It covers three main topics - saving a PDF document to the file system, saving to a stream, and saving in PDF/A or PDF/X formats. The document-saving process to the file system and stream involves using the `save()` method from the `Document` class, allowing for straightforward manipulation such as adding pages. For saving in PDF/A or PDF/X formats, the article highlights the ISO standards pertinent to each format, emphasizing their use for archiving and graphics exchange, respectively. It describes the necessity of using the `convert` method to prepare documents for these specific formats before saving. Code snippets are provided to illustrate each process, demonstrating the practical implementation of these tasks.
---

## Save PDF document to file system

You can save the created or manipulated PDF document to file system using [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## Save PDF document to stream

You can also save the created or manipulated PDF document to stream by using overloads of `Save` methods.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## Save PDF/A or PDF/X format

PDF/A is an ISO-standardized version of the Portable Document Format (PDF) for use in archiving and long-term preservation of electronic documents.
PDF/A differs from PDF in that it prohibits features not suitable for long-term archiving, such as font linking (as opposed to font embedding) and encryption. ISO requirements for PDF/A viewers include color management guidelines, embedded font support, and a user interface for reading embedded annotations.

PDF/X is a subset of the PDF ISO standard. The purpose of PDF/X is to facilitate graphics exchange, and it therefore has a series of printing-related requirements which do not apply to standard PDF files.

In both cases, the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method is used to store the documents, while the documents must be prepared using the [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```
