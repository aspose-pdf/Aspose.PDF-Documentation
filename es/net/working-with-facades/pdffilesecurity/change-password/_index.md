---
title: Cambiar la Contraseña de un Archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/change-password/
description: Explora cómo modificar la contraseña de un documento PDF en .NET para mejorar la seguridad del archivo con Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change Password of PDF File",
    "alternativeHeadline": "Securely Change PDF Passwords with Ease",
    "abstract": "Mejora fácilmente la seguridad de tu PDF cambiando su contraseña con la clase PdfFileSecurity. Esta funcionalidad permite a los usuarios modificar tanto las contraseñas de usuario como las de propietario, asegurando una protección robusta contra el acceso no autorizado mientras se gestionan los permisos de manera efectiva. Optimiza la configuración de seguridad de tu documento sin esfuerzo con una implementación sencilla.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "250",
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
    "url": "/net/change-password/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-password/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Cambiar la Contraseña de un Archivo PDF

Para cambiar la contraseña de un archivo PDF, necesitas crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesecurity) y luego llamar al método [ChangePassword](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). Debes pasar la contraseña de propietario existente y las nuevas contraseñas de usuario y propietario al método [ChangePassword](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- La **contraseña de usuario**, si está establecida, es lo que necesitas proporcionar para abrir un PDF. Acrobat/Reader pedirá al usuario que ingrese la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- La **contraseña de propietario**, si está establecida, controla los permisos, como imprimir, editar, extraer, comentar, etc. Acrobat/Reader no permitirá estas acciones según la configuración de permisos. Acrobat requerirá esta contraseña si deseas establecer/cambiar permisos.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo cambiar las contraseñas de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        // Create PdfFileSecurity object if the document is encrypted
        if (pdfFileInfo.IsEncrypted)    
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256);
                // Save PDF document
                fileSecurity.Save(dataDir + "sample_encrtypted1.pdf");
            }
        }
    }
}
```