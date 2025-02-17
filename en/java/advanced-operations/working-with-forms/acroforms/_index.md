---
title: Working with AcroForms in PDF 
linktitle: AcroForms
type: docs
weight: 10
url: /java/acroforms/
description: Learn how to work with AcroForms in PDF documents, including form field creation, modification, and data extraction using Aspose.PDF in Java.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to work with AcroForms in PDF documents using Aspose.PDF for Java
Abstract: The article "Fundamentals of AcroForms" explores AcroForms, the original technology for creating PDF forms, introduced by Adobe in 1998. AcroForms are page-oriented and accept inputs in Forms Data Format (FDF) and XML Forms Data Format (xFDF), supported by third-party vendors. AcroForms are highlighted for their portability across platforms and the ability to add pages to a PDF form document through the use of Templates, enabling the integration of multiple database records. The article contrasts AcroForms with Adobe XML Forms Architecture (XFA) forms, highlighting that both are PDF forms but differ in capabilities. AcroForms, included in the PDF 1.2 specification, are known for supporting Templates, whereas XFA forms, introduced in the PDF 1.5 specification, offer document reflow capabilities. The article suggests that PDFs are optimal for electronic form distribution due to their ability to be filled and returned without printing. 
SoftwareApplication: java
---

## Fundamentals of AcroForms

**AcroForms** are the original PDF forms technology. AcroForms is a page oriented form. They were first introduced in 1998. They accept input in Forms Data Format or FDF and XML Forms Data Format or xFDF. Third party vendors support AcroForms. When Adobe introduced the AcroForms, they referred to them as “PDF form that is authored with Adobe Acrobat Pro/Standard and that is not a special type of static or dynamic XFA form. Acroforms are portable and they work on all platforms.

You can use AcroForms to add additional pages to the PDF form document. Thanks to the concept of Templates, you can use AcroForms to support populating the form with multiple database records.

PDF 1.7 supports two different methods for integrating data and PDF forms.

*AcroForms (also known as Acrobat forms)*, introduced and included in the PDF 1.2 format specification.

*Adobe XML Forms Architecture (XFA) forms*, introduced in the PDF 1.5 format specification as an optional feature (The XFA specification is not included in the PDF specification, it is only referenced.

In order to understand **Acroforms** vs **XFA** forms, we need to understand the basics first. For starters, both are PDF forms that you can use. Acroforms is the older one, created back in 1998, and it is still referred as the classic PDF form. XFA forms are webpages you can save as a PDF, and appeared back in 2003. It took some time before PDF started accepting XFA forms.

AcroForms have capabilities not found in XFA and conversely XFA has some capabilities not found in AcroForms.  For example:

- AcroForms support the concept of “Templates”, allowing additional pages to be added to the PDF form document to support populating the form with multiple database records.
- XFA supports the concept of document reflow allowing a field to resize if needed to accommodate data.

So, PDFs are the best file format for forms since they can be distributed electronically and have information filled out within the document and sent back to the sender without needing to print or ship off via traditional mail.

For a more detailed study of the possibilities of working with forms, study the following articles in the section:

-[Create AcroForm](/pdf/java/create-forms/) - create form from scratch, adding RadioButtonField, TextBoxField, Caption Field using Java.

-[Fill AcroForm](/pdf/java/fill-form/) - to fill a form field, get the field from the Document object's Form collection.

-[Extract Data AcroForm](/pdf/java/extract-form/) - get values from all and individual the fields and etc.

-[Modifing AcroForm](/pdf/java/modifing-form/) -  get/set FieldLimit, remove fields in existing form, set form field font other than the 14 Core PDF Fonts with Java.
