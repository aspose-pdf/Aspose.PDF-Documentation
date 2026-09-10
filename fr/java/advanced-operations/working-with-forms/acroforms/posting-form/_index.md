---
title: Publication de formulaires au format PDF via Java
linktitle: Formulaires de publication
type: docs
weight: 75
url: /java/posting-form/
description: Ajoutez des boutons de soumission et des actions de soumission aux PDF AcroForms à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajoutez des boutons de soumission et des actions de publication de formulaire aux fichiers PDF avec Java
Abstract: Cet article montre comment ajouter une fonctionnalité de soumission aux formulaires PDF à l'aide d'Aspose.PDF pour Java. Il couvre la création d'un bouton de soumission avec FormEditor et la création d'un champ de bouton personnalisé qui utilise SubmitFormAction pour plus de contrôle sur l'URL et les indicateurs de soumission.
---
Aspose.PDF pour Java prend en charge la création de boutons de soumission basés sur la façade et sur le DOM.


## 
Ajouter un bouton de soumission avec FormEditor


1. 
Créez une façade [FormEditor] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) pour le document PDF source.

1. 
Ajoutez l'objet bouton de soumission configuré via la façade [FormEditor] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/).

1. 
Enregistrez le document PDF mis à jour.

```java
public static void addSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    editor.bindPdf(inputFile.toString());
    try {
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show",
                100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

## Ajouter manuellement une action de soumission


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez le [SubmitFormAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) et l'URL [FileSpecification] (https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).

1. 
Créez le [ButtonField] (https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) sur la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et attribuez l'action de soumission.

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        submitAction.setUrl(new FileSpecification("http://localhost:3000/submit"));
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), new Rectangle(10, 10, 100, 40));
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getPdfActions().add(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```
