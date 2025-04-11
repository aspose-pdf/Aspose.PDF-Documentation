---
title: Trabajando con Firma en Archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/working-with-signature-in-a-pdf-file/
description: Esta sección explica cómo extraer información de la firma, extraer imágenes de la firma, cambiar el idioma, etc. utilizando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Signature in PDF File",
    "alternativeHeadline": "Extract Signature Details and Images from PDFs",
    "abstract": "La nueva funcionalidad en Aspose.PDF for .NET mejora la seguridad de los documentos PDF al permitir a los usuarios extraer información y imágenes de firmas con la clase PdfFileSignature. Esta característica también incluye la capacidad de personalizar firmas digitales, suprimir información específica como ubicación y razón, y cambiar la configuración del idioma para el texto de la firma, proporcionando un conjunto de herramientas integral para gestionar firmas PDF de manera eficiente.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "878",
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
    "url": "/net/working-with-signature-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-signature-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Cómo Extraer Información de la Firma

Aspose.PDF for .NET admite la función de firmar digitalmente archivos PDF utilizando la clase PdfFileSignature. Actualmente, también es posible determinar la validez de un certificado, pero no podemos extraer el certificado completo. La información que se puede extraer es la clave pública, la huella digital y el emisor, etc.

Para extraer información de la firma, hemos introducido el método ExtractCertificate(..) en la clase PdfFileSignature. Por favor, echa un vistazo al siguiente fragmento de código que demuestra los pasos para extraer el certificado del objeto PdfFileSignature:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureInfo()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdfFileSignature.GetSignatureNames();
        if (sigNames.Count > 0)
        {
            SignatureName sigName = sigNames[0];            
            // Extract signature certificate
            Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
            if (cerStream != null)
            {
                using (cerStream)
                {
                    using (FileStream fs = new FileStream(dataDir + "extracted_cert.pfx", FileMode.CreateNew))
                    {
                        cerStream.CopyTo(fs);
                    }
                }
            }
            
        }
    }
}
```

## Extracción de Imagen del Campo de Firma (PdfFileSignature)

Aspose.PDF for .NET admite la función de firmar digitalmente los archivos PDF utilizando la clase PdfFileSignature y, al firmar el documento, también puedes establecer una imagen para SignatureAppearance. Ahora esta API también proporciona la capacidad de extraer información de la firma, así como la imagen asociada con el campo de firma.

Para extraer información de la firma, hemos introducido el método ExtractImage(..) en la clase PdfFileSignature. Por favor, echa un vistazo al siguiente fragmento de código que demuestra los pasos para extraer la imagen del objeto PdfFileSignature:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var signature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        signature.BindPdf(dataDir + "ExtractingImage.pdf");

        if (signature.ContainsSignature())
        {
            // Get list of signature names
            foreach (string sigName in signature.GetSignatureNames())
            {                
                // Extract signature image
                using (Stream imageStream = signature.ExtractImage(sigName))
                {
                    if (imageStream != null)
                    {
                        imageStream.Position = 0;
                        using (FileStream fs = new FileStream(dataDir + "ExtractImages_out.jpg", FileMode.OpenOrCreate))
                        {
                            imageStream.CopyTo(fs);
                        }
                    }
                }
            }
        }
    }
}
```

## Suprimir Ubicación y Razón

La funcionalidad de Aspose.PDF permite una configuración flexible para la instancia de firma digital. La clase [PdfFileSignature](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilesignature) proporciona la capacidad de firmar un archivo PDF. La implementación del método Sign permite firmar el PDF y pasar el objeto de firma particular a esta clase. El método Sign contiene un conjunto de atributos para la personalización de la firma digital de salida. En caso de que necesites suprimir algunos atributos de texto de la firma resultante, puedes dejarlos vacíos. El siguiente fragmento de código demuestra cómo suprimir las dos filas de Ubicación y Razón del bloque de firma:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SupressLocationReason()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
        // Set signature appearance
        pdfFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdfFileSignature.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## Características de Personalización para Firma Digital

Aspose.PDF for .NET permite características de personalización para una firma digital. El método Sign de la clase [SignatureCustomAppearance](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/signaturecustomappearance) se implementa con 6 sobrecargas para tu uso cómodo. Por ejemplo, puedes configurar la firma resultante solo mediante la instancia de la clase SignatureCustomAppearance y los valores de sus propiedades. El siguiente fragmento de código demuestra cómo ocultar la leyenda "Firmado digitalmente por" de la firma digital de salida de tu PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizationFeaturesForDigitalSign()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1
        // Create signature appearance
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            FontSize = 6,
            FontFamilyName = "Times New Roman",
            DigitalSignedLabel = "Signed by:"
        };
        // Set signature appearance
        signature.CustomAppearance = signatureCustomAppearance;

        pdfFileSignature.Sign(1, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## Cambiar el Idioma en el Texto de la Firma Digital

Usando la API Aspose.PDF for .NET, puedes firmar un archivo PDF utilizando cualquiera de los siguientes tres tipos de firmas:

- PKCS#1.
- PKCS#7.
- PKCS#12.

Cada una de las firmas proporcionadas contiene un conjunto de propiedades de configuración implementadas para tu conveniencia (localización, formato de fecha y hora, familia de fuentes, etc.). La clase [SignatureCustomAppearance](https://reference.aspose.com/pdf/es/net/aspose.pdf.forms/signaturecustomappearance) proporciona la funcionalidad correspondiente. El siguiente fragmento de código demuestra cómo cambiar el idioma en el texto de la firma digital:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeLanguageInDigitalSignText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();   
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");
        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

        // Create any of the three signature types
        var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Pruebas Firma",
            ContactInfo = "Contacto Pruebas",
            Location = "Población (Provincia)",
            Date = DateTime.Now
        };
        
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            DateSignedAtLabel = "Fecha",
            DigitalSignedLabel = "Digitalmente firmado por",
            ReasonLabel = "Razón",
            LocationLabel = "Localización",
            FontFamilyName = "Arial",
            FontSize = 10d,
            Culture = System.Globalization.CultureInfo.InvariantCulture,
            DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
        };
        // Set signature appearance
        pkcs.CustomAppearance = signatureCustomAppearance;
        // Sign the PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```