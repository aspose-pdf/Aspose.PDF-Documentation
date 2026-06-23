---
title: Posting Forms in PDF via Java
linktitle: Posting Forms
type: docs
weight: 75
url: /java/posting-form/
description: Add submit buttons and submission actions to PDF AcroForms using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add submit buttons and form post actions to PDF files with Java
Abstract: This article shows how to add submit functionality to PDF forms using Aspose.PDF for Java. It covers creating a submit button with FormEditor and building a custom button field that uses SubmitFormAction for more control over the submission URL and flags.
---
Aspose.PDF for Java supports both facade-based and DOM-based submit button creation.

## Add a submit button with FormEditor

1. Create a [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) facade for the source PDF document.
1. Add the configured submit button object through the [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) facade.
1. Save the updated PDF document.

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

## Add a submit action manually

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create the [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) and URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. Create the [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) on the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and assign the submit action.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
