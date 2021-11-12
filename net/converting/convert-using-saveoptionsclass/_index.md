---
title: Convert PDF using SaveOptions class
linktitle: SaveOptions class
type: docs
weight: 30
url: /net/convert-pdf-using-saveoptionsclass/
lastmod: "2021-11-01"
description: This topic show you how to Aspose.PDF allows to convert PDF to SVG format with SaveOptions class.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

This article teacher you how to convert PDF to <abbr title="Scalable Vector Graphics">SVG</abbr> using C# and SaveOptions class.

{{% alert color="success" %}}
**Try to convert PDF to SVG online**

Aspose.PDF for .NET presents you online free application ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to SVG with Free App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** is a family of specifications of an XML-based file format for two-dimensional vector graphics, both static and dynamic (interactive or animated). The SVG specification is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted and if required, compressed. As XML files, SVG images can be created and edited with any text editor, but it is often more convenient to create them with drawing programs such as Inkscape.

Aspose.PDF for .NET supports the feature to convert SVG image to PDF format and also offers the capability to convert PDF files to SVG format. To accomplish this requirement, the [`SvgSaveOptions`](https://apireference.aspose.com/pdf/net/aspose.pdf/svgsaveoptions/methods/index) class has been introduced into the Aspose.PDF namespace. Instantiate an object of SvgSaveOptions and pass it as a second argument to the [`Document.Save(..)`](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method.

The following code snippet shows the steps for converting a PDF file to SVG format with .NET.

```csharp
public static void ConvertPDFtoSVG()
        {
            // Load PDF document
            Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
            // Instantiate an object of SvgSaveOptions
            SvgSaveOptions saveOptions = new SvgSaveOptions
            {
                // Do not compress SVG image to Zip archive
                CompressOutputToZipArchive = false,
                TreatTargetFileNameAsDirectory = true                
            };
            
            // Save the output in SVG files
            document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
        }
```
