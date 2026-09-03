---
title: Publicar formularios en PDF mediante Java
linktitle: Publicar formularios
type: docs
weight: 75
url: /es/java/posting-form/
description: Agregar botones de envío y acciones de envío a los AcroForms de PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar botones de envío y acciones de publicación de formularios a archivos PDF con Java
Abstract: Este artículo muestra cómo agregar funcionalidad de envío a formularios PDF usando Aspose.PDF for Java. Cubre la creación de un botón de envío con FormEditor y la construcción de un campo de botón personalizado que utiliza SubmitFormAction para un mayor control sobre la URL de envío y los indicadores.
---
Aspose.PDF for Java admite la creación de botones de envío tanto facade-based como DOM-based.

## Agregar un botón de envío con FormEditor

1. Crear un [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) fachada para el documento PDF de origen.
1. Agregar el objeto botón de envío configurado a través del [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) fachada.
1. Guarde el documento PDF actualizado.

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

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear el [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) y URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. Crear el [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) en el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y asignar la acción de envío.
1. Guardar el PDF actualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
