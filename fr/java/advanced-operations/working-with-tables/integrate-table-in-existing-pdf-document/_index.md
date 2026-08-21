---
title: Intégrer des tableaux PDF avec des sources de données en Java
linktitle: Intégrer le tableau
type: docs
weight: 30
url: /java/integrate-table/
description: Découvrez comment intégrer des tableaux PDF à des sources de données structurées telles que des fichiers CSV en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créez des tableaux PDF à partir de données structurées avec Java
Abstract: Cet article explique comment intégrer des tableaux PDF avec des données externes à l'aide d'Aspose.PDF pour Java. Il couvre la lecture des données CSV, la sélection de colonnes spécifiques, la création d'un objet Table stylisé à partir des lignes analysées et le rendu du résultat dans un document PDF.
---
L'exemple Java crée des tableaux PDF à partir de données CSV sans recourir à des bibliothèques de trames de données externes.


## 
Construire un tableau à partir de lignes CSV



Utilisez cet exemple lorsque les colonnes CSV sélectionnées doivent être transformées en un tableau PDF stylisé.


1. 
Créez une [Table] (https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) et configurez ses bordures.

1. 
Détectez les index de colonnes requis à partir de la ligne d’en-tête CSV.
1. Ajoutez la ligne d'en-tête et le nombre demandé de lignes de données, puis renvoyez le tableau.


```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## 
Créer un PDF à partir de données CSV



Utilisez cet exemple lorsque l’entrée CSV doit être restituée sous forme de document tableau PDF.


1. 
Lisez les lignes CSV du fichier d'entrée.

1. 
Prévisualisez un sous-ensemble des lignes analysées dans la console.
1. Créez un [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), ajoutez le tableau généré et enregistrez le fichier de sortie.


```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## 
Rechercher les index de colonnes CSV par nom



Utilisez cette assistante lorsque des colonnes nommées spécifiques doivent être situées dans la ligne d'en-tête CSV.


1. 
Parcourez les noms de colonnes demandés.

1. 
Recherchez dans la ligne d'en-tête les index correspondants.
1. Renvoie les positions des colonnes collectées.


```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## 
Lire les lignes CSV d'un fichier



Utilisez cet assistant lorsque la source CSV doit être chargée en mémoire avant la génération de la table.


1. 
Lisez toutes les lignes du fichier d'entrée.

1. 
Divisez chaque ligne avec l'assistant de l'analyseur CSV.
1. Renvoie les valeurs de ligne collectées.


```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## 
Diviser une ligne CSV en valeurs



Utilisez cet assistant lorsqu'une ligne CSV peut contenir des valeurs entre guillemets et des guillemets d'échappement.


1. 
Parcourez les caractères de la ligne.

1. 
Vérifiez si l'analyseur se trouve actuellement dans le texte cité.
1. Créez la liste de valeurs finale et renvoyez-la sous forme de tableau.

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```
