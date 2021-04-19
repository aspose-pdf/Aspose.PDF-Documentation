---
title: Working with AcroForms in PDF using Aspose.PDF for .NET
linktitle: AcroForms
type: docs
weight: 10
url: /net/acroforms/
description: With Aspose.PDF for .NET you may create a form from scratch, fill the form field in a PDF document, extract data from the form, add or remove fields in the existing form.
lastmod: "2021-04-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
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

For more detailed learning of the capabilities of the Java library, see the following articles:

- [Create Form](/pdf/net/create-form) - create form from scratch with C#.
- [Fill Form](/pdf/net/fill-form) - fill form field in your PDF document. 
- [Extract Form](/pdf/net/extract-form) - get value from all or an individual field of PDF document.
- [Modifing Form](/pdf/net/modifing-form) - get or set FieldLimit, set form field font and etc.
- [Posting AcroForm Data](/pdf/net/posting-acroform-data/) -  import and export form data to and XML file.
