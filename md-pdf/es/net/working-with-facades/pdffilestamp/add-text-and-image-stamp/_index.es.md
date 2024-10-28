---
title: Agregar Sello de Texto e Imagen
type: docs
weight: 20
url: /net/add-text-and-image-stamp/
description: Esta sección explica cómo agregar un sello de texto e imagen con Aspose.PDF Facades usando la clase PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Agregar Sello de Texto en Todas las Páginas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) te permite agregar un sello de texto en todas las páginas de un archivo PDF. En orden de añadir un sello de texto, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Necesita crear el sello de texto usando el método [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Puede establecer otros atributos como origen, rotación, fondo, etc., usando el objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) también. Luego puede agregar el sello en el archivo PDF usando el método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarde el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código le muestra cómo agregar un sello de texto en todas las páginas de un archivo PDF.

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Agregar una Marca de Texto en Páginas Específicas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) te permite agregar una marca de texto en páginas específicas de un archivo PDF. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Para agregar un sello de texto, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the text stamp using [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.  
También necesita crear el sello de texto utilizando el método [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) objeto también. Como deseas agregar una marca de texto en páginas específicas del archivo PDF, también necesitas establecer la propiedad [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propiedad requiere un arreglo de enteros que contiene los números de las páginas en las que deseas agregar la marca. Luego puedes agregar la marca en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarda el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código te muestra cómo agregar una marca de texto en páginas específicas de un archivo PDF.

```csharp
 public static void AddTextStampOnParticularPagesInPdfFile()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Crear marca
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Establecer páginas específicas
            stamp.Pages = new int[] { 2 };

            // Agregar marca al archivo PDF
            fileStamp.AddStamp(stamp);

            // Guardar archivo PDF actualizado
            fileStamp.Save(_dataDir + "AddTextStamp-Page_out.pdf");

            // Cerrar fileStamp
            fileStamp.Close();
        }
```
## Añadir Sello de Imagen en Todas las Páginas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) te permite añadir un sello de imagen en todas las páginas de un archivo PDF. En orden de agregar una estampilla de imagen, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Necesitas crear el sello de imagen usando el método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. usando también el objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Luego, puedes agregar el sello en el archivo PDF usando el método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarda el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código te muestra cómo agregar un sello de imagen en todas las páginas de un archivo PDF.

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Crear sello
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Establecer páginas particulares
            stamp.Pages = new int[] { 2 };

            // Agregar sello al archivo PDF
            fileStamp.AddStamp(stamp);

            // Guardar archivo PDF actualizado
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // Cerrar fileStamp
            fileStamp.Close();
        }
```
### Controlar la calidad de imagen al añadir como sello

Al añadir una imagen como objeto de sello, también puedes controlar la calidad de la imagen. Para cumplir con este requisito, se ha añadido la propiedad Quality para la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Indica la calidad de la imagen en porcentajes (los valores válidos son 0..100).

## Añadir un Sello de Imagen en Páginas Particulares de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) te permite añadir un sello de imagen en páginas particulares de un archivo PDF. En order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Con el fin de agregar un sello de imagen, primero necesita crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the image stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.

También necesitas crear el sello de imagen usando el método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You can set other attributes like origin, rotation, background etc.  
Puedes establecer otros atributos como origen, rotación, fondo, etc. usando el objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) también. Como desea agregar un sello de imagen en páginas particulares del archivo PDF, también necesita establecer la propiedad [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propiedad requiere un arreglo de enteros que contenga los números de las páginas en las que desea agregar el sello. Luego puede agregar el sello en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarde el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código le muestra cómo agregar un sello de imagen en páginas particulares en un archivo PDF.

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Crear sello
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Agregar sello al archivo PDF
            fileStamp.AddStamp(stamp);

            // Guardar archivo PDF actualizado
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // Cerrar fileStamp
            fileStamp.Close();
        }
```