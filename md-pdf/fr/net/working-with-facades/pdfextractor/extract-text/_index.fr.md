---
title: Extraire le texte d'un fichier PDF
type: docs
weight: 30
url: /net/extract-text/
description: Cette section explique comment extraire du texte d'un PDF en utilisant la classe PdfExtractor.
lastmod: "2021-06-05"
---

Dans cet article, nous examinerons en détail l'extraction de texte d'un fichier PDF. Toutes ces fonctionnalités d'extraction sont fournies en un seul endroit, dans la classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). Nous verrons comment utiliser ces fonctionnalités dans notre code.

La classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) offre trois types de capacités d'extraction. Ces trois catégories sont Texte, Images et Pièces jointes. Afin de réaliser une extraction dans chacune de ces trois catégories, PdfExtractor propose diverses méthodes qui fonctionnent ensemble pour vous donner le résultat final.

Par exemple, pour extraire du texte, vous pouvez utiliser trois méthodes c'est-à-dire. ```
[ExtractText, GetText, HasNextPageText et GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index).
``` Maintenant, afin de commencer à extraire du texte, tout d'abord, vous devez appeler la méthode [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index); cela extraira le texte du fichier PDF et le stockera en mémoire. Après cela, la méthode [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) prendra ce texte extrait et le sauvegardera sur le disque à l'emplacement spécifié dans un fichier. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) vous aide à parcourir chaque page et à vérifier si la page suivante contient du texte ou non. Si elle contient du texte, alors [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) vous aidera à sauvegarder le texte d'une page individuelle dans le fichier.

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // Créer un objet de la classe PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Lier le PDF d'entrée
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // ExtractText
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extraire le texte dans des fichiers séparés
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
Pour extraire le mode d'extraction de texte, utilisez le code suivant :

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // Créez un objet de la classe PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Liez le PDF d'entrée
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // Extraire le texte
    // pdfExtractor.ExtractTextMode = 0; //mode pur
    pdfExtractor.ExtractTextMode = 1; //mode brut
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extraire le texte dans des fichiers séparés
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```