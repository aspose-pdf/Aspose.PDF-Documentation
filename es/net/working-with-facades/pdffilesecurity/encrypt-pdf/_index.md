---
title: Cifrar archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/encrypt-pdf-file/
description: Este tema explica cómo cifrar un archivo PDF utilizando la clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "Descubre cómo mejorar la seguridad de tus documentos sensibles con la nueva función de cifrado de PDF utilizando la clase PdfFileSecurity. Esta funcionalidad te permite proteger con contraseña tus archivos PDF, asegurando que solo los usuarios autorizados puedan acceder a ellos. Explora varios tipos de cifrado y algoritmos, incluyendo AES con una longitud de clave de hasta 256 bits, para una protección robusta durante el intercambio y archivo de archivos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "273",
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
    "url": "/net/encrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/encrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Cifrar un documento PDF protege su contenido de accesos no autorizados desde el exterior, especialmente durante el intercambio o archivo de archivos.

Los documentos PDF confidenciales pueden ser cifrados y protegidos con contraseña. Solo los usuarios que conocen la contraseña podrán descifrar, abrir y ver estos documentos.

Veamos cómo funciona el cifrado de PDF con la biblioteca Aspose.PDF.

## Cifrar archivo PDF utilizando diferentes tipos de cifrado y algoritmos

Para cifrar un archivo PDF, necesitas crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesecurity) y luego llamar al método [EncryptFile](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Puedes pasar la contraseña de usuario, la contraseña de propietario y los privilegios al método [EncryptFile](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). También necesitas pasar los valores de KeySize y Algorithm a este método.

Revisa una posible lista de tales [CryptoAlgorithm](https://reference.aspose.com/pdf/es/net/aspose.pdf/cryptoalgorithm):

|**Nombre del miembro**|**Valor**|**Descripción**|
| :- | :- | :- |
|RC4x40|0|RC4 con longitud de clave 40.|
|RC4x128|1|RC4 con longitud de clave 128.|
|AESx128|2|AES con longitud de clave 128.|
|AESx256|3|AES con longitud de clave 256.|

El siguiente fragmento de código te muestra cómo cifrar un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256,
            Aspose.Pdf.Facades.Algorithm.AES);
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleEncrypted_out.pdf");
    }
}
```