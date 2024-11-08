---
title: Buscar y Obtener Texto de las Páginas de PDF
linktitle: Buscar y Obtener Texto
type: docs
weight: 60
url: /es/python-net/search-and-get-text-from-pdf/
description: Este artículo explica cómo usar varias herramientas para buscar y obtener texto de Aspose.PDF para .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Buscar y Obtener Texto de las Páginas de PDF",
    "alternativeHeadline": "Herramientas para buscar y obtener texto de las Páginas de PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, buscar texto, obtener texto de pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Este artículo explica cómo usar varias herramientas para buscar y obtener texto de Aspose.PDF para .NET."
}
</script>


## Buscar y Obtener Texto de Todas las Páginas del Documento PDF

La clase [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) te permite encontrar texto que coincide con una frase particular en todas las páginas de un documento PDF. Para buscar texto en todo el documento, necesitas llamar al método Accept de la colección Pages. El método [Accept](https://reference.aspose.com/pdf/python-net/aspose.pdf.page/accept/methods/3) toma un objeto TextFragmentAbsorber como parámetro, el cual devuelve una colección de objetos TextFragment. Puedes iterar a través de todos los fragmentos y obtener sus propiedades como Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor, etc.

El siguiente fragmento de código te muestra cómo buscar texto en todas las páginas.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda ingresada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// Aceptar el absorbedor para todas las páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Iterar a través de los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Texto : {0} ", textFragment.Text);
    Console.WriteLine("Posición : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Fuente - Nombre : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Fuente - EsAccesible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Fuente - EstáIncrustada : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Fuente - EsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Tamaño de Fuente : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Color de Primer Plano : {0} ", textFragment.TextState.ForegroundColor);
}
```


En caso de que necesite buscar texto dentro de cualquier página PDF en particular, especifique el número de página de la colección de páginas de la instancia del Documento y llame al método Accept contra esa página (como se muestra en la línea de código a continuación).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Aceptar el absorbedor para una página en particular
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Buscar y Obtener Segmentos de Texto de Todas las Páginas del Documento PDF

Para buscar segmentos de texto de todas las páginas, primero necesita obtener los objetos TextFragment del documento.
 TextFragmentAbsorber te permite encontrar texto que coincide con una frase particular en todas las páginas de un documento PDF. Para buscar texto en todo el documento, necesitas llamar al método Accept de la colección Pages. El método Accept toma un objeto TextFragmentAbsorber como parámetro, que devuelve una colección de objetos TextFragment. Una vez que la TextFragmentCollection se extrae del documento, necesitas recorrer esta colección y obtener TextSegmentCollection de cada objeto TextFragment. Después de eso, puedes obtener todas las propiedades del objeto TextSegment individual. El siguiente fragmento de código te muestra cómo buscar segmentos de texto en todas las páginas.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figura");
// Aceptar el absorber para todas las páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Recorrer los fragmentos
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
        Console.WriteLine("Fuente - EstáIncorporada : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Fuente - EsSubconjunto : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Tamaño de Fuente : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Color de Primer Plano : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```

Para buscar y obtener TextSegments de una página particular de un PDF, necesitas especificar el índice de la página particular al llamar al método Accept(..). Por favor, revisa las siguientes líneas de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Aceptar el absorbedor para todas las páginas
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Buscar y Obtener Texto de todas las páginas usando Expresión Regular

TextFragmentAbsorber te ayuda a buscar y recuperar texto, de todas las páginas, basado en una expresión regular.
 Primero, necesitas pasar una expresión regular al constructor de TextFragmentAbsorber como la frase. Después de eso, debes establecer la propiedad TextSearchOptions del objeto TextFragmentAbsorber. Esta propiedad requiere un objeto TextSearchOptions y necesitas pasar true como parámetro a su constructor al crear nuevos objetos. Como deseas recuperar texto coincidente de todas las páginas, necesitas llamar al método Accept de la colección Pages. TextFragmentAbsorber devuelve un TextFragmentCollection que contiene todos los fragmentos que coinciden con los criterios especificados por la expresión regular. El siguiente fragmento de código te muestra cómo buscar y obtener texto de todas las páginas basado en una expresión regular.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// Crear objeto TextAbsorber para encontrar todas las frases que coinciden con la expresión regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Como 1999-2000

// Establecer la opción de búsqueda de texto para especificar el uso de la expresión regular
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Aceptar el absorbente para todas las páginas
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
    Console.WriteLine("Fuente - EsIncorporada : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Fuente - EsSubconjunto : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Tamaño de Fuente : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Color de Primer Plano : {0} ", textFragment.TextState.ForegroundColor);
}
```

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// Para buscar una coincidencia exacta de una palabra, puede considerar usar una expresión regular.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// Para buscar una cadena en mayúsculas o minúsculas, puede considerar usar una expresión regular.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// Para buscar todas las cadenas (analizar todas las cadenas) dentro del documento PDF, por favor intente usar la siguiente expresión regular.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// Encontrar coincidencia de la cadena de búsqueda y obtener cualquier cosa después de la cadena hasta el salto de línea.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// Por favor use la siguiente expresión regular para encontrar texto siguiendo la coincidencia del regex.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// Para buscar Hipervínculos/URL's dentro del documento PDF, por favor intente usar la siguiente expresión regular.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```


## Buscar Texto basado en Regex y Agregar Hipervínculo

Si deseas agregar un hipervínculo sobre una frase de texto basada en una expresión regular, primero encuentra todas las frases que coinciden con esa expresión regular particular usando TextFragmentAbsorber y agrega un hipervínculo sobre estas frases.

Para encontrar una frase y agregar un hipervínculo sobre ella:

1. Pasa la expresión regular como un parámetro al constructor de TextFragmentAbsorber.
2. Crea un objeto TextSearchOptions que especifique si se usa la expresión regular o no.
3. Obtén las frases coincidentes en TextFragments.
4. Recorre las coincidencias para obtener sus dimensiones rectangulares, cambia el color de primer plano a azul (opcional - para que parezca un hipervínculo y crea un enlace usando el método CreateWebLink(..) de la clase PdfContentEditor.
5. Guarda el PDF actualizado usando el método Save del objeto Document. El siguiente fragmento de código te muestra cómo buscar texto dentro de un archivo PDF usando una expresión regular y agregar hipervínculos sobre las coincidencias.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crea un objeto absorber para encontrar todas las instancias de la frase de búsqueda de entrada
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Habilitar búsqueda con expresión regular
absorber.TextSearchOptions = new TextSearchOptions(true);
// Abrir documento
PdfContentEditor editor = new PdfContentEditor();
// Vincular archivo PDF de origen
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Aceptar el absorbedor para la página
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Recorrer los fragmentos
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


## Buscar y Dibujar Rectángulo alrededor de cada Fragmento de Texto

Aspose.PDF para .NET admite la función de buscar y obtener las coordenadas de cada carácter o fragmento de texto. Así que, para estar seguros de las coordenadas que se devuelven para cada carácter, podemos considerar resaltar (añadir un rectángulo) alrededor de cada carácter.

En el caso de un párrafo de texto, puede considerar usar alguna expresión regular para determinar la ruptura de párrafo y dibujar un rectángulo alrededor de él. Por favor, eche un vistazo al siguiente fragmento de código. El siguiente fragmento de código obtiene las coordenadas de cada carácter y crea un rectángulo alrededor de cada carácter.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
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

Puede intentar buscar texto en un documento usando Aspose.PDF y obtener los resultados en línea en este [enlace](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF para .NET admite la función de buscar y obtener las coordenadas de cada carácter o fragmentos de texto. Entonces, para estar seguro de las coordenadas que se devuelven para cada carácter, podemos considerar resaltar (agregar un rectángulo) alrededor de cada carácter. El siguiente fragmento de código obtiene las coordenadas de cada carácter y crea un rectángulo alrededor de cada carácter.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
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


## Añadir y Buscar Texto Oculto

A veces queremos añadir texto oculto en un documento PDF y luego buscar texto oculto y usar su posición para el post-procesamiento. Para su conveniencia, Aspose.PDF para .NET proporciona estas capacidades. Puede añadir texto oculto durante la generación del documento. También puede encontrar texto oculto utilizando TextFragmentAbsorber. Para añadir texto oculto, establezca TextState.Invisible en 'true' para el texto añadido. TextFragmentAbsorber encuentra todo el texto que coincide con el patrón (si se especifica). Es el comportamiento predeterminado que no se puede cambiar. Para verificar si el texto encontrado es realmente invisible, se puede usar la propiedad TextState.Invisible. El fragmento de código a continuación muestra cómo usar esta característica.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//Crear documento con texto oculto
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("Este es un texto común.");
TextFragment frag2 = new TextFragment("Este es un texto invisible.");

//Establecer propiedad de texto - invisible
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

Aspose.PDF para .NET proporciona la capacidad de buscar documentos usando la opción estándar de Regex de .NET. El TextFragmentAbsorber se puede usar para este propósito como se muestra en el siguiente ejemplo de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Crear objeto Regex para encontrar todas las palabras
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// Abrir documento
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// Obtener una página en particular
Page page = document.Pages[1];

// Crear objeto TextAbsorber para encontrar todas las instancias del regex de entrada
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
    "name": "Aspose.PDF para la Biblioteca .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>