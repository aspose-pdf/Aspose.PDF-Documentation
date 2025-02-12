---
title: Working with XFA Forms in PDF 
linktitle: XFA Forms
type: docs
weight: 20
url: /java/xfa-forms/
description: Explore how to handle XFA forms in PDF documents, including form data processing and conversion, with Aspose.PDF in Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Overview of XML Forms Architecture and its application in PDF forms
Abstract: This article provides an overview of XML Forms Architecture (XFA) and its application in PDF forms, specifically focusing on the conversion of dynamic XFA forms to standard AcroForms. XFA, introduced in 1999, is a proprietary XML specification used for web forms and later adapted for PDFs. PDF documents support two types of forms - AcroForms, introduced in PDF 1.2, and XFA forms, included as an optional feature in PDF 1.5. Unlike AcroForms, XFA forms generate content at runtime, complicating content extraction and manipulation. The article discusses a solution using Aspose.PDF, a tool that allows developers to convert XFA forms into AcroForms, which are more static and standardized. The conversion process is illustrated with a Java code snippet that demonstrates loading a dynamic XFA form, setting the form type to AcroForm, and saving the transformed document.
SoftwareApplication: java   
---

XFA stands for XML Forms Architecture. It's a set of proprietary XML specifications built originally for use with web forms in 1999, and has since become available for PDF.

## Convert Dynamic XFA Form to Standard AcroForm

Dynamic forms are based on an XML specification known as XFA, the “XML Forms Architecture”. It can also convert dynamic XFA form to standard Acroform. The information about the form (as far as PDF is concerned) is very vague – it specifies that fields exist, with properties, and JavaScript events, but does not specify any rendering. The objects of XFA form are drawn at the time loading the document.

Currently PDF supports two different methods for integrating data and PDF forms:

- AcroForms (also known as Acrobat forms), introduced and included in the PDF 1.2 format specification.

- Adobe XML Forms Architecture (XFA) forms, introduced in the PDF 1.5 format specification as an optional feature. (The XFA specification is not included in the PDF specification, it is only referenced.)

It's not possible to extract or manipulate pages of XFA Forms, because the form content is generated at runtime (during XFA form viewing) within the application trying to display or render the XFA form. Aspose.PDF has a feature that allows developers to convert XFA forms to standard AcroForms.

```java
// Load dynamic XFA form
Document document = new Document("XFAform.pdf");
// Set the form fields type as standard AcroForm
document.getForm().setType(FormType.Standard);
// Save the resultant PDF
document.save("Standard_AcroForm.pdf");
```