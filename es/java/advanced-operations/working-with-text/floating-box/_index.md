---
title: Utilice FloatingBox para el diseño de PDF en Java
linktitle: Usando caja flotante
type: docs
weight: 30
url: /java/floating-box/
description: Aprenda a utilizar FloatingBox para diseño de texto, contenido de varias columnas y posicionamiento preciso en documentos PDF con Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cree y coloque contenedores flotantes con estilo en PDF con Java
Abstract: Este artículo explica cómo utilizar FloatingBox en Aspose.PDF para Java. Cubre la colocación de texto en contenedores flotantes con bordes, la creación de diseños repetitivos de varias columnas, el uso de colores de fondo, desplazamientos absolutos y opciones de alineación horizontal o vertical.
---
Aspose.PDF para Java utiliza `FloatingBox` para crear contenedores de texto reutilizables y diseños basados ​​en columnas.


## 
Crear y agregar un cuadro flotante



Utilice este ejemplo cuando el texto deba colocarse dentro de un contenedor flotante con borde.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree un `FloatingBox`, establezca su tamaño y borde, y agregue contenido de texto.
1. Agregue el cuadro a la página y guarde el documento.


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

## 
Crear un diseño repetido de varias columnas



Utilice este ejemplo cuando el texto largo deba fluir en varias columnas dentro de un cuadro flotante.


1. 
Crea una página y configura márgenes.

1. 
Calcule los anchos de las columnas y configure los ajustes de la columna `FloatingBox`.
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

## 
Comience cada fragmento como el primer elemento de una columna.



Utilice este ejemplo cuando cada fragmento insertado deba comenzar un nuevo segmento de flujo de columna.


1. 
Cree una página y configure `FloatingBox` de varias columnas.

1. 
Cree fragmentos de texto y márquelos con `setFirstParagraphInColumn(true)`.
1. Agregue el cuadro a la página y guarde el PDF.


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

## 
Agregar un cuadro flotante con color de fondo



Utilice este ejemplo cuando el contenedor flotante deba tener un relleno de fondo visible.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree un `FloatingBox`, establezca su color de fondo y agregue texto.
1. Coloque el cuadro en la página y guarde el documento.


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

## 
Colocar un cuadro flotante con desplazamientos absolutos



Utilice este ejemplo cuando el cuadro flotante deba aparecer en un desplazamiento exacto en la página.


1. 
Cree una página y prepare el contenido del texto circundante.

1. 
Cree un `FloatingBox`, establezca el posicionamiento absoluto y asigne desplazamientos superior e izquierdo.
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

## 
Alinear texto dentro de cuadros flotantes



Utilice este ejemplo cuando los cuadros flotantes deban mostrar diferentes alineaciones verticales con la misma alineación horizontal.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree múltiples objetos `FloatingBox` con diferentes configuraciones de alineación.
1. Agréguelos a la página y guarde el resultado.

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
