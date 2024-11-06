---
title: Supprimer des tableaux d'un PDF existant
linktitle: Supprimer des tableaux
type: docs
weight: 40
url: fr/java/remove-tables-from-existing-pdf/
description: Aspose.PDF pour Java vous permet de supprimer un tableau et plusieurs tableaux de votre document PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF pour Java offre la possibilité d'insérer/créer un tableau dans un document PDF lors de sa génération à partir de zéro ou vous pouvez également ajouter l'objet tableau dans n'importe quel document PDF existant. Cependant, vous pouvez avoir besoin de [Manipuler des tableaux dans un PDF existant](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/) où vous pouvez mettre à jour le contenu des cellules de tableau existantes. Cependant, vous pouvez être confronté à la nécessité de supprimer des objets tableau d'un document PDF existant.

{{% /alert %}}

Pour supprimer les tableaux, nous devons utiliser la classe [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) pour saisir les tableaux dans le PDF existant et ensuite appeler la méthode [Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-).

## Supprimer un tableau d'un document PDF

Nous avons ajouté une nouvelle fonction, c'est-à-dire Remove(), à la classe existante [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) afin de supprimer un tableau d'un document PDF. Une fois que l'absorbeur trouve avec succès les tables sur la page, il devient capable de les supprimer. Veuillez consulter l'extrait de code suivant montrant comment supprimer un tableau d'un document PDF :

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // Charger le document PDF existant
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // Créer un objet TableAbsorber pour trouver les tables
        TableAbsorber absorber = new TableAbsorber();

        // Visiter la première page avec l'absorbeur
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Obtenir le premier tableau de la page
        AbsorbedTable table = absorber.getTableList().get(0);

        // Supprimer le tableau
        absorber.remove(table);

        // Enregistrer le PDF
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## Supprimer plusieurs tables d'un document PDF

Parfois, un document PDF peut contenir plus d'une table et vous pourriez avoir besoin de supprimer plusieurs tables de celui-ci. Afin de supprimer plusieurs tables d'un document PDF, veuillez utiliser l'extrait de code suivant :

```java
    public static void RemoveMultipleTable() {
        // Charger le document PDF existant
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Créer un objet TableAbsorber pour trouver les tables
        TableAbsorber absorber = new TableAbsorber();

        // Visiter la deuxième page avec l'absorbeur
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // Boucle à travers la copie de la collection et suppression des tables
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // Enregistrer le document
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```