---
title: Extrayendo texto sin formato de un archivo PDF 
linktitle: Extraer texto de PDF
type: docs
weight: 10
url: /es/java/extract-text-from-all-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF usando Aspose.PDF para Java. De páginas enteras, de una parte específica, basado en columnas, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer texto de todas las páginas de un documento PDF

Extraer texto de un documento PDF es un requisito común. En este ejemplo, verás cómo Aspose.PDF para Java permite extraer texto de todas las páginas de un documento PDF. Para extraer texto de todas las páginas del PDF:

1. Crea un objeto de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Abre el PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y llama al método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) de la colección [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. La clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorbe el texto del documento y lo devuelve en la propiedad **Text**.

El siguiente fragmento de código te muestra cómo extraer texto de todas las páginas de un documento PDF.

```java
public static void ExtractFromAllPages(){
    // La ruta al directorio de documentos.
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // Abrir documento
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Crear objeto TextAbsorber para extraer texto
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // Aceptar el absorbedor para todas las páginas
    pdfDocument.getPages().accept(textAbsorber);
    
    // Obtener el texto extraído
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // Escribir una línea de texto en el archivo
        writer.write(extractedText);            
        // Cerrar el flujo
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```


## Extraer texto de páginas usando Text Device

Puedes usar la clase **TextDevice** para extraer texto de un archivo PDF. TextDevice utiliza [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) en su implementación, por lo tanto, de hecho, hacen lo mismo, pero TextDevice está implementado para unificar el enfoque "Device" para extraer cualquier cosa de la página como ImageDevice, PageDevice, etc. TextAbsorber puede extraer texto de Page, todo el PDF o XForm, este TextAbsorber es más universal.

### Extraer texto de todas las páginas

Los siguientes pasos y fragmento de código te muestran cómo extraer texto de un PDF usando el dispositivo de texto.

1. Crear un objeto de la clase Document con el archivo PDF de entrada especificado
1. Crear un objeto de la clase TextDevice
1. Usar un objeto de la clase TextExtractOptions para especificar opciones de extracción
1. Usar el método Process de la clase TextDevice para convertir el contenido en texto
1. Guardar el texto en el archivo de salida

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // abrir documento
    Document pdfDocument = new Document("input.pdf");
    // archivo de texto en el que se guardará el texto extraído
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // iterar a través de todas las páginas del archivo PDF
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // crear dispositivo de texto
        TextDevice textDevice = new TextDevice();
        // establecer opciones de extracción de texto - establecer modo de extracción de texto (Raw o Pure)
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // obtener el texto de las páginas del PDF y guardarlo en el objeto OutputStream
        textDevice.process(page, text_stream);
    }
    // cerrar objeto de flujo
    text_stream.close();
}
```


## Extraer texto de una región específica de la página

La clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) proporciona la capacidad de extraer texto de una página particular o de todas las páginas de un documento PDF. Esta clase devuelve el texto extraído en la propiedad **Text**. Sin embargo, si tenemos el requisito de extraer texto de una región específica de la página, podemos usar la propiedad **Rectangle** de [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions). La propiedad Rectangle toma un objeto Rectangle como valor y usando esta propiedad, podemos especificar la región de la página de la cual necesitamos extraer el texto.

Se llama al método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) de una página para extraer el texto.
 Crea objetos de las clases [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). Llama al método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) en la página individual, como **Page** Index, del objeto **Document**. El **Index** es el número de página particular de donde se necesita extraer el texto. Puedes obtener el texto de la propiedad **Text** de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). El siguiente fragmento de código te muestra cómo extraer texto de una página individual.

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // abrir documento
    Document doc = new Document("page_0001.pdf");
    // crear objeto TextAbsorber para extraer texto
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // aceptar el absorber para la primera página
    doc.getPages().get_Item(1).accept(absorber);
    // obtener el texto extraído
    String extractedText = absorber.getText();
    // crear un escritor y abrir el archivo
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // escribir los contenidos extraídos
    writer.write(extractedText);
    // cerrar el escritor
    writer.close();
}
```

## Extraer texto basado en columnas

