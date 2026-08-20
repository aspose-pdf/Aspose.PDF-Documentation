---
title: Trabajar con acciones de PDF en Java
linktitle: Acciones
type: docs
weight: 20
url: /java/actions/
description: Aprenda a agregar, actualizar y eliminar acciones de documentos, páginas y formularios en archivos PDF usando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Agregue acciones de documentos, páginas y formularios a archivos PDF en Java
Abstract: Este artículo explica cómo trabajar con acciones en documentos PDF usando Aspose.PDF para Java. Cubre acciones con nombre para imprimir y navegar por páginas, ocultar campos de formulario, enviar formularios, asignar acciones de inicio de JavaScript y agregar o eliminar acciones de apertura y cierre de páginas.
---
Aspose.PDF para Java le permite asignar acciones a botones, documentos y páginas para hacer que los archivos PDF sean interactivos.


## 
Agregar una acción de impresión con nombre



Utilice este ejemplo cuando un botón de la página deba activar el comando de impresión.


1. 
Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y seleccione la página de destino.

1. 
Cree un [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) y asigne una [NamedAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/namedaction/) para imprimir.
1. Agregue el botón al formulario y guarde el documento.


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

## 
Agregar una acción de ocultar



Utilice este ejemplo cuando un botón deba mostrar u ocultar un conjunto de campos de formulario, como casillas de verificación.


1. 
Abra el [Documento] PDF de origen (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y recopile los widgets del formulario de destino.

1. 
Cree un botón y asígnele una [HideAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/hideaction/).
1. Agregue el botón al formulario y guarde el documento actualizado.


```java
public static void addNamedActionHide(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<WidgetAnnotation> checkboxes = new ArrayList<>();
        for (WidgetAnnotation field : document.getForm()) {
            if (field instanceof CheckboxField) {
                checkboxes.add(field);
            }
        }

        Rectangle rect = new Rectangle(10, 410, 140, 440, true);
        ButtonField hideButton = new ButtonField(document.getPages().get_Item(1), rect);
        hideButton.setPartialName("HideButton");
        hideButton.setValue("Hide Checkboxes");
        hideButton.getAnnotationActions().setOnReleaseMouseBtn(
                new HideAction(checkboxes.toArray(new WidgetAnnotation[0]), true));

        document.getForm().add(hideButton, 1);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar botones de navegación de página



Este ejemplo crea botones de primera, anterior, siguiente y última página en todo el documento.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree botones de navegación para cada página y asigne la acción predefinida correspondiente.
1. Agregue los botones al formulario y guarde el documento.


```java
public static void addNavigationButtons(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        for (Page page : document.getPages()) {
            ButtonField firstPageButton = new ButtonField(page, new Rectangle(10, 10, 110, 40, true));
            firstPageButton.setPartialName("First Page");
            firstPageButton.setValue("First Page");
            firstPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            firstPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            firstPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            firstPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.FirstPage));
            document.getForm().add(firstPageButton);

            ButtonField previousPageButton = new ButtonField(page, new Rectangle(120, 10, 220, 40, true));
            previousPageButton.setPartialName("Previous Page");
            previousPageButton.setValue("Previous Page");
            previousPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            previousPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            previousPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            previousPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.PrevPage));
            document.getForm().add(previousPageButton);

            ButtonField nextPageButton = new ButtonField(page, new Rectangle(230, 10, 330, 40, true));
            nextPageButton.setPartialName("Next Page");
            nextPageButton.setValue("Next Page");
            nextPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            nextPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            nextPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            nextPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.NextPage));
            document.getForm().add(nextPageButton);

            ButtonField lastPageButton = new ButtonField(page, new Rectangle(340, 10, 440, 40, true));
            lastPageButton.setPartialName("Last Page");
            lastPageButton.setValue("Last Page");
            lastPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            lastPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            lastPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            lastPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.LastPage));
            document.getForm().add(lastPageButton);
        }

        document.save(outputFile.toString());
    }
}
```

## 
Agregar una acción de envío



Utilice este ejemplo cuando un botón deba enviar datos de formulario a una URL.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree una [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) con la URL de destino y las banderas.
1. Asigne la acción a un campo de botón y guarde el documento.


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

## 
Agregar acciones de lanzamiento a nivel de documento



Este ejemplo asigna acciones de JavaScript que se ejecutan cuando el documento se abre, guarda o imprime.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree los objetos [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) necesarios para los eventos del documento.
1. Asigne las acciones y guarde el documento.


```java
public static void addLaunchActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setOpenAction(new JavascriptAction("app.launchURL('http://localhost:3000/open');"));
        document.getActions().setBeforeSaving(
                new JavascriptAction("app.launchURL('http://localhost:3000/save');"));
        document.getActions().setBeforePrinting(
                new JavascriptAction("app.launchURL('http://localhost:3000/print');"));

        document.save(outputFile.toString());
    }
}
```

## 
Agregar acciones de apertura y cierre de página



Utilice este ejemplo cuando una página específica deba activar acciones de apertura y cierre.


1. 
Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y asegúrese de que exista la página de destino.

1. 
Cree las acciones de navegación de página y JavaScript.
1. Asigne las acciones de la página y guarde el documento.


```java
public static void addPageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        GoToAction action = new GoToAction(page);
        action.setDestination(new XYZExplicitDestination(page, 0, page.getPageInfo().getHeight(), 1));
        page.getActions().setOnOpen(action);
        page.getActions().setOnClose(
                new JavascriptAction("app.launchURL('http://localhost:3000/page/3');"));

        document.save(outputFile.toString());
    }
}
```

## 
Eliminar acciones de página



Utilice este enfoque cuando las acciones de apertura y cierre previamente asignadas deban borrarse de una página.


1. 
Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y asegúrese de que exista la página de destino.

1. 
Elimina todas las acciones de esa página.
1. Guarde el documento actualizado.

```java
public static void removePageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        page.getActions().removeActions();

        document.save(outputFile.toString());
    }
}
```
