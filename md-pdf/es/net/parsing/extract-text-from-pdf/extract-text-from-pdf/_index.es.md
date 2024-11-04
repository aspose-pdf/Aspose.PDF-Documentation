---
title: Extraer texto de PDF C#
linktitle: Extraer texto de PDF
type: docs
weight: 10
url: /net/extract-text-from-all-pdf/
description: Este artículo describe varias maneras de extraer texto de documentos PDF utilizando Aspose.PDF en C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer texto de todas las páginas de un documento PDF

Extraer texto de un documento PDF es un requisito común. En este ejemplo, verás cómo Aspose.PDF para .NET permite extraer texto de todas las páginas de un documento PDF. Necesitas crear un objeto de la clase **TextAbsorber**. Después, abre el PDF usando la clase **Document** y llama al método **Accept** de la colección **Pages**. La clase **TextAbsorber** absorbe el texto del documento y lo devuelve en la propiedad **Text**. El siguiente fragmento de código te muestra cómo extraer texto de todas las páginas de un documento PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Crear objeto TextAbsorber para extraer texto
TextAbsorber textAbsorber = new TextAbsorber();
// Aceptar el absorbente para todas las páginas
pdfDocument.Pages.Accept(textAbsorber);
// Obtener el texto extraído
string extractedText = textAbsorber.Text;
// Crear un escritor y abrir el archivo
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Escribir una línea de texto en el archivo
tw.WriteLine(extractedText);
// Cerrar el flujo
tw.Close();
```
Llame al método **Accept** en una página particular del objeto Document. El índice es el número de página particular de donde se necesita extraer el texto.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// Crear objeto TextAbsorber para extraer texto
TextAbsorber textAbsorber = new TextAbsorber();

// Aceptar el absorbedor para una página particular
pdfDocument.Pages[1].Accept(textAbsorber);

// Obtener el texto extraído
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// Crear un escritor y abrir el archivo
TextWriter tw = new StreamWriter(dataDir);

// Escribir una línea de texto en el archivo
tw.WriteLine(extractedText);

// Cerrar el flujo
tw.Close();
```
## Extraer texto de páginas usando Text Device

Puedes usar la clase **TextDevice** para extraer texto de un archivo PDF. TextDevice utiliza TextAbsorber en su implementación, así que, de hecho, hacen lo mismo pero TextDevice solo se implementó para unificar el enfoque de "Device" para extraer cualquier cosa de la página como ImageDevice, PageDevice, etc. TextAbsorber puede extraer texto de una Página, un PDF completo o un XForm, este TextAbsorber es más universal.

### Extraer texto de todas las páginas

Los siguientes pasos y fragmento de código te muestran cómo extraer texto de un PDF usando el dispositivo de texto.

1. Crear un objeto de la clase Document con el archivo PDF de entrada especificado
1. Crear un objeto de la clase TextDevice
1. Usar objeto de la clase TextExtractOptions para especificar opciones de extracción
1. Usar el método Process de la clase TextDevice para convertir contenidos a texto
1. Guardar el texto en el archivo de salida

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// Cadena para mantener el texto extraído
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // Crear dispositivo de texto
        TextDevice textDevice = new TextDevice();

        // Establecer opciones de extracción de texto - establecer modo de extracción de texto (Raw o Pure)
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // Convertir una página en particular y guardar texto en el stream
        textDevice.Process(pdfPage, textStream);
        // Convertir una página en particular y guardar texto en el stream
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // Cerrar stream de memoria
        textStream.Close();

        // Obtener texto del stream de memoria
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// Guardar el texto extraído en archivo de texto
File.WriteAllText(dataDir, builder.ToString());
```
## Extraer texto de una región específica de la página

La clase **TextAbsorber** proporciona la capacidad de extraer texto de una o todas las páginas de un documento PDF. Esta clase devuelve el texto extraído en la propiedad **Text**. Sin embargo, si necesitamos extraer texto de una región específica de la página, podemos usar la propiedad **Rectangle** de **TextSearchOptions**. La propiedad Rectangle toma un objeto Rectangle como valor y usando esta propiedad, podemos especificar la región de la página de la cual necesitamos extraer el texto.

El método **Accept** de una página se llama para extraer el texto. Crea objetos de las clases **Document** y **TextAbsorber**. Llama al método **Accept** en la página individual, como **Page** Index, del objeto **Document**. El **Index** es el número de página particular de donde se necesita extraer el texto. Puedes obtener texto de la propiedad **Text** de la clase **TextAbsorber**. El siguiente fragmento de código te muestra cómo extraer texto de una página individual.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Crear objeto TextAbsorber para extraer texto
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// Aceptar el absorber para la primera página
pdfDocument.Pages[1].Accept(absorber);

// Obtener el texto extraído
string extractedText = absorber.Text;
// Crear un escritor y abrir el archivo
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Escribir una línea de texto en el archivo
tw.WriteLine(extractedText);
// Cerrar el flujo
tw.Close();
```

