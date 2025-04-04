---
title: Establecer Privilegios en PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/set-privileges/
description: Descubre cómo modificar los privilegios de usuario en archivos PDF, restringiendo ciertas acciones utilizando Aspose.PDF en .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "Presentando la nueva capacidad de establecer privilegios en archivos PDF existentes utilizando la clase PdfFileSecurity, permitiendo a los usuarios especificar permisos para acciones como imprimir y copiar. Además, los usuarios ahora pueden eliminar fácilmente derechos extendidos de documentos PDF, asegurando un mayor control sobre las modificaciones y la seguridad del documento. Esta funcionalidad simplifica la gestión de PDF mientras mejora el cumplimiento de la seguridad.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "436",
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
    "url": "/net/set-privileges/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Establecer Privilegios en un Archivo PDF Existente

Para establecer los privilegios de un archivo PDF, crea un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesecurity) y llama al método SetPrivilege. Puedes especificar los privilegios utilizando el objeto DocumentPrivilege y luego pasar este objeto al método SetPrivilege. El siguiente fragmento de código te muestra cómo establecer los privilegios de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilege1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege
        fileSecurity.SetPrivilege(privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivileges_out.pdf");
    }
}
```

Consulta el siguiente método especificando una contraseña:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegeWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege and passwords
        fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivilegesPassword_out.pdf");
    }
}
```

## Eliminar la Funcionalidad de Derechos Extendidos del PDF

Los documentos PDF admiten la funcionalidad de derechos extendidos para permitir al usuario final completar datos en campos de formulario utilizando Adobe Acrobat Reader y luego guardar una copia del formulario completado. Sin embargo, esto asegura que el archivo PDF no sea modificado y si se realiza alguna modificación en la estructura del PDF, se pierden los derechos extendidos. Al visualizar dicho documento, se muestra un mensaje de error que indica que los derechos extendidos han sido eliminados porque el documento fue modificado. Recientemente, recibimos un requerimiento para eliminar los derechos extendidos de un documento PDF.

Para eliminar los derechos extendidos de un archivo PDF, se ha añadido un nuevo método llamado RemoveUsageRights() a la clase PdfFileSignature. Otro método llamado ContainsUsageRights() se ha añadido para determinar si el PDF de origen contiene derechos extendidos.

{{% alert color="primary" %}}
A partir de Aspose.PDF for .NET 9.5.0, se han actualizado los nombres de los siguientes métodos. Ten en cuenta que los métodos anteriores aún están en la API, pero han sido marcados como obsoletos y serán eliminados. Por lo tanto, se recomienda intentar utilizar los métodos actualizados.

- El método IsContainSignature(.) fue renombrado a ContainsSignature(..).
- El método IsCoversWholeDocument(..) fue renombrado a CoversWholeDocument(..).
{{% /alert %}}

El siguiente código muestra cómo eliminar los derechos de uso del documento:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveExtendedRights()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
    
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        if (pdfSign.ContainsUsageRights())
        {
            pdfSign.RemoveUsageRights();
        }
        // Save PDF document
        pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
    }
}
```