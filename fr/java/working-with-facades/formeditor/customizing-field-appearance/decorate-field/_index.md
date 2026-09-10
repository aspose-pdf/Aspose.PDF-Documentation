---
title: Décorer le champ
linktitle: Décorer le champ
type: docs
weight: 10
url: /java/decorate-field/
description: Apprenez à décorer un champ de formulaire PDF avec des couleurs et un alignement en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Décorer un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, configurer un FormFieldFacade avec des couleurs et un alignement, décorer un champ et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Décorer un champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Configurez un `FormFieldFacade` avec les couleurs et l'alignement requis.

3. 
Passez la façade à l'éditeur et appelez `decorateField(...)`.

4. 
Enregistrez le document mis à jour.

```java
public static void decorateField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        FormFieldFacade facade = new FormFieldFacade();
        facade.setBackgroundColor(Color.RED);
        facade.setTextColor(Color.BLUE);
        facade.setBorderColor(Color.GREEN);
        facade.setAlignment(FormFieldFacade.ALIGN_CENTER);
        editor.setFacade(facade);
        editor.decorateField("First Name");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
