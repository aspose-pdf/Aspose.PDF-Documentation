---
title: Extraire les textes en SuperScripts et SubScripts d'un PDF
linktitle: Extraire les SuperScripts et SubScripts
type: docs
weight: 30
url: /net/extract-superscripts-subscripts-from-pdf/
description: Cet article décrit diverses méthodes pour extraire les textes en SuperScripts et SubScripts d'un PDF en utilisant Aspose.PDF en C#. 
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire les textes en SuperScripts et SubScripts

Extraire du texte d'un document PDF est une chose courante. Cependant, dans un tel texte, lorsqu'il est extrait, les **SuperScripts et SubScripts** qu'il contient, qui sont typiques pour les documents techniques et les articles, peuvent ne pas être affichés. Un SubScript ou un SuperScript est un caractère, un nombre ou une lettre placé(e) en dessous ou au-dessus d'une ligne de texte régulière. Il est généralement plus petit que le reste du texte.

**Les SubScripts et les SuperScripts** sont le plus souvent utilisés dans les formules, les expressions mathématiques et les spécifications de composés chimiques.
**Les indices inférieurs et supérieurs** sont le plus souvent utilisés dans les formules, les expressions mathématiques et les spécifications des composés chimiques.
Dans l'une des dernières versions, la bibliothèque **Aspose.PDF pour .NET** a ajouté la prise en charge de l'extraction du texte des indices supérieurs et inférieurs des PDF.

Utilisez la classe **TextFragmentAbsorber** et vous pouvez déjà faire tout ce que vous voulez avec le texte trouvé, c'est-à-dire, vous pouvez simplement utiliser l'intégralité du texte. Essayez le prochain extrait de code :

L'extrait de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

Ou utilisez **TextFragments** séparément et faites toutes sortes de manipulations avec eux, par exemple, triez par coordonnées ou par taille.

L'extrait de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
