---
title: Vérifier la signature dans un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/verify-signature-in-pdf/
description: Cette section explique comment vérifier la signature dans un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Verify Signature in PDF File",
    "alternativeHeadline": "Verify Signatures in PDF Files Efficiently",
    "abstract": "La fonctionnalité permet aux utilisateurs de vérifier efficacement les signatures dans les fichiers PDF en utilisant la classe PdfFileSignature. Avec des méthodes pour vérifier à la fois l'existence d'une signature et sa validité, cette fonctionnalité simplifie le processus d'assurance de l'authenticité et de l'intégrité des documents. Optimisez la gestion des documents en confirmant sans effort la sécurité de vos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/verify-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/verify-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Vérifier si le fichier PDF est signé à l'aide d'une signature

Pour vérifier si un fichier PDF est signé à l'aide d'une [signature particulière](/pdf/fr/net/working-with-signature-in-a-pdf-file/), utilisez la méthode VerifySigned de la classe [PdfFileSignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature). Cette méthode nécessite le nom de la signature et renvoie true si le PDF est signé avec ce nom de signature. Il est également possible de vérifier qu'un [PDF est signé](/pdf/fr/net/working-with-signature-in-a-pdf-file/), sans vérifier avec quelle signature il est signé.

### Vérifier qu'un PDF est signé avec une signature donnée

Le code suivant vous montre comment vérifier si un PDF est signé à l'aide d'une signature donnée.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSigned()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {      
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.ContainsSignature())
        {
            Console.WriteLine("Document Signed");
        }
    }
}
```

### Vérifier qu'un PDF est signé

Pour déterminer si un fichier est signé, sans fournir le nom de la signature, utilisez le code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSignedWithGivenSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("PDF Signed");
        }
    }
}
```

## Vérifier si la signature est valide

La méthode [VerifySignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature) vous permet de valider une signature particulière. Cette méthode nécessite le nom de la signature en entrée et renvoie true si la signature est valide. Le code suivant vous montre comment valider une signature.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IsPdfSignatureValid()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("Signature Verified");
        }
    }
}
```