---
title: Remplacer le Texte - Façades
type: docs
weight: 40
url: /net/replace-text-facades/
description: Cette section explique comment travailler avec le Texte - Façades en utilisant la classe PdfContentEditor.
lastmod: "2021-06-24"
draft: false
---

## Remplacer le Texte dans un Fichier PDF Existant

Pour remplacer du texte dans un fichier PDF existant, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier un fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Après cela, vous devez appeler la méthode [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index). Vous devez enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Le code suivant vous montre comment remplacer du texte dans un fichier PDF existant.

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(_dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // save the output file
    editor.Save(_dataDir + "PdfContentEditorDemo01.pdf");
    }
```

Vérifiez comment cela apparaît dans le document original :

![Remplacer le Texte](replace_text1.png)

Et vérifiez le résultat après avoir remplacé le texte :

![Résultat du remplacement du Texte](replace_text2.png)


Dans le deuxième exemple, vous verrez comment, en plus de remplacer le texte, vous pouvez également augmenter ou diminuer la taille de la police :
```csharp
public static void ReplaceText02()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // enregistrer le fichier de sortie
        editor.Save(_dataDir + "PdfContentEditorDemo02.pdf");
    }
```

Pour des possibilités plus avancées pour travailler avec notre texte, nous utiliserons la méthode [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate). Avec cette méthode, nous pouvons rendre le texte gras, en italique, coloré, et ainsi de suite.

```csharp
    public static void ReplaceText03()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        TextState textState = new TextState
        {
            ForegroundColor = Color.Red,
            FontSize = 12,
        };
        editor.ReplaceText("Value", "Label", textState);

        // enregistrer le fichier de sortie
        editor.Save(_dataDir + "PdfContentEditorDemo03.pdf");
    }
```

Au cas où vous auriez besoin de remplacer tout le texte spécifié dans le document, utilisez l'extrait de code suivant. C'est-à-dire, le remplacement du texte aura lieu partout où le texte spécifié pour le remplacement sera rencontré, et il comptera également le nombre de tels remplacements.

```csharp
public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.ReplaceText("Value", "Label")) count++;

        Console.WriteLine($"{count} occurrences have been replaced.");

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![Remplacer tout le texte](replace_text3.png)

Le code suivant montre comment effectuer tous les remplacements de texte mais sur une page spécifique de votre document.

```csharp
public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.ReplaceText("9999", 2, "ABCDE")) count++;
        Console.WriteLine($"{count} occurrences have been replaced.");

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```
Dans l'extrait de code suivant, nous montrerons comment remplacer, par exemple, un nombre donné par les lettres dont nous avons besoin.

```csharp
   public static void ReplaceText06()
    {
        PdfContentEditor editor = new PdfContentEditor
        {
            ReplaceTextStrategy = new ReplaceTextStrategy
            {
                IsRegularExpressionUsed = true,
                ReplaceScope = ReplaceTextStrategy.Scope.ReplaceAll
            }
        };
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("\\d{4}", "ABCDE");
        // enregistrer le fichier de sortie
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```