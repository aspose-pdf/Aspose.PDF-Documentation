---
title: Travailler avec les formulaires XFA
linktitle: Formulaires XFA
type: docs
weight: 20
url: /java/xfa-forms/
description: Découvrez comment convertir des formulaires XFA en AcroForms standard dans des documents PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertissez des formulaires PDF basés sur XFA en AcroForms standard avec Java
Abstract: Cet article explique comment utiliser des formulaires basés sur XFA à l'aide d'Aspose.PDF pour Java. Il couvre la conversion d'un formulaire XFA dynamique en un AcroForm standard et la gestion des documents XFA qui nécessitent l'option ignorer les besoins de rendu avant la conversion.
---
Les formulaires XFA peuvent être convertis en AcroForms standard afin de pouvoir être traités avec les API de formulaire PDF classiques.


## 
Convertir un formulaire XFA dynamique en AcroForm


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez au document [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) et définissez les propriétés [FormType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) requises.

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Convertissez un formulaire XFA avec `ignoreNeedsRendering`


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez au document [Form] (https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) et définissez les propriétés `ignoreNeedsRendering` et [FormType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) requises.

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertXfaFormWithIgnoreNeedsRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (!document.getForm().getNeedsRendering() && document.getForm().hasXfa()) {
            document.getForm().setIgnoreNeedsRendering(true);
        }
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```
