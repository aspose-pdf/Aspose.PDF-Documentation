---
title: Convert PDF using ImageDevice class 
linktitle: ImageDevice class 
type: docs
weight: 10
url: /net/convert-pdf-using-imagedeviceclass/
lastmod: "2021-11-01"
description: This topic show you how to Aspose.PDF allows to convert PDF to various images formats. Convert PDF pages to PNG, JPEG, BMP images with a few lines of code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for .NET** library allows you to successfully, quickly and easily convert your PDF documents to the most popular Images formats.

This section will show you how to convert PDF documents to image formats such as: BMP, JPEG, GIF, PNG, and EMF formats.

The [BmpDevice](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) class allows you to convert PDF pages to <abbr title="Bitmap Image File">BMP</abbr> images. This class provides a method named [Process](https://apireference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) which allows you to convert a particular page of the PDF file to Bmp image format

The EmfDevice class allows you to convert PDF pages to <abbr title="Enhanced Meta File">EMF</abbr> images. This class provides a method named Process which allows you to convert a particular page of the PDF file to EMF image format.

The JpegDevice class allows you to convert PDF pages to JPEG images. This class provides a method named Process which allows you to convert a particular page of the PDF file to JPEG image format with C#.

The PngDevice class allows you to convert PDF pages to <abbr title="Portable Network Graphics">PNG</abbr>  images. This class provides a method named Process which allows you to convert a particular page of the PDF file to PNG image format.

Use the following code snippets to convert PDF to Image:

```csharp
 public static class ExampleConvertPdfToImage
    {
        private static readonly string _dataDir = @"C:\Samples\";
        // BMP, JPEG, GIF, PNG, EMF
        public static void ConvertPDFusingImageDevice()
        {
            // Create Resolution object            
            Resolution resolution = new Resolution(300);
            BmpDevice bmpDevice = new BmpDevice(resolution);
            JpegDevice jpegDevice = new JpegDevice(resolution);
            GifDevice gifDevice = new GifDevice(resolution);
            PngDevice pngDevice = new PngDevice(resolution);
            EmfDevice emfDevice = new EmfDevice(resolution);

            Document document = new Document(_dataDir + "ConvertAllPagesToBmp.pdf");
            
            ConvertPDFtoImage(bmpDevice, "bmp", document);
            ConvertPDFtoImage(jpegDevice,"jpeg", document);
            ConvertPDFtoImage(gifDevice, "gif", document);
            ConvertPDFtoImage(pngDevice, "png", document);
            ConvertPDFtoImage(emfDevice, "emf", document);
            
        }
```

```csharp
 public static void ConvertPDFtoImage(ImageDevice imageDevice, string ext, Document pdfDocument)
        {
            for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
            {
                using (FileStream imageStream = new FileStream($"{_dataDir}image{pageCount}_out.{ext}", FileMode.Create))
                {
                    // Convert a particular page and save the image to stream
                    imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

                    // Close stream
                    imageStream.Close();
                }
            }
        }
```

{{% alert color="success" %}}
**Try to convert PDF to PNG online**

As an example of how our free applications work please check the next feature.

Aspose.PDF for .NET presents you online free application ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), where you may try to investigate the functionality and quality it works.

[![How to convert PDF to PNG using Free App](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}




