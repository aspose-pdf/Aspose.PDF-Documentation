---
title: Extraer texto de PDF C#
linktitle: Extraer texto de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/extract-text-from-all-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF utilizando Aspose.PDF en C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "Descubre la poderosa nueva funcionalidad en Aspose.PDF for .NET que permite a los desarrolladores extraer texto de documentos PDF sin esfuerzo. Esta característica admite la extracción de todas las páginas o regiones específicas, se adapta a diseños de múltiples columnas e incluso permite la recuperación de texto resaltado con solo unas pocas líneas de código. Mejora tus capacidades de procesamiento de documentos y agiliza la extracción de contenido con esta herramienta versátil",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Extraer texto de todas las páginas de un documento PDF

Extraer texto de un documento PDF es un requisito común. En este ejemplo, verás cómo Aspose.PDF for .NET permite extraer texto de todas las páginas de un documento PDF. Necesitas crear un objeto de la clase **TextAbsorber**. Después de eso, abre el PDF usando la clase **Document** y llama al método **Accept** de la colección **Pages**. La clase **TextAbsorber** absorbe el texto del documento y lo devuelve en la propiedad **Text**. El siguiente fragmento de código te muestra cómo extraer texto de todas las páginas de un documento PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

Llama al método **Accept** en una página particular del objeto Document. El índice es el número de página particular desde donde se necesita extraer el texto.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Extraer texto de páginas usando Text Device

Puedes usar la clase **TextDevice** para extraer texto de un archivo PDF. **TextDevice** utiliza **TextAbsorber** en su implementación, por lo tanto, de hecho, hacen lo mismo, pero **TextDevice** se implementó para unificar el enfoque "Device" para extraer cualquier cosa de la página como ImageDevice, PageDevice, etc. **TextAbsorber** puede extraer texto de una página, de todo el PDF o de un XForm, este **TextAbsorber** es más universal.

### Extraer texto de todas las páginas

Los siguientes pasos y el fragmento de código te muestran cómo extraer texto de un PDF usando el dispositivo de texto.

1. Crea un objeto de la clase Document con el archivo PDF de entrada especificado.
1. Crea un objeto de la clase TextDevice.
1. Usa el objeto de la clase TextExtractOptions para especificar las opciones de extracción.
1. Usa el método Process de la clase TextDevice para convertir el contenido a texto.
1. Guarda el texto en el archivo de salida.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## Extraer texto de una región particular de la página

La clase **TextAbsorber** proporciona la capacidad de extraer texto de una página particular o de todas las páginas de un documento PDF. Esta clase devuelve el texto extraído en la propiedad **Text**. Sin embargo, si tenemos el requisito de extraer texto de una región particular de la página, podemos usar la propiedad **Rectangle** de **TextSearchOptions**. La propiedad Rectangle toma un objeto Rectangle como valor y usando esta propiedad, podemos especificar la región de la página de la que necesitamos extraer el texto.

Se llama al método **Accept** de una página para extraer el texto. Crea objetos de las clases **Document** y **TextAbsorber**. Llama al método **Accept** en la página individual, como índice **Page**, del objeto **Document**. El **Index** es el número de página particular desde donde se necesita extraer el texto. Puedes obtener el texto de la propiedad **Text** de la clase **TextAbsorber**. El siguiente fragmento de código te muestra cómo extraer texto de una página individual.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Extraer texto basado en columnas

Un archivo PDF puede estar compuesto de texto, imágenes, anotaciones, archivos adjuntos, gráficos, etc., y Aspose.PDF for .NET ofrece la función de agregar y manipular todos estos elementos. Esta API es notable cuando se trata de la adición y extracción de texto de documentos PDF y podemos encontrarnos con un escenario donde un documento PDF está compuesto de más de una columna (documento de múltiples columnas) y necesitamos extraer el contenido de la página respetando el mismo diseño, entonces Aspose.PDF for .NET es la opción correcta para cumplir con este requisito. Un enfoque es reducir el tamaño de la fuente del contenido dentro del documento PDF y luego realizar la extracción de texto. El siguiente fragmento de código muestra los pasos para reducir el tamaño del texto y luego intentar extraer texto del documento PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### Segundo enfoque - Usando ScaleFactor

En esta nueva versión, también hemos introducido varias mejoras en **TextAbsorber** y en el mecanismo interno de formato de texto. Así que ahora, durante la extracción de texto usando el modo 'Puro', puedes especificar la opción ScaleFactor y puede ser otro enfoque para extraer texto de un documento PDF de múltiples columnas además del enfoque mencionado anteriormente. Este factor de escala puede ajustarse para modificar la cuadrícula que se utiliza para el mecanismo interno de formato de texto durante la extracción de texto. Especificar los valores de ScaleFactor entre 1 y 0.1 (incluyendo 0.1) tiene el mismo efecto que la reducción de la fuente.

Especificar los valores de ScaleFactor entre 0.1 y -0.1 se trata como un valor cero, pero hace que el algoritmo calcule automáticamente el factor de escala necesario durante la extracción de texto. El cálculo se basa en el ancho promedio de glifos de la fuente más popular en la página, pero no podemos garantizar que en el texto extraído ninguna cadena de columna alcance el inicio de la siguiente columna. Ten en cuenta que si no se especifica un valor de ScaleFactor, se utilizará el valor predeterminado de 1.0. Esto significa que no se llevará a cabo ninguna escala. Si el valor de ScaleFactor especificado es mayor que 10 o menor que -0.1, se utilizará el valor predeterminado de 1.0.

Proponemos el uso de auto-escalado (ScaleFactor = 0) al procesar un gran número de archivos PDF para la extracción de contenido de texto. O establecer manualmente una reducción redundante del ancho de la cuadrícula (aproximadamente ScaleFactor = 0.5). Sin embargo, no debes determinar si la escala es necesaria para documentos concretos o no. Si estableces una reducción redundante del ancho de la cuadrícula para el documento (que no la necesita), el contenido de texto extraído seguirá siendo completamente adecuado. Por favor, echa un vistazo al siguiente fragmento de código.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

Ten en cuenta que no hay una correspondencia directa entre el nuevo ScaleFactor y el antiguo coeficiente de reducción manual de fuentes. Sin embargo, por defecto, el algoritmo tiene en cuenta el valor del tamaño de fuente que ya se ha reducido debido a algunas razones internas. Por ejemplo, reducir el tamaño de fuente de 10 a 7 tiene el mismo efecto que establecer un factor de escala de 5/8 (= 0.625).

{{% /alert %}}

## Extraer texto resaltado de un documento PDF

En varios escenarios de extracción de texto de un documento PDF, puedes encontrarte con el requisito de extraer solo el texto resaltado del documento PDF. Para implementar la funcionalidad, hemos agregado los métodos **TextMarkupAnnotation.GetMarkedText()** y **TextMarkupAnnotation.GetMarkedTextFragments()** en la API. Puedes extraer texto resaltado de un documento PDF filtrando **TextMarkupAnnotation** y utilizando los métodos mencionados. El siguiente fragmento de código muestra cómo puedes extraer texto resaltado de un documento PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## Acceder a elementos de fragmento de texto y segmento desde XML

A veces necesitamos acceder a elementos **TextFragment** o **TextSegment** al procesar documentos PDF generados a partir de XML. Aspose.PDF for .NET proporciona acceso a tales elementos por nombre. El siguiente fragmento de código muestra cómo usar esta funcionalidad.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```