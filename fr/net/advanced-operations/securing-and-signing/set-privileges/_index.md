---
title: Définir les privilèges, chiffrer et déchiffrer un PDF
linktitle: Chiffrer et déchiffrer un fichier PDF
type: docs
weight: 20
url: fr/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Chiffrer un fichier PDF avec C# en utilisant différents types de chiffrement et algorithmes. Déchiffrer également les fichiers PDF en utilisant le mot de passe du propriétaire.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Définir les privilèges, chiffrer et déchiffrer un PDF",
    "alternativeHeadline": "Comment chiffrer et déchiffrer un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, chiffrer pdf, déchiffrer pdf",
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
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Chiffrer un fichier PDF avec C# en utilisant différents types de chiffrement et algorithmes. Déchiffrer également les fichiers PDF en utilisant le mot de passe du propriétaire."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Définir des privilèges sur un fichier PDF existant

Pour définir des privilèges sur un fichier PDF, créez un objet de la classe [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) et spécifiez les droits que vous souhaitez appliquer au document. Une fois les privilèges définis, passez cet objet en argument à la méthode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Le code suivant montre comment définir les privilèges d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Charger un fichier PDF source
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Instancier l'objet Document Privileges
    // Appliquer des restrictions sur tous les privilèges
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // Autoriser uniquement la lecture à l'écran
    documentPrivilege.AllowScreenReaders = true;
    // Chiffrer le fichier avec un mot de passe Utilisateur et Propriétaire.
    // Il est nécessaire de définir le mot de passe, afin que lorsque l'utilisateur visualise le fichier avec le mot de passe utilisateur,
    // Seule l'option de lecture à l'écran soit activée
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // Sauvegarder le document mis à jour
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## Chiffrer un fichier PDF en utilisant différents types et algorithmes de chiffrement

Vous pouvez utiliser la méthode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) pour chiffrer un fichier PDF. Vous pouvez passer le mot de passe utilisateur, le mot de passe propriétaire et les permissions à la méthode [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). De plus, vous pouvez passer n'importe quelle valeur de l'énumération [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). Cette énumération offre différentes combinaisons d'algorithmes de chiffrement et de tailles de clés. Vous pouvez passer la valeur de votre choix. Enfin, sauvegardez le fichier PDF chiffré en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>Veuillez spécifier des mots de passe utilisateur et propriétaire différents lors du chiffrement du fichier PDF.

- Le **mot de passe utilisateur**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF.
- Le **mot de passe utilisateur**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF.
- Le **mot de passe propriétaire**, s'il est défini, contrôle les permissions, telles que l'impression, l'édition, l'extraction, les commentaires, etc. Acrobat/Reader interdira ces actions en fonction des paramètres de permission. Acrobat exigera ce mot de passe si vous souhaitez définir/modifier les permissions.

Le code suivant montre comment crypter des fichiers PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Ouvrir le document
Document document = new Document(dataDir+ "Encrypt.pdf");
// Crypter PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// Sauvegarder le PDF mis à jour
document.Save(dataDir);
```

## Décrypter un fichier PDF en utilisant le mot de passe propriétaire

De plus en plus, les utilisateurs échangent des fichiers PDF avec cryptage pour empêcher l'accès non autorisé aux documents, tels que l'impression/la copie/le partage / l'extraction d'informations sur le contenu d'un fichier PDF.
De plus en plus, les utilisateurs échangent des fichiers PDF avec chiffrement pour empêcher l'accès non autorisé aux documents, tels que l'impression/la copie/le partage/l'extraction d'informations sur le contenu d'un fichier PDF.
À cet égard, il est nécessaire d'accéder au fichier PDF chiffré, puisque cet accès ne peut être obtenu que par un utilisateur autorisé. De plus, les gens cherchent diverses solutions pour décrypter les fichiers PDF sur Internet.

Il est préférable de résoudre ce problème une fois pour toutes en utilisant la bibliothèque Aspose.PDF.

Pour décrypter le fichier PDF, vous devez d'abord créer un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) et ouvrir le PDF en utilisant le mot de passe du propriétaire.
Pour décrypter le fichier PDF, vous devez d'abord créer un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) et ouvrir le PDF en utilisant le mot de passe du propriétaire.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Ouvrir le document
Document document = new Document(dataDir + "Decrypt.pdf", "password");
// Décrypter PDF
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// Sauvegarder le PDF mis à jour
document.Save(dataDir);
```

