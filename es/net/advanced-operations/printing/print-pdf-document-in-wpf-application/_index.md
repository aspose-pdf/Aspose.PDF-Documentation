---
title: Imprimir PDF en aplicación WPF
linktitle: Imprimir documento PDF en aplicación WPF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/print-pdf-document-in-wpf-application/
description: C# Imprimir documentos PDF desde una aplicación WPF. Este ejemplo de código muestra cómo imprimir documentos PDF desde una aplicación WPF utilizando C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Print PDF in WPF application",
    "alternativeHeadline": "Print PDF Documents Directly from WPF Applications",
    "abstract": "La nueva función permite la impresión sin problemas de documentos PDF directamente desde una aplicación WPF utilizando C#. Esta funcionalidad permite a los usuarios convertir archivos PDF a formato XPS y imprimirlos de manera eficiente, mejorando las capacidades de gestión de documentos dentro de sus aplicaciones. Con un ejemplo de código sencillo, los desarrolladores pueden implementar fácilmente esta función para optimizar sus procesos de impresión de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Print PDF, WPF application, C# PDF printing, Aspose.PDF library, convert PDF to XPS, direct printing, view PDF document, DocViewer class, MemoryStream object, FixedDocumentSequence",
    "wordcount": "406",
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
    "url": "/net/print-pdf-document-in-wpf-application/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-pdf-document-in-wpf-application/"
    },
    "dateModified": "2024-11-25",
    "description": "C# Imprimir documentos PDF desde una aplicación WPF. Este ejemplo de código muestra cómo imprimir documentos PDF desde una aplicación WPF utilizando C#."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Impresión directa

La biblioteca Aspose.PDF tiene la capacidad de convertir archivos PDF a XPS. Podemos usar esta función para organizar la impresión de documentos.
Consideremos el ejemplo para la impresión directa:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DirectPrintWpf()
{
    // Select a PDF document to print
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(openFileDialog.FileName))
        {
            using (var memoryStream = new MemoryStream())
            {
                // Convert the document to the XPS format
                document.Save(memoryStream, SaveFormat.Xps);
        
                // Create XPS package
                using (var package = Package.Open(memoryStream))
                {
                    //Create URI for the XPS package
                    //Any Uri will actually be fine here. It acts as a placeholder for the
                    //Uri of the package inside the PackageStore
                    var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
                    var packageUri = new Uri(inMemoryPackageName);
        
                    //Add the package to PackageStore
                    PackageStore.AddPackage(packageUri, package);
        
                    // Open the XPS document from the package
                    using (var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName))
                    {
                        // Get the root document sequence
                        var fixedDocumentSequence = xpsDoc.GetFixedDocumentSequence();
        
                        // Open a print dialog to set printing options
                        var printDialog = new PrintDialog();
                        if (printDialog.ShowDialog() == true)
                        {
                            if (fixedDocumentSequence != null)
                            {
                                // Print converted document
                                printDialog.PrintDocument(fixedDocumentSequence.DocumentPaginator,
                                    "A fixed document");
                            }
                        }
        
                        // Remove the package from the store and close the document after the print
                        PackageStore.RemovePackage(packageUri);
                    }
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DirectPrintWpf()
{
    // Select a PDF document to print
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog())
    {
        // Open PDF document
        using var document = new Aspose.Pdf.Document(openFileDialog.FileName);
        
        // Convert the document to the XPS format
        using var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);
        
        // Create XPS package
        using var package = Package.Open(memoryStream);
        
        //Create URI for the XPS package
        //Any Uri will actually be fine here. It acts as a placeholder for the
        //Uri of the package inside the PackageStore
        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);
        
        //Add the package to PackageStore
        PackageStore.AddPackage(packageUri, package);
        
        // Open the XPS document from the package
        using var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        
        // Get the root document sequence
        var fixedDocumentSequence = xpsDoc.GetFixedDocumentSequence();
        
        // Open a print dialog to set printing options
        var printDialog = new PrintDialog();
        if (printDialog.ShowDialog() == true)
        {
            if (fixedDocumentSequence != null)
            {
                // Print converted document
                printDialog.PrintDocument(fixedDocumentSequence.DocumentPaginator,
                    "A fixed document");
            }
        }
        
        // Remove the package from the store and close the document after the print
        PackageStore.RemovePackage(packageUri);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

En este caso, seguiremos estos pasos:

1. Abrir el archivo PDF usando OpenFileDialog.
1. Convertir PDF a XPS y almacenarlo en un objeto MemoryStream.
1. Asociar el objeto MemoryStream con el paquete Xps.
1. Agregar el paquete al Almacén de Paquetes.
1. Crear un XpsDocument basado en el paquete.
1. Obtener una instancia de FixedDocumentSequence.
1. Enviar esta secuencia a la impresora usando PrintDialog.

## Ver y imprimir documento

En muchos casos, los usuarios quieren ver el documento antes de imprimir. Para implementar una vista, podemos usar un control `DocumentViewer`.
La mayoría de los pasos para implementar este enfoque son similares al ejemplo anterior.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PreviewDocumentWithDocumentViewer(DocumentViewer docViewer)
{
    // Select a PDF document to print
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(openFileDialog.FileName))
        {
            using (var memoryStream = new MemoryStream())
            {
                // Convert the document to the XPS format
                document.Save(memoryStream, SaveFormat.Xps);

                // Create XPS package
                using (var package = Package.Open(memoryStream))
                {
                    //Create URI for the XPS package
                    var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
                    var packageUri = new Uri(inMemoryPackageName);

                    //Add package to PackageStore
                    PackageStore.AddPackage(packageUri, package);

                    // Open the XPS document from the package
                    using (var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName))
                    {
                        // Display the document in the DocumentViewer
                        docViewer.Document = xpsDoc.GetFixedDocumentSequence();
                    }
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PreviewDocumentWithDocumentViewer(DocumentViewer docViewer)
{
    // Select a PDF document to print
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        // Open PDF document
        using var document = new Aspose.Pdf.Document(openFileDialog.FileName);

        // Convert the document to the XPS format
        using var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);

        // Create XPS package
        using var package = Package.Open(memoryStream);

        //Create URI for the XPS package
        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Add package to PackageStore
        PackageStore.AddPackage(packageUri, package);

        // Open the XPS document from the package
        using var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);

        // Display the document in the DocumentViewer
        docViewer.Document = xpsDoc.GetFixedDocumentSequence();
    }
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