---
title: Définir des privilèges, chiffrer et déchiffrer un PDF
linktitle: Chiffrer et déchiffrer un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Chiffrer un fichier PDF avec C# en utilisant différents types et algorithmes de chiffrement. De plus, déchiffrer des fichiers PDF en utilisant le mot de passe propriétaire.
lastmod: "2024-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges, Encrypt and Decrypt PDF",
    "alternativeHeadline": "Set PDF Privileges and Secure with Encryption with C#",
    "abstract": "La nouvelle fonctionnalité permet aux utilisateurs de chiffrer et de déchiffrer efficacement des fichiers PDF en utilisant C# avec une variété de types et d'algorithmes de chiffrement. En utilisant les mots de passe utilisateur et propriétaire, elle offre un contrôle robuste sur l'accès et les autorisations des documents, garantissant la confidentialité et l'intégrité du contenu PDF tout en simplifiant la gestion de la sécurité pour les développeurs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1586",
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
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Chiffrer un fichier PDF avec C# en utilisant différents types et algorithmes de chiffrement. De plus, déchiffrer des fichiers PDF en utilisant le mot de passe propriétaire."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Définir des privilèges sur un fichier PDF existant

Pour définir des privilèges sur un fichier PDF, créez un objet de la classe [DocumentPrivilege](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/documentprivilege) et spécifiez les droits que vous souhaitez appliquer au document. Une fois les privilèges définis, passez cet objet en argument à la méthode [Encrypt](https://reference.aspose.com/pdf/fr/net/aspose.pdf.document/encrypt/methods/1) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document). Le code suivant vous montre comment définir les privilèges d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegesOnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate Document Privileges object
        // Apply restrictions on all privileges
        var documentPrivilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
        // Only allow screen reading
        documentPrivilege.AllowScreenReaders = true;
        // Encrypt the file with User and Owner password
        // Need to set the password, so that once the user views the file with user password
        // Only screen reading option is enabled
        document.Encrypt("user", "owner", documentPrivilege, Aspose.Pdf.CryptoAlgorithm.AESx128, false);
        // Save PDF document
        document.Save(dataDir + "SetPrivileges_out.pdf");
    }
}
```

## Chiffrer un fichier PDF en utilisant différents types et algorithmes de chiffrement

Vous pouvez utiliser la méthode [Encrypt](https://reference.aspose.com/pdf/fr/net/aspose.pdf.document/encrypt/methods/1) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document) pour chiffrer un fichier PDF. Vous pouvez passer le mot de passe utilisateur, le mot de passe propriétaire et les autorisations à la méthode [Encrypt](https://reference.aspose.com/pdf/fr/net/aspose.pdf.document/encrypt/methods/1). De plus, vous pouvez passer n'importe quelle valeur de l'énumération [CryptoAlgorithm](https://reference.aspose.com/pdf/fr/net/aspose.pdf/cryptoalgorithm). Cette énumération fournit différentes combinaisons d'algorithmes de chiffrement et de tailles de clé. Vous pouvez passer la valeur de votre choix. Enfin, enregistrez le fichier PDF chiffré en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.document/save/methods/4) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).

>Veuillez spécifier des mots de passe utilisateur et propriétaire différents lors du chiffrement du fichier PDF.

- Le **mot de passe utilisateur**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à un utilisateur d'entrer le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
- Le **mot de passe propriétaire**, s'il est défini, contrôle les autorisations, telles que l'impression, l'édition, l'extraction, les commentaires, etc. Acrobat/Reader interdira ces actions en fonction des paramètres d'autorisation. Acrobat exigera ce mot de passe si vous souhaitez définir/changer des autorisations.

Le code suivant vous montre comment chiffrer des fichiers PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Encrypt.pdf"))
    {
        // Encrypt PDF
        document.Encrypt("user", "owner", 0, Aspose.Pdf.CryptoAlgorithm.RC4x128);
        // Save PDF document
        document.Save(dataDir + "Encrypt_out.pdf");
    }
}
```

## Déchiffrer un fichier PDF en utilisant le mot de passe propriétaire

De plus en plus, les utilisateurs échangent des fichiers PDF avec chiffrement pour empêcher l'accès non autorisé aux documents, tels que l'impression/copier/partager/extraire des informations sur le contenu d'un fichier PDF. Aujourd'hui, c'est le meilleur choix pour chiffrer un fichier PDF car cela maintient la confidentialité et l'intégrité du contenu. 
À cet égard, il est nécessaire d'accéder au fichier PDF chiffré, car cet accès ne peut être obtenu que par un utilisateur autorisé. De plus, les gens recherchent diverses solutions pour déchiffrer des fichiers PDF sur Internet.

Il est préférable de résoudre ce problème une fois en utilisant la bibliothèque Aspose.PDF.

