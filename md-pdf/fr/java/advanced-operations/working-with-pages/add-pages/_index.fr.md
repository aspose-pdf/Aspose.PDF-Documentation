---
title: Ajouter des Pages dans un PDF 
linktitle: Ajouter des Pages
type: docs
weight: 10
url: /java/add-pages/
description: Cet article explique comment insérer (ajouter) une page à l'emplacement souhaité dans un fichier PDF. Apprenez comment déplacer, supprimer (effacer) des pages d'un fichier PDF en utilisant la bibliothèque Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter ou Insérer une Page dans un Fichier PDF

Aspose.PDF pour Java vous permet d'insérer une page dans un document PDF à n'importe quel emplacement dans le fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF. Vous devez passer l'emplacement où vous souhaitez insérer la page vierge à la méthode d'insertion. Cette section montre comment ajouter des pages à un PDF avec Aspose.PDF pour Java.

### Insérer une Page Vide dans un Fichier PDF à l'Emplacement Souhaité

Le code suivant montre comment insérer une page vide dans un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF d'entrée.

1. Appelez la méthode Insert de la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) avec l'index spécifié.
1. Enregistrez le PDF de sortie en utilisant la méthode Save.

Le snippet de code suivant vous montre comment insérer une page dans un fichier PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // Ajouter une page
        document.getPages().add();

        // Insérer une page vide dans un PDF
        document.getPages().insert(2);

        // Enregistrer le PDF mis à jour
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

Dans l'exemple ci-dessus, nous avons ajouté une page vide avec des paramètres par défaut. Si vous devez faire en sorte que la taille de la page soit la même qu'une autre page du document, vous devez ajouter quelques lignes de code :

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // Ajouter une page
        Page page1 = document.getPages().add();

        // Insérer une page vide dans un PDF
        Page page2 = document.getPages().insert(2);
        ;
        // copier les paramètres de la page depuis la page 1
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // Enregistrer le PDF mis à jour
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### Ajouter une Page Vide à la Fin d'un Fichier PDF

Parfois, vous souhaitez vous assurer qu'un document se termine par une page vide. Ce sujet explique comment insérer une page vide à la fin du document PDF.

Pour insérer une page vide à la fin d'un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF d'entrée.
1. Appelez la méthode Add de la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection), sans aucun paramètre.
1. Enregistrez le PDF de sortie en utilisant la méthode Save.

Le fragment de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // Ajouter une page
        document.getPages().add();

        // Insérer une page vide à la fin d'un fichier PDF
        document.getPages().add();

        // Enregistrer le PDF mis à jour
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```