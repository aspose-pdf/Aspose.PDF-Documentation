---
title: Importer et exporter des données de formulaire
linktitle: Importer et exporter des données de formulaire
type: docs
weight: 80
url: /java/import-export-form-data/
description: Importez et exportez les données des champs AcroForm aux formats XML, FDF, XFDF et JSON à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importer et exporter des données de formulaire PDF avec Java
Abstract: Cet article explique comment échanger des données AcroForm avec des formats externes à l'aide d'Aspose.PDF pour Java. Il couvre l'importation et l'exportation de données XML, FDF et XFDF via la façade de formulaire et l'extraction des valeurs des champs de formulaire au format JSON.
---
Aspose.PDF pour Java prend en charge plusieurs formats d'échange de données courants pour les formulaires interactifs.


## 
Importer des données de formulaire à partir de XML



Utilisez cet exemple lorsque les valeurs du formulaire sont stockées dans un fichier XML et doivent être appliquées à un formulaire PDF.


1. 
Créez une façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) et liez le PDF source.

1. 
Ouvrez le flux d'entrée XML et importez les données dans le formulaire.
1. Enregistrez le document PDF mis à jour.


```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
Exporter les données du formulaire vers XML



Utilisez cet exemple lorsque vous devez stocker les valeurs AcroForm actuelles au format XML.


1. 
Créez une façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) et liez le PDF source.

1. 
Ouvrez le flux de sortie du fichier XML.
1. Exportez les données du formulaire au format XML.


```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## 
Importer les données du formulaire depuis FDF



Utilisez cet exemple lorsque les valeurs du formulaire arrivent au format d'échange FDF.


1. 
Créez une façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) et liez le PDF source.

1. 
Ouvrez le flux d'entrée FDF et importez les données.
1. Enregistrez le document PDF rempli.


```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
Exporter les données du formulaire vers FDF



Utilisez cet exemple lorsque les valeurs du formulaire PDF doivent être partagées sous forme de fichier FDF.


1. 
Créez une façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) et liez le PDF source.

1. 
Ouvrez le flux de sortie du fichier FDF.
1. Exportez les données du formulaire au format FDF.


```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## 
Importer des données de formulaire depuis XFDF



Utilisez cet exemple lorsque les données du formulaire sont fournies au format XFDF et doivent être fusionnées dans un PDF.


1. 
Créez une façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) et liez le PDF source.

1. 
Ouvrez le flux d'entrée XFDF et importez les valeurs.
1. Enregistrez le document PDF mis à jour.


```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
Exporter les données du formulaire vers XFDF



Utilisez cet exemple lorsque vous avez besoin d'un fichier d'échange XML pour les valeurs AcroForm.


1. 
Créez une façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) et liez le PDF source.

1. 
Ouvrez le flux de sortie du fichier XFDF.
1. Exportez les valeurs actuelles du formulaire vers XFDF.


```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## 
Extraire les champs du formulaire vers JSON



Utilisez cet exemple lorsque les valeurs du formulaire doivent être exportées vers une représentation JSON légère.


1. 
Ouvrez le PDF avec la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. 
Parcourez les noms de champs et sérialisez leurs valeurs dans du texte JSON.
1. Écrivez le contenu JSON dans le fichier cible.


```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## 
Réutiliser l'assistant d'extraction JSON



Utilisez cet exemple lorsque vous souhaitez une méthode wrapper dédiée qui délègue à la routine d'exportation JSON principale.


1. 
Appelez l'assistant d'extraction JSON existant avec le PDF source et le chemin de sortie.

1. 
Réutilisez la même logique d’extraction sans dupliquer le code de sérialisation.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
