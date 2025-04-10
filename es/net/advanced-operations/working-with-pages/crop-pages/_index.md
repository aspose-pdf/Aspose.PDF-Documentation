---
title: Recortar páginas PDF programáticamente C#
linktitle: Recortar páginas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /es/net/crop-pages/
description: Puede obtener propiedades de página, como el ancho, la altura, el sangrado, el recorte y el trimbox utilizando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET introduce una poderosa nueva característica que permite a los desarrolladores acceder y manipular programáticamente varias propiedades de página de un PDF, incluyendo el media box, bleed box, trim box, art box y crop box. Esta funcionalidad agiliza el proceso de personalización de diseños PDF, asegurando precisión en la presentación de documentos y mejorando la calidad de impresión mientras minimiza los bordes blancos. Con fragmentos de código fáciles de usar, los usuarios pueden integrar sin problemas estas capacidades en sus aplicaciones, mejorando la gestión y manipulación de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1197",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2025-04-10",
    "description": "Puede obtener propiedades de página, como el ancho, la altura, el sangrado, el recorte y el trimbox utilizando Aspose.PDF for .NET."
}
</script>

## Obtener propiedades de página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, la altura, el sangrado, el recorte y el trimbox. Aspose.PDF le permite acceder a estas propiedades.

- **Media box**: El media box es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo, A4, A5, US Letter, etc.) seleccionado cuando el documento fue impreso en PostScript o PDF. En otras palabras, el media box determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Bleed box**: Si el documento tiene sangrado, el PDF también tendrá un bleed box. El sangrado es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprima y se corte a tamaño ("recortado"), la tinta llegue hasta el borde de la página. Incluso si la página está mal recortada - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Trim box**: El trim box indica el tamaño final de un documento después de imprimir y recortar.
- **Art box**: El art box es la caja dibujada alrededor del contenido real de las páginas en sus documentos. Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: El crop box es el tamaño de "página" en el que se muestra su documento PDF en Adobe Acrobat. En la vista normal, solo se muestran los contenidos del crop box en Adobe Acrobat. Para descripciones detalladas de estas propiedades, lea la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de página.
- **Page.Rect**: la intersección (rectángulo comúnmente visible) del MediaBox y DropBox. La imagen a continuación ilustra estas propiedades.
Para más detalles, visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

El fragmento a continuación muestra cómo recortar la página:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

En este ejemplo utilizamos un archivo de muestra [aquí](crop_page.pdf). Inicialmente, nuestra página se ve como se muestra en la Figura 1.

Después del cambio, la página se verá como en la Figura 2.

### Recortar espacios en blanco alrededor de una página

Por ejemplo, puede recortar espacios en blanco alrededor de una página utilizando cualquier biblioteca gráfica que pueda cargar bitmaps:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TrimWhiteSpaceAroundPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TrimWhiteSpaceAroundPage.pdf"))
    {
        var device = new Aspose.Pdf.Devices.PngDevice(new Resolution(300));

        using (var imageStr = new MemoryStream())
        {
            // Convert page to PNG image
            device.Process(document.Pages[1], imageStr);
            using (var pageBitmap = new Bitmap(imageStr))
            {
                document.Pages[1].CropBox = GetNewCropBox(pageBitmap, document.Pages[1].CropBox);
            }
        }
        // Save PDF document
        document.Save(dataDir + "TrimWhiteSpaceAroundPage_out.pdf");
    }
}

