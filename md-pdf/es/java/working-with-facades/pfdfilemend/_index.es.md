---
title: PdfFileMend Class
type: docs
weight: 20
url: /java/pdffilemend-class/
description: Esta sección explica cómo trabajar con Aspose.PDF Facades usando la clase PdfFileMend.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Parecería una tarea no difícil insertar [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) en un documento PDF, siempre que tengas la versión original editable de este documento. Supongamos que creaste un documento, y luego recordaste que necesitas agregar otra línea o estamos hablando de un mayor volumen de documentos, en ambos casos te ayudará Aspose.PDF Facades. Consideremos la posibilidad de agregar texto en un archivo PDF existente con la clase [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend).

## Agregar Texto en un Archivo PDF Existente (facades)

Podemos agregar texto de varias maneras.
 Considera el primero. Tomamos el [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) y lo añadimos a la Página. Después, indicamos las coordenadas de la esquina inferior izquierda, y luego añadimos nuestro texto a la Página.

```java
    public static void AddText01()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("¡Bienvenido a Aspose!");

        mender.AddText(message, 1, 10, 750);

        // guardar el archivo de salida
        mender.Save(_dataDir + "PdfFileMend01_output.pdf");
    }
```

Revisa cómo se ve:

![Añadir Texto](/pdf/net/images/add_text.png)

La segunda forma de añadir [FormattedText](https://reference.aspose.com/pdf//java/com.aspose.pdf.facades/formattedtext). Además, indicamos un rectángulo en el que nuestro texto debería encajar.

```java
public static void AddText02()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("¡Bienvenido a Aspose! ¡Bienvenido a Aspose!");

        mender.AddText(message, 1, 10, 700, 55, 810);
        mender.WrapMode = WordWrapMode.ByWords;

        // guardar el archivo de salida
        mender.Save(_dataDir + "PdfFileMend02_output.pdf");
    }
```

El tercer ejemplo proporciona la capacidad de añadir texto a páginas especificadas. En nuestro ejemplo, vamos a añadir un pie de foto en las páginas 1 y 3 del documento.

```java
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

## Añadir Imagen en un Archivo PDF Existente (facades)

¿Alguna vez has intentado añadir una imagen a un archivo PDF existente?
 Estamos seguros de que sabes que esta no es una tarea fácil. Tal vez estés llenando un formulario en línea y necesitas adjuntar una foto para identificación o adjuntar tu foto a un currículum existente. Anteriormente, tal tarea se resolvía creando una foto, adjuntándola a un documento, escaneándola y enviándola. Este proceso era muy engorroso y consumía mucho tiempo.

Agregar imágenes y texto en un archivo PDF existente es un requisito común y el espacio de nombres com.aspose.pdf.facades cumple muy bien con este requisito. Proporciona una clase [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) que te permite agregar imágenes en el archivo PDF.

Este artículo te mostrará cómo insertar una imagen en un PDF usando com.aspose.pdf.facades. También hay varias opciones para agregar imágenes al PDF.

Inserta una imagen en el documento PDF configurando los parámetros del rectángulo.

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // Cargar imagen en el flujo
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // guardar el archivo de salida
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![Agregar Imagen](/pdf/net/images/add_image1.png)

Consideremos el segundo fragmento de código. Al usar variaciones de los parámetros de la clase [CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters), podemos obtener diferentes efectos de diseño. Probamos uno de ellos.

```java
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


![Add Image](/pdf/net/images/add_image2.png)

En el siguiente fragmento de código utilizamos [ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType). ImageFilterType indica el tipo de códec de flujo que se utilizará para la codificación, por defecto Jpeg. Si cargas una imagen desde un formato PNG, entonces se guardará en el documento como JPEG (o en otro formato que haya especificado).

```java
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


En el siguiente fragmento de código, puede notar el uso del método [IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--).

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) es una bandera, que indica si se debe aplicar una máscara a la imagen para lograr la transparencia de la imagen original

```java
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