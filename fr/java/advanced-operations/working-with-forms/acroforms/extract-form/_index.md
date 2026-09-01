---
title: Extraire AcroForm - Extraire les données d'un formulaire PDF en Java
linktitle: Extraire AcroForm
type: docs
weight: 30
url: /java/extract-form/
description: Extrayez les valeurs des champs AcroForm dans les documents PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les valeurs des champs de formulaire à partir de fichiers PDF avec Java
Abstract: Cet article montre comment extraire des données des champs AcroForm à l'aide d'Aspose.PDF pour Java. L'exemple parcourt les noms de champs avec la façade Form, lit chaque valeur actuelle et stocke le résultat dans une carte pour le traitement en aval.
---
Utilisez la façade `Form` lorsque vous avez besoin d'un simple flux d'extraction de nom de champ à valeur de champ.


## 
Extraire les valeurs de tous les champs AcroForm


1. 
Ouvrez le document de formulaire PDF avec la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. 
Parcourez les noms de champs de la façade [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) et lisez chaque valeur de champ actuelle dans une carte.

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```
