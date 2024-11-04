---
title: Saut de page dans un PDF existant
type: docs
weight: 30
url: /java/page-break-in-existing-pdf/
description: Cette section explique comment insérer des sauts de page dans un PDF existant en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Par défaut, le contenu à l'intérieur des fichiers PDF est ajouté dans une disposition de Haut-Gauche à Bas-Droite. Une fois que le contenu dépasse la marge inférieure de la page, le saut de page se produit. Cependant, vous pouvez rencontrer un besoin d'insérer un saut de page selon les exigences. Une méthode nommée AddPageBreak(...) a été ajoutée dans la classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) pour répondre à ce besoin.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- src est le document source/chemin vers le document/flux avec le document source
- dest est le document de destination/chemin où le document sera enregistré/flux où le document sera enregistré
- PageBreak est un tableau d'objets de saut de page. Il a deux propriétés : l'index de la page où le saut de page doit être placé et la position verticale du saut de page sur la page.

## Exemple 1 (Ajouter un saut de page)

```java
   public static void PageBrakeExample01() {
        // Instancier l'objet Document
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // Instancier un objet Document vide
        Document dest = new Document();
        // Créer un objet PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // Enregistrer le fichier résultant
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## Exemple 2

```java
  public static void PageBrakeExample02() {
        // Créer un objet PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## Exemple 3

```java
 public static void PageBrakeExample03() {
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```