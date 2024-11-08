---
title: Manage Header and Footer
type: docs
weight: 40
url: /es/net/manage-header-and-footer/
description: Esta sección explica cómo gestionar el Encabezado y el Pie de Página con Aspose.PDF Facades usando la Clase PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Agregar Encabezado en un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) te permite agregar un encabezado en un archivo PDF. En order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. Puedes dar formato al texto del encabezado utilizando la clase [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Una vez que estés listo para añadir un encabezado en el archivo, necesitas llamar al método [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). También necesitas especificar al menos el margen superior en el método [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Finalmente, guarda el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). El siguiente fragmento de código te muestra cómo añadir un encabezado en un archivo PDF.

```csharp
 public static void AddHeader()
        {
            // Crear objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Crear texto formateado para el número de página
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Añadir encabezado
            fileStamp.AddHeader(formattedText, 10);

            // Guardar archivo PDF actualizado
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // Cerrar fileStamp
            fileStamp.Close();
        }
```
## Add Footer in a PDF File

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) te permite añadir un pie de página en un archivo PDF. In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

Para agregar un pie de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Puedes dar formato al texto del pie de página usando la clase [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Una vez estés listo para añadir el pie de página en el archivo, necesitas llamar al método [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). También necesitas especificar al menos el margen inferior en el método [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Finalmente, guarda el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). El siguiente fragmento de código te muestra cómo añadir un pie de página en un archivo PDF.

```csharp
 public static void AddFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Add footer
            fileStamp.AddFooter(formattedText, 10);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Agregar Imagen en el Encabezado de un Archivo PDF Existente

La clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) te permite agregar una imagen en el encabezado de un archivo PDF. Para agregar una imagen en el encabezado, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Después de eso, necesitas llamar al método [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Puedes pasar la imagen al método [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Finalmente, guarda el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). El siguiente fragmento de código te muestra cómo agregar una imagen en el encabezado de un archivo PDF.

```csharp
public static void AddImageHeader()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add Header
                fileStamp.AddHeader(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // Close fileStamp
                fileStamp.Close();
            }
        }
```
## Add Image in Footer of an Existing PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class permite añadir una imagen en el pie de página de un archivo PDF. Para agregar una imagen en el pie de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Después de eso, necesitas llamar al método [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Puedes pasar la imagen al método [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Finalmente, guarda el archivo PDF de salida usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF.

```csharp
public static void AddImageFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add footer
                fileStamp.AddFooter(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Close fileStamp
                fileStamp.Close();
            }
        }
```