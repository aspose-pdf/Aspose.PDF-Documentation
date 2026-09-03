---
title: Anotaciones interactivas usando Java
linktitle: Anotaciones interactivas
type: docs
weight: 60
url: /java/interactive-annotations/
description: Aprenda a agregar, inspeccionar y eliminar anotaciones de enlaces en documentos PDF utilizando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones PDF interactivas en Java.
Abstract: Este artículo explica cómo trabajar con anotaciones de enlaces interactivos en archivos PDF usando Aspose.PDF para Java. Cubre la localización de texto, la creación de una anotación de enlace sobre el área de texto coincidente, la lectura de anotaciones de enlaces existentes y su eliminación.
---
Las anotaciones interactivas en esta sección se centran en flujos de trabajo basados ​​en enlaces y botones que responden a las acciones del usuario dentro de un visor de PDF.


## 
Agregar una anotación de enlace



Utilice este ejemplo cuando necesite colocar un enlace en el que se pueda hacer clic sobre el texto que se encuentra en la página.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Localice el fragmento de texto de destino y cree una [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) sobre su rectángulo.
1. Asigne una [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) y guarde el documento actualizado.


```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
Obtener anotaciones de enlaces



Este ejemplo escanea la colección de anotaciones de la página e informa la ubicación de cada anotación de enlace.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Repita las anotaciones en la página de destino.
1. Filtre las anotaciones por [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` e imprima sus rectángulos.


```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 
Eliminar anotaciones de enlaces



Utilice este enfoque cuando las anotaciones de enlaces existentes deban eliminarse de la página.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Recopile anotaciones cuyo tipo sea [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`.
1. Elimine las anotaciones recopiladas y guarde el archivo de salida.


```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Agregar una anotación de línea



Este ejemplo crea una anotación de línea interactiva con estilos de flecha, configuraciones de borde y una nota emergente.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree una [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) con puntos de inicio y finalización.
1. Configure su apariencia y anotación emergente, luego guarde el documento.


```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));

        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar botones de navegación



Utilice este ejemplo cuando el PDF deba incluir botones de página anterior y página siguiente para una navegación interactiva.


1. Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y asegúrese de que el documento tenga las páginas requeridas.

1. Cree controles [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) con acciones de navegación predefinidas.
1. Agregue los botones a la colección de formularios y guarde el documento actualizado.


```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
Agregar un botón de impresión



Este ejemplo crea un botón que activa el comando de impresión cuando el usuario hace clic en él.


1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue una página.

1. Cree un [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) y asigne la acción predefinida de impresión.
1. Configure el borde y el fondo del botón, agréguelo al formulario y guarde el documento.

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
