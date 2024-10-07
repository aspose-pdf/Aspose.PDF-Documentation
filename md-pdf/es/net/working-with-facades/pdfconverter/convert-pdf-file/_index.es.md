---
title: Convertir archivo PDF
type: docs
weight: 30
url: /net/convert-pdf-file/
description: Esta sección explica cómo convertir un archivo PDF con Aspose.PDF Facades usando la clase PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Convertir páginas PDF a diferentes formatos de imagen (Facades)

Para convertir páginas PDF a diferentes formatos de imagen, necesitas crear un objeto [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) y abrir el archivo PDF usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesita llamar al método [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) para las tareas de inicialización. Luego, puede recorrer todas las páginas usando los métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) y [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). El método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) le permite crear una imagen de una página en particular. También necesita pasar el ImageFormat a este método para crear una imagen de un tipo específico, es decir, JPEG, GIF o PNG, etc. Finalmente, llame al método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) de la clase [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter). El siguiente fragmento de código le muestra cómo convertir páginas PDF a imágenes.

```csharp
 public static void ConvertPdfPagesToImages01()
        {
            // Crear objeto PdfConverter
            PdfConverter converter = new PdfConverter();

            // Vincular archivo pdf de entrada
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Inicializar el proceso de conversión
            converter.DoConvert();

            // Comprobar si existen páginas y luego convertir a imagen una por una
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Cerrar el objeto PdfConverter
            converter.Close();
        }
```
En el siguiente fragmento de código, mostraremos cómo puedes cambiar algunos parámetros. Con [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) configuramos el marco 'CropBox'. Además, podemos cambiar la [Resolución](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) especificando el número de puntos por pulgada. El siguiente es [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - modo de presentación del formulario. Luego indicamos la [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) con la cual se establece el número de página del inicio de la conversión. También podemos especificar la última página estableciendo un rango.

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // Crear objeto PdfConverter
            PdfConverter converter = new PdfConverter();

            // Vincular archivo pdf de entrada
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Inicializar el proceso de conversión
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // Verificar si existen páginas y luego convertir a imagen una por una
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Cerrar el objeto PdfConverter
            converter.Close();
        }
```

## See also

Aspose.PDF for .NET permite convertir documentos PDF a varios formatos y también convertir de otros formatos a PDF. Además, puede verificar la calidad de la conversión de Aspose.PDF y ver los resultados en línea con la aplicación Aspose.PDF converter. Aprenda la sección de [Converting](/pdf/net/converting/) para resolver sus tareas.