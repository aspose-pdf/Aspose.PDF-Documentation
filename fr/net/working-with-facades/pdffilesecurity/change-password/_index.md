---
title: Changer le mot de passe d'un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/change-password/
description: Découvrez comment modifier le mot de passe d'un document PDF en .NET pour améliorer la sécurité des fichiers avec Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change Password of PDF File",
    "alternativeHeadline": "Securely Change PDF Passwords with Ease",
    "abstract": "Améliorez facilement la sécurité de votre PDF en changeant son mot de passe avec la classe PdfFileSecurity. Cette fonctionnalité permet aux utilisateurs de modifier à la fois les mots de passe utilisateur et propriétaire, garantissant une protection robuste contre l'accès non autorisé tout en gérant efficacement les autorisations. Optimisez vos paramètres de sécurité de document sans effort avec une mise en œuvre simple.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Changer le mot de passe d'un fichier PDF

Pour changer le mot de passe d'un fichier PDF, vous devez créer un objet [PdfFileSecurity](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesecurity) puis appeler la méthode [ChangePassword](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). Vous devez passer le mot de passe propriétaire existant ainsi que les nouveaux mots de passe utilisateur et propriétaire à la méthode [ChangePassword](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- Le **mot de passe utilisateur**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à un utilisateur d'entrer le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
- Le **mot de passe propriétaire**, s'il est défini, contrôle les autorisations, telles que l'impression, l'édition, l'extraction, les commentaires, etc. Acrobat/Reader interdira ces actions en fonction des paramètres d'autorisation. Acrobat exigera ce mot de passe si vous souhaitez définir/changer les autorisations.

{{% /alert %}}

Le code suivant vous montre comment changer les mots de passe d'un fichier PDF.

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