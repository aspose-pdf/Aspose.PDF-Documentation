---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 50
url: /python-net/licensing/
description: Aspose.PDF for Python invites its customers to get a Classic license. As well as use a limited license to better explore the product.
lastmod: "2025-02-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Licensing of Aspose.PDF for Python
Abstract: The article discusses the limitations and licensing options for Aspose.PDF for Python. It highlights that the evaluation version allows full functionality testing but adds a watermark to generated PDFs, stating "Evaluation Only" along with copyright information. For users wishing to test without these limitations, a 30-day Temporary License is available. The article further explains how to implement a classic license by loading it from a file or stream, recommending placing the license file in the same directory as the Aspose.PDF.dll file and setting the license using the `Aspose.Pdf.License` class. Code snippets are provided to illustrate the licensing process.
---

## Limitation of an evaluation version

We want our customers to test our components thoroughly before buying so the evaluation version allows you to use it as you would normally.

- **PDF created with an evaluation watermark.** The evaluation version of Aspose.PDF for Python provides full product functionality, but all the pages in the generated PDF documents are watermarked with "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" at the top.

>If you want to test Aspose.PDF without the evaluation version limitations, you can also request a 30-day Temporary License. Please refer to [How to get a Temporary License?](https://purchase.aspose.com/temporary-license)

## Classic license

The license can be loaded from a file or stream object. The easiest way to set a license is to put the license file in the same folder as the Aspose.PDF.dll file and specify the file name without a path, as shown in the example below.

If you use any other Aspose for Python component along with Aspose.PDF for Python, please specify the namespace for License like [Aspose.Pdf.License class]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```
