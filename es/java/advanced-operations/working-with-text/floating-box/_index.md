---
title: Utilice FloatingBox para el diseño de PDF en Java
linktitle: Usando FloatingBox
type: docs
weight: 30
url: /es/java/floating-box/
description: Aprenda cómo usar FloatingBox para el diseño de texto, contenido en varias columnas y posicionamiento preciso en documentos PDF con Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cree y posicione contenedores FloatingBox con estilo en PDF con Java
Abstract: Este artículo explica cómo usar FloatingBox en Aspose.PDF for Java. Cubre la colocación de texto en contenedores flotantes con borde, la creación de diseños de varias columnas repetitivos, el uso de colores de fondo, desplazamientos absolutos y opciones de alineación horizontal o vertical.
---
Aspose.PDF for Java utiliza `FloatingBox` para crear contenedores de texto reutilizables y diseños basados en columnas.

## Crear y agregar un cuadro flotante

Utilice este ejemplo cuando el texto deba colocarse dentro de un contenedor flotante con borde.

1. Cree un nuevo documento PDF y agregue una página.
1. Crear un `FloatingBox`, establezca su tamaño y borde, y agregue contenido de texto.
1. Añade el cuadro a la página y guarda el documento.

```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## Crear un diseño multicolumna repetitivo

Utiliza este ejemplo cuando el texto largo debe fluir a través de múltiples columnas dentro de una sola caja flotante.

1. Crear una página y configurar los márgenes.
1. Calcule los anchos de columna y configure el `FloatingBox` configuración de columnas.
1. Añadir fragmentos de texto repetidos al cuadro y guardar el documento.

```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Inicie cada fragmento como el primer elemento en una columna

Utilice este ejemplo cuando cada fragmento insertado deba iniciar un nuevo segmento de flujo de columna.

1. Crear una página y configurar varias columnas `FloatingBox`.
1. Crear fragmentos de texto y marcarlos con `setFirstParagraphInColumn(true)`.
1. Añade la caja a la página y guarda el PDF.

```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Agregar una caja flotante con color de fondo

Utilice este ejemplo cuando el contenedor flotante deba tener un relleno de fondo visible.

1. Cree un nuevo documento PDF y agregue una página.
1. Crear un `FloatingBox`, establezca su color de fondo, y añada texto.
1. Coloca el cuadro en la página y guarda el documento.

```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Posicionar una caja flotante con desplazamientos absolutos

Utilice este ejemplo cuando el cuadro flotante deba aparecer en un desplazamiento exacto en la página.

1. Crear una página y preparar el contenido de texto circundante.
1. Crear un `FloatingBox`, establece posicionamiento absoluto y asigna desplazamientos superior e izquierdo.
1. Agrega el contenido a la página y guarda el documento.

```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## Alinear el texto dentro de cajas flotantes

Utilice este ejemplo cuando los cuadros flotantes deban demostrar diferentes alineaciones verticales con la misma alineación horizontal.

1. Cree un nuevo documento PDF y agregue una página.
1. Crear varios `FloatingBox` objetos con diferentes configuraciones de alineación.
1. Añádelos a la página y guarda el resultado.

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
