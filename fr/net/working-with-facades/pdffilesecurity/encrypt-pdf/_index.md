---
title: Chiffrer un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/encrypt-pdf-file/
description: Ce sujet explique comment chiffrer un fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "Découvrez comment améliorer la sécurité de vos documents sensibles avec la nouvelle fonctionnalité de chiffrement PDF utilisant la classe PdfFileSecurity. Cette fonctionnalité vous permet de protéger par mot de passe vos fichiers PDF, garantissant que seuls les utilisateurs autorisés peuvent y accéder. Explorez différents types et algorithmes de chiffrement, y compris AES avec une longueur de clé allant jusqu'à 256 bits, pour une protection robuste lors du partage et de l'archivage des fichiers.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Chiffrer un document PDF protège son contenu contre l'accès non autorisé de l'extérieur, en particulier lors du partage ou de l'archivage de fichiers.

Les documents PDF confidentiels peuvent être chiffrés et protégés par mot de passe. Seuls les utilisateurs qui connaissent le mot de passe pourront déchiffrer, ouvrir et visualiser ces documents.

Examinons comment fonctionne le chiffrement PDF avec la bibliothèque Aspose.PDF.

## Chiffrer un fichier PDF en utilisant différents types et algorithmes de chiffrement

Pour chiffrer un fichier PDF, vous devez créer un objet [PdfFileSecurity](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesecurity) puis appeler la méthode [EncryptFile](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Vous pouvez passer le mot de passe utilisateur, le mot de passe propriétaire et les privilèges à la méthode [EncryptFile](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Vous devez également passer les valeurs KeySize et Algorithm à cette méthode.

Consultez une liste possible de tels [CryptoAlgorithm](https://reference.aspose.com/pdf/fr/net/aspose.pdf/cryptoalgorithm) :

|**Nom du membre**|**Valeur**|**Description**|
| :- | :- | :- |
|RC4x40|0|RC4 avec une longueur de clé de 40.|
|RC4x128|1|RC4 avec une longueur de clé de 128.|
|AESx128|2|AES avec une longueur de clé de 128.|
|AESx256|3|AES avec une longueur de clé de 256.|

Le code suivant vous montre comment chiffrer un fichier PDF.

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