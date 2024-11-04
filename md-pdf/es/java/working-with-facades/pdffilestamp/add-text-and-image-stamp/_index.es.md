---
title: Añadir Sello de Texto e Imagen
type: docs
weight: 20
url: /java/add-text-and-image-stamp/
description: Esta sección explica cómo agregar un Sello de Texto e Imagen con com.aspose.pdf.facades usando la Clase PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Añadir Sello de Texto en Todas las Páginas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) te permite añadir un sello de texto en todas las páginas de un archivo PDF.
 En orden de agregar una marca de texto, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) y [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Necesitas también crear el sello de texto usando el método BindLogo de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. usando el objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) también. Luego, puedes añadir el sello en el archivo PDF usando el método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, guarda el archivo PDF de salida usando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código te muestra cómo añadir un sello de texto en todas las páginas de un archivo PDF.

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Crear sello
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("¡Hola Mundo!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Añadir sello al archivo PDF
        fileStamp.addStamp(stamp);

        // Guardar archivo PDF actualizado
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // Cerrar fileStamp
        fileStamp.close();
    }
```

## Añadir Sello de Texto en Páginas Particulares de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) te permite añadir un sello de texto en páginas particulares de un archivo PDF.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) y [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) clases. Necesitas crear el sello de texto utilizando el método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. usando el objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) también. Como deseas agregar una marca de texto en páginas específicas del archivo PDF, también necesitas establecer la propiedad [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Esta propiedad requiere un arreglo de enteros que contenga los números de las páginas en las que deseas agregar la marca. Luego puedes agregar la marca en el archivo PDF usando el método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, guarda el archivo PDF de salida usando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código te muestra cómo agregar una marca de texto en páginas específicas de un archivo PDF.

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Crear marca
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Establecer páginas específicas
        stamp.setPages(new int[] { 2 });

        // Agregar marca al archivo PDF
        fileStamp.addStamp(stamp);

        // Guardar archivo PDF actualizado
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // Cerrar fileStamp
        fileStamp.close();
    }
```

## Agregar Sello de Imagen en Todas las Páginas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite agregar un sello de imagen en todas las páginas de un archivo PDF.
 En orden de agregar un sello de imagen, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) y [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Necesitas también crear el sello de imagen utilizando el método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. utilizando el objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) también. Luego, puedes agregar el sello en el archivo PDF utilizando el método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, guarda el archivo PDF de salida utilizando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código te muestra cómo agregar un sello de imagen en todas las páginas de un archivo PDF.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Crear sello
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Agregar sello al archivo PDF
        fileStamp.addStamp(stamp);

        // Guardar archivo PDF actualizado
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // Cerrar fileStamp
        fileStamp.close();
    }
```

### Controlar la calidad de la imagen al agregar como sello

Al agregar una imagen como objeto de sello, también puedes controlar la calidad de la imagen. Para cumplir con este requisito, se ha agregado la propiedad Quality a la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Indica la calidad de la imagen en porcentajes (valores válidos son 0..100).

## Agregar sello de imagen en páginas particulares de un archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) te permite agregar un sello de imagen en páginas particulares de un archivo PDF.
 Para agregar un sello de imagen, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) y [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Necesitas crear el sello de imagen utilizando el método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. usando el objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) también. Como desea agregar una marca de imagen en páginas particulares del archivo PDF, también necesita establecer la propiedad [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Esta propiedad requiere un array de enteros que contenga los números de las páginas en las que desea agregar la marca. Luego puede agregar la marca en el archivo PDF usando el método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, guarde el archivo PDF de salida usando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código le muestra cómo agregar una marca de imagen en páginas particulares de un archivo PDF.

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Crear marca
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Establecer páginas particulares
        stamp.setPages(new int[] { 2 });

        // Agregar marca al archivo PDF
        fileStamp.addStamp(stamp);

        // Guardar archivo PDF actualizado
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // Cerrar fileStamp
        fileStamp.close();
    }
```