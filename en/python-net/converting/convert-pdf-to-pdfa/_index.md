---
title: Convert PDF to PDF/A formats in Python
linktitle: Convert PDF to PDF/A formats
type: docs
weight: 100
url: /python-net/convert-pdf-to-pdfa/
lastmod: "2025-02-27"
description: Learn how to convert PDF files to PDF/A format for compliance with archiving standards using Aspose.PDF in Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to convert PDF to PDF/A format using Aspose.PDF for Python
Abstract: The article describes the process of converting a PDF file to a PDF/A compliant format using Aspose.PDF for Python. It emphasizes the necessity of validating the PDF file before conversion, following Adobe Preflight to ensure PDF/A conformance. The validation process involves storing results in an XML file, which is then used during conversion through the `Convert` method of the Document class. The article highlights the ability to specify actions for elements that cannot be converted using the `ConvertErrorAction` enumeration. Additionally, it introduces an online application, "PDF to PDF/A-1A", allowing users to explore the functionality and quality of Aspose.PDF's conversion process. A code snippet is provided to demonstrate converting a PDF to a PDF/A-1b compliant file using Aspose.PDF for Python.
---

**Aspose.PDF for Python** allows you to convert a PDF file to a <abbr title="Portable Document Format / A">PDF/A</abbr> compliant PDF file. Before doing so, the file must be validated. This topic explains how.

{{% alert color="primary" %}}

Please note we follow Adobe Preflight for validating PDF/A conformance. All tools on the market have their own “representation” of PDF/A conformance. Please check this article on PDF/A validation tools for reference. We chose Adobe products for verifying how Aspose.PDF produces PDF files because Adobe is at the center of everything connected to PDF.

{{% /alert %}}

Convert the file using the Document class Convert method. Before converting the PDF to PDF/A compliant file, validate the PDF using the Validate method. The validation result is stored in an XML file and then this result is also passed to the Convert method. You can also specify the action for the elements which cannot be converted using the ConvertErrorAction enumeration.

{{% alert color="success" %}}
**Try to convert PDF to PDF/A online**

Aspose.PDF for Python presents you online free application ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Convert PDF file to PDF/A-1b

The following code snippet shows how to convert PDF files to PDF/A-1b compliant PDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import pydicom

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, "python", outfile)

    document = apdf.Document(path_infile)
    document.convert(
        self.dataDir + "pdf_pdfa.log",
        apdf.PdfFormat.PDF_A_1B,
        apdf.ConvertErrorAction.DELETE,
    )
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

