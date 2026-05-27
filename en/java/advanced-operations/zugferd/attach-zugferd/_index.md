---
title: Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in Java
linktitle: Attach ZUGFeRD to PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Learn how to generate a PDF document with ZUGFeRD in Aspose.PDF for Python via .NET
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to attach ZUGFeRD to a PDF document
Abstract: The article provides a step-by-step guide on how to attach ZUGFeRD (a format for electronic invoices) to a PDF document using the Aspose.PDF library. The procedure begins with importing the necessary library and setting up the directory paths for input and output files. It involves loading the target PDF file into a Document object, and creating a FileSpecification object for the XML invoice metadata file. Key properties like `mime_type` and `af_relationship` are set to ensure proper integration of the metadata. The XML file is then added to the PDF's embedded files collection, effectively attaching it as metadata. Subsequently, the PDF document is converted to the PDF/A-3A format, which is suitable for archiving electronic documents, before saving the final PDF with the embedded ZUGFeRD. The article concludes with a Python code snippet that demonstrates the implementation of these steps, showcasing the integration of ZUGFeRD with a PDF for enhanced document management.
---
