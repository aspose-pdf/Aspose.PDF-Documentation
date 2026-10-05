---
title: Lecture des valeurs du formulaire
linktitle: Lecture des valeurs du formulaire
type: docs
weight: 60
url: /java/reading-form-values/
description: Découvrez comment inspecter les noms et les valeurs des champs de formulaire PDF en Java à l'aide de la façade Form dans Aspose.PDF.
lastmod: "2026-09-22"
TechArticle: true
AlternativeHeadline: Lire les noms et valeurs des champs du formulaire PDF en Java
Abstract: Cette section couvre les flux de travail de lecture de formulaire Java implémentés dans l'ensemble d'exemples de façade Form actuel pour Aspose.PDF for Java. Le référentiel fournit un exemple général d’inspection des champs et utilise des notes explicites sur les limites des exemples pour les pages spécialisées qui ne disposent pas encore d'exemples Java correspondants.
---
La classe Java `FormExamples` illustre les principaux flux de travail de traitement de formulaires exposés par l'API Facades.

## Obtenir les valeurs des champs

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
