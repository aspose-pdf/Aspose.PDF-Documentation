---
title: Supprimer des tableaux des documents PDF existants
linktitle: Supprimer des tableaux
description: Découvrez comment supprimer un ou plusieurs tableaux de documents PDF existants en Java.
lastmod: "2026-06-09"
type: docs
weight: 50
url: /java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer un ou plusieurs tableaux des fichiers PDF avec Java
Abstract: Cet article explique comment supprimer des tableaux de documents PDF existants à l'aide d'Aspose.PDF pour Java. Il présente TableAbsorber pour localiser les tables et montre comment supprimer une seule table ou supprimer toutes les tables détectées d'une page.
---
Utilisez `TableAbsorber` lorsque vous devez supprimer un ou plusieurs tableaux détectés d'un PDF existant.


## 
Supprimer une table détectée



Utilisez cet exemple lorsque seule la première table correspondante sur une page doit être supprimée.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Visitez la page cible avec [TableAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Supprimez le premier tableau détecté et enregistrez le document.


```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer toutes les tables détectées d'une page



Utilisez cet exemple lorsque chaque table correspondante sur la page doit être supprimée.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Visitez la page cible avec [TableAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) et copiez les tables détectées dans une liste.
1. Supprimez chaque tableau détecté et enregistrez le PDF mis à jour.

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