// Determine white areas with System.Drawing
private static Aspose.Pdf.Rectangle GetNewCropBox(Bitmap pageBitmap, Aspose.Pdf.Rectangle prevCropBox)
{
    var imageBitmapData = pageBitmap.LockBits(new Rectangle(0, 0, pageBitmap.Width, pageBitmap.Height),
                            ImageLockMode.ReadOnly, PixelFormat.Format32bppRgb);

    int toHeight = pageBitmap.Height;
    int toWidth = pageBitmap.Width;

    int? leftNonWhite = null;
    int? rightNonWhite = null;
    int? topNonWhite = null;
    int? bottomNonWhite = null;

    var imageRowBytes = new byte[imageBitmapData.Stride];
    for (int y = 0; y < toHeight; y++)
    {

        // Copy the row data to byte array
        if (IntPtr.Size == 4)
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt32() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }
        else
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt64() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }

        int? leftNonWhite_row = null;
        int? rightNonWhite_row = null;

        for (int x = 0; x < toWidth; x++)
        {
            if (imageRowBytes[x * 4] != 255
                || imageRowBytes[x * 4 + 1] != 255
                || imageRowBytes[x * 4 + 2] != 255)
            {
                if (leftNonWhite_row == null)
                {
                    leftNonWhite_row = x;
                }

                rightNonWhite_row = x;
            }
        }

        if (leftNonWhite_row != null || rightNonWhite_row != null)
        {
            if (topNonWhite == null)
            {
                topNonWhite = y;
            }

            bottomNonWhite = y;
        }

        if (leftNonWhite_row != null
            && (leftNonWhite == null || leftNonWhite > leftNonWhite_row))
        {
            leftNonWhite = leftNonWhite_row;
        }
        if (rightNonWhite_row != null
            && (rightNonWhite == null || rightNonWhite < rightNonWhite_row))
        {
            rightNonWhite = rightNonWhite_row;
        }
    }

    leftNonWhite = leftNonWhite ?? 0;
    rightNonWhite = rightNonWhite ?? toWidth;
    topNonWhite = topNonWhite ?? 0;
    bottomNonWhite = bottomNonWhite ?? toHeight;

    double xCoef = prevCropBox.Width / toWidth;
    double yCoef = prevCropBox.Height / toHeight;

    pageBitmap.UnlockBits(imageBitmapData);
    
    // Create crop box with correction to previous crop box
    return
        new Aspose.Pdf.Rectangle(
            leftNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - bottomNonWhite.Value * yCoef,
            rightNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - topNonWhite.Value * yCoef
        );
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TrimWhiteSpaceAroundPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "TrimWhiteSpaceAroundPage.pdf");
    var device = new Aspose.Pdf.Devices.PngDevice(new Resolution(300));

    using var imageStr = new MemoryStream();

    // Convert page to PNG image
    device.Process(document.Pages[1], imageStr);
    using var pageBitmap = new Bitmap(imageStr);
    document.Pages[1].CropBox = GetNewCropBox(pageBitmap, document.Pages[1].CropBox);

    // Save PDF document
    document.Save(dataDir + "TrimWhiteSpaceAroundPage_out.pdf");
}

// Determine white areas with System.Drawing
private static Aspose.Pdf.Rectangle GetNewCropBox(Bitmap pageBitmap, Aspose.Pdf.Rectangle prevCropBox)
{
    var imageBitmapData = pageBitmap.LockBits(new Rectangle(0, 0, pageBitmap.Width, pageBitmap.Height),
                            ImageLockMode.ReadOnly, PixelFormat.Format32bppRgb);

    int toHeight = pageBitmap.Height;
    int toWidth = pageBitmap.Width;

    int? leftNonWhite = null;
    int? rightNonWhite = null;
    int? topNonWhite = null;
    int? bottomNonWhite = null;

    var imageRowBytes = new byte[imageBitmapData.Stride];
    for (int y = 0; y < toHeight; y++)
    {

        // Copy the row data to byte array
        if (IntPtr.Size == 4)
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt32() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }
        else
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt64() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }

        int? leftNonWhite_row = null;
        int? rightNonWhite_row = null;

        for (int x = 0; x < toWidth; x++)
        {
            if (imageRowBytes[x * 4] != 255
                || imageRowBytes[x * 4 + 1] != 255
                || imageRowBytes[x * 4 + 2] != 255)
            {
                if (leftNonWhite_row == null)
                {
                    leftNonWhite_row = x;
                }

                rightNonWhite_row = x;
            }
        }

        if (leftNonWhite_row != null || rightNonWhite_row != null)
        {
            if (topNonWhite == null)
            {
                topNonWhite = y;
            }

            bottomNonWhite = y;
        }

        if (leftNonWhite_row != null
            && (leftNonWhite == null || leftNonWhite > leftNonWhite_row))
        {
            leftNonWhite = leftNonWhite_row;
        }
        if (rightNonWhite_row != null
            && (rightNonWhite == null || rightNonWhite < rightNonWhite_row))
        {
            rightNonWhite = rightNonWhite_row;
        }
    }

    leftNonWhite = leftNonWhite ?? 0;
    rightNonWhite = rightNonWhite ?? toWidth;
    topNonWhite = topNonWhite ?? 0;
    bottomNonWhite = bottomNonWhite ?? toHeight;

    double xCoef = prevCropBox.Width / toWidth;
    double yCoef = prevCropBox.Height / toHeight;

    pageBitmap.UnlockBits(imageBitmapData);
    
    // Create crop box with correction to previous crop box
    return
        new Aspose.Pdf.Rectangle(
            leftNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - bottomNonWhite.Value * yCoef,
            rightNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - topNonWhite.Value * yCoef
        );
}
```
{{< /tab >}}
{{< /tabs >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>