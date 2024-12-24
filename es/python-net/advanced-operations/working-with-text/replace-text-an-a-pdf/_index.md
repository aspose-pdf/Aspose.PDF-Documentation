---
title: Reemplazar Texto en PDF a través de Python
linktitle: Reemplazar Texto en PDF
type: docs
weight: 40
url: /es/python-net/replace-text-in-pdf/
description: Aprende más sobre varias formas de reemplazar y eliminar texto de Aspose.PDF para Python a través de la biblioteca .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Reemplazar Texto en PDF",
    "alternativeHeadline": "Reemplazo y Eliminación de Texto en Archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, reemplazar texto, eliminar texto",
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
    "url": "/python-net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/replace-text-in-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Aprende más sobre varias formas de reemplazar y eliminar texto de Aspose.PDF para Python a través de la biblioteca .NET."
}
</script>


## Reemplazar texto en todas las páginas de un documento PDF

{{% alert color="primary" %}}

Puede intentar encontrar y reemplazar el texto en el documento usando Aspose.PDF y obtener los resultados en línea en este [enlace](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para reemplazar texto en todas las páginas de un documento PDF, primero necesita usar [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) para encontrar la frase particular que desea reemplazar. Después de eso, debe recorrer todos los TextFragments para reemplazar el texto y cambiar cualquier otro atributo. Una vez hecho esto, solo necesita guardar el PDF de salida usando el método Save del objeto Document. El siguiente fragmento de código le muestra cómo reemplazar texto en todas las páginas de un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
    absorber = ap.text.TextFragmentAbsorber("format")

    # Aceptar el absorber para todas las páginas
    document.pages.accept(absorber)

    # Obtener los fragmentos de texto extraídos
    collection = absorber.text_fragments

    # Recorrer los fragmentos
    for text_fragment in collection:
        # Actualizar texto y otras propiedades
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # Guardar el documento
    document.save(output_pdf)
```


## Reemplazar texto en una región específica de la página

Para reemplazar texto en una región particular de la página, primero necesitamos instanciar un objeto TextFragmentAbsorber, especificar la región de la página usando la propiedad TextSearchOptions.Rectangle y luego iterar a través de todos los TextFragments para reemplazar el texto. Una vez que estas operaciones se completan, solo necesitamos guardar el PDF de salida usando el método Save del objeto Document. El siguiente fragmento de código te muestra cómo reemplazar texto en todas las páginas del documento PDF.

```python
// cargar archivo PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// instanciar objeto TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// buscar texto dentro de los límites de la página
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

// guardar archivo PDF actualizado después de reemplazar el texto
pdf.Save("c:/pdftest/TextUpdated.pdf");
```


## Reemplazar Texto Basado en una Expresión Regular

Si deseas reemplazar algunas frases basadas en una expresión regular, primero necesitas encontrar todas las frases que coincidan con esa expresión regular particular utilizando TextFragmentAbsorber. Tendrás que pasar la expresión regular como un parámetro al constructor de TextFragmentAbsorber. También necesitas crear un objeto TextSearchOptions que especifique si se está utilizando la expresión regular o no. Una vez que obtengas las frases coincidentes en TextFragments, necesitas iterar a través de todas ellas y actualizarlas según sea necesario. Finalmente, necesitas guardar el PDF actualizado usando el método Save del objeto Document. El siguiente fragmento de código te muestra cómo reemplazar texto basado en una expresión regular.

```python
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// Crear objeto TextAbsorber para encontrar todas las frases que coinciden con la expresión regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Como 1999-2000

// Establecer opción de búsqueda de texto para especificar el uso de expresión regular
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Aceptar el absorbente para una sola página
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Iterar a través de los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Actualizar texto y otras propiedades
    textFragment.Text = "Nueva Frase";
    // Establecer a una instancia de un objeto.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```


## Reemplazar fuentes en un archivo PDF existente

Aspose.PDF para Python a través de .NET admite la capacidad de reemplazar texto en un documento PDF. Sin embargo, a veces tienes el requisito de solo reemplazar la fuente que se está utilizando dentro del documento PDF. Así que, en lugar de reemplazar el texto, solo la fuente que se está utilizando es reemplazada. Una de las sobrecargas del constructor TextFragmentAbsorber acepta un objeto TextEditOptions como argumento y podemos usar el valor RemoveUnusedFonts de la enumeración TextEditOptions.FontReplace para cumplir con nuestros requisitos. El siguiente fragmento de código muestra cómo reemplazar la fuente dentro del documento PDF.

```python
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Cargar archivo PDF de origen
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Buscar fragmentos de texto y establecer la opción de edición para eliminar fuentes no usadas
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// Aceptar el absorbedor para todas las páginas
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
// Guardar documento actualizado
pdfDocument.Save(dataDir);
```


## El reemplazo de texto debería reordenar automáticamente el contenido de la página

Aspose.PDF para Python a través de .NET admite la función de buscar y reemplazar texto dentro del archivo PDF. Sin embargo, recientemente algunos clientes encontraron problemas durante el reemplazo de texto cuando un TextFragment particular se reemplaza con contenido más pequeño y algunos espacios extra se muestran en el PDF resultante o en caso de que el TextFragment se reemplace con una cadena más larga, entonces las palabras se superponen al contenido existente de la página. Así que el requisito era introducir un mecanismo que, una vez que se reemplace el texto dentro de un documento PDF, el contenido debe reordenarse.

Para atender los escenarios mencionados anteriormente, Aspose.PDF para Python a través de .NET ha sido mejorado para que no aparezcan tales problemas al reemplazar texto dentro del archivo PDF. El siguiente fragmento de código muestra cómo reemplazar texto dentro de un archivo PDF y el contenido de la página debe reordenarse automáticamente.

```python
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Cargar archivo PDF de origen
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Crear objeto TextFragment Absorber con expresión regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Reemplazar cada TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Establecer la fuente del fragmento de texto que se reemplaza
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Establecer tamaño de fuente
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Reemplazar el texto con una cadena más grande que el marcador de posición
    textFragment.Text = "Esta es una cadena más grande para la prueba de este problema";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Guardar PDF resultante
doc.Save(dataDir);
```


## Renderización de Símbolos Reemplazables durante la creación de PDF

Los símbolos reemplazables son símbolos especiales en una cadena de texto que pueden ser reemplazados con el contenido correspondiente en tiempo de ejecución. Los símbolos reemplazables que actualmente admite el nuevo Modelo de Objetos del Documento del espacio de nombres Aspose.PDF son `$P`, `$p`, `\n`, `\r`. Los símbolos `$p` y `$P` se utilizan para manejar la numeración de páginas en tiempo de ejecución. `$p` se reemplaza con el número de la página donde se encuentra la clase Paragraph actual. `$P` se reemplaza con el número total de páginas en el documento. Al agregar `TextFragment` a la colección de párrafos de documentos PDF, no admite el salto de línea dentro del texto. Sin embargo, para agregar texto con un salto de línea, utilice `TextFragment` con `TextParagraph`:

- use "\r\n" o Environment.NewLine en TextFragment en lugar de un solo "\n";
- cree un objeto TextParagraph. Agregará texto con división de líneas;
- agregue el TextFragment con TextParagraph.AppendLine;
- agregue el TextParagraph con TextBuilder.AppendParagraph.

```python
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inicializar un nuevo TextFragment con texto que contiene los marcadores de nueva línea requeridos
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nombre del Solicitante: " + Environment.NewLine + " Joe Smoe");

// Establecer propiedades del fragmento de texto si es necesario
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Crear objeto TextParagraph
TextParagraph par = new TextParagraph();

// Agregar nuevo TextFragment al párrafo
par.AppendLine(textFragment);

// Establecer la posición del párrafo
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Crear objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Agregar el TextParagraph usando TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```


## Símbolos reemplazables en el área de Encabezado/Pie de página

Los símbolos reemplazables también pueden colocarse dentro de la sección de Encabezado/Pie de página del archivo PDF. Por favor, echa un vistazo al siguiente fragmento de código para obtener detalles sobre cómo agregar un símbolo reemplazable en la sección del pie de página.

```python
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Asignar la instancia de marginInfo a la propiedad Margin de sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Instanciar un párrafo de texto que almacenará el contenido a mostrar como encabezado
TextFragment t1 = new TextFragment("título del informe");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Nombre del Informe");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Crear un objeto HeaderFooter para la sección
HeaderFooter hfFoot = new HeaderFooter();
// Establecer el objeto HeaderFooter para pie de página impar y par
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Agregar un párrafo de texto que contenga el número de página actual del total de páginas
TextFragment t3 = new TextFragment("Generado en fecha de prueba");
TextFragment t4 = new TextFragment("nombre del informe ");
TextFragment t5 = new TextFragment("Página $p de $P");

// Instanciar un objeto tabla
Table tab2 = new Table();

// Agregar la tabla en la colección de párrafos de la sección deseada
hfFoot.Paragraphs.Add(tab2);

// Establecer los anchos de columna de la tabla
tab2.ColumnWidths = "165 172 165";

// Crear filas en la tabla y luego celdas en las filas
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// Establecer la alineación vertical del texto como centrado
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total for Java es una compilación de cada componente Java ofrecido por Aspose. Se compila en un#$NL" + "diario para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes Java. #$NL " + "Usando Aspose.Total for Java los desarrolladores pueden crear una amplia gama de aplicaciones. #$NL #$NL #$NP" + "Aspose.Total for Java es una compilación de cada componente Java ofrecido por Aspose. Se compila en un#$NL" + "diario para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes Java. #$NL " + "Usando Aspose.Total for Java los desarrolladores pueden crear una amplia gama de aplicaciones. #$NL #$NL #$NP" + "Aspose.Total for Java es una compilación de cada componente Java ofrecido por Aspose. Se compila en un#$NL" + "diario para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes Java. #$NL " + "Usando Aspose.Total for Java los desarrolladores pueden crear una amplia gama de aplicaciones. #$NL #$NL"))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Agregar la tabla en la colección de párrafos de la sección deseada
page.Paragraphs.Add(table);

// Establecer el borde de celda predeterminado usando el objeto BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Establecer el borde de la tabla usando otro objeto BorderInfo personalizado
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Crear filas en la tabla y luego celdas en las filas
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
            c1 = row.Cells.Add("Aspose.Total for Java es una compilación de cada componente Java ofrecido por Aspose. Se compila en un" + CRLF + "diario para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes Java. " + CRLF + "diario para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes Java. " + CRLF + "Usando Aspose.Total for Java los desarrolladores pueden crear una amplia gama de aplicaciones.");
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


## Eliminar Fuentes No Utilizadas del Archivo PDF

Aspose.PDF para Python a través de .NET admite la función de incrustar fuentes al crear un documento PDF, así como la capacidad de incrustar fuentes en archivos PDF existentes. A partir de Aspose.PDF para Python a través de .NET 7.3.0, también te permite eliminar fuentes duplicadas o no utilizadas de documentos PDF.

Para reemplazar fuentes, utiliza el siguiente enfoque:

1. Llama a la clase [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Llama al parámetro TextEditOptions.FontReplace.RemoveUnusedFonts de la clase TextFragmentAbsorber. (Esto elimina las fuentes que se han vuelto no utilizadas durante el reemplazo de fuentes).
1. Establece la fuente individualmente para cada fragmento de texto.

El siguiente fragmento de código reemplaza la fuente para todos los fragmentos de texto de todas las páginas del documento y elimina las fuentes no utilizadas.

```python
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Cargar archivo PDF de origen
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Iterar a través de todos los TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Guardar documento actualizado
doc.Save(dataDir);
```


## Eliminar Todo el Texto del Documento PDF

### Eliminar Todo el Texto usando Operadores

En alguna operación de texto, necesitas eliminar todo el texto del documento PDF y para eso, usualmente necesitas establecer el texto encontrado como un valor de cadena vacía. El punto es que cambiar el texto para una multitud de fragmentos de texto invoca una serie de operaciones de verificación y ajuste de posición del texto. Son esenciales en los escenarios de edición de texto. La dificultad es que no puedes determinar cuántos fragmentos de texto serán eliminados en el escenario donde se procesan en un bucle.

Por lo tanto, recomendamos usar otro enfoque para el escenario de eliminar todo el texto de las páginas PDF. Por favor, considera el siguiente fragmento de código que funciona muy rápido.

```python
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
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
    "name": "Aspose.PDF para Python a través de la Biblioteca .NET",
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para Python",
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