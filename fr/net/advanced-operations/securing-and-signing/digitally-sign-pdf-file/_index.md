---
title: Ajouter une signature numérique ou signer numériquement un PDF en C#
linktitle: Signer numériquement un PDF
type: docs
weight: 10
url: /fr/net/digitally-sign-pdf-file/
description: Signer numériquement des documents PDF en utilisant C# ou VB.NET. Vérifier ou valider les PDF signés numériquement en utilisant C# ou VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Comment signer numériquement un PDF",
    "alternativeHeadline": "Travailler avec des PDF signés numériquement",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, signer numériquement pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Signer numériquement des documents PDF en utilisant C# ou VB.NET. Vérifier ou valider les PDF signés numériquement en utilisant C# ou VB.NET."
}
</script>
Aspose.PDF pour .NET prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe SignatureField. Vous pouvez également certifier un fichier PDF avec un certificat PKCS12. Quelque chose de similaire à [Ajouter des signatures et de la sécurité dans Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Lorsque vous signez un document PDF en utilisant une signature, vous confirmez essentiellement son contenu "tel quel". Par conséquent, tout autre changement effectué par la suite invalide la signature et ainsi, vous sauriez si le document a été modifié. Alors qu'en certifiant un document d'abord, cela vous permet de spécifier les modifications qu'un utilisateur peut apporter au document sans invalider la certification.

En d'autres termes, le document serait toujours considéré comme conservant son intégrité et le destinataire pourrait toujours faire confiance au document. Pour plus de détails, veuillez visiter Certifier et signer un PDF. En général, certifier un document peut être comparé à la signature de code d'un exécutable .NET.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Fonctionnalités de signature Aspose.PDF pour .NET

Nous pouvons utiliser les classes et méthodes suivantes pour la signature de PDF

- Classe [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)
- Énumération [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)
- Propriété [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) dans la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)

## Signer un PDF avec des signatures numériques

```csharp
public static void SignDocument()
{
    string inFile = System.IO.Path.Combine(_dataDir,"DigitallySign.pdf");
    string outFile = System.IO.Path.Combine(_dataDir,"DigitallySign_out.pdf");
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020"); // Utiliser les objets PKCS7/PKCS7Detached
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Enregistrer le fichier PDF de sortie
            signature.Save(outFile);
        }
    }
}
```
## Ajouter un horodatage à la signature numérique

### Comment signer numériquement un PDF avec horodatage

Aspose.PDF pour .NET prend en charge la signature numérique du PDF avec un serveur d'horodatage ou un service Web.

Pour répondre à cette exigence, la classe [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) a été ajoutée à l'espace de noms Aspose.PDF. Veuillez regarder le fragment de code suivant qui obtient l'horodatage et l'ajoute au document PDF :

```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(System.IO.Path.Combine(_dataDir,"SimpleResume.pdf")))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Start2020");
            TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", string.Empty); // Le nom d'utilisateur/le mot de passe peuvent être omis
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Créer l'un des trois types de signature
            signature.Sign(1, "Raison de la signature", "Contact", "Lieu", true, rect, pkcs);
            // Enregistrer le fichier PDF de sortie
            signature.Save(System.IO.Path.Combine(_dataDir, "DigitallySignWithTimeStamp_out.pdf"));
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour la bibliothèque .NET",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
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
```

