---
title: Work with PDF Actions in Java
linktitle: Actions
type: docs
weight: 20
url: /java/actions/
description: Learn how to add, update, and remove document, page, and form actions in PDF files using Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Add document, page, and form actions to PDF files in Java
Abstract: This article explains how to work with actions in PDF documents using Aspose.PDF for Java. It covers named actions for printing and page navigation, hiding form fields, submitting forms, assigning JavaScript launch actions, and adding or removing page open and close actions.
---
Aspose.PDF for Java lets you assign actions to buttons, documents, and pages to make PDF files interactive.

## Add a print button with a named action

```java
public static void addNamedActionPrint(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setPartialName("printButton");
        printButton.setValue("Print");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setWidth(1);
        printButton.setBorder(border);

        document.getForm().add(printButton, 1);
        document.save(outputFile.toString());
    }
}
```

## Add a button that hides form fields

The example source also includes `addNamedActionHide`, which gathers checkbox widgets and assigns a `HideAction` to a button.

## Add navigation buttons

`addNavigationButtons` creates buttons for first, previous, next, and last page navigation by assigning `NamedAction` values such as `PredefinedAction.FirstPage` and `PredefinedAction.NextPage`.

## Add a submit action

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        FileSpecification submitUrl = new FileSpecification();
        submitUrl.setFileSystem("URL");
        submitUrl.setName("http://localhost:3000/submit");
        submitAction.setUrl(submitUrl);
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), rect);
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getAnnotationActions().setOnReleaseMouseBtn(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```

## Add document and page actions

The `ActionsExamples` class also demonstrates:

- `addLaunchActions` to set document open, before-save, and before-print JavaScript actions.
- `addPageActions` to assign `GoToAction` and `JavascriptAction` handlers to a page.
- `removePageActions` to clear page actions with `page.getActions().removeActions()`.
