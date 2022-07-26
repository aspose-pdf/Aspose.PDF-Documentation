---
title: Working with XFA Forms in PDF 
linktitle: XFA Forms
type: docs
weight: 20
url: /java/xfa-forms/
description: With Aspose.PDF for Java you may create a form from scratch, fill the form field in a PDF document, extract data from the form, add or remove fields in the existing form.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA stands for XML Forms Architecture. It’s a set of proprietary XML specifications built originally for use with web forms in 1999, and has since become available for PDF.

## Convert Dynamic XFA Form to Standard AcroForm

Dynamic forms are based on an XML specification known as XFA, the “XML Forms Architecture”. It can also convert dynamic XFA form to standard Acroform. The information about the form (as far as PDF is concerned) is very vague – it specifies that fields exist, with properties, and JavaScript events, but does not specify any rendering. The objects of XFA form are drawn at the time loading the document.

Currently PDF supports two different methods for integrating data and PDF forms:

- AcroForms (also known as Acrobat forms), introduced and included in the PDF 1.2 format specification.

- Adobe XML Forms Architecture (XFA) forms, introduced in the PDF 1.5 format specification as an optional feature. (The XFA specification is not included in the PDF specification, it is only referenced.)

It’s not possible to extract or manipulate pages of XFA Forms, because the form content is generated at runtime (during XFA form viewing) within the application trying to display or render the XFA form. Aspose.PDF has a feature that allows developers to convert XFA forms to standard AcroForms.

```java
// Load dynamic XFA form
Document document = new Document("XFAform.pdf");
// Set the form fields type as standard AcroForm
document.getForm().setType(FormType.Standard);
// Save the resultant PDF
document.save("Standard_AcroForm.pdf");
```