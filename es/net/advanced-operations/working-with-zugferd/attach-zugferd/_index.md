---
title: Creando un PDF compatible con PDF/3-A y adjuntando una factura ZUGFeRD en C#
linktitle: Adjuntar ZUGFeRD a PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/attach-zugferd/
description: Aprenda cómo generar un documento PDF con ZUGFeRD en Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "Descubra la nueva funcionalidad que permite a los desarrolladores generar documentos PDF compatibles con PDF/A-3B y adjuntar sin problemas facturas ZUGFeRD utilizando C#. Esta característica simplifica el proceso de incrustar metadatos de factura en archivos PDF, asegurando la preservación a largo plazo de los documentos y el cumplimiento de los estándares de facturación electrónica.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también enfrentar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Adjuntar ZUGFeRD a PDF

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

Recomendamos seguir los siguientes pasos para adjuntar ZUGFeRD a PDF:

* Defina una variable de ruta que apunte a una carpeta donde se encuentran los archivos PDF de entrada y salida.
* Cree un objeto de documento cargando un archivo PDF existente (por ejemplo, "ZUGFeRD-test.pdf") desde la ruta.
* Cree un objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) proporcionando la ruta y la descripción de otro archivo llamado "factur-x.xml", que contiene metadatos de factura conforme al estándar ZUGFeRD.
* Agregue propiedades al objeto de especificación de archivo, como la descripción, el tipo MIME y la relación AF. La relación AF indica cómo se relaciona el archivo incrustado con el documento PDF. En este caso, se establece en "Alternativa", lo que significa que el archivo incrustado es una representación alternativa del contenido PDF.
* Agregue el objeto de especificación de archivo a la colección de archivos incrustados del documento. El nombre del archivo debe especificarse según el estándar ZUGFeRD, por ejemplo, "factur-x.xml".
* Convierta el documento al formato PDF/A-3B, un subconjunto de PDF que asegura la preservación a largo plazo de documentos electrónicos. PDF/A-3B permite incrustar archivos de cualquier formato en documentos PDF.
* Guarde el documento convertido como un nuevo archivo PDF (por ejemplo, "ZUGFeRD-res.pdf").

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

El método de conversión toma un flujo, un formato PDF y una acción de error de conversión como parámetros. El parámetro de flujo se puede usar para guardar el registro de conversión. El parámetro de acción de error de conversión especifica qué hacer si ocurren errores durante la conversión. En este caso, se establece en "Eliminar", lo que significa que cualquier elemento que no cumpla con el formato PDF/A-3B se eliminará del documento.