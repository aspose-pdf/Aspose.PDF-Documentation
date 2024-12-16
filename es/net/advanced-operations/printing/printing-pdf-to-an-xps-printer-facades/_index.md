---
title: Impresión de PDF en una impresora XPS
linktitle: Impresión de PDF en una impresora XPS (Facades)
type: docs
weight: 20
url: /es/net/printing-pdf-to-an-xps-printer-facades/
description: Esta página muestra cómo imprimir PDF en una impresora XPS utilizando la clase PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Impresión de PDF en una impresora XPS",
    "alternativeHeadline": "Cómo imprimir PDF en una impresora XPS",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, pdf a una impresora XPS",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta página muestra cómo imprimir PDF en una impresora XPS utilizando la clase PdfViewer."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## **Imprimir PDF en impresora XPS en C#**

Puedes imprimir un archivo PDF en una impresora XPS, o en alguna otra impresora virtual, utilizando la clase [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Para hacer esto, crea un objeto de la clase PdfViewer y abre el archivo PDF utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Puedes configurar diferentes ajustes de impresión utilizando las clases PrinterSettings y PageSettings. También necesitas establecer la propiedad PrinterName en la impresora XPS u otra impresora virtual que tengas instalada.

Finalmente, usa el método [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) para imprimir el PDF en la impresora XPS u otra impresora virtual. El siguiente fragmento de código te muestra cómo imprimir el archivo PDF en una impresora XPS.

```csharp
public static void PrintToXpsPrinter()
{
    // Crear objeto PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Abrir archivo PDF de entrada
    viewer.BindPdf(_dataDir + "input.pdf");

    // Establecer atributos para la impresión
    viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
    viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada
    viewer.PrintPageDialog = false;   // No mostrar el diálogo de número de página al imprimir

    // Crear objetos para la configuración de impresora y página y PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Establecer nombre de la impresora XPS/PDF
    ps.PrinterName = "Microsoft XPS Document Writer";
    // O establecer la impresora PDF
    // Ps.PrinterName = "Adobe PDF";

    // Establecer tamaño de página (si es necesario)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Establecer márgenes de página (si es necesario)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Imprimir documento usando configuración de impresora y página
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Cerrar el archivo PDF después de imprimir
    viewer.Close();
}
```

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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
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
```

