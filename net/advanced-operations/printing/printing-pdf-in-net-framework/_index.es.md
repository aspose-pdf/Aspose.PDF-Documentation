---
title: Impresión de PDF en .NET Framework
linktitle: Impresión de PDF en .NET Framework
type: docs
weight: 10
url: /net/printing-pdf-in-net-framework/
keywords: "print pdf file c#, c# print pdf"
description: Puede imprimir archivos PDF en la impresora predeterminada utilizando la configuración de impresora y página con C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Impresión de PDF en .NET Framework",
    "alternativeHeadline": "Cómo imprimir PDF en .NET Framework",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, pdf en .NET Framework",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2022-02-04",
    "description": "Puede imprimir archivos PDF en la impresora predeterminada utilizando la configuración de impresora y página con C#."
}
</script>
## **Imprimir archivo PDF en C# - Imprimir archivo PDF en la impresora predeterminada usando las configuraciones de impresora y página**

Este artículo describe cómo imprimir un archivo PDF en la impresora predeterminada utilizando las configuraciones de impresora y página en C#.

La clase [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) permite imprimir un archivo PDF en la impresora predeterminada. Necesitas crear un objeto PdfViewer y abrir el PDF utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Para especificar diferentes configuraciones de impresión, utiliza las clases `PageSettings` y `PrinterSettings`. Finalmente, llama al método [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) para imprimir el PDF en la impresora predeterminada. El siguiente fragmento de código muestra cómo imprimir PDF en la impresora predeterminada con configuraciones de impresora y página.

```csharp
public static void SimplePrint()
{
    // Crear objeto PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Abrir archivo PDF de entrada
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // Establecer atributos para la impresión
    viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
    viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada
    viewer.PrintPageDialog = false;   // No producir el diálogo de número de página al imprimir

    // Crear objetos para configuraciones de impresora y página y PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // Establecer nombre de la impresora
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // Establecer tamaño de página (si es necesario)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Establecer márgenes de página (si es necesario)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Imprimir documento usando configuraciones de impresora y página
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Cerrar el archivo PDF después de imprimir
    viewer.Close();
}
```
Para mostrar un diálogo de impresión, intente usar el siguiente fragmento de código:

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // El código de impresión del documento va aquí
    // Imprimir documento usando configuraciones de impresora y página
    viewer.PrintDocumentWithSettings(pgs, ps);
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