## Extraer texto basado en columnas

Un archivo PDF puede constar de elementos como Texto, Imagen, Anotaciones, Adjuntos, Gráficos, etc. y Aspose.PDF para .NET ofrece la característica de añadir así como manipular todos estos elementos.
Un archivo PDF puede contener elementos como Texto, Imagen, Anotaciones, Adjuntos, Gráficos, etc. y Aspose.PDF para .NET ofrece la característica de agregar y manipular todos estos elementos.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // Necesita reducir el tamaño de la fuente al menos un 70%
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```
### Segundo enfoque - Usando ScaleFactor

En esta nueva versión, también hemos introducido varias mejoras en TextAbsorber y en el mecanismo interno de formateo de texto. Ahora, durante la extracción de texto utilizando el modo ‘Pure’, puedes especificar la opción ScaleFactor y puede ser otro enfoque para extraer texto de un documento PDF de múltiples columnas además del enfoque mencionado anteriormente. Este factor de escala puede ajustarse para adaptar la cuadrícula que se utiliza para el mecanismo de formateo de texto interno durante la extracción de texto. Especificar los valores de ScaleFactor entre 1 y 0.1 (incluyendo 0.1) tiene el mismo efecto que la reducción de fuente.

Especificar los valores de ScaleFactor entre 0.1 y -0.1 se trata como un valor cero, pero hace que el algoritmo calcule el factor de escala necesario durante la extracción de texto automáticamente.
Especificar valores de ScaleFactor entre 0.1 y -0.1 se trata como un valor cero, pero hace que el algoritmo calcule el factor de escala necesario durante la extracción automática de texto.

Proponemos el uso de auto-escalado (ScaleFactor = 0) al procesar un gran número de archivos PDF para la extracción de contenido de texto. O establecer manualmente una reducción redundante del ancho de la cuadrícula (aproximadamente ScaleFactor = 0.5). Sin embargo, no debe determinar si el escalado es necesario para documentos concretos o no. Si establece una reducción redundante del ancho de la cuadrícula para el documento (que no lo necesita), el contenido de texto extraído seguirá siendo completamente adecuado. Por favor, eche un vistazo al siguiente fragmento de código.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// Establecer el factor de escala a 0.5 es suficiente para dividir columnas en la mayoría de los documentos
// Establecer cero permite que el algoritmo elija el factor de escala automáticamente
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}
Tenga en cuenta que no existe una correspondencia directa entre el nuevo ScaleFactor y el antiguo coeficiente de reducción manual de la fuente. Sin embargo, el algoritmo por defecto toma en cuenta el valor del tamaño de la fuente que ya se ha reducido por algunas razones internas. Por ejemplo, reducir el tamaño de la fuente de 10 a 7 tiene el mismo efecto que establecer un factor de escala a 5/8 (= 0.625).
{{% /alert %}}

## Extraer texto resaltado de un documento PDF

En varios escenarios de extracción de texto de un documento PDF, puede surgir la necesidad de extraer solo el texto resaltado del documento PDF. Para implementar esta funcionalidad, hemos añadido los métodos TextMarkupAnnotation.GetMarkedText() y TextMarkupAnnotation.GetMarkedTextFragments() en la API. Puede extraer texto resaltado de un documento PDF filtrando TextMarkupAnnotation y utilizando los métodos mencionados. El siguiente fragmento de código muestra cómo puede extraer texto resaltado de un documento PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// Iterar a través de todas las anotaciones
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // Filtrar TextMarkupAnnotation
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // Recuperar fragmentos de texto destacados
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // Mostrar texto destacado
            Console.WriteLine(tf.Text);
        }
    }
}
```

## Acceder a los elementos de Fragmento de Texto y Segmento desde XML

A veces necesitamos acceso a los elementos TextFragement o TextSegment cuando procesamos documentos PDF generados desde XML.
A veces necesitamos acceder a los elementos TextFragement o TextSegment cuando procesamos documentos PDF generados a partir de XML.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```
