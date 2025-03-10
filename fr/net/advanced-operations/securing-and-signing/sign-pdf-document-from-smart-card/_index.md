---
title: Comment ajouter une signature de carte intelligente à un PDF
linktitle: Signature PDF avec carte intelligente
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for .NET vous permet de signer des documents PDF à partir d'une carte intelligente en utilisant un champ de signature.
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
    "abstract": "Aspose.PDF for .NET permet désormais une signature PDF transparente utilisant des cartes intelligentes, améliorant la sécurité numérique en permettant aux utilisateurs d'authentifier des documents avec leurs certificats numériques stockés. Cette fonctionnalité prend en charge à la fois les champs de signature et les options de signature avancées, garantissant conformité et intégrité dans les transactions PDF.",
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
    "description": "Aspose.PDF for .NET vous permet de signer des documents PDF à partir d'une carte intelligente en utilisant un champ de signature."
}
</script>

Aspose.PDF for .NET offre la fonctionnalité d'ajouter des signatures numériques à partir d'un emplacement de magasin de clés. Vous pouvez appliquer la signature en acceptant le certificat fourni par le magasin de certificats, la carte intelligente ou la [carte PIV](https://whatis.techtarget.com/definition/personal-identity-verification-PIV-card) connectée au système au moment de l'exécution.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Voici les extraits de code pour signer un document PDF à partir d'une carte intelligente :

## Signer avec une carte intelligente en utilisant un champ de signature

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

## Signer avec une carte intelligente en utilisant la signature de fichier PDF

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

Vous pouvez utiliser la classe ExternalSignature pour un service de signature externe. ExternalSignature crée des signatures PKCS7 et PKCS7 détachées.
Vous pouvez passer l'algorithme de hachage souhaité au constructeur d'ExternalSignature. Notez que les signatures non détachées ne peuvent utiliser que SHA1.
Il sera choisi automatiquement si vous ne spécifiez pas explicitement l'algorithme de hachage. Pour les signatures non détachées, ce sera SHA1 ; pour les détachées, ce sera SHA-256 pour une clé RSA. Pour une clé ECDSA, la taille du hachage dépend de la taille de la clé.

Le constructeur d'ExternalSignature accepte également un certificat de clé (il peut être au format Base64). Vous pouvez passer un certificat contenant une clé privée et un certificat contenant uniquement une clé publique. Dans les deux cas, la signature sera effectuée extérieurement dans le code délégué CustomSignHash, mais l'algorithme externe doit créer une signature correspondant à la clé du certificat passé. Le certificat est nécessaire pour générer correctement le document signé. La signature ECDSA ne prend pas en charge SHA-1.

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

Pour créer une signature, une estimation préliminaire de la longueur de la future signature numérique est requise.
Si vous utilisez SignHash pour créer une signature numérique, vous pouvez constater que le délégué est appelé deux fois pendant le processus de sauvegarde du document.
Si pour une raison quelconque vous ne pouvez pas vous permettre deux appels, par exemple, si une demande de code PIN se produit pendant l'appel, vous pouvez utiliser l'option __AvoidEstimatingSignatureLength__ pour les classes PKCS1, PKCS7, PKCS7Detached et ExternalSignature.
Définir cette option évite l'étape d'estimation de la longueur de la signature en définissant une valeur fixe comme longueur attendue - __DefaultSignatureLength__. La valeur par défaut pour la propriété DefaultSignatureLength est de 3000 octets.
L'option AvoidEstimatingSignatureLength ne fonctionne que si le délégué SignHash est défini dans la propriété CustomSignHash.
Si la longueur de la signature résultante dépasse la longueur attendue spécifiée par la propriété DefaultSignatureLength, vous recevrez une __SignatureLengthMismatchException__ indiquant la longueur réelle.
Vous pouvez ajuster la valeur du paramètre DefaultSignatureLength à votre discrétion.

Pour __ExternalSignature__, l'option AvoidEstimatingSignatureLength peut être utilisée même si CustomSignHash n'est pas utilisé.

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