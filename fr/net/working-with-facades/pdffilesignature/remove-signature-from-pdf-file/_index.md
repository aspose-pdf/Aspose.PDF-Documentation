---
title: Supprimer la signature d'un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/remove-signature-from-pdf/
description: Cette section explique comment supprimer une signature d'un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Signature from PDF File",
    "alternativeHeadline": "Effortlessly Remove Signatures from PDF Files",
    "abstract": "La fonctionnalité permet aux utilisateurs de supprimer efficacement les signatures numériques des fichiers PDF en utilisant la classe PdfFileSignature. Cette fonctionnalité offre de la flexibilité, permettant la suppression de signatures spécifiques tout en conservant éventuellement les champs de signature pour une utilisation future, améliorant ainsi les capacités de gestion des documents.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Supprimer la signature numérique du fichier PDF

Lorsqu'une signature a été ajoutée à un fichier PDF, il est possible de la supprimer. Vous pouvez supprimer soit une signature particulière, soit toutes les signatures d'un fichier. La méthode la plus rapide pour supprimer la signature supprime également le champ de signature, mais il est possible de simplement supprimer la signature, en conservant le champ de signature afin que le fichier puisse être signé à nouveau.

La méthode RemoveSignature de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) vous permet de supprimer une signature d'un fichier PDF. Cette méthode prend le nom de la signature comme entrée. Soit spécifiez le nom de la signature directement, pour supprimer toutes les signatures, obtenez les noms des signatures en utilisant la méthode [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

L'extrait de code suivant montre comment supprimer la signature numérique du fichier PDF.

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

### Supprimer la signature mais conserver le champ de signature

Comme indiqué ci-dessus, la méthode [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) vous permet de supprimer des champs de signature des fichiers PDF. Lorsque vous utilisez cette méthode avec des versions antérieures à 9.3.0, la signature et le champ de signature sont tous deux supprimés. Certains développeurs souhaitent supprimer uniquement la signature et conserver le champ de signature afin qu'il puisse être utilisé pour resigné le document. Pour conserver le champ de signature et supprimer uniquement la signature, veuillez utiliser l'extrait de code suivant.

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

L'exemple suivant montre comment supprimer toutes les signatures des champs.

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