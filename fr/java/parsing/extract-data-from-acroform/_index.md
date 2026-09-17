---
title: Extraire des données d'AcroForm à l'aide de Java
linktitle: Extraire des données d'AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: Aspose.PDF facilite l'extraction des données des champs de formulaire à partir de fichiers PDF. Découvrez comment extraire des données d'AcroForms et les enregistrer au format JSON, XML ou FDF.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des données d'AcroForm via Java
Abstract: Cet article explique comment extraire et exporter des données AcroForm à partir de fichiers PDF avec Aspose.PDF pour Java. Il couvre la lecture de tous les champs de formulaire, la récupération d'une valeur de champ par nom, l'exportation des données de champ au format JSON et l'écriture des données de formulaire aux formats XML, FDF et XFDF.
---
## Extraire tous les champs du formulaire



Utilisez `com.aspose.pdf.facades.Form` pour lire les noms et les valeurs des champs sans passer par le modèle objet complet du document.


1. 
Ouvrez le formulaire PDF source avec la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) afin que les champs AcroForm puissent être lus sans parcourir le modèle objet complet du document.

1. 
Appelez `getFieldNames()` pour collecter tous les identifiants de champs présents dans le formulaire.

1. 
Parcourez ces noms de champs et appelez `getField(fieldName)` pour lire chaque valeur de champ.
1. Créez la chaîne de sortie à partir des paires clé-valeur extraites et imprimez les données agrégées du formulaire.

1. 
Fermez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) dans le bloc `finally`.


```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## 
Récupérer une valeur de champ par nom


1. 
Ouvrez le formulaire PDF source avec la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. 
Appelez `getField(fieldName)` avec le nom du champ demandé pour lire sa valeur actuelle à partir des données AcroForm.
1. Imprimez la valeur du champ extraite.

1. 
Fermez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) dans le bloc `finally`.


```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## 
Exporter les champs du formulaire vers JSON


1. 
Ouvrez le formulaire PDF source avec la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. 
Appelez `getFieldNames()` pour collecter tous les identifiants de champs disponibles dans l'AcroForm.
1. Parcourez ces champs, échappez les noms et les valeurs et créez une chaîne d'objet JSON.

1. 
Écrivez le résultat JSON dans le fichier de sortie.

1. 
Fermez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) dans le bloc `finally`.


```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
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
Exporter les données du formulaire vers XML, FDF et XFDF


1. 
Créez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sans encore lier de document.
1. Ouvrez un flux de sortie pour le fichier XML et liez le PDF source à la façade avec `bindPdf(...)`.

1. 
Appelez `exportXml(stream)` pour que les données actuelles du champ de formulaire soient sérialisées au format XML.

1. 
Fermez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) une fois l'exportation terminée.


```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

1. 
Créez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sans encore lier de document.

1. 
Ouvrez un flux de sortie pour le fichier FDF et liez le PDF source à la façade avec `bindPdf(...)`.
1. Appelez `exportFdf(stream)` pour que les données du champ du formulaire soient sérialisées au format FDF.

1. 
Fermez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) une fois l'exportation terminée.


```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

1. 
Créez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sans encore lier de document.

1. 
Ouvrez un flux de sortie pour le fichier XFDF et liez le PDF source à la façade avec `bindPdf(...)`.

1. 
Appelez `exportXfdf(stream)` pour que les données du champ du formulaire soient sérialisées au format XFDF.
1. Fermez la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) une fois l'exportation terminée.

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
