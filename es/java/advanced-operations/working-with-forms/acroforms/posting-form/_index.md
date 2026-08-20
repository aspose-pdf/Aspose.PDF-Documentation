---
title: Publicar formularios en PDF a través de Java
linktitle: Formularios de publicación
type: docs
weight: 75
url: /java/posting-form/
description: Agregue botones de envío y acciones de envío a PDF AcroForms usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue botones de envío y acciones de publicación de formularios a archivos PDF con Java
Abstract: Este artículo muestra cómo agregar la funcionalidad de envío a formularios PDF usando Aspose.PDF para Java. Cubre la creación de un botón de envío con FormEditor y la creación de un campo de botón personalizado que utiliza SubmitFormAction para tener más control sobre la URL de envío y las banderas.
---
Aspose.PDF para Java admite la creación de botones de envío tanto basados ​​en fachada como en DOM.


## 
Agregue un botón de envío con FormEditor


1. 
Cree una fachada de [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) para el documento PDF de origen.

1. 
Agregue el objeto del botón de envío configurado a través de la fachada [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/).

1. 
Guarde el documento PDF actualizado.

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

## Agregar una acción de envío manualmente


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree la [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) y la URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).

1. 
Cree el [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) en la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y asigne la acción de envío.

1. 
Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
