---
title: Extraer Texto de un Archivo PDF
type: docs
weight: 30
url: /es/net/extract-text/
description: Esta sección explica cómo extraer texto de un pdf usando la clase PdfExtractor.
lastmod: "2021-06-05"
---

En este artículo, examinaremos los detalles de la extracción de texto de un archivo PDF. Todas estas características de extracción se proporcionan en un solo lugar, en la clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). Veremos cómo usar estas características en nuestro código.

La clase [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) proporciona tres tipos de capacidades de extracción. Estas tres categorías son Texto, Imágenes y Adjuntos. Para realizar la extracción en cada una de estas tres categorías, PdfExtractor proporciona varios métodos que trabajan juntos para darte el resultado final.

Por ejemplo, para extraer texto puedes usar tres métodos, es decir, [ExtractText, GetText, HasNextPageText and GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index). Ahora, para comenzar a extraer texto, primero debes llamar al método [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index); esto extraerá el texto del archivo PDF y lo almacenará en memoria. Después de eso, el método [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) tomará este texto extraído y lo guardará en el disco en un lugar especificado en un archivo. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) te ayuda a recorrer cada página y verificar si la siguiente página tiene algún texto o no. Si contiene algún texto, entonces [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) te ayudará a guardar el texto de una página individual en el archivo.

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // Crear un objeto de la clase PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Vincular el PDF de entrada
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // ExtractText
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extraer el texto en archivos separados
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
To Extract the Text Extraction Mode use the following code:

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // Crear un objeto de la clase PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Enlazar el PDF de entrada
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // Extraer texto
    // pdfExtractor.ExtractTextMode = 0; //modo puro
    pdfExtractor.ExtractTextMode = 1; //modo sin procesar
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extraer el texto en archivos separados
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```