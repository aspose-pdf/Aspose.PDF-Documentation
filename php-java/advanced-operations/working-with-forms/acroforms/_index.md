---
title: Working with AcroForms in PDF 
linktitle: AcroForms
type: docs
weight: 10
url: /php-java/acroforms/
description: With Aspose.PDF for PHP via Java you may create a form from scratch, fill the form field in a PDF document, extract data from the form, add or remove fields in the existing form.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Fundamentals of AcroForms

**AcroForms** are the original PDF forms technology. AcroForms is a page oriented form. They were first introduced in 1998. They accept input in Forms Data Format or FDF and XML Forms Data Format or xFDF. Third party vendors support AcroForms. When Adobe introduced the AcroForms, they referred to them as “PDF form that is authored with Adobe Acrobat Pro/Standard and that is not a special type of static or dynamic XFA form. Acroforms are portable and they work on all platforms.

You can use AcroForms to add additional pages to the PDF form document. Thanks to the concept of Templates, you can use AcroForms to support populating the form with multiple database records.

PDF 1.7 supports two different methods for integrating data and PDF forms.

*AcroForms (also known as Acrobat forms)*, introduced and included in the PDF 1.2 format specification.

*Adobe XML Forms Architecture (XFA) forms*, introduced in the PDF 1.5 format specification as an optional feature The XFA specification is not included in the PDF specification, it is only referenced.

In order to understand **Acroforms** vs **XFA** forms, we need to understand the basics first. For starters, both are PDF forms that you can use. Acroforms is the older one, created back in 1998, and it is still referred as the classic PDF form. XFA forms are webpages you can save as a PDF, and appeared back in 2003. It took some time before PDF started accepting XFA forms.

AcroForms have capabilities not found in XFA and conversely XFA has some capabilities not found in AcroForms.  For example:

- AcroForms support the concept of “Templates”, allowing additional pages to be added to the PDF form document to support populating the form with multiple database records.
- XFA supports the concept of document reflow allowing a field to resize if needed to accommodate data.

So, PDFs are the best file format for forms since they can be distributed electronically and have information filled out within the document and sent back to the sender without needing to print or ship off via traditional mail.

For a more detailed study of the possibilities of working with forms, study the following articles in the section:

-[Create AcroForm](/pdf/php-java/create-form/) - create form from scratch, adding RadioButtonField, TextBoxField, Caption Field using PHP.

-[Fill AcroForm](/pdf/php-java/fill-form/) - to fill a form field, get the field from the Document object's Form collection.

-[Extract Data AcroForm](/pdf/php-java/extract-form/) - get values from all and individual the fields and etc.

-[Modifing AcroForm](/pdf/php-java/modifing-form/) -  get/set FieldLimit, remove fields in existing form, set form field font other than the 14 Core PDF Fonts with PHP.
