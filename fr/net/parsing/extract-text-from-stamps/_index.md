---
title: Extraire le texte des tampons en utilisant C#
type: docs
weight: 60
url: fr/net/extract-text-from-stamps/
description: Apprenez à utiliser une fonctionnalité spéciale d'Aspose.PDF pour .NET - l'extraction de texte à partir des annotations de tampon
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire le texte des annotations de tampon

Aspose.PDF pour NET vous permet d'extraire du texte à partir des annotations de tampon. Pour extraire le texte des Annotations de Tampon dans un PDF, les étapes suivantes peuvent être utilisées.

1. Créer un objet de classe `Document`
1. Obtenir l'`Annotation` désirée à partir de la liste des annotations d'une page
1. Définir un nouvel objet de la classe `TextAbsorber`
1. Utiliser la méthode visit de TextAbsorber pour obtenir le Texte

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```

