---
title: Trabajando con Artefactos 
linktitle: Trabajando con Artefactos
type: docs
weight: 110
url: /java/artifacts/
description: Esta página describe cómo trabajar con la clase Artifact usando Aspose.PDF para Java. Los fragmentos de código muestran cómo agregar una imagen de fondo a las páginas PDF y cómo obtener cada marca de agua en la primera página de un archivo PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Los artefactos son generalmente objetos gráficos u otras marcas que no son parte del contenido redactado. En tus ejemplos de PDF, los artefactos incluyen diferente información, como encabezados o pies de página, líneas u otros gráficos que separan secciones de la página, o imágenes decorativas.

La clase [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) contiene:


- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – obtiene el tipo de artefacto (soporta valores de la enumeración Artifact.ArtifactType donde los valores incluyen Fondo, Diseño, Página, Paginación e Indefinido).
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – obtiene el subtipo de artefacto (admite los valores de la enumeración Artifact.ArtifactSubtype donde los valores incluyen Background, Footer, Header, Undefined, Watermark).

Una marca de agua creada con Adobe Acrobat se llama artefacto (como se describe en 14.8.2.2 Contenido Real y Artefactos de la especificación PDF). Para trabajar con artefactos, Aspose.PDF tiene dos clases: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) y [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection).

Para obtener todos los artefactos en una página particular, la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) tiene la propiedad Artifacts. Este tema explica cómo trabajar con artefactos en archivos PDF.

El siguiente fragmento de código muestra cómo establecer una marca de agua en la primera página de un archivo PDF.

```java

public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


Las imágenes de fondo se pueden utilizar para añadir una marca de agua u otro diseño sutil a los documentos. En Aspose.PDF para Java, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) se puede usar para agregar una imagen de fondo a un objeto de página.

El siguiente fragmento de código muestra cómo agregar una imagen de fondo a las páginas PDF usando el objeto BackgroundArtifact.

```java

    public static void SetBackground() throws FileNotFoundException {

        // Abrir documento
        Document pdfDocument = new Document();
                
        // Añadir una nueva página al objeto documento
        Page page = pdfDocument.getPages().add();

        // Crear objeto de artefacto de fondo
        BackgroundArtifact background = new BackgroundArtifact();

        // Especificar la imagen para el objeto backgroundartifact
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // Añadir BackgroundArtifact a la colección de artefactos de la página
        page.getArtifacts().add(background);

        // Guardar PDF modificado
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## Ejemplos de Programación: Obtener Marca de Agua

El siguiente fragmento de código muestra cómo obtener cada marca de agua en la primera página de un archivo PDF.

```java
    public static void GettingWatermarks() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // Iterar y obtener sub-tipo, texto y ubicación del artefacto
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## Ejemplos de Programación: Contar Artefactos de un Tipo Particular

Para calcular el total de artefactos de un tipo particular (por ejemplo, el número total de marcas de agua), use el siguiente código:

```java
    public static void CountingArtifacts() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // Si el tipo de artefacto es marca de agua, incrementar el contador
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("La página contiene " + count + " marcas de agua");
    }
```