---
title: Générateur de tableaux
type: docs
weight: 130
url: /net/plugins/tablegenerator/
description: Permet d'ajouter/insérer un tableau sur le numéro de page spécifié du document PDF.
lastmod: "2024-01-24"
draft: false
---

Avez-vous besoin de créer des tableaux dynamiques et visuellement attrayants dans vos documents PDF en utilisant .NET ? Aspose.PDF pour .NET offre une classe puissante TableGenerator qui simplifie le processus. Dans ce chapitre, nous allons parcourir les étapes pour générer des tableaux dans un document PDF en utilisant [Aspose.PDF Table Generator](https://products.aspose.org/pdf/net/table-generator/), de la création d'un document de démonstration à la génération de tableaux avec la classe TableGenerator.
Plongeons et apprenons comment générer des tableaux étape par étape.

## Prérequis

Vous aurez besoin des éléments suivants :

* Visual Studio 2019 ou plus récent
* Aspose.PDF pour .NET 24.3 ou plus récent
* Un fichier PDF d'exemple

## Création d'un document de démonstration

Avant de plonger dans la génération de tableaux, créons un document de démonstration avec des pages vides où nos tableaux seront insérés.
Avant de plonger dans la génération de tableaux, créons un document de démonstration avec des pages vides où nos tableaux seront insérés.

* Créez un nouveau document PDF.
* Ajoutez des pages vides au document.
* Enregistrez le document dans le fichier spécifié.

```cs
// <summary>
// Crée un document de démonstration avec des pages vides.
//
// Paramètres:
// - fileName: Le chemin et le nom du fichier de sortie.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // Créez un nouveau document PDF.
    var document = new Aspose.Pdf.Document();

    // Ajoutez quatre pages vides au document.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // Enregistrez le document dans le fichier spécifié.
    document.Save(fileName);
}
```

## Génération de Tableaux

Une fois que nous avons notre document de démonstration prêt, nous pouvons commencer à générer des tableaux en utilisant la classe `TableGenerator`. Le fragment suivant montre comment générer des tableaux avec divers types de contenu et options de formatage. Voici comment générer des tableaux :

* Créez une nouvelle instance de la classe `TableGenerator`.
* Créer une nouvelle instance de la classe `TableGenerator`.
* Créer des options de table et spécifier les sources de données des fichiers d'entrée et de sortie.
* Ajouter des tables avec des lignes et des cellules aux options, en spécifiant le contenu et le formatage.
* Traiter la génération de la table en utilisant la méthode `Process` et obtenir le conteneur de résultat.

### Création de Tables

Pour créer une table en utilisant Aspose.PDF, suivez ces étapes :

```cs
// Créer une nouvelle instance de la classe TableGenerator.
var generator = new TableGenerator();

// Créer des options de table et ajouter des tables de démonstration.
var options = new TableOptions();

// Ajouter les sources de données des fichiers d'entrée et de sortie aux options.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// Ajouter la première table aux options.
options
    .InsertPageAfter(1)
    .AddTable()
```

Dans le code ci-dessus, nous créons une instance de `TableOptions` et spécifions les sources de données des fichiers d'entrée et de sortie pour le document PDF.
Dans le code ci-dessus, nous créons une instance de `TableOptions` et spécifions les sources de données de fichiers d'entrée et de sortie pour le document PDF.

### Ajout de contenu aux tables

Une fois la table créée, vous pouvez la remplir avec des lignes et des cellules contenant différents types de contenu, tels que du texte, du HTML, des images, etc. Voici comment ajouter du contenu à une table :

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>En-tête 1</h1>")) // Ajouter du contenu HTML à la cellule.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>En-tête 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>En-tête 3</h3>"));
```

Dans cet exemple, nous ajoutons une ligne à la table et la remplissons avec des cellules contenant des fragments HTML représentant des en-têtes.

Méthodes utiles :

* **InsertPageAfter** : Insère une page après le numéro de page spécifié.
* **InsertPageBefore** : Insère une page avant le numéro de page spécifié.
* **AddTable** : Ajoute une table au document.
* **AddTable**: Ajoute une table au document.
* **AddRow**: Ajoute une ligne à la table.
* **AddCell**: Ajoute des cellules à la ligne.
* **AddParagraph**: Ajoute du contenu à la cellule.

Vous pouvez ajouter les types de contenu suivants en tant que paragraphe :

* **HtmlFragment** - un contenu basé sur le balisage HTML
* **TeXFragment** - un contenu basé sur le balisage TeX/LaTeX
* **TextFragment** - un contenu texte simple
* **Image** - graphiques

## Réalisation de la génération de table

Après avoir ajouté le contenu, nous pouvons commencer à créer la table.

```cs
// Traiter la génération de la table et obtenir le conteneur de résultats.
var resultContainer = generator.Process(options);

// Imprimer le nombre de résultats dans la collection de résultats.
Console.WriteLine(resultContainer.ResultCollection.Count);
```

La méthode `Process` effectue la génération de la table. Cette méthode peut également être encapsulée avec try-catch pour gérer les erreurs.

Ci-dessous, vous pouvez voir le code complet de l'exemple :

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // Représente une classe qui démontre l'utilisation de la génération de table dans Aspose.Pdf.
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // Exécute la démonstration de génération de table.
        // </summary>
        internal static void Run()
        {
            // Créer un document de démonstration et générer des tables.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // Crée un document de démonstration avec quatre pages vides.
        //
        // Paramètres :
        // - fileName: Le chemin et le nom du fichier de sortie.
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // Créer un nouveau document PDF.
            var document = new Aspose.Pdf.Document();

            // Ajouter quatre pages vides au document.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // Sauvegarder le document dans le fichier spécifié.
            document.Save(fileName);
        }

        // <summary>
        // Génère des tables en utilisant la classe TableGenerator.
        // </summary>
        internal static void CreateDemoTable()
        {
            // Créer une nouvelle instance de la classe TableGenerator.
            var generator = new TableGenerator();

            // Créer des options de table et ajouter des tables de démonstration.
            var options = new TableOptions();

            // Ajouter des sources de fichiers de données d'entrée et de sortie aux options.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // Ajouter la première table aux options.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>En-tête 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>En-tête 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>En-tête 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small L'équation $E=mc^2$, découverte en 1905 par Albert Einstein.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cellule 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cellule 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Cellule 3 1a"))
                            .AddParagraph(new TextFragment("Cellule 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cellule 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cellule 3 3"));

            // Ajouter la deuxième table aux options.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("En-tête 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("En-tête 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("En-tête 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // Traiter la génération de la table et obtenir le conteneur de résultats.
            var resultContainer = generator.Process(options);

            // Imprimer le nombre de résultats dans la collection de résultats.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```

