---
title: Créer un document PDF de manière programmatique
linktitle: Créer PDF
type: docs
weight: 10
url: /fr/net/create-document/
description: Cette page décrit comment créer un document PDF de zéro avec la bibliothèque Aspose.PDF.
---

Aspose.PDF pour l'API .NET vous permet de créer et de lire des fichiers PDF en utilisant C# et VB.NET. L'API peut être utilisée dans une variété d'applications .NET, y compris WinForms, ASP.NET, et plusieurs autres. Dans cet article, nous allons montrer comment utiliser Aspose.PDF pour l'API .NET pour générer et lire facilement des fichiers PDF dans des applications .NET.

## Comment créer un fichier PDF en utilisant C#

Pour créer un fichier PDF en utilisant C#, les étapes suivantes peuvent être utilisées.

1. Créer un objet de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Ajouter un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à la collection [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) de l'objet Document
1.
1.
1. Enregistrez le document PDF résultant

Le prochain extrait de code fonctionne également avec une nouvelle interface graphique [Aspose.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Initialiser l'objet document
Document document = new Document();
// Ajouter une page
Page page = document.Pages.Add();
// Ajouter du texte à la nouvelle page
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Bonjour le monde !"));
// Sauvegarder le PDF mis à jour
document.Save(dataDir + "HelloWorld_out.pdf")
```

Dans ce cas, nous créons un document PDF d'une page avec un format de page A4, en orientation portrait. Notre page contiendra un "Bonjour, le monde" dans la partie supérieure gauche de la page.