## Changer le mot de passe d'un fichier PDF

Si vous souhaitez changer le mot de passe d'un fichier PDF, vous devez d'abord ouvrir le fichier PDF en utilisant le mot de passe du propriétaire avec l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
Si vous souhaitez changer le mot de passe d'un fichier PDF, vous devez d'abord ouvrir le fichier PDF en utilisant le mot de passe du propriétaire avec l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- Le mot de passe utilisateur, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à l'utilisateur d'entrer le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
>- Le mot de passe du propriétaire, s'il est défini, contrôle les permissions, telles que l'impression, l'édition, l'extraction, les commentaires, etc. Acrobat/Reader interdira ces choses en fonction des paramètres de permission. Acrobat exigera ce mot de passe si vous souhaitez définir/modifier les permissions.

Le code suivant vous montre comment changer le mot de passe d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// Ouvrir le document
Document document = new Document(dataDir + "ChangePassword.pdf", "owner");
// Changer le mot de passe
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// Sauvegarder le PDF mis à jour
document.Save(dataDir);
```

## Comment déterminer si le PDF source est protégé par un mot de passe

**Aspose.PDF pour .NET** offre d'excellentes capacités de gestion des documents PDF. Lors de l'utilisation de la classe Document de l'espace de noms Aspose.PDF pour ouvrir un document PDF protégé par mot de passe, nous devons fournir les informations de mot de passe en argument au constructeur de Document et dans le cas où ces informations ne sont pas fournies, un message d'erreur est généré. En effet, lors de la tentative d'ouverture d'un fichier PDF avec l'objet Document, le constructeur essaie de lire le contenu du fichier PDF et si le mot de passe correct n'est pas fourni, un message d'erreur est généré (cela se produit pour empêcher l'accès non autorisé au document).

Lorsque vous traitez avec des fichiers PDF chiffrés, vous pouvez rencontrer le scénario où vous souhaiteriez détecter si un PDF a un mot de passe d'ouverture et/ou un mot de passe de modification.
Lorsque vous traitez avec des fichiers PDF chiffrés, vous pouvez rencontrer le scénario où vous seriez intéressé à détecter si un PDF a un mot de passe d'ouverture et/ou un mot de passe de modification.

### Obtenir des informations sur la sécurité du document PDF

PdfFileInfo contient trois propriétés pour obtenir des informations sur la sécurité du document PDF.

1. La propriété PasswordType retourne la valeur de l'énumération PasswordType :
    - PasswordType.None - le document n'est pas protégé par mot de passe
    - PasswordType.User - le document a été ouvert avec un mot de passe utilisateur (ou mot de passe d'ouverture du document)
    - PasswordType.Owner - le document a été ouvert avec un mot de passe propriétaire (ou mot de passe de permissions, de modification)
    - PasswordType.Inaccessible - le document est protégé par mot de passe mais un mot de passe est nécessaire pour l'ouvrir alors qu'un mot de passe invalide (ou aucun mot de passe) a été fourni.
2. Propriété booléenne HasOpenPassword - est utilisée pour déterminer si le fichier d'entrée nécessite un mot de passe lors de son ouverture.
3. Propriété booléenne HasEditPassword - est utilisée pour déterminer si le fichier d'entrée nécessite un mot de passe pour modifier son contenu.

### Déterminer le bon mot de passe à partir d'un tableau
### Déterminer le mot de passe correct à partir d'un tableau

Parfois, il est nécessaire de déterminer le mot de passe correct à partir d'un tableau de mots de passe et d'ouvrir le document avec le mot de passe correct. Le fragment de code suivant démontre les étapes pour itérer à travers le tableau de mots de passe et essayer d'ouvrir le document avec le mot de passe correct.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// Charger le fichier PDF source
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// Déterminer si le PDF source est crypté
Console.WriteLine("Le fichier est protégé par mot de passe " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Le nombre de pages dans le document est = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Mot de passe = " + passwords[passwordcount] + " n'est pas correct");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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

