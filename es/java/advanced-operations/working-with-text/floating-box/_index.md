---
title: Utilizar FloatingBox para el diseño de PDF en Java
linktitle: Utilizar FloatingBox
type: docs
weight: 30
url: /es/java/floating-box/
description: Aprende a usar FloatingBox para el diseño de texto, contenido de varias columnas y posicionamiento preciso en documentos PDF con Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Crear y posiciona contenedores FloatingBox con estilo en PDF con Java
Abstract: Este artículo explica cómo usar FloatingBox en Aspose.PDF for Java. Cubre la colocación de texto en contenedores flotantes con bordes, la creación de diseños de varias columnas repetitivos, el uso de colores de fondo, desplazamientos absolutos y opciones de alineación horizontal o vertical.
---
Aspose.PDF for Java usa `FloatingBox` para crear contenedores de texto reutilizables y diseños basados en columnas.

## Crear y añadir una caja flotante

Utiliza este ejemplo cuando el texto debe colocarse dentro de un contenedor flotante con borde.

1. Cree un nuevo documento PDF y añada una página.
1. Cree un `FloatingBox`, establezca su tamaño y borde, y agregue contenido de texto.
1. Añada el cuadro a la página y guarde el documento.

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

Utilice este ejemplo cuando el texto largo deba fluir a través de varias columnas dentro de una sola caja flotante.

1. Cree una página y configure los márgenes.
1. Calcule los anchos de columna y configure el `FloatingBox` configuración de columnas.
1. Agregue fragmentos de texto repetidos al cuadro y guarde el documento.

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

## Iniciar cada fragmento como el primer elemento en una columna

Utilice este ejemplo cuando cada fragmento insertado deba comenzar un nuevo segmento de flujo de columna.

1. Cree una página y configure la multi-columna `FloatingBox`.
1. Cree fragmentos de texto y márquelos con `setFirstParagraphInColumn(true)`.
1. Añada el cuadro a la página y guarde el PDF.

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

## Agregar un cuadro flotante con color de fondo

Utilice este ejemplo cuando el contenedor flotante deba tener un relleno de fondo visible.

1. Cree un nuevo documento PDF y añada una página.
1. Cree un `FloatingBox`, establezca su color de fondo, y agregue texto.
1. Coloque la caja en la página y guarde el documento.

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

Utilice este ejemplo cuando el cuadro flotante debe aparecer con un desplazamiento exacto en la página.

1. Cree una página y prepare el contenido de texto circundante.
1. Cree un `FloatingBox`, establecer posicionamiento absoluto y asigne desplazamientos superior e izquierdo.
1. Agregue el contenido a la página y guarde el documento.

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

## Alinear texto dentro de cuadros flotantes

Utilice este ejemplo cuando los cuadros flotantes deben demostrar diferentes alineaciones verticales con la misma alineación horizontal.

1. Cree un nuevo documento PDF y añada una página.
1. Cree varios `FloatingBox` objetos con diferentes configuraciones de alineación.
1. Añádalos a la página y guarde el resultado.

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
