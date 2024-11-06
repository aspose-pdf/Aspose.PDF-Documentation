---
title: Remplacer le Texte dans un Fichier PDF
type: docs
weight: 40
url: fr/java/replace-text/
description: Cette section explique comment remplacer du texte avec Aspose.PDF Facades - un ensemble d'outils pour les opérations populaires avec les PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Remplacer le Texte dans un Fichier PDF Existant (facades)

Pour remplacer du texte dans un fichier PDF existant, vous devez créer un objet de la classe [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), et lier un fichier PDF d'entrée en utilisant la méthode bindPdf. Ensuite, vous devez appeler la méthode [replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-).
Vous devez enregistrer le fichier PDF mis à jour en utilisant la méthode save de la classe [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Le snippet de code suivant vous montre comment remplacer du texte dans un fichier PDF existant.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.TextState;
import com.aspose.pdf.facades.PdfContentEditor;
import com.aspose.pdf.facades.ReplaceTextStrategy;

public class PdfContentEditorText {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ReplaceText01(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label");

        // enregistrer le fichier de sortie
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


Vérifiez comment cela apparaît dans le document original :

![Remplacer le Texte](replace_text1.png)

Et vérifiez le résultat après avoir remplacé le texte :

![Résultat du remplacement du Texte](replace_text2.png)

Dans le deuxième exemple, vous verrez comment, en plus de remplacer le texte, vous pouvez également augmenter ou diminuer la taille de la police :

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // enregistrez le fichier de sortie
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

Pour des possibilités plus avancées de travail avec notre texte, nous utiliserons la méthode [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState). Avec cette méthode, nous pouvons rendre le texte gras, en italique, coloré, etc.

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // enregistrez le fichier de sortie
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    

```


Dans le cas où vous avez besoin de remplacer tout le texte spécifié dans le document, utilisez l'extrait de code suivant. C'est-à-dire que le remplacement du texte aura lieu partout où le texte spécifié pour le remplacement sera rencontré, et il comptera également le nombre de ces remplacements.

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" occurrences have been replaced.");

        // sauvegarder le fichier de sortie
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![Remplacer tout le texte](replace_text3.png)

L'extrait de code suivant montre comment effectuer tous les remplacements de texte mais sur une page spécifique de votre document.

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" occurrences have been replaced.");

        // sauvegarder le fichier de sortie
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


Dans le prochain extrait de code, nous allons montrer comment remplacer, par exemple, un nombre donné par les lettres dont nous avons besoin.

```java
    public static void ReplaceText06()
    {
        PdfContentEditor editor = new PdfContentEditor();
        ReplaceTextStrategy replaceTextStrategy = new ReplaceTextStrategy();
        replaceTextStrategy.setRegularExpressionUsed(true);
        replaceTextStrategy.setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.setReplaceTextStrategy(replaceTextStrategy);
        
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.replaceText("\\d{4}", "ABCDE");

        // enregistrer le fichier de sortie
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```