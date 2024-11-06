---
title: Convertir páginas de PDF en imágenes y reconocer códigos de barras
type: docs
weight: 10
url: es/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Los documentos PDF generalmente comprenden texto, imágenes, tablas, adjuntos, gráficos, anotaciones y otros objetos. Algunos de nuestros clientes necesitan incrustar códigos de barras en documentos y luego identificar códigos de barras en el archivo PDF. El siguiente artículo explica cómo transformar las páginas de un archivo PDF en imágenes e identificar códigos de barras en las imágenes con Aspose.Barcode para .NET.

{{% /alert %}}
### **Convirtiendo Páginas en Imágenes y Reconociendo Códigos de Barras**

{{% alert color="primary" %}}

Aspose.PDF para .NET es un producto muy poderoso para gestionar documentos PDF. Facilita la conversión de páginas de documentos PDF en imágenes. Aspose.BarCode para .NET es un producto igualmente poderoso para generar y reconocer códigos de barras.

La clase PdfConverter bajo el espacio de nombres Aspose.PDF.Facades soporta la conversión de páginas PDF a varios formatos de imagen.
{{% /alert %}}
#### **Usando Aspose.PDF.Facades**

{{% alert color="primary" %}}

La clase PdfConverter contiene un método llamado GetNextImage que genera una imagen de la página actual del PDF. Para especificar el formato de imagen de salida, este método acepta un argumento de la enumeración System.Drawing.Imaging.ImageFormat.

Aspose.Barcode contiene un espacio de nombres, BarCodeRecognition, que incluye la clase BarCodeReader. La clase BarCodeReader te permite leer, determinar e identificar códigos de barras desde archivos de imagen.

Para los propósitos de este ejemplo, primero convierte una página de un archivo PDF en una imagen con Aspose.PDF.Facades.PdfConverter.
{{% /alert %}}
##### **Ejemplos de Programación**
**C#**

{{< highlight csharp >}}

 //Crear un objeto PdfConverter

PdfConverter converter = new PdfConverter();

//Vincular el archivo PDF de entrada

converter.BindPdf("Source.pdf");

// Especificar la página de inicio a procesar

converter.StartPage = 1;

// Especificar la página final para el procesamiento

converter.EndPage = 1;

// Crear un objeto Resolution para especificar la resolución de la imagen resultante

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

//Iniciar el proceso de conversión

converter.DoConvert();

// Crear un objeto MemoryStream para contener la imagen resultante

MemoryStream imageStream = new MemoryStream();

//Verificar si existen páginas y luego convertir a imagen una por una

while (converter.HasNextImage())

{

    // Guardar la imagen en el formato de imagen dado

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    // Establecer la posición del stream al inicio del stream

     // Establece la posición del flujo al inicio del mismo

    imageStream.Position = 0;

    // Instancia un objeto BarCodeReader

    Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

    // String txtResult.Text = "";

    while (barcodeReader.Read())

    {

        // Obtén el texto del código de barras de la imagen del código de barras

        string code = barcodeReader.GetCodeText();

        // Escribe el texto del código de barras en la salida de la consola

        Console.WriteLine("BARCODE : " + code);

    }

    // Cierra el objeto BarCodeReader para liberar el archivo de imagen

    barcodeReader.Close();

}

// Cierra la instancia de PdfConverter y libera los recursos

converter.Close();

// Cierra el flujo que contiene el objeto de imagen

imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}

En los fragmentos de código anteriores, la imagen de salida se guarda en un objeto MemoryStream.
```
En los fragmentos de código anteriores, la imagen de salida se guarda en un objeto MemoryStream.

{{% /alert %}}

{anchor:devices]
#### **Usando la Clase PngDevice**
En Aspose.PDF.Devices, está la PngDevice. Esta clase permite convertir páginas en documentos PDF en imágenes PNG.

Para el propósito de este ejemplo, carga el archivo PDF fuente en el Documento y convierte las páginas del documento en imágenes PNG. Cuando se hayan creado las imágenes, utiliza la clase BarCodeReader bajo Aspose.BarCodeRecognition para identificar y leer los códigos de barras en las imágenes.

{{% alert color="primary" %}}

Los ejemplos de código dados aquí recorren las páginas del documento PDF e intentan identificar códigos de barras en cada página.

{{% /alert %}}
##### **Ejemplos de Programación**
**C#**

{{< highlight csharp >}}

// Abrir el documento PDF

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// Recorrer las páginas individuales del archivo PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())

using (MemoryStream imageStream = new MemoryStream())
{
    //Crear un objeto Resolution
    Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);

    // Instancia un objeto PngDevice pasando un objeto Resolution como argumento a su constructor
    Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);

    //Convertir una página en particular y guardar la imagen en el stream
    pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

    // Establecer la posición del stream al inicio del Stream
    imageStream.Position = 0;

    // Instanciar un objeto BarCodeReader
    Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

    // String txtResult.Text = "";

    while (barcodeReader.Read())
    {
        // Obtener el texto del código de barras desde la imagen del código de barras
        string code = barcodeReader.GetCodeText();
    }
}
```
```csharp
string code = barcodeReader.GetCodeText();

// Escribe el texto del código de barras en la salida de la consola

Console.WriteLine("CÓDIGO DE BARRAS : " + code);

}

// Cierra el objeto BarCodeReader para liberar el archivo de imagen

barcodeReader.Close();

}

}
```

{{< /highlight >}}

{{% alert color="primary" %}}
Para más información sobre los temas tratados en este artículo, por favor visite:

- Convertir páginas de PDF a diferentes formatos de imagen (Facades)
- Convertir todas las páginas de PDF a imágenes PNG
- [Leer códigos de barras](https://docs.aspose.com/barcode/net/read-barcodes/)

{{% /alert %}}
