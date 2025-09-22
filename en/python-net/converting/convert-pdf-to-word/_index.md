---
title: Convert PDF to Microsoft Word Documents in Python
linktitle: Convert PDF to Word 2003/2019
type: docs
weight: 10
url: /python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: Learn how to convert PDF documents to Word format in Python using Aspose.PDF for easy document editing.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Convert PDF to Word in Python
Abstract: This article provides a comprehensive guide on converting PDF files to Microsoft Word formats (DOC and DOCX) using Python, specifically utilizing the Aspose.PDF library. It outlines the advantages of converting PDFs to editable Word documents, enabling easier content manipulation such as text, tables, and images. The article details the process of converting PDF to DOC (Word 97-2003 format) and DOCX, with code snippets demonstrating these conversions through Python. The process involves creating a `Document` object from the PDF and saving it in the desired format using the `save()` method and the `SaveFormat` enumeration. Additionally, it introduces the `DocSaveOptions` class, which allows further customization of the conversion process, such as specifying recognition modes. The article also highlights online applications provided by Aspose.PDF for testing the conversion quality and functionality. The content includes a structured overview and links to corresponding sections for each format.
---

## Convert PDF to DOC

One of the most popular features is the PDF to Microsoft Word DOC conversion, which makes content management easier. **Aspose.PDF for Python via .NET** allows you to convert PDF files not only to DOC but also to DOCX format, easily and efficiently.

The [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) class provides numerous properties that improve the process of converting PDF files to DOC format. Among these properties, Mode enables you to specify the recognition mode for PDF content. You can specify any value from the RecognitionMode enumeration for this property. Each of these values has specific benefits and limitations:

Steps: Convert PDF to DOC in Python

1. Load the PDF into an 'ap.Document' object.
1. Create a 'DocSaveOptions' instance.
1. Set the format property to 'DocFormat.DOC' to ensure the output is in .doc format (older Word format).
1. Save the PDF as a Word document using the specified save options.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Try to convert PDF to DOC online**

Aspose.PDF for Python presents you online free application ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), where you may try to investigate the functionality and quality it works.

[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convert PDF to DOCX

Aspose.PDF for Python API lets you read and convert PDF documents to DOCX using Python via .NET. DOCX is a well-known format for Microsoft Word documents whose structure was changed from plain binary to a combination of XML and binary files. Docx files can be opened with Word 2007 and lateral versions but not with the earlier versions of MS Word which support DOC file extensions.

The following Python code snippet shows the process of converting a PDF file into DOCX format.

Steps: Convert PDF to DOCX in Python

1. Load the source PDF using 'ap.Document'.
1. Create an instance of 'DocSaveOptions'.
1. Set the format property to 'DocFormat.DOC_X' to generate a .docx file (modern Word format).
1. Save the PDF as a DOCX file with the configured save options.
1. Print a confirmation message after conversion.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

The [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) class has a property named Format which provides the capability to specify the format of the resultant document, that is, DOC or DOCX. In order to convert a PDF file to DOCX format, please pass the Docx value from the DocSaveOptions.DocFormat enumeration.

{{% alert color="warning" %}}
**Try to convert PDF to DOCX online**

Aspose.PDF for Python presents you online free application ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}
