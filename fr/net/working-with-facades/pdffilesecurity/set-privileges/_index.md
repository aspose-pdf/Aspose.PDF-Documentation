---
title: Définir des privilèges sur un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/set-privileges/
description: Découvrez comment modifier les privilèges des utilisateurs dans les fichiers PDF, en restreignant certaines actions à l'aide d'Aspose.PDF dans .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "Présentation de la nouvelle capacité à définir des privilèges sur des fichiers PDF existants à l'aide de la classe PdfFileSecurity, permettant aux utilisateurs de spécifier des autorisations pour des actions telles que l'impression et la copie. De plus, les utilisateurs peuvent désormais facilement supprimer des droits étendus des documents PDF, garantissant un meilleur contrôle sur les modifications et la sécurité des documents. Cette fonctionnalité simplifie la gestion des PDF tout en améliorant la conformité en matière de sécurité.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Définir des privilèges sur un fichier PDF existant

Pour définir les privilèges d'un fichier PDF, créez un objet [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) et appelez la méthode SetPrivilege. Vous pouvez spécifier les privilèges à l'aide de l'objet DocumentPrivilege, puis passer cet objet à la méthode SetPrivilege. L'extrait de code suivant vous montre comment définir les privilèges d'un fichier PDF.

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

Voir la méthode suivante en spécifiant un mot de passe :

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

## Supprimer la fonctionnalité de droits étendus du PDF

Les documents PDF prennent en charge la fonctionnalité de droits étendus pour permettre à l'utilisateur final de remplir des données dans des champs de formulaire en utilisant Adobe Acrobat Reader, puis de sauvegarder une copie du formulaire rempli. Cependant, cela garantit que le fichier PDF n'est pas modifié et si une modification de la structure du PDF est effectuée, la fonctionnalité de droits étendus est perdue. Lors de la visualisation d'un tel document, un message d'erreur s'affiche, indiquant que les droits étendus ont été supprimés parce que le document a été modifié. Récemment, nous avons reçu une demande pour supprimer les droits étendus d'un document PDF.

Pour supprimer les droits étendus d'un fichier PDF, une nouvelle méthode nommée RemoveUsageRights() a été ajoutée à la classe PdfFileSignature. Une autre méthode nommée ContainsUsageRights() a été ajoutée pour déterminer si le PDF source contient des droits étendus.

{{% alert color="primary" %}}
À partir de Aspose.PDF for .NET 9.5.0, les noms des méthodes suivantes ont été mis à jour. Veuillez noter que les méthodes précédentes sont toujours dans l'API mais ont été marquées comme obsolètes et seront supprimées. Il est donc recommandé d'essayer d'utiliser les méthodes mises à jour.

- La méthode IsContainSignature(.) a été renommée ContainsSignature(..).
- La méthode IsCoversWholeDocument(..) a été renommée CoversWholeDocument(..).
{{% /alert %}}

Le code suivant montre comment supprimer les droits d'utilisation du document :

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