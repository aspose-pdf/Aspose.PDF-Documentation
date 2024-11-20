---
title: Añadiendo Imágenes y Texto
type: docs
weight: 10
url: /es/net/adding-images-and-text-using-pdffilemend-class/
description: Esta sección explica cómo añadir imágenes y texto usando la clase PdfFileMend.
lastmod: "2021-06-05"
draft: false
---

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class puede ayudarte a añadir imágenes y texto en un documento PDF existente, en una ubicación especificada.
``` It provides two methods with the names [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) y [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) método permite agregar imágenes de tipo JPG, GIF, PNG y BMP. [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) método toma un argumento de tipo clase [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) y lo agrega en el archivo PDF existente. Las imágenes y el texto se pueden agregar en una región rectangular especificada por las coordenadas de los puntos inferior izquierdo y superior derecho. Al agregar imágenes, puede especificar la ruta del archivo de imagen o un flujo de un archivo de imagen. Para especificar el número de página en el que se necesita agregar la imagen o el texto, ambos métodos proporcionan un argumento de número de página. Por lo tanto, no solo puede agregar las imágenes y el texto en la ubicación especificada, sino también en una página especificada.

Las imágenes son una parte importante del contenido de un documento PDF. Manipular imágenes en un archivo PDF existente es un requisito común para las personas que trabajan con archivos PDF. En este artículo, exploraremos cómo se pueden manipular las imágenes, en un archivo PDF existente, con la ayuda del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) de [Aspose.PDF para .NET](/pdf/es/net/). Todas las operaciones relacionadas con imágenes del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) han sido consolidadas en este artículo.

## Detalles de implementación

El [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) te permite agregar nuevas imágenes en un archivo PDF existente. Puedes también reemplazar o eliminar una imagen existente. Un archivo PDF también puede ser convertido a imágenes. Puedes convertir cada página individual en una sola imagen o un archivo PDF completo en una sola imagen. Te permite formatos, es decir, JPEG, BMP, PNG y TIFF, etc. También puedes extraer las imágenes de un archivo PDF. Puedes usar cuatro clases del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) para implementar estas operaciones, es decir, [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) y [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## Operaciones de Imagen

En esta sección, vamos a examinar detalladamente estas operaciones de imagen. Vamos a ver fragmentos de código para mostrar el uso de las clases y métodos relacionados. En primer lugar, echemos un vistazo a cómo agregar una imagen en un archivo PDF existente. Podemos usar el método [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) de la clase [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) para agregar una nueva imagen. Usando este método, no solo puedes especificar el número de página en el que deseas agregar la imagen, sino que también se puede especificar la ubicación de la imagen.

## Agregar Imagen en un Archivo PDF Existente (Facades)

Puedes usar el método [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) de la clase [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). El método [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) requiere que se agregue la imagen, el número de página en el que necesita ser agregada y la información de coordenadas. Después de eso, guarde el archivo PDF actualizado usando el método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

En el siguiente ejemplo, agregamos una imagen a la página usando imageStream:

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Cargar imagen en el stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // guardar el archivo de salida
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Agregar Imagen](/pdf/es/net/images/add_image1.png)

Con la ayuda de [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), podemos superponer una imagen sobre otra:
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Cargar imagen en el flujo
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // guardar el archivo de salida
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![Add Image](/pdf/es/net/images/add_image2.png)

Hay varias formas de almacenar una imagen en un archivo PDF. Demostraremos una de ellas en el siguiente ejemplo:

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Cargar imagen en el flujo
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // guardar el archivo de salida
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Cargar imagen en el flujo
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // guardar el archivo de salida
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## Agregar Texto en un Archivo PDF Existente (facades)

Podemos agregar texto de varias maneras. Considera el primero. Tomamos el [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) y lo añadimos a la Página. Después, indicamos las coordenadas de la esquina inferior izquierda y luego añadimos nuestro texto a la Página.

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // guarda el archivo de salida
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

Mira cómo se ve:

![Add Text](/pdf/es/net/images/add_text.png)

La segunda forma de añadir [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Además, indicamos un rectángulo en el que nuestro texto debe encajar.

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // guarda el archivo de salida
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
El tercer ejemplo proporciona la capacidad de Agregar Texto a páginas específicas. En nuestro ejemplo, agreguemos un pie de foto en las páginas 1 y 3 del documento.

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("¡Bienvenido a Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // guardar el archivo de salida
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```