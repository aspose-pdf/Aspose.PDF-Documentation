---
title: Cómo agregar una firma de tarjeta inteligente a un PDF
linktitle: Firma de PDF con tarjeta inteligente
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for .NET te permite firmar documentos PDF desde una tarjeta inteligente utilizando un campo de firma.
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to add Smart Card signature to PDF",
    "alternativeHeadline": "Add Smart Card Signatures to PDF Documents Easily",
    "abstract": "Aspose.PDF for .NET ahora permite la firma de PDF sin problemas utilizando tarjetas inteligentes, mejorando la seguridad digital al permitir a los usuarios autenticar documentos con sus certificados digitales almacenados. Esta funcionalidad admite tanto campos de firma como opciones de firma avanzadas, asegurando cumplimiento e integridad en las transacciones PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Smart Card signature, PDF signing, Aspose.PDF for .NET, digital signatures, external signing service, PKCS7 signature, certificate selection, hash algorithm, signature field, signing PDF documents",
    "wordcount": "755",
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
    "url": "/net/sign-pdf-document-from-smart-card/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sign-pdf-document-from-smart-card/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET te permite firmar documentos PDF desde una tarjeta inteligente utilizando un campo de firma."
}
</script>

Aspose.PDF for .NET ofrece la funcionalidad de agregar firmas digitales desde una ubicación de almacén de claves. Puedes aplicar la firma aceptando el certificado proporcionado por el almacén de certificados, tarjeta inteligente o [tarjeta PIV](https://whatis.techtarget.com/definition/personal-identity-verification-PIV-card) conectada al sistema en tiempo de ejecución.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

A continuación se presentan los fragmentos de código para firmar un documento PDF desde una tarjeta inteligente:

## Firmar con tarjeta inteligente usando campo de firma

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetSignatureInfo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open a document stream
    using (var fs = new FileStream(dataDir + "blank.pdf", FileMode.Open, FileAccess.ReadWrite))
    {
        // Open PDF document from stream
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create a signature field
            var field1 = new Aspose.Pdf.Forms.SignatureField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 10, 10));

            // Sign with certificate selection in the windows certificate store
            var store = new X509Store(StoreLocation.CurrentUser);
            store.Open(OpenFlags.ReadOnly);
            
            // Manually chose the certificate in the store
            var sel = X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, X509SelectionFlag.SingleSelection);

            // Set an external signature settings
            var externalSignature = new Aspose.Pdf.Forms.ExternalSignature(sel[0])
            {
                Authority = "Me",
                Reason = "Reason",
                ContactInfo = "Contact"
            };
            // Set a name of signature field
            field1.PartialName = "sig1";
            // Add the signature field to the document
            document.Form.Add(field1, 1);
            // Sign the document
            field1.Sign(externalSignature);
            // Save PDF document
            document.Save(dataDir + "externalSignature1_out.pdf");
        }
    }
}

private static void VerifyExternalSignature()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "externalSignature1.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = pdfSign.GetSignatureNames();
            for (int index = 0; index <= sigNames.Count - 1; index++)
            {
                if (!pdfSign.VerifySignature(sigNames[index]))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

## Firmar con tarjeta inteligente usando firma de archivo PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void SignWithSmartCard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
        {   
            // Bind PDF document
            pdfSign.BindPdf(document);

            // Sign with certificate selection in the windows certificate store
            var store = new X509Store(StoreLocation.CurrentUser);
            store.Open(OpenFlags.ReadOnly);
            // Manually chose the certificate in the store
            var sel = X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, X509SelectionFlag.SingleSelection);
            
            // Set an external signature settings
            var externalSignature = new Aspose.Pdf.Forms.ExternalSignature(sel[0]);
            pdfSign.SignatureAppearance = dataDir + "demo.png";
            // Sign the document
            pdfSign.Sign(1, "Reason", "Contact", "Location", true, new System.Drawing.Rectangle(100, 100, 200, 200), externalSignature);
            // Save PDF document
            pdfSign.Save(dataDir + "externalSignature2_out.pdf");
        }
    }
}

