---
title: Desencriptar archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/decrypt-pdf-file/
description: Explora métodos para desencriptar archivos PDF protegidos por contraseña en .NET, asegurando el acceso al contenido del documento utilizando Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decrypt PDF File",
    "alternativeHeadline": "Unlock Encrypted PDFs with Ease Using PdfFileSecurity",
    "abstract": "Desbloquea tus documentos PDF sin esfuerzo con la nueva función Desencriptar archivo PDF utilizando la clase PdfFileSecurity. Esta funcionalidad permite a los usuarios eliminar la protección por contraseña de PDFs encriptados, habilitando un acceso y manipulación sin problemas del documento. Experimenta un enfoque sencillo para la gestión de documentos aprovechando el poderoso método DecryptFile para un manejo seguro de PDFs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "235",
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
    "url": "/net/decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Un documento PDF encriptado con una contraseña o certificado debe ser desbloqueado antes de que se pueda realizar otra operación sobre él. Si intentas operar en un documento PDF encriptado, se lanzará una excepción. Después de desbloquear un PDF encriptado, puedes realizar una o más operaciones sobre él.

## Desencriptar archivo PDF usando la contraseña del propietario

{{% alert color="primary" %}}
Prueba en línea <br>
Puedes intentar desbloquear el documento usando Aspose.PDF y obtener los resultados en línea en este enlace:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Para desencriptar un archivo PDF, necesitas crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) y luego llamar al método [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). También necesitas pasar la contraseña del propietario al método [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). El siguiente fragmento de código te muestra cómo desencriptar un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        if (pdfFileInfo.IsEncrypted)
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                // Decrypt PDF document
                fileSecurity.DecryptFile("P@ssw0rd");
                // Save PDF document
                fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
            }
        }
    }
}
```