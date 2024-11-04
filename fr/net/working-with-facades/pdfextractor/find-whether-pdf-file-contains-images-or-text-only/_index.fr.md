---
title: Trouver si le PDF contient des images ou du texte
linktitle: Vérifier la présence de texte et d'images
type: docs
weight: 40
url: /net/find-whether-pdf-file-contains-images-or-text-only/
description: Ce sujet explique comment trouver si un fichier PDF contient uniquement des images ou du texte avec la classe PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

## Contexte

Un fichier PDF peut contenir à la fois du texte et des images. Parfois, un utilisateur peut avoir besoin de savoir si un fichier PDF contient uniquement du texte, ou s'il contient uniquement des images. Nous pouvons également déterminer s'il contient les deux ou aucun.

{{% alert color="primary" %}}

Le code ci-dessous vous montre comment répondre à cette exigence.

{{% /alert %}}

```csharp
 public static void CheckIfPdfContainsTextOrImages()
{
    // Instancier un objet memoryStream pour contenir le texte extrait du document
    MemoryStream ms = new MemoryStream();
    // Instancier un objet PdfExtractor
    PdfExtractor extractor = new PdfExtractor();

    // Lier le document PDF d'entrée à l'extracteur
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // Extraire le texte du document PDF d'entrée
    extractor.ExtractText();
    // Enregistrer le texte extrait dans un fichier texte
    extractor.GetText(ms);
    // Vérifier si la longueur de MemoryStream est supérieure ou égale à 1

    bool containsText = ms.Length >= 1;

    // Extraire les images du document PDF d'entrée
    extractor.ExtractImage();

    // Appeler la méthode HasNextImage dans une boucle while. Lorsque les images seront terminées, la boucle se terminera
    bool containsImage = extractor.HasNextImage();

    // Maintenant, déterminer si ce PDF est uniquement du texte ou uniquement des images

    if (containsText && !containsImage)
        Console.WriteLine("Le PDF contient uniquement du texte");
    else if (!containsText && containsImage)
        Console.WriteLine("Le PDF contient uniquement des images");
    else if (containsText && containsImage)
        Console.WriteLine("Le PDF contient à la fois du texte et des images");
    else if (!containsText && !containsImage)
        Console.WriteLine("Le PDF ne contient ni texte ni images");
}
```