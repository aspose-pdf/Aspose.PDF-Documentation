---
title: Extraer imágenes de PDF y reconocer códigos de barras
type: docs
weight: 20
url: es/net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Los documentos PDF suelen estar compuestos por texto, imagen, tabla, adjuntos, gráficos, anotaciones y otros objetos relacionados. Hay casos en los que los códigos de barras están incrustados dentro del archivo PDF y algunos clientes tienen la necesidad de identificar los códigos de barras presentes dentro del archivo PDF. El siguiente artículo explica los pasos sobre cómo extraer imágenes de las páginas de PDF e identificar los códigos de barras dentro de ellas.

{{% /alert %}}

De acuerdo al Modelo de Objeto de Documento de Aspose.PDF para .NET, un archivo PDF contiene una o más páginas donde cada página contiene una colección de imágenes, formularios y fuentes en el objeto de recursos.
Según el Modelo de Objeto de Documento de Aspose.PDF para .NET, un archivo PDF contiene una o más páginas donde cada página contiene una colección de Imágenes, Formularios y Fuentes en el objeto Recursos.

**C#**

```csharp

//abrir documento
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// recorrer las páginas individuales del archivo PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // recorrer cada imagen extraída de las páginas del PDF
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            //guardar imagen de salida
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // establecer la posición del stream al principio del Stream
            imageStream.Position = 0;
   
            // Instanciar objeto BarCodeReader
   
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // obtener el texto del código de barras de la imagen del código de barras
                string code = barcodeReader.GetCodeText();
   
                // escribir el texto del código de barras en la salida de la consola
                Console.WriteLine("CÓDIGO DE BARRAS : " + code);
            }
   
            // cerrar objeto BarCodeReader para liberar el archivo de imagen
   
            barcodeReader.Close();
        }
    }
}

```
Para más detalles sobre los temas tratados en este artículo, por favor visite los siguientes enlaces:

- [Extraer imágenes del archivo PDF](/net/extract-images-from-the-pdf-file/)
- [Leer códigos de barras](https://docs.aspose.com/barcode/net/read-barcodes/)