Un archivo PDF puede estar compuesto por elementos de Texto, Imagen, Anotaciones, Adjuntos, Gráficos, etc., y Aspose.PDF para .NET ofrece la función de agregar y manipular todos estos elementos. Esta API es notable cuando se trata de la adición y extracción de Texto de un documento PDF y podemos encontrarnos con un escenario donde un documento PDF está compuesto por más de una columna (documento PDF de múltiples columnas) y necesitamos extraer el contenido de la página manteniendo el mismo diseño, entonces Aspose.PDF para .NET es la elección correcta para cumplir con este requisito. Un enfoque es reducir el tamaño de la fuente de los contenidos dentro del documento PDF y luego realizar la extracción de texto. El siguiente fragmento de código muestra los pasos para reducir el tamaño del texto y luego intentar extraer texto del documento PDF.

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // abrir documento
    Document doc = new Document("page_0001.pdf");
    // crear objeto TextAbsorber para extraer texto
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // aceptar el absorbedor para la primera página
    doc.getPages().get_Item(1).accept(absorber);
    // obtener el texto extraído
    String extractedText = absorber.getText();
    // crear un escritor y abrir el archivo
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // escribir el contenido extraído
    writer.write(extractedText);
    // cerrar escritor
    writer.close();
}
```


### Segundo enfoque - Usando ScaleFactor

En esta nueva versión, también hemos introducido varias mejoras en TextAbsorber y en el mecanismo interno de formato de texto. Así que ahora, durante la extracción de texto usando el modo 'Puro', puedes especificar la opción ScaleFactor y puede ser otro enfoque para extraer texto de un documento PDF de varias columnas además del enfoque mencionado anteriormente. Este factor de escala puede ajustarse para modificar la cuadrícula que se utiliza para el mecanismo interno de formato de texto durante la extracción de texto. Especificar valores de ScaleFactor entre 1 y 0.1 (incluyendo 0.1) tiene el mismo efecto que la reducción de fuente.

Especificar los valores de ScaleFactor entre 0.1 y -0.1 se trata como un valor cero, pero hace que el algoritmo calcule automáticamente el factor de escala necesario durante la extracción de texto. El cálculo se basa en el ancho promedio del glifo de la fuente más popular en la página, pero no podemos garantizar que en el texto extraído ninguna cadena de una columna alcance el inicio de la siguiente columna. Tenga en cuenta que si no se especifica el valor de ScaleFactor, se utilizará el valor predeterminado de 1.0. Esto significa que no se llevará a cabo ningún escalado. Si el valor de ScaleFactor especificado es más de 10 o menos de -0.1, se utilizará el valor predeterminado de 1.0.

We propose the usage of auto-scaling (ScaleFactor = 0) when processing a large number of PDF files for text content extraction. Or manually set redundant reducing of grid width (about ScaleFactor = 0.5). However, you must not determine whether scaling is necessary for concrete documents or not. If You set redundant reducing of grid width for the document (that doesn't need in it), the extracted text content will remain fully adequate. Please take a look at the following code snippet.

Proponemos el uso de escalado automático (ScaleFactor = 0) al procesar un gran número de archivos PDF para la extracción de contenido de texto. O establecer manualmente la reducción redundante del ancho de la cuadrícula (aproximadamente ScaleFactor = 0.5). Sin embargo, no debe determinar si el escalado es necesario para documentos concretos o no. Si configura una reducción redundante del ancho de la cuadrícula para el documento (que no lo necesita), el contenido de texto extraído seguirá siendo completamente adecuado. Por favor, eche un vistazo al siguiente fragmento de código.

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // Setting scale factor to 0.5 is enough to split columns in the majority of documents
    // Setting of zero allows to algorithm choose scale factor automatically
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

Tenga en cuenta que no hay una correspondencia directa entre el nuevo ScaleFactor y el antiguo coeficiente de reducción manual de fuentes. Sin embargo, por defecto, el algoritmo toma en cuenta el valor del tamaño de fuente que ya se ha reducido por algunas razones internas. Por ejemplo, reducir el tamaño de la fuente de 10 a 7 tiene el mismo efecto que establecer un factor de escala a 5/8 (= 0.625).

{{% /alert %}}

## Extraer Texto Resaltado de un Documento PDF

En varios escenarios de extracción de texto de un documento PDF, puede surgir un requisito para extraer solo el texto resaltado del documento PDF. Para implementar la funcionalidad, hemos agregado los métodos TextMarkupAnnotation.GetMarkedText() y TextMarkupAnnotation.GetMarkedTextFragments() en la API. Puede extraer texto resaltado de un documento PDF filtrando TextMarkupAnnotation y usando los métodos mencionados. El siguiente fragmento de código muestra cómo puede extraer texto resaltado de un documento PDF.

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // Recorre todas las anotaciones
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // Filtrar TextMarkupAnnotation
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // Recuperar fragmentos de texto resaltado
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // Mostrar texto resaltado
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## Acceder a Fragmentos de Texto y Elementos de Segmento desde XML

A veces necesitamos acceder a elementos TextFragment o TextSegment al procesar documentos PDF generados a partir de XML. Aspose.PDF para .NET proporciona acceso a dichos elementos por nombre. El siguiente fragmento de código muestra cómo usar esta funcionalidad.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```