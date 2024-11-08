---
title: Add PDF Page Stamp
type: docs
weight: 10
url: /es/net/add-pdf-page-stamp/
description: Esta sección explica cómo trabajar con Aspose.PDF Facades utilizando la clase PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Agregar sello de página PDF en todas las páginas de un archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) te permite agregar un sello de página PDF en todas las páginas de un archivo PDF. En orden de agregar un sello de página de PDF, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Necesitas también crear el sello de página PDF usando el método [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. usando el objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) también. Luego puedes añadir el sello en el archivo PDF usando el método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarda el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código te muestra cómo añadir un sello de página PDF en todas las páginas de un archivo PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Agregar Sello de Página PDF en Páginas Particulares en un Archivo PDF

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) la clase permite agregar un sello de página PDF en páginas particulares de un archivo PDF. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Para añadir un sello a la página PDF, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You also need to create the PDF page stamp using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.

También necesitas crear el sello de página PDF usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). You can set other attributes like origin, rotation, background etc.  
Puede establecer otros atributos como origen, rotación, fondo, etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) objeto también. 
Como desea agregar una estampilla de página PDF en páginas específicas del archivo PDF, también necesita establecer la propiedad [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) de la clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propiedad requiere un array de enteros que contenga los números de las páginas en las que desea agregar la estampilla. Luego puede agregar la estampilla en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarde el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código le muestra cómo agregar una estampilla de página PDF en páginas específicas en un archivo PDF.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Crear estampilla
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Agregar estampilla al archivo PDF
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
## Añadir Número de Página en un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) te permite añadir números de página en un archivo PDF. En orden de agregar números de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class.

Si desea mostrar el número de página como “Página X de N” siendo X el número de página actual y N el número total de páginas en el archivo PDF, primero debe obtener el recuento de páginas utilizando la propiedad [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) de la clase [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). En orden de obtener el número de página actual, puedes usar el signo **#** en tu texto donde quieras. Puedes dar formato al texto del número de página utilizando la clase [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Si deseas comenzar la numeración de página desde un número específico, entonces puedes establecer la propiedad [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Una vez que estés listo para agregar el número de página en el archivo, necesitas llamar al método [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarda el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código te muestra cómo agregar el número de página en un archivo PDF.

```csharp
 public static void AddPageNumberInPdfFile()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir Documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Obtener el número total de páginas
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Crear texto formateado para el número de página
            FormattedText formattedText = new FormattedText($"Página # de {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Establecer el número de inicio para la primera página; podrías querer comenzar desde 2 o más
            fileStamp.StartingNumber = 1;

            // Agregar número de página
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Guardar archivo PDF actualizado
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Cerrar fileStamp
            fileStamp.Close();
        }
```
### Estilo de numeración personalizada

La clase PdfFileStamp ofrece la funcionalidad de agregar información de número de página como objeto de sello dentro del documento PDF. Antes de esta versión, la clase solo soportaba 1,2,3,4 como estilo de numeración de páginas. Sin embargo, ha habido un requisito de algunos clientes para usar un estilo de numeración personalizado al colocar el sello de número de página dentro del documento PDF. Para cumplir con este requisito, se ha introducido la propiedad [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle), que acepta los valores de la enumeración [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle). A continuación se especifican los valores ofrecidos en esta enumeración.

- LettersLowercase
- LettersUppercase
- NumeralsArabic
- NumeralsRomanLowercase
- NumeralsRomanUppercase

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Obtener el número total de páginas
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Crear texto formateado para el número de página
            FormattedText formattedText = new FormattedText($"Página # de {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Especificar estilo de numeración como Números Romanos Mayúsculas
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // Establecer el número de inicio para la primera página; es posible que desee comenzar desde 2 o más
            fileStamp.StartingNumber = 1;

            // Agregar número de página
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Guardar archivo PDF actualizado
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Cerrar fileStamp
            fileStamp.Close();
        }
```