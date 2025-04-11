---
title: Eliminar firma de archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/remove-signature-from-pdf/
description: Esta sección explica cómo eliminar la firma de un archivo PDF utilizando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Signature from PDF File",
    "alternativeHeadline": "Effortlessly Remove Signatures from PDF Files",
    "abstract": "La funcionalidad permite a los usuarios eliminar de manera eficiente firmas digitales de archivos PDF utilizando la clase PdfFileSignature. Esta característica proporciona flexibilidad, permitiendo la eliminación de firmas específicas mientras se conservan opcionalmente los campos de firma para su uso futuro, mejorando las capacidades de gestión de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "434",
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
    "url": "/net/remove-signature-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-signature-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Eliminar firma digital del archivo PDF

Cuando se ha añadido una firma a un archivo PDF, es posible eliminarla. Puede eliminar una firma particular o todas las firmas en un archivo. El método más rápido para eliminar la firma también elimina el campo de firma, pero es posible eliminar solo la firma, manteniendo el campo de firma para que el archivo pueda ser firmado nuevamente.

El método RemoveSignature de la clase [PdfFileSignature](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesignature) le permite eliminar una firma de un archivo PDF. Este método toma el nombre de la firma como entrada. Puede especificar el nombre de la firma directamente, para eliminar todas las firmas, o obtener los nombres de las firmas utilizando el método [GetSignNames](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

El siguiente fragmento de código muestra cómo eliminar la firma digital del archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignature()
{  
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdFileSignature.GetSignNames();
        // Remove all the signatures from the PDF file
        for (int index = 0; index < sigNames.Count; index++)
        {
            Console.WriteLine($"Removed {sigNames[index]}");
            pdFileSignature.RemoveSignature(sigNames[index]);
        }

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```

### Eliminar firma pero mantener el campo de firma

Como se mostró anteriormente, el método [RemoveSignature](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) de la clase [PdfFileSignature](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesignature) le permite eliminar campos de firma de archivos PDF. Al usar este método con versiones anteriores a 9.3.0, tanto la firma como el campo de firma se eliminan. Algunos desarrolladores desean eliminar solo la firma y mantener el campo de firma para que se pueda usar para volver a firmar el documento. Para mantener el campo de firma y eliminar solo la firma, utilice el siguiente fragmento de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignatureButKeepField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {       
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");

        pdFileSignature.RemoveSignature("Signature1", false);

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```

El siguiente ejemplo muestra cómo eliminar todas las firmas de los campos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveSignatureButKeepField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {       
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");

        var sigNames = pdFileSignature.GetSignatureNames();
        foreach (var sigName in sigNames)
        {
            pdFileSignature.RemoveSignature(sigName, false);
        }

        // Save PDF document
        pdFileSignature.Save(dataDir + "RemoveSignature_out.pdf");
    }
}
```