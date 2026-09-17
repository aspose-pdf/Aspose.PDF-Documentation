---
title: Lecture des valeurs du formulaire
linktitle: Lecture des valeurs du formulaire
type: docs
weight: 60
url: /java/reading-form-values/
description: Découvrez comment inspecter les noms et les valeurs des champs de formulaire PDF en Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Lire les noms et valeurs des champs du formulaire PDF en Java
Abstract: Cette section couvre les flux de travail de lecture de formulaire Java implémentés dans l'ensemble d'exemples de façade de formulaire actuel pour Aspose.PDF pour Java. Le référentiel fournit un exemple général d'inspection sur le terrain et utilise des notes de portée explicites pour les pages spécialisées qui ne disposent pas encore d'exemples Java correspondants.
---
La classe Java `FormExamples` illustre les principaux workflows de traitement de formulaires exposés par l'API Facades.


## 
Obtenir les valeurs des champs



Utilisez `FormExamples.inspectFormFields(...)` pour inspecter les noms de champs et leurs valeurs actuelles.

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
