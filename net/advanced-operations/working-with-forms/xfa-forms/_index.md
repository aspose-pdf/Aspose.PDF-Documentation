---
title: Working with XFA Forms using Aspose.PDF for .NET
linktitle: XFA Forms
type: docs
weight: 10
url: /net/xfa-forms/
description: Aspose.PDF for .NET API lets you work with XFA and XFA Acroform fields in a PDF document. The Aspose.PDF.Facades.
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Dynamic forms are based on an XML specification known as XFA, the “XML Forms Architecture”. It can also convert dynamic XFA form to standard Acroform. The information about the form (as far as PDF is concerned) is very vague – it specifies that fields exist, with properties, and JavaScript events, but does not specify any rendering. The objects of XFA form are drawn at the time loading the document.

{{% /alert %}}

Form class provides the capability to deal with static AcroForm and you can get a particular field instance using the Form class’ GetFieldFacade(..) method. However, XFA fields cannot be accessed via the Form.GetFieldFacade(..) method. Instead, use [Document.Form.XFA](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) to get/set field values and manipulate XFA field template (set field properties).

## Fill XFA fields

The following code snippet shows you how to fill fields in XFA form.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Load XFA form
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// Get names of XFA form fields
string[] names = doc.Form.XFA.FieldNames;

// Set field values
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// Save the updated document
doc.Save(dataDir);
```

## Convert XFA-to-Acroform

{{% alert color="primary" %}}

Try online
You can check the quality of Aspose.PDF conversion and view the results online at this link: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Dynamic forms are based on an XML specification known as XFA, the “XML Forms Architecture”. The information about the form (as far as a PDF is concerned) is very vague – it specifies that fields exist, with properties, and JavaScript events, but does not specify any rendering.

Currently, PDF supports two different methods for integrating data and PDF forms:

- AcroForms (also known as Acrobat forms), introduced and included in the PDF 1.2 format specification.
- Adobe XML Forms Architecture (XFA) forms, introduced in the PDF 1.5 format specification as an optional feature (The XFA specification is not included in the PDF specification, it is only referenced.)

We cannot extract or manipulate pages of XFA Forms, because the form content is generated at runtime (during XFA form viewing) within the application trying to display or render the XFA form. Aspose.PDF has a feature that allows developers to convert XFA forms to standard AcroForms.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Load dynamic XFA form
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// Set the form fields type as standard AcroForm
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// Save the resultant PDF
document.Save(dataDir);
```

## Get XFA field properties

To access field properties, first use Document.Form.XFA.Teamplate to access the field template. The following code snippet shows the steps of getting X and Y coordinates of XFA a form field.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Load XFA form
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// Set field values
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";

// Get field position
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// Get field position
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// Save the updated document
doc.Save(dataDir);
```
