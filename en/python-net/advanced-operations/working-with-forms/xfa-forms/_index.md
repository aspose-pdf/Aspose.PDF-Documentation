---
title: Working with XFA Forms
linktitle: XFA Forms
type: docs
weight: 20
url: /python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API lets you work with XFA and XFA Acroform fields in a PDF document.
lastmod: "2025-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

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

```python

```

## Use of IgnoreNeedsRendering

In some cases (e.g, in the case of a static XFA form), conversion to AcroForm may suffer from the disabled NeedsRendering flag that signals that the form isn’t dynamically rendered. To convert such forms and remove the XFA form, it’s recommended to use the IgnoreNeedsRendering property to count the document as dynamically rendered and to calculate element conversion properly.