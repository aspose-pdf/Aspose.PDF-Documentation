---
title: Buscar y Obtener Texto de las Páginas de un PDF
linktitle: Buscar y Obtener Texto
type: docs
weight: 60
url: /es/net/search-and-get-text-from-pdf/
description: Este artículo explica cómo utilizar diversas herramientas para buscar y obtener un texto de Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Buscar y Obtener Texto de las Páginas de un PDF",
    "alternativeHeadline": "Herramientas para buscar y obtener texto de las páginas de un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, buscar texto, obtener texto de pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica cómo utilizar diversas herramientas para buscar y obtener un texto de Aspose.PDF para .NET."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Buscar y Obtener Texto de Todas las Páginas de un Documento PDF

La clase [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) te permite encontrar texto, que coincida con una frase particular, de todas las páginas de un documento PDF. Para buscar texto en todo el documento, necesitas llamar al método Accept de la colección de Páginas. El método [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) toma como parámetro el objeto TextFragmentAbsorber, que devuelve una colección de objetos TextFragment. Puedes recorrer todos los fragmentos y obtener sus propiedades como Texto, Posición (XIndent, YIndent), Nombre de Fuente, Tamaño de Fuente, EsAccesible, EstáIncrustado, EsSubconjunto, Color de Primer Plano, etc.

El siguiente fragmento de código te muestra cómo buscar texto en todas las páginas.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda ingresada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("texto");

// Aceptar el absorber para todas las páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Recorrer los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Texto : {0} ", textFragment.Text);
    Console.WriteLine("Posición : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Fuente - Nombre : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Fuente - EsAccesible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Fuente - EstáIncrustada : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Fuente - EsSubconjunto : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Tamaño de Fuente : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Color de Primer Plano : {0} ", textFragment.TextState.ForegroundColor);
}
```
En caso de que necesite buscar texto dentro de una página específica de cualquier PDF, por favor especifique el número de página de la colección de páginas de la instancia del Documento y llame al método Accept en esa página (como se muestra en la línea de código a continuación).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Aceptar el absorbedor para una página en particular
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Buscar y Obtener Segmentos de Texto de Todas las Páginas del Documento PDF

Para buscar segmentos de texto de todas las páginas, primero necesita obtener los objetos TextFragment del documento.
Para buscar segmentos de texto de todas las páginas, primero necesitas obtener los objetos TextFragment del documento.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda ingresada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// Aceptar el absorbedor para todas las páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Iterar a través de los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("Texto : {0} ", textSegment.Text);
        Console.WriteLine("Posición : {0} ", textSegment.Position);
        Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("Fuente - Nombre : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("Fuente - EsAccesible : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("Fuente - EstáIncrustada : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Fuente - EsSubconjunto : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Tamaño de Fuente : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Color de Primer Plano : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```
Para buscar y obtener Segmentos de Texto de una página específica del PDF, necesita especificar el índice de la página particular al llamar al método Accept(..). Por favor, mire las siguientes líneas de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Aceptar el absorbedor para todas las páginas
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Buscar y obtener texto de todas las páginas utilizando Expresión Regular

TextFragmentAbsorber le ayuda a buscar y recuperar texto, de todas las páginas, basado en una expresión regular.
TextFragmentAbsorber te ayuda a buscar y recuperar texto, de todas las páginas, basado en una expresión regular.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// El camino al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// Crear objeto TextAbsorber para encontrar todas las frases que coinciden con la expresión regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Como 1999-2000

// Establecer opción de búsqueda de texto para especificar el uso de expresión regular
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Aceptar el absorber para todas las páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Recorrer los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Texto : {0} ", textFragment.Text);
    Console.WriteLine("Posición : {0} ", textFragment.Position);
    Console.WriteLine("Indentación X : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("Indentación Y : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Fuente - Nombre : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Fuente - EsAccesible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Fuente - EstáIncrustada : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Fuente - EsSubconjunto : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Tamaño de la Fuente : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Color de Primer Plano : {0} ", textFragment.TextState.ForegroundColor);
}
```
```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// Para buscar una coincidencia exacta de una palabra, podría considerar usar una expresión regular.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bPalabra\b", new TextSearchOptions(true));

// Para buscar una cadena en mayúsculas o minúsculas, podría considerar usar una expresión regular.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Línea", new TextSearchOptions(true));

// Para buscar todas las cadenas (analizar todas las cadenas) dentro del documento PDF, intente usar la siguiente expresión regular.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// Encuentre la coincidencia de la cadena de búsqueda y obtenga cualquier cosa después de la cadena hasta el salto de línea.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)el ((.)*)");

// Por favor use la siguiente expresión regular para encontrar texto siguiente a la coincidencia del regex.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=palabra).*");