Pour déchiffrer le fichier PDF, vous devez d'abord créer un objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document) et ouvrir le PDF en utilisant le mot de passe du propriétaire. Après cela, vous devez appeler la méthode [Decrypt](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/decrypt) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document). Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.document/save/methods/4) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document). Le code suivant vous montre comment déchiffrer le fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "Decrypt.pdf", "password"))
    {
        // Decrypt PDF
        document.Decrypt();
        // Save PDF document
        document.Save(dataDir + "Decrypt_out.pdf");
    }
}
```

## Changer le mot de passe d'un fichier PDF

Si vous souhaitez changer le mot de passe d'un fichier PDF, vous devez d'abord ouvrir le fichier PDF en utilisant le mot de passe propriétaire avec l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document). Après cela, vous devez appeler la méthode [ChangePasswords](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/changepasswords) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document). Vous devez passer le mot de passe propriétaire actuel ainsi que le nouveau mot de passe utilisateur et le nouveau mot de passe propriétaire à cette méthode. Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.document/save/methods/4) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).

>- Le mot de passe utilisateur, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à un utilisateur d'entrer le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
>- Le mot de passe propriétaire, s'il est défini, contrôle les autorisations, telles que l'impression, l'édition, l'extraction, les commentaires, etc. Acrobat/Reader interdira ces actions en fonction des paramètres d'autorisation. Acrobat exigera ce mot de passe si vous souhaitez définir/changer des autorisations.

Le code suivant vous montre comment changer le mot de passe d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "ChangePassword.pdf", "owner"))
    {
        // Change password
        document.ChangePasswords("owner", "newuser", "newowner");
        // Save PDF document
        document.Save(dataDir + "ChangePassword_out.pdf");
    }
}
```

## Comment - déterminer si le PDF source est protégé par un mot de passe

**Aspose.PDF for .NET** offre de grandes capacités pour traiter des documents PDF. Lors de l'utilisation de la classe Document de l'espace de noms Aspose.PDF pour ouvrir un document PDF qui est protégé par un mot de passe, nous devons fournir les informations de mot de passe comme argument au constructeur Document et dans le cas où ces informations ne sont pas fournies, un message d'erreur est généré. En fait, lorsque vous essayez d'ouvrir un fichier PDF avec l'objet Document, le constructeur essaie de lire le contenu du fichier PDF et dans le cas où le mot de passe correct n'est pas fourni, un message d'erreur est généré (cela se produit pour empêcher l'accès non autorisé au document).

Lorsqu'il s'agit de fichiers PDF chiffrés, vous pouvez rencontrer le scénario où vous seriez intéressé à détecter si un PDF a un mot de passe d'ouverture et/ou un mot de passe d'édition. Parfois, il y a des documents qui ne nécessitent pas d'informations de mot de passe lors de leur ouverture, mais qui nécessitent des informations pour modifier le contenu du fichier. Ainsi, pour répondre aux exigences ci-dessus, la classe PdfFileInfo présente sous Aspose.PDF.Facades fournit les propriétés qui peuvent aider à déterminer les informations requises.

### Obtenir des informations sur la sécurité du document PDF

PdfFileInfo contient trois propriétés pour obtenir des informations sur la sécurité du document PDF.

1. La propriété PasswordType retourne la valeur d'énumération PasswordType :
    - PasswordType.None - le document n'est pas protégé par un mot de passe.
    - PasswordType.User - le document a été ouvert avec le mot de passe utilisateur (ou mot de passe d'ouverture du document).
    - PasswordType.Owner - le document a été ouvert avec le mot de passe propriétaire (ou mot de passe d'autorisation, d'édition).
    - PasswordType.Inaccessible - le document est protégé par un mot de passe mais le mot de passe est nécessaire pour l'ouvrir alors qu'un mot de passe invalide (ou aucun mot de passe) a été fourni.
2. La propriété booléenne HasOpenPassword - est utilisée pour déterminer si le fichier d'entrée nécessite un mot de passe lors de son ouverture.
3. La propriété booléenne HasEditPassword - est utilisée pour déterminer si le fichier d'entrée nécessite un mot de passe pour modifier son contenu.

### Déterminer le mot de passe correct à partir d'un tableau

Parfois, il est nécessaire de déterminer le mot de passe correct à partir d'un tableau de mots de passe et d'ouvrir le document avec le mot de passe correct. Le code suivant démontre les étapes pour itérer à travers le tableau de mots de passe et essayer d'ouvrir le document avec le mot de passe correct.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineCorrectPasswordFromArray()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var info = new  Aspose.Pdf.Facades.PdfFileInfo())
    {
        // Bind PDF document
        info.BindPdf(dataDir + "IsPasswordProtected.pdf");
        // Determine if the source PDF is encrypted
        Console.WriteLine("File is password protected " + info.IsEncrypted);
    
        String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
    
        for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
        {
            try
            {
                using (var document = new Aspose.Pdf.Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]))
                {
                    if (document.Pages.Count > 0)
                    {
                        Console.WriteLine("Number of Page in document are = " + document.Pages.Count);
                    }
                }
            }
            catch (Aspose.Pdf.InvalidPasswordException)
            {
                Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
            }
        }
    }
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