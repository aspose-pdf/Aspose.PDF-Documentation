---
title: Licence Aspose PDF
linktitle: Licence et limitations
type: docs
weight: 90
url: /fr/net/licensing/
description: Aspose. PDF pour .NET invite ses clients à obtenir une licence classique et une licence mesurée. Ainsi qu'à utiliser une licence limitée pour mieux explorer le produit.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitation d'une version d'évaluation

Nous voulons que nos clients testent nos composants de manière approfondie avant d'acheter, donc la version d'évaluation vous permet de l'utiliser comme vous le feriez normalement.

- **PDF créé avec un filigrane d'évaluation.** La version d'évaluation de Aspose.PDF pour .NET offre toutes les fonctionnalités du produit, mais toutes les pages des documents PDF générés sont marquées avec "Évaluation uniquement. Créé avec Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en haut.

- **La limite du nombre d'éléments de collection qui peuvent être traités.**
Dans la version d'évaluation de n'importe quelle collection, vous pouvez traiter seulement quatre éléments (par exemple, seulement 4 pages, 4 champs de formulaire, etc.).
Dans la version d'évaluation de toute collection, vous ne pouvez traiter que quatre éléments (par exemple, seulement 4 pages, 4 champs de formulaire, etc.).

>Si vous souhaitez tester Aspose.HTML pour .NET sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez consulter [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

## Licence classique

La licence peut être chargée à partir d'un fichier ou d'un objet stream. Le moyen le plus simple de définir une licence est de placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier le nom du fichier sans chemin, comme le montre l'exemple ci-dessous.

Si vous utilisez un autre composant Aspose pour .NET en plus de Aspose.PDF pour .NET, veuillez spécifier l'espace de noms pour License comme [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Chargement d'une licence à partir d'un fichier

Le moyen le plus simple d'appliquer une licence est de mettre le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier uniquement le nom du fichier sans chemin.

Lorsque vous appelez la méthode [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), le nom de la licence que vous passez doit être celui de votre fichier de licence.
Lorsque vous appelez la méthode [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), le nom de licence que vous passez doit être celui de votre fichier de licence.

```csharp

public static void SetLicenseExample()
{
    // Initialiser l'objet licence
    Aspose.Pdf.License licence = new Aspose.Pdf.License();
    try
    {
        // Définir la licence
        licence.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // quelque chose s'est mal passé
        throw;
    }
    Console.WriteLine("Licence définie avec succès.");
}
```
### Chargement de la licence à partir d'un objet stream

L'exemple suivant montre comment charger une licence à partir d'un stream.

```csharp
public static void SetLicenseFromStream()
{
    // Initialiser l'objet licence
    Aspose.Pdf.License licence = new Aspose.Pdf.License();
    // Charger la licence depuis le flux de fichier
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // Définir la licence
    licence.SetLicense(myStream);
    Console.WriteLine("Licence définie avec succès.");
}
```
## Licence Mesurée

Aspose.PDF permet aux développeurs d'appliquer une clé mesurée. Il s'agit d'un nouveau mécanisme de licence. Le nouveau mécanisme de licence sera utilisé conjointement avec la méthode de licence existante. Les clients qui souhaitent être facturés en fonction de l'utilisation des fonctionnalités de l'API peuvent utiliser la licence mesurée. Pour plus de détails, veuillez vous référer à la section FAQ sur la Licence Mesurée.

Une nouvelle classe Metered a été introduite pour appliquer la clé mesurée. Voici le code exemple démontrant comment définir les clés publiques et privées mesurées.

Pour plus de détails, veuillez vous référer à la section [FAQ sur la Licence Mesurée](https://purchase.aspose.com/faqs/licensing/metered).

```csharp
public static void SetMeteredLicense()
{
    // définir les clés publiques et privées mesurées
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // Accéder à la propriété setMeteredKey et passer les clés publiques et privées comme paramètres
    metered.SetMeteredKey(
        "<tapez ici la clé publique>",
        "<tapez ici la clé privée>");

    // Charger le document depuis le disque.
    Document doc = new Document("input.pdf");
    //Obtenir le nombre de pages du document
    Console.WriteLine(doc.Pages.Count);
}
```
Veuillez noter que les applications COM qui travaillent avec **Aspose.PDF pour .NET** doivent également utiliser la classe License.

Un point qui nécessite une considération :
Veuillez noter que les ressources intégrées sont incluses dans l'assemblage de la manière dont elles sont ajoutées, c'est-à-dire si vous ajoutez un fichier texte en tant que ressource intégrée dans l'application et ouvrez l'EXE résultant dans le bloc-notes, vous verrez le contenu exact du fichier texte. Ainsi, lors de l'utilisation du fichier de licence comme ressource intégrée, n'importe qui peut ouvrir le fichier exe dans un éditeur de texte simple et voir/extraire le contenu de la licence intégrée.

Par conséquent, afin d'ajouter une couche supplémentaire de sécurité lors de l'intégration de la licence avec l'application, vous pouvez compresser/chiffrer la licence et, après cela, vous pouvez l'intégrer dans l'assemblage. Supposons que nous ayons un fichier de licence Aspose.PDF.lic, alors créons Aspose.PDF.zip avec le mot de passe test et intégrons ce fichier zip dans la solution. Le fragment de code suivant peut être utilisé pour initialiser la licence :

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //Obtenir le nombre de pages du document
            Console.WriteLine(doc.Pages.Count);
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
    }
}
```
changefreq: "monthly"
type: docs
### Application d'une licence acquise avant le 22/01/2005

Aspose.PDF pour .NET ne prend plus en charge les anciennes licences. Si vous avez une licence datant d'avant le 22 janvier 2005 et que vous avez mis à jour vers une version plus récente d'Aspose.PDF, veuillez contacter notre équipe commerciale pour obtenir un nouveau fichier de licence.