// Para buscar hipervínculos/URLs dentro del documento PDF, intente usar la siguiente expresión regular.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```
## Buscar texto basado en Regex y agregar hipervínculo

Si quieres agregar un hipervínculo sobre una frase de texto basada en una expresión regular, primero encuentra todas las frases que coincidan con esa expresión regular específica usando TextFragmentAbsorber y agrega un hipervínculo sobre estas frases.

Para encontrar una frase y agregar un hipervínculo sobre ella:

1. Pasa la expresión regular como parámetro al constructor de TextFragmentAbsorber.
2. Crea un objeto TextSearchOptions que especifica si se utiliza la expresión regular o no.
3. Obtén las frases coincidentes en TextFragments.
4. Recorre las coincidencias para obtener sus dimensiones rectangulares, cambia el color de primer plano a azul (opcional - para que parezca un hipervínculo y crea un enlace usando el método CreateWebLink(..) de la clase PdfContentEditor.
5. Guarda el PDF actualizado utilizando el método Save del objeto Document.
El siguiente fragmento de código te muestra cómo buscar texto dentro de un archivo PDF usando una expresión regular y agregar hipervínculos sobre las coincidencias.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crea un objeto absorber para encontrar todas las instancias de la frase de búsqueda de entrada
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Habilita la búsqueda de expresión regular
absorber.TextSearchOptions = new TextSearchOptions(true);
// Abre el documento
PdfContentEditor editor = new PdfContentEditor();
// Vincula el archivo PDF fuente
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Acepta el absorber para la página
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Recorre los fragmentos
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```
## Buscar y Dibujar un Rectángulo alrededor de cada Fragmento de Texto

Aspose.PDF para .NET soporta la característica de buscar y obtener las coordenadas de cada carácter o fragmentos de texto. Por lo tanto, para estar seguros de las coordenadas que se devuelven para cada carácter, podríamos considerar resaltar (añadiendo un rectángulo) alrededor de cada carácter.

En caso de un párrafo de texto, podrías considerar usar alguna expresión regular para determinar el fin del párrafo y dibujar un rectángulo alrededor de él. Por favor, echa un vistazo al siguiente fragmento de código. Este fragmento de código obtiene las coordenadas de cada carácter y crea un rectángulo alrededor de cada uno.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Crear objeto TextAbsorber para encontrar todas las frases que coincidan con la expresión regular

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```
## Resaltar cada carácter en un documento PDF

{{% alert color="primary" %}}

Puedes intentar buscar texto en un documento utilizando Aspose.PDF y obtener los resultados en línea en este [enlace](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF para .NET soporta la característica de buscar y obtener las coordenadas de cada carácter o fragmentos de texto. Por lo tanto, para estar seguros sobre las coordenadas que se devuelven para cada carácter, podríamos considerar resaltar (añadiendo un rectángulo) alrededor de cada carácter. El siguiente fragmento de código obtiene las coordenadas de cada carácter y crea un rectángulo alrededor de cada uno.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// Crear objeto TextAbsorber para encontrar todas las palabras
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Recorrer los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```

## Agregar y Buscar Texto Oculto

A veces queremos agregar texto oculto en un documento PDF y luego buscar texto oculto y utilizar su posición para el post-procesamiento. Para su conveniencia, Aspose.PDF para .NET ofrece estas habilidades. Puede agregar texto oculto durante la generación del documento. Además, puede encontrar texto oculto utilizando TextFragmentAbsorber. Para agregar texto oculto, establezca TextState.Invisible en 'verdadero' para el texto agregado. TextFragmentAbsorber encuentra todo el texto que coincide con el patrón (si se especifica). Es el comportamiento predeterminado que no se puede cambiar. Para verificar si el texto encontrado es realmente invisible, se puede usar la propiedad TextState.Invisible. El fragmento de código a continuación muestra cómo usar esta función.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//Crear documento con texto oculto
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("Este es un texto común.");
TextFragment frag2 = new TextFragment("Este es un texto invisible.");

//Establecer la propiedad del texto - invisible
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//Buscar texto en el documento
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //Hacer algo con los fragmentos
    Console.WriteLine("Texto '{0}' en pos {1} invisibilidad: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```
## Búsqueda de texto con .NET Regex

Aspose.PDF para .NET proporciona la capacidad de buscar documentos utilizando la opción Regex estándar de .NET. El TextFragmentAbsorber puede usarse para este propósito como se muestra en el ejemplo de código a continuación.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crea objeto Regex para encontrar todas las palabras
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// Abrir documento
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// Obtener una página en particular
Page page = document.Pages[1];

// Crear objeto TextAbsorber para encontrar todas las instancias del regex ingresado
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// Aceptar el absorber para la página
page.Accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Recorrer los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

