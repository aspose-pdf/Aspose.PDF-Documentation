---
title: Manipuler des tableaux dans des documents PDF existants
linktitle: Manipuler des tables
type: docs
weight: 40
url: /fr/java/manipulating-tables/
description: Découvrez comment inspecter et modifier des tableaux dans des documents PDF existants à l'aide de Java.
lastmod: "2026-09-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspecter et modifier les tableaux PDF existants avec Java
Abstract: Cet article explique comment manipuler des tableaux déjà présents dans les documents PDF à l'aide d'Aspose.PDF for Java. Il couvre la localisation des tableaux avec TableAbsorber, la mise à jour du texte à l'intérieur d'une cellule et le remplacement d’un tableau détecté par un nouvel objet Table.
---
Utilisez `TableAbsorber` lorsque vous devez localiser des tableaux existants et mettre à jour leur contenu.

## Remplacer le texte à l'intérieur d'une cellule de tableau

Utilisez cet exemple lorsque le texte d'une cellule détectée doit être mis à jour sans reconstruire l'intégralité du tableau.

1. Ouvrez le PDF source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et visitez la page avec [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Vérifiez que le tableau cible et les fragments de texte de cellule existent.
1. Remplacez le texte de la cellule et enregistrez le document mis à jour.

```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## Remplacer un tableau détecté par un nouveau tableau

Utilisez cet exemple lorsque le tableau d’origine doit être entièrement remplacée par un nouveau tableau.

1. Ouvrez le PDF source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et détectez les tableaux sur la page.
1. Créez une nouvelle [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) avec la structure souhaitée.
1. Remplacez le tableau absorbé et enregistrez le PDF de sortie.

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
