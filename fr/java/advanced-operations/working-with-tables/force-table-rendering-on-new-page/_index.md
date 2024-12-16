---
title: Forcer le Rendu de Table sur une Nouvelle Page
type: docs
weight: 20
url: /fr/java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## Rendre une Table sur une Nouvelle Page

Par défaut, les paragraphes sont ajoutés à la collection Paragraphs d'un objet Page. Cependant, il est possible de rendre une table sur une nouvelle page au lieu de directement après l'objet de niveau paragraphe précédemment ajouté sur la page.

### Ajouter une Table

Pour rendre une table sur une nouvelle page, utilisez la méthode [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) dans la classe [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph). Le code suivant montre comment faire.

```java
public static void RenderTableOnNewPage(){
        Document doc = new Document();
        PageInfo pageInfo = doc.getPageInfo();
        MarginInfo marginInfo = pageInfo.getMargin();

        marginInfo.setLeft (37);
        marginInfo.setRight (37);
        marginInfo.setTop (37);
        marginInfo.setBottom (37);

        pageInfo.setLandscape(true);

        Table table = new Table();
        table.setColumnWidths ("50 100");
        // Page ajoutée.
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("Contenu 1"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("HHHHH"));
        }
        Paragraphs paragraphs = curPage.getParagraphs();
        paragraphs.add(table);
        /********************************************/
        Table table1 = new Table();
        table.setColumnWidths ("100 100");
        for (int i = 1; i <= 10; i++)
        {
            Row row = table1.getRows().add();
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("LAAAAAAA"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("LAAGGGGGG"));
        }
        table1.setInNewPage (true);
        // Je veux garder la table 1 à la page suivante s'il vous plaît...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

La classe com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) permet de créer/rendre des tableaux dans les documents PDF. Une fonctionnalité similaire est également prise en charge par la classe aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), mais nous encourageons nos clients à essayer d'utiliser le dernier Modèle d'Objet Document (DOM) du package com.aspose.pdf, car toutes les nouvelles fonctionnalités et résolutions de problèmes sont effectuées dans le nouveau DOM. Cependant, l'ancien Aspose.PDF pour Java (le package aspose.pdf) a une méthode [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) dans la classe paragraphe, afin que le paragraphe soit rendu sur une nouvelle page. Pour la compatibilité ascendante, la méthode [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) a été ajoutée à la classe [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph).

{{% /alert %}}