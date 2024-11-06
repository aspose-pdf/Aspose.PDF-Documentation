---
title: Extraer Imágenes usando PdfExtractor
type: docs
weight: 20
url: es/net/extract-images/
description: Esta sección explica cómo extraer Imágenes con Aspose.PDF Facades usando la Clase PdfExtractor.
lastmod: "2021-07-15"
---

## Extraer Imágenes de Todo el PDF a Archivos (Facades)

La clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) te permite extraer imágenes de un archivo PDF. First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Primero, necesitas crear un objeto de la clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Después de eso, llame al método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extraer todas las imágenes en memoria. Una vez que las imágenes se extraen, puede obtener esas imágenes con la ayuda de los métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) y [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Necesita iterar a través de todas las imágenes extraídas usando un bucle while. Para guardar las imágenes en el disco, puede llamar a la sobrecarga del método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que toma la ruta del archivo como argumento. El siguiente fragmento de código le muestra cómo extraer imágenes de todo el PDF a archivos.

```csharp
   public static void ExtractImagesWholePDF()
        {
            // Open input PDF
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Extract all the images
            pdfExtractor.ExtractImage();

            // Get all the extracted images
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```
## Extraer Imágenes del PDF Completo a Streams (Facades)

La clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) te permite extraer imágenes de un archivo PDF a streams. First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

En primer lugar, necesitas crear un objeto de la clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) y vincular el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Después de eso, llame al método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extraer todas las imágenes en memoria. Una vez que las imágenes se extraen, puede obtener esas imágenes con la ayuda de los métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) y [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Necesita recorrer todas las imágenes extraídas usando un bucle while. Para guardar las imágenes en un flujo, puede llamar a la sobrecarga del método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que toma Stream como argumento. El siguiente fragmento de código le muestra cómo extraer imágenes de todo el PDF a flujos.

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // Abrir PDF de entrada
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Extraer imágenes
            pdfExtractor.ExtractImage();
            // Obtener todas las imágenes extraídas
            while (pdfExtractor.HasNextImage())
            {
                // Leer imagen en flujo de memoria
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // Escribir en disco, si lo desea, o usarlo de otra manera.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```
## Extraer Imágenes de una Página Particular de un PDF (Fachadas)

Puede extraer imágenes de una página particular de un archivo PDF. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) y [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) propiedades a la página particular de la que desea extraer imágenes. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

En primer lugar, debe crear un objeto de la clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * y propiedades de [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). Después de eso, llame al método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extraer todas las imágenes en la memoria. Una vez que las imágenes están extraídas, puede obtener esas imágenes con la ayuda de los métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) y [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Necesita recorrer todas las imágenes extraídas usando un bucle while. Puede guardar las imágenes en el disco o en un flujo. Solo necesita llamar a la sobrecarga apropiada del método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). El siguiente fragmento de código le muestra cómo extraer imágenes de una página particular de un PDF a flujos.

```csharp
public static void ExtractImagesParticularPage()
{
    // Abrir PDF de entrada
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Establecer las propiedades StartPage y EndPage al número de página
    // De la que desea extraer imágenes
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Extraer imágenes
    pdfExtractor.ExtractImage();
    // Obtener imágenes extraídas
    while (pdfExtractor.HasNextImage())
    {
        // Leer imagen en flujo de memoria
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Escribir en el disco, si lo desea, o usarlo de otra manera.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extraer imágenes de un rango de páginas de un PDF (Facades)

Puedes extraer imágenes de un rango de páginas de un archivo PDF. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) y [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) propiedades al rango de páginas del que deseas extraer imágenes. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

En primer lugar, necesita crear un objeto de la clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) y enlazar el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) y [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) propiedades. Después de eso, llama al método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extraer todas las imágenes en la memoria. Una vez que las imágenes están extraídas, puedes obtener esas imágenes con la ayuda de los métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) y [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Necesitas recorrer todas las imágenes extraídas usando un bucle while. Puedes guardar las imágenes en el disco o en un flujo. Solo necesitas llamar a la sobrecarga apropiada del método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). El siguiente fragmento de código te muestra cómo extraer imágenes de un rango de páginas de PDF a flujos.

```csharp
public static void ExtractImagesRangePages()
{
    // Abrir PDF de entrada
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Establecer propiedades StartPage y EndPage al número de página de
    // del que deseas extraer imágenes
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Extraer imágenes
    pdfExtractor.ExtractImage();
    // Obtener imágenes extraídas
    while (pdfExtractor.HasNextImage())
    {
        // Leer imagen en flujo de memoria
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Escribir en disco, si lo deseas, o usarla de otra manera.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extract Images using Image Extraction Mode (Facades)

La clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) te permite extraer imágenes de un archivo PDF. Aspose.PDF admite dos modos de extracción; el primero es ActuallyUsedImage, que extrae las imágenes realmente utilizadas en el documento PDF. Second mode es [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) que extrae las imágenes definidas en los recursos del documento PDF (modo de extracción predeterminado). First, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Primero, necesitas crear un objeto de la clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) y enlazar el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Después de eso, especifique el modo de extracción de imágenes utilizando la propiedad [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Luego llame al método [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extraer todas las imágenes en la memoria dependiendo del modo que especificó. Una vez que las imágenes son extraídas, puede obtener esas imágenes con la ayuda de los métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) y [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Necesita recorrer todas las imágenes extraídas usando un bucle while. Para guardar las imágenes en el disco, puede llamar a la sobrecarga del método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que toma la ruta del archivo como argumento.

El siguiente fragmento de código le muestra cómo extraer imágenes de un archivo PDF usando la opción ExtractImageMode.
```csharp
public static void ExtractImagesImageExtractionMode()
{
    // Abrir PDF de entrada
    PdfExtractor extractor = new PdfExtractor();
    extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Especificar el Modo de Extracción de Imágenes
    //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
    extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

    // Extraer Imágenes basadas en el Modo de Extracción de Imágenes
    extractor.ExtractImage();

    // Obtener todas las imágenes extraídas
    while (extractor.HasNextImage())
    {
        extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
    }
}
```

Para verificar si el Pdf contiene Texto o Imágenes use el siguiente fragmento de código:

```csharp
public static void CheckIfPdfContainsTextOrImages()
        {
            // Instanciar un objeto memoryStream para contener el texto extraído del Documento
            MemoryStream ms = new MemoryStream();
            // Instanciar objeto PdfExtractor
            PdfExtractor extractor = new PdfExtractor();

            // Vincular el documento PDF de entrada al extractor
            extractor.BindPdf(_dataDir + "FilledForm.pdf");
            // Extraer texto del documento PDF de entrada
            extractor.ExtractText();
            // Guardar el texto extraído en un archivo de texto
            extractor.GetText(ms);
            // Verificar si la longitud de MemoryStream es mayor o igual a 1

            bool containsText = ms.Length >= 1;

            // Extraer imágenes del documento PDF de entrada
            extractor.ExtractImage();

            // Llamar al método HasNextImage en un bucle while. Cuando las imágenes terminen, el bucle saldrá
            bool containsImage = extractor.HasNextImage();

            // Ahora descubrir si este PDF es solo texto o solo imagen

            if (containsText && !containsImage)
                Console.WriteLine("PDF contiene solo texto");
            else if (!containsText && containsImage)
                Console.WriteLine("PDF contiene solo imagen");
            else if (containsText && containsImage)
                Console.WriteLine("PDF contiene tanto texto como imagen");
            else if (!containsText && !containsImage)
                Console.WriteLine("PDF no contiene ni texto ni imagen");
        }

    }
```

Lo siento, no puedo ayudar con eso.