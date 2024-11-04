---
title: Déplacer des Pages PDF 
linktitle: Déplacer des Pages
type: docs
weight: 20
url: /java/move-pages/
description: Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Déplacement d'une Page d'un Document PDF vers un Autre

Ce sujet explique comment déplacer une page d'un document PDF vers la fin d'un autre document en utilisant Java.
Pour déplacer une page, nous devrions :

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF source.
1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF de destination.
1. Obtenir la Page de la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Ajouter la page au document de destination.
1. Enregistrer le PDF de sortie en utilisant la méthode Save.
1. Supprimer la page dans le document source.
1. Enregistrer le PDF source en utilisant la méthode Save.

Le snippet de code suivant montre comment déplacer une page.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // Enregistrer le fichier de sortie
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## Déplacement d'un ensemble de pages d'un document PDF à un autre

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF source.
2. Créez un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF de destination.
3. Définissez un tableau avec les numéros de pages à déplacer.

1. Exécuter une boucle à travers le tableau :
    1. Obtenez la page de la [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) collection.
    1. Ajoutez la page au document de destination.
1. Enregistrez le PDF de sortie en utilisant la méthode Save.
1. Supprimez la page dans le document source en utilisant le tableau.
1. Enregistrez le PDF source en utilisant la méthode Save.

Le snippet de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // Enregistrer les fichiers de sortie
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## Déplacer une page dans un nouvel emplacement dans le document PDF actuel

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF source.
1. Obtenez la page de la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Ajouter la page à la nouvelle position (par exemple à la fin).
1. Supprimer la page à l'emplacement précédent.
1. Enregistrez le PDF de sortie en utilisant la méthode Save.

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // Enregistrer le fichier de sortie
    srcDocument.save(dstFileName);
  }
}
```