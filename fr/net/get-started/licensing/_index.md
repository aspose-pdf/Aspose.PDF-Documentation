---
title: Licence Aspose PDF
linktitle: Licences et limitations
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /fr/net/licensing/
description: Aspose. PDF pour .NET invite ses clients à obtenir une licence classique et une licence à la consommation. Ainsi qu'à utiliser une licence limitée pour mieux explorer le produit.
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF pour .NET introduit un cadre de licence robuste comprenant à la fois des licences classiques et à la consommation, permettant aux utilisateurs de choisir entre des prix fixes et des options de facturation basées sur l'utilisation. La licence classique peut être facilement chargée à partir d'un fichier ou d'un flux, tandis que la licence à la consommation innovante offre une mesure flexible basée sur l'utilisation de l'API, répondant à des besoins utilisateurs divers. Cette stratégie de double licence améliore l'accessibilité et l'évolutivité des solutions PDF pour les développeurs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
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
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Limitation d'une version d'évaluation

Nous voulons que nos clients testent nos composants en profondeur avant d'acheter, donc la version d'évaluation vous permet de l'utiliser comme vous le feriez normalement.

- **PDF créé avec un filigrane d'évaluation.** La version d'évaluation de Aspose.PDF for .NET offre une fonctionnalité complète du produit, mais toutes les pages des documents PDF générés sont marquées avec le texte "Évaluation uniquement. Créé avec Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." en haut.

- **Limiter le nombre de pages pouvant être traitées.**
Dans la version d'évaluation, vous ne pouvez traiter que les quatre premières pages d'un document.

>Si vous souhaitez tester Aspose.PDF for .NET sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

## Licence classique

La licence peut être chargée à partir d'un fichier ou d'un objet de flux. La manière la plus simple de définir une licence est de placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier le nom du fichier sans chemin, comme indiqué dans l'exemple ci-dessous.

Si vous utilisez un autre composant Aspose pour .NET avec Aspose.PDF for .NET, veuillez spécifier l'espace de noms pour la licence comme [Aspose.Pdf.License](https://reference.aspose.com/pdf/fr/net/aspose.pdf/license).

### Chargement d'une licence à partir d'un fichier

La manière la plus simple d'appliquer une licence est de placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier simplement le nom du fichier sans chemin.

Lorsque vous appelez la méthode [SetLicense](https://reference.aspose.com/pdf/fr/net/aspose.pdf/license/methods/setlicense/index), le nom de la licence que vous passez doit être celui de votre fichier de licence. Par exemple, si vous changez le nom du fichier de licence en "Aspose.PDF.lic.xml", passez ce nom de fichier à la méthode Pdf.SetLicense(…).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### Chargement de la licence à partir d'un objet de flux

L'exemple suivant montre comment charger une licence à partir d'un flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## Licence à la consommation

Aspose.PDF permet aux développeurs d'appliquer une clé à la consommation. Le mécanisme de licence à la consommation sera utilisé avec la méthode de licence existante. Les clients qui souhaitent être facturés en fonction de l'utilisation des fonctionnalités de l'API peuvent utiliser la licence à la consommation. Pour plus de détails, veuillez vous référer à la section FAQ sur la licence à la consommation.
Ce guide fournit des meilleures pratiques pour une mise en œuvre fluide et pour éviter les interruptions dues aux changements de statut de licence.

La classe "Metered" est utilisée pour appliquer des clés à la consommation. Voici un exemple de code démontrant comment définir des clés publiques et privées à la consommation.

Pour plus de détails, veuillez vous référer à la section [FAQ sur la licence à la consommation](https://purchase.aspose.com/faqs/licensing/metered).

__Méthodes de licence à la consommation__

Pour appliquer la licence à la consommation, utilisez la méthode `SetMeteredKey` pour activer la licence à la consommation en fournissant vos clés publiques et privées. Cela doit être fait une fois lors de l'initialisation de l'application pour garantir une licence appropriée.

Exemple :

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
Vérifier l'état de la licence utilise `IsMeteredLicensed()` pour vérifier si la licence à la consommation est active.

Exemple :

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
La méthode `Metered.GetConsumptionCredit()` est utilisée pour obtenir des informations sur les crédits de consommation.
La méthode `Metered.GetConsumptionQuantity()` est utilisée pour obtenir des informations sur la taille du fichier de consommation.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");
    // Get current Consumption Credit and Quantity
    var currentMonthCreditsSpent = Aspose.Pdf.Metered.GetConsumptionCredit();
    var currentMonthConsumedMegabytes = Aspose.Pdf.Metered.GetConsumptionQuantity();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Add five pages
        AddPages(document, 5);

        // Save PDF document
        document.Save(dataDir + "output.pdf");

        // Wait to be sure the transaction completed
        System.Threading.Thread.Sleep(10000);
        // Get current Consumption Credit and Quantity
        var nowCredit = Aspose.Pdf.Metered.GetConsumptionCredit();
        var nowQuantity = Aspose.Pdf.Metered.GetConsumptionQuantity();
        Console.WriteLine("Credit: was={0} now={1} difference={2}", currentMonthCreditsSpent, nowCredit, nowCredit - currentMonthCreditsSpent);
        Console.WriteLine("Quantity: was={0} now={1} difference={2}", currentMonthConsumedMegabytes, nowQuantity, nowQuantity - currentMonthConsumedMegabytes); 
    }
}