private static void VerifyExternalSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "externalSignature1.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = pdfSign.GetSignatureNames();
            for (int index = 0; index <= sigNames.Count - 1; index++)
            {
                if (!pdfSign.VerifySignature(sigNames[index]))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

Puedes usar la clase ExternalSignature para un servicio de firma externo. ExternalSignature crea firmas PKCS7 y firmas PKCS7 separadas.
Puedes pasar el algoritmo de hash deseado al constructor de ExternalSignature. Ten en cuenta que las firmas no separadas solo pueden usar SHA1.
Se elegirá automáticamente si no especificas explícitamente el algoritmo de hash. Para firmas no separadas, será SHA1; para separadas, será SHA-256 para una clave RSA. Para una clave ECDSA, el tamaño del hash depende del tamaño de la clave.

El constructor de ExternalSignature también acepta un certificado de clave (puede estar en formato Base64). Puedes pasar un certificado que contenga una clave privada y un certificado que contenga solo una clave pública. En cualquier caso, la firma se realizará externamente en el código delegado CustomSignHash, pero el algoritmo externo debe crear una firma correspondiente a la clave del certificado pasado. El certificado es necesario para generar el documento firmado correctamente. La firma ECDSA no admite SHA-1.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithExternalService()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
        {
            // Bind PDF document
            sign.BindPdf(document);

            // Get public certificate
            X509Certificate2 signerCert = GetPublicCertificate();

            // Set a certificate and a digest algorithm
            var signature = new Aspose.Pdf.Forms.ExternalSignature(signerCert, Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Define a delegate to external sign
            Aspose.Pdf.Forms.SignHash customSignHash = delegate(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
            {
                return CallExternalSignatureService(signableHash, digestHashAlgorithm);
            };
            // Set a sign hash
            signature.CustomSignHash = customSignHash;
            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), signature);
            // Save PDF document
            sign.Save(dataDir + "ExternalSignature_out.pdf");
        }
    }
}

private static X509Certificate2 GetPublicCertificate()
{
    // Your code to get a public certificate. The certificate can be supplied by a third-party service or a smart card
}

private static byte[] CallExternalSignatureService(byte[] hash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
{
    // Call a third-party service that provides a digital signature service
    // The method must return signed data
    // The digestHashAlgorithm argument points to the digest algorithm that was applied to the data to produce the value of the hash argument
}
```

Para crear una firma, se requiere una estimación preliminar de la longitud de la futura firma digital.
Si usas SignHash para crear una firma digital, puedes encontrar que el delegado se llama dos veces durante el proceso de guardado del documento.
Si por alguna razón no puedes permitirte dos llamadas, por ejemplo, si ocurre una solicitud de código PIN durante la llamada, puedes usar la opción __AvoidEstimatingSignatureLength__ para las clases PKCS1, PKCS7, PKCS7Detached y ExternalSignature.
Configurar esta opción evita el paso de estimación de longitud de la firma al establecer un valor fijo como la longitud esperada - __DefaultSignatureLength__. El valor predeterminado para la propiedad DefaultSignatureLength es 3000 bytes.
La opción AvoidEstimatingSignatureLength solo funciona si el delegado SignHash está configurado en la propiedad CustomSignHash.
Si la longitud de la firma resultante excede la longitud esperada especificada por la propiedad DefaultSignatureLength, recibirás una __SignatureLengthMismatchException__ que indica la longitud real.
Puedes ajustar el valor del parámetro DefaultSignatureLength a tu discreción.

Para __ExternalSignature__, la opción AvoidEstimatingSignatureLength se puede usar incluso si no se utiliza CustomSignHash.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithExternalService()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
        {
            // Bind PDF document
            sign.BindPdf(document);

            // Get public certificate
            X509Certificate2 signerCert = GetPublicCertificate();

            // Set a certificate and a digest algorithm
            var signature = new Aspose.Pdf.Forms.ExternalSignature(signerCert, Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Define a delegate to external sign
            Aspose.Pdf.Forms.SignHash customSignHash = delegate(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
            {
                return CallExternalSignatureService(signableHash, digestHashAlgorithm);
            };
            // Set a sign hash
            signature.CustomSignHash = customSignHash;

            // Set an option to avoiding twice SignHash calling.
            signature.AvoidEstimatingSignatureLength = true;
            signature.DefaultSignatureLength = 3500;

            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), signature);
            // Save PDF document
            sign.Save(dataDir + "ExternalSignature_out.pdf");
        }
    }
}

private static X509Certificate2 GetPublicCertificate()
{
    // Your code to get a public certificate. The certificate can be supplied by a third-party service or a smart card
}

private static byte[] CallExternalSignatureService(byte[] hash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
{
    // Call a third-party service that provides a digital signature service
    // The method must return signed data
    // The digestHashAlgorithm argument points to the digest algorithm that was applied to the data to produce the value of the hash argument
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