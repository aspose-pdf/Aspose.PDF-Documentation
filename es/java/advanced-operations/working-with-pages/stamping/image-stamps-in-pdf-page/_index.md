---
title: Agregar sellos de imagen en PDF programáticamente
linktitle: Sellos de imagen en archivo PDF
type: docs
weight: 10
url: es/java/image-stamps-in-pdf-page/
description: Agrega el sello de imagen en tu documento PDF usando la clase ImageStamp con la biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Agregar sello de imagen en archivo PDF

Puede usar la clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) para agregar una imagen como sello en el documento PDF. La clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) proporciona métodos para especificar altura, ancho, y opacidad, etc.

Para agregar un sello de imagen:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y un objeto ImageStamp usando las propiedades requeridas.

1. Llama al método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para añadir el sello al PDF.

El siguiente fragmento de código muestra cómo añadir un sello de imagen en el archivo PDF.

```java
public static void AddImageStampInPDFFile() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Crear sello de imagen
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // Añadir sello a una página en particular
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // Guardar documento de salida
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## Controlar la Calidad de Imagen al Agregar un Sello

La clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) te permite agregar una imagen como un sello en un documento PDF. También te permite controlar la calidad de la imagen al agregar una imagen como marca de agua en un archivo PDF. Para permitir esto, se ha añadido un método llamado setQuality(...) a la clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). Un método similar también se puede encontrar en la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) del paquete com.aspose.pdf.facades.

El siguiente fragmento de código te muestra cómo controlar la calidad de la imagen al agregarla como sello en el archivo PDF.

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Crear sello de imagen
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## Sello de Imagen como Fondo en Caja Flotante

La API Aspose.PDF te permite añadir un sello de imagen como fondo en una caja flotante. La propiedad BackgroundImage de la clase FloatingBox se puede usar para establecer el sello de imagen de fondo para una caja flotante como se muestra en el siguiente ejemplo de código.

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // Instanciar objeto Documento
        Document doc = new Document();
        // Agregar página al documento PDF
        Page page = doc.getPages().add();

        // Crear objeto FloatingBox
        FloatingBox aBox = new FloatingBox(200, 100);

        // Establecer posición izquierda para FloatingBox
        aBox.setLeft(40);
        // Establecer posición superior para FloatingBox
        aBox.setTop(80);
        // Establecer la alineación horizontal para FloatingBox
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // Agregar fragmento de texto a la colección de párrafos de FloatingBox
        aBox.getParagraphs().add(new TextFragment("texto principal"));
        // Establecer borde para FloatingBox
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // Añadir imagen de fondo
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // Establecer color de fondo para FloatingBox
        aBox.setBackgroundColor(Color.getYellow());

        // Añadir FloatingBox a la colección de párrafos del objeto página
        page.getParagraphs().add(aBox);
        // Guardar el documento PDF
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```