private static void AddPages(Document document, int n)
{
    for (int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
} 
```

__Meilleures pratiques pour la licence à la consommation__

✅ Approche recommandée : Modèle Singleton
Pour garantir une configuration de licence stable :

- Appliquez la licence une fois au démarrage de l'application.
- Utilisez un modèle singleton (ou une approche similaire) pour créer et réutiliser l'instance de licence à la consommation.
- Vérifiez périodiquement l'état de la licence en utilisant `IsMeteredLicensed()`. Réappliquez la licence uniquement si elle devient invalide.
- Si cela est correctement mis en œuvre, la licence reste valide pendant 24 heures même si le serveur de licence est temporairement indisponible.

Exemple : Mise en œuvre du Singleton

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ Erreurs courantes à éviter :

- Applications fréquentes de la licence
- Ne créez pas une nouvelle instance de licence à la consommation pour chaque opération.
- Si le serveur de licence est inaccessible pendant l'initialisation, la licence peut revenir en mode d'évaluation.
- Ne pas appliquer la licence de manière répétée pour chaque opération.
- Des applications fréquentes de la licence peuvent entraîner un retour en mode d'essai si le serveur de licence est temporairement indisponible.

__Résumé :__

✅ Définissez la licence à la consommation une fois au démarrage de l'application.
✅ Utilisez un modèle singleton pour gérer une seule instance.
✅ Vérifiez périodiquement et réappliquez la licence si nécessaire.
❌ Évitez les applications fréquentes de la licence pour prévenir le retour en mode d'essai.
En suivant ces meilleures pratiques, vous garantissez une utilisation fluide et ininterrompue d'Aspose.PDF avec la licence à la consommation.

Si la licence a été initialisée, alors tant que cet objet "vit", même si la connexion au serveur de licence est perdue pour une raison quelconque, la licence sera considérée comme active pendant 7 jours supplémentaires. Si vous initialisez une licence chaque fois que vous devez faire quelque chose et qu'il n'y a pas de connexion au serveur au moment de l'initialisation, alors la licence passera en mode d'évaluation.
Il convient de souligner que si un utilisateur a initialisé une licence, alors tant que cet objet "vit", même si la connexion au serveur de licence est perdue pour une raison quelconque, la licence sera considérée comme active pendant 24 heures supplémentaires. Si vous initialisez une licence chaque fois que vous devez faire quelque chose et qu'il n'y a pas de connexion au serveur au moment de l'initialisation, alors la licence passera en mode d'évaluation.

Veuillez noter que les applications COM qui travaillent avec **Aspose.PDF for .NET** doivent également utiliser la classe License.

Un point qui nécessite une considération :
Veuillez noter que les ressources intégrées sont incluses dans l'assemblage de la manière dont elles sont ajoutées, c'est-à-dire que si vous ajoutez un fichier texte en tant que ressource intégrée dans l'application et ouvrez l'EXE résultant dans le bloc-notes, vous verrez le contenu exact du fichier texte. Donc, lors de l'utilisation du fichier de licence en tant que ressource intégrée, quiconque peut ouvrir le fichier exe dans un éditeur de texte simple et voir/extraire le contenu de la licence intégrée.

Par conséquent, afin de mettre une couche de sécurité supplémentaire lors de l'intégration de la licence avec l'application, vous pouvez compresser/chiffrer la licence et après cela, vous pouvez l'intégrer dans l'assemblage. Supposons que nous ayons le fichier de licence Aspose.PDF.lic, alors faisons Aspose.PDF.zip avec le mot de passe test et intégrons ce fichier zip dans la solution. Le code suivant peut être utilisé pour initialiser la licence :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
}

private static Stream GetSecureLicenseFromStream()
{
    var assembly = Assembly.GetExecutingAssembly();
    var memoryStream = new MemoryStream();
    using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
    {
        using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
        {
            var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
            unpackedLicense?.Open().CopyTo(memoryStream);
        }
    }

    memoryStream.Position = 0;
    return memoryStream;
}
```