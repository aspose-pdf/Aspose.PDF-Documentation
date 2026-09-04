---
title: Añadir Sello de Página PDF
type: docs
weight: 10
url: /es/java/add-pdf-page-stamp/
description: Esta sección explica cómo trabajar con Aspose.PDF Facades usando la Clase PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Añadir Sello de Página PDF en Todas las Páginas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite añadir un sello de página PDF en todas las páginas de un archivo PDF.
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) y [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) clases. Necesita también crear el sello de página PDF utilizando el método [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Puede establecer otros atributos como origen, rotación, fondo, etc. utilizando también el objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Luego puede agregar el sello en el archivo PDF utilizando el método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, guarde el archivo PDF de salida utilizando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código muestra cómo agregar un sello de página PDF en todas las páginas de un archivo PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir Documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Crear sello
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Agregar sello al archivo PDF
            fileStamp.AddStamp(stamp);

            // Guardar archivo PDF actualizado
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Cerrar fileStamp
            fileStamp.Close();
        }
```

## Añadir Sello de Página PDF en Páginas Particulares de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite añadir un sello de página PDF en páginas particulares de un archivo PDF.
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) y [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) clases. Necesitas crear el sello de página PDF usando el método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. usando el objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) también. Como desea agregar un sello de página PDF en páginas particulares del archivo PDF, también necesita establecer la propiedad [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) de la clase [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Esta propiedad requiere un arreglo de enteros que contenga los números de las páginas en las que desea agregar el sello. Luego puede agregar el sello en el archivo PDF usando el método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, guarde el archivo PDF de salida usando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código le muestra cómo agregar un sello de página PDF en páginas particulares en un archivo PDF.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir Documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Crear sello
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Agregar sello al archivo PDF
            fileStamp.AddStamp(stamp);

            // Guardar archivo PDF actualizado
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Cerrar fileStamp
            fileStamp.Close();
        }

        // Agregar números de página PDF
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## Añadir Número de Página en un Archivo PDF (facades)

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) te permite añadir números de página en un archivo PDF.
 Para agregar números de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Si deseas mostrar el número de página como "Página X de N" siendo X el número de página actual y N el número total de páginas en el archivo PDF, primero necesitas obtener el conteo de páginas usando la propiedad getNumberOfpages de la clase [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Para obtener el número de la página actual, puedes usar el signo **#** en tu texto en cualquier lugar que desees. Puedes dar formato al texto del número de página usando la clase [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Si deseas comenzar la numeración de páginas desde un número específico, puedes establecer la propiedad setStartingNumber. Una vez que estés listo para agregar el número de página en el archivo, necesitas llamar al método addPageNumber de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, guarda el archivo PDF de salida usando el método Save de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp).

El siguiente fragmento de código te muestra cómo agregar un número de página en un archivo PDF.
```java
 public static void AddPageNumberInPdfFile() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Obtener el número total de páginas
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Crear texto formateado para el número de página
        FormattedText formattedText = new FormattedText("Página # de " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Establecer el número inicial para la primera página; podrías querer empezar desde 2 o más
        fileStamp.setStartingNumber(1);

        // Añadir número de página
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // Guardar archivo PDF actualizado
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Cerrar fileStamp
        fileStamp.close();
    }
```


### Estilo de Numeración Personalizado

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) ofrece la función de agregar información de número de página como objeto de sello dentro del documento PDF. Antes de esta versión, la clase solo soportaba 1,2,3,4 como estilo de numeración de páginas. Sin embargo, ha habido una demanda de algunos clientes para usar un estilo de numeración personalizado al colocar el sello de número de página dentro del documento PDF. Para cumplir con este requisito, se ha introducido la propiedad [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle), que acepta los valores de la enumeración [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle). A continuación se especifican los valores ofrecidos en esta enumeración.

```java
 public static void AddCustomPageNumberInPdfFile() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Obtener el número total de páginas
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Crear texto formateado para el número de página
        FormattedText formattedText = new FormattedText("Página # de " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Especificar estilo de numeración como Números Romanos Mayúsculas
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // Establecer número inicial para la primera página; puede que quieras empezar desde 2 o más
        fileStamp.setStartingNumber(1);

        // Agregar número de página
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // Guardar archivo PDF actualizado
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Cerrar fileStamp
        fileStamp.close();
    }
```