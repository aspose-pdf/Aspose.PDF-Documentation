---
title: Replace Text in PDF
linktitle: Replace Text in PDF
type: docs
weight: 40
url: es/net/replace-text-in-pdf/
description: Aprende más sobre las diversas maneras de reemplazar y eliminar texto de la biblioteca Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text in PDF",
    "alternativeHeadline": "Replacing and Removing Text in PDF File",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, dreplace text, remove text",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Aprende más sobre las diversas maneras de reemplazar y eliminar texto de la biblioteca Aspose.PDF para .NET."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Reemplazar texto en todas las páginas de un documento PDF

{{% alert color="primary" %}}

Puedes intentar encontrar y reemplazar el texto en el documento usando Aspose.PDF y obtener los resultados en línea en este [enlace](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para reemplazar texto en todas las páginas de un documento PDF, primero necesitas usar TextFragmentAbsorber para encontrar la frase particular que deseas reemplazar. Después de eso, necesitas recorrer todos los TextFragments para reemplazar el texto y cambiar cualquier otro atributo. Una vez que hayas hecho eso, solo necesitas guardar el PDF de salida usando el método Save del objeto Document. El siguiente fragmento de código te muestra cómo reemplazar texto en todas las páginas de un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");

// Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda ingresada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("texto");

// Aceptar el absorber para todas las páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Recorrer los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Actualizar texto y otras propiedades
    textFragment.Text = "TEXTO";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// Guardar el documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Reemplazar texto en una región específica de la página

Para reemplazar texto en una región específica de la página, primero necesitamos instanciar el objeto TextFragmentAbsorber, especificar la región de la página usando la propiedad TextSearchOptions.Rectangle y luego iterar a través de todos los TextFragments para reemplazar el texto. Una vez completadas estas operaciones, solo necesitamos guardar el PDF de salida utilizando el método Save del objeto Document. El siguiente fragmento de código te muestra cómo reemplazar texto en todas las páginas de un documento PDF.

```csharp
// cargar archivo PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// instanciar objeto TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// buscar texto dentro del límite de la página
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// especificar la región de la página para las opciones de búsqueda de texto
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// buscar texto desde la primera página del archivo PDF
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// iterar a través de cada TextFragment
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // actualizar texto a caracteres en blanco
    tf.Text = "";
}

// guardar archivo PDF actualizado después de reemplazar texto
pdf.Save("c:/pdftest/TextUpdated.pdf");
```
## Reemplazar texto basado en una expresión regular

Si deseas reemplazar algunas frases basadas en expresiones regulares, primero necesitas encontrar todas las frases que coincidan con esa expresión regular utilizando TextFragmentAbsorber. Deberás pasar la expresión regular como parámetro al constructor de TextFragmentAbsorber. También necesitas crear un objeto TextSearchOptions que especifique si se está utilizando o no la expresión regular. Una vez que obtengas las frases coincidentes en TextFragments, necesitas recorrer todas ellas y actualizar según sea necesario. Finalmente, debes guardar el PDF actualizado utilizando el método Save del objeto Document. El siguiente fragmento de código te muestra cómo reemplazar texto basado en una expresión regular.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// Crear objeto TextAbsorber para encontrar todas las frases que coincidan con la expresión regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Como 1999-2000

// Establecer la opción de búsqueda de texto para especificar el uso de expresiones regulares
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Aceptar el absorbedor para una sola página
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// Obtener las colecciones de fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Recorrer los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Actualizar texto y otras propiedades
    textFragment.Text = "Nueva Frase";
    // Establecer en una instancia de un objeto.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```
## Reemplazar fuentes en un archivo PDF existente

Aspose.PDF para .NET soporta la capacidad de reemplazar texto en un documento PDF. Sin embargo, a veces tienes el requerimiento de solo reemplazar la fuente que se está utilizando dentro del documento PDF. Así que en lugar de reemplazar el texto, solo se reemplaza la fuente que se está utilizando. Una de las sobrecargas del constructor de TextFragmentAbsorber acepta un objeto TextEditOptions como argumento y podemos usar el valor RemoveUnusedFonts de la enumeración TextEditOptions.FontReplace para cumplir nuestros requisitos. El siguiente fragmento de código muestra cómo reemplazar la fuente dentro de un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Cargar el archivo PDF fuente
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Buscar fragmentos de texto y establecer la opción de edición como eliminar fuentes no utilizadas
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// Aceptar el absorbente para todas las páginas
pdfDocument.Pages.Accept(absorber);
// Recorrer todos los TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // Si el nombre de la fuente es ArialMT, reemplazar el nombre de la fuente con Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// Guardar el documento actualizado
pdfDocument.Save(dataDir);
```
## La Sustitución de Texto debería reorganizar automáticamente los Contenidos de la Página

Aspose.PDF para .NET soporta la función de buscar y reemplazar texto dentro del archivo PDF. Sin embargo, recientemente algunos clientes encontraron problemas durante el reemplazo de texto cuando un TextFragment particular es reemplazado con contenidos más pequeños y se muestran espacios extras en el PDF resultante o en caso de que el TextFragment sea reemplazado con una cadena más larga, entonces las palabras se superponen a los contenidos existentes de la página. Por lo tanto, se planteó la necesidad de introducir un mecanismo que una vez que el texto dentro de un documento PDF es reemplazado, los contenidos deberían reorganizarse.

Para atender los escenarios mencionados anteriormente, Aspose.PDF para .NET ha sido mejorado de modo que no aparezcan dichos problemas al reemplazar texto dentro del archivo PDF. El siguiente fragmento de código muestra cómo reemplazar texto dentro del archivo PDF y cómo los contenidos de la página deberían reorganizarse automáticamente.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Cargar archivo PDF fuente
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Crear objeto TextFragment Absorber con expresión regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Reemplazar cada TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Establecer fuente del fragmento de texto que se está reemplazando
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Establecer tamaño de fuente
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Reemplazar el texto con una cadena más larga que el marcador de posición
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Guardar PDF resultante
doc.Save(dataDir);
```
## Representación de Símbolos Reemplazables durante la creación de PDF

Los símbolos reemplazables son símbolos especiales en una cadena de texto que pueden ser reemplazados con contenido correspondiente en tiempo de ejecución. Los símbolos reemplazables actualmente soportados por el nuevo Modelo de Objeto de Documento del espacio de nombres Aspose.PDF son `$P`, `$p`, `\n`, `\r`. Los símbolos `$p` y `$P` se utilizan para manejar la numeración de páginas en tiempo de ejecución. `$p` se reemplaza con el número de la página donde se encuentra la clase Paragraph actual. `$P` se reemplaza con el número total de páginas en el documento. Al agregar `TextFragment` a la colección de párrafos de documentos PDF, no se admite el salto de línea dentro del texto. Sin embargo, para agregar texto con un salto de línea, por favor use `TextFragment` con `TextParagraph`:

- use "\r\n" o Environment.NewLine en TextFragment en lugar de un solo "\n";
- cree un objeto TextParagraph. Esto añadirá texto con división de líneas;
- agregue el TextFragment con TextParagraph.AppendLine;
- agregue el TextParagraph con TextBuilder.AppendParagraph.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inicialice un nuevo TextFragment con texto que contenga los marcadores de nueva línea requeridos
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nombre del Solicitante: " + Environment.NewLine + " Joe Smoe");

// Establezca las propiedades del fragmento de texto si es necesario
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Cree un objeto TextParagraph
TextParagraph par = new TextParagraph();

// Agregue un nuevo TextFragment al párrafo
par.AppendLine(textFragment);

// Establezca la posición del párrafo
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Cree un objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Agregue el TextParagraph usando TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## Símbolos reemplazables en el área de Encabezado/Pie de página

Los símbolos reemplazables también pueden colocarse dentro de la sección de Encabezado/Pie de página de un archivo PDF. Por favor, revise el siguiente fragmento de código para detalles sobre cómo añadir un símbolo reemplazable en la sección del pie de página.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Asigne la instancia de marginInfo a la propiedad Margin de sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Instancie un párrafo de texto que almacenará el contenido para mostrar como encabezado
TextFragment t1 = new TextFragment("título del informe");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Nombre_Informe");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Cree un objeto HeaderFooter para la sección
HeaderFooter hfFoot = new HeaderFooter();
// Establezca el objeto HeaderFooter para pie de página impar y par
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Añada un párrafo de texto que contenga el número de página actual del total de páginas
TextFragment t3 = new TextFragment("Generado en fecha de prueba");
TextFragment t4 = new TextFragment("nombre del informe ");
TextFragment t5 = new TextFragment("Página $p de $P");

// Instancie un objeto de tabla
Table tab2 = new Table();

// Añada la tabla en la colección de párrafos de la sección deseada
hfFoot.Paragraphs.Add(tab2);

// Establezca las anchuras de columna de la tabla
tab2.ColumnWidths = "165 172 165";

// Cree filas en la tabla y luego celdas en las filas
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// Establezca la alineación vertical del texto como centrada
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Añada la tabla en la colección de párrafos de la sección deseada
page.Paragraphs.Add(table);

// Establezca el borde de celda predeterminado usando el objeto BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Establezca el borde de la tabla usando otro objeto BorderInfo personalizado
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Cree filas en la tabla y luego celdas en las filas
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total para Java es una compilación de cada componente de Java ofrecido por Aspose. Se compila a" + CRLF + "diario para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes de Java. " + CRLF + "diario para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes de Java. " + CRLF + "Usando Aspose.Total para Java los desarrolladores pueden crear una amplia gama de aplicaciones.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```
## Eliminar fuentes no utilizadas de un archivo PDF

Aspose.PDF para .NET admite la función de incrustar fuentes al crear un documento PDF, así como la capacidad de incrustar fuentes en archivos PDF existentes. Desde Aspose.PDF para .NET 7.3.0, también permite eliminar fuentes duplicadas o no utilizadas de documentos PDF.

Para reemplazar fuentes, utiliza el siguiente enfoque:

1. Llama a la clase [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber).
1. Llama al parámetro TextFragmentAbsorber class’ TextEditOptions.FontReplace.RemoveUnusedFonts. (Esto elimina las fuentes que se han vuelto innecesarias durante el reemplazo de fuentes).
1. Establece la fuente individualmente para cada fragmento de texto.

El siguiente fragmento de código reemplaza la fuente para todos los fragmentos de texto de todas las páginas del documento y elimina las fuentes no utilizadas.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Cargar archivo PDF fuente
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Iterar a través de todos los TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
```
## Eliminar todo el texto de un documento PDF

### Eliminar todo el texto utilizando operadores

En algunas operaciones de texto, necesitas eliminar todo el texto de un documento PDF y para eso, necesitas establecer el texto encontrado como un valor de cadena vacío usualmente. El punto es que cambiar el texto para múltiples fragmentos de texto invoca una serie de operaciones de verificación y ajuste de posición de texto. Estas son esenciales en los escenarios de edición de texto. La dificultad es que no puedes determinar cuántos fragmentos de texto se eliminarán en el escenario donde se procesan en un bucle.

Por lo tanto, recomendamos usar otro enfoque para el escenario de eliminar todo el texto de las páginas PDF. Considere el siguiente fragmento de código que funciona muy rápido.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// Recorrer todas las páginas del documento PDF
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // Seleccionar todo el texto en la página
    page.Contents.Accept(operatorSelector);
    // Eliminar todo el texto
    page.Contents.Delete(operatorSelector.Selected);
}
// Guardar el documento
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la biblioteca .NET",
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

