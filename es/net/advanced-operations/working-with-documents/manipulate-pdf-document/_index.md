---
title: Manipular Documento PDF en C#
linktitle: Manipular Documento PDF
type: docs
weight: 20
url: /es/net/manipulate-pdf-document/
description: Este artículo contiene información sobre cómo validar un Documento PDF para el Estándar PDF A, cómo trabajar con TOC, cómo establecer la fecha de expiración de un PDF, etc.
keywords: "manipulate pdf c#"
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipular Documento PDF",
    "alternativeHeadline": "Cómo manipular un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, dotnet, manipular archivo pdf",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo contiene información sobre cómo validar un Documento PDF para el Estándar PDF A, cómo trabajar con TOC, cómo establecer la fecha de expiración de un PDF, etc."
}
</script>
## **Manipular Documento PDF en C#**

## Validar Documento PDF para el Estándar PDF A (A 1A y A 1B)

Para validar un documento PDF para la compatibilidad PDF/A-1a o PDF/A-1b, utiliza el método Validate de la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Este método te permite especificar el nombre del archivo en el que se guardará el resultado y el tipo de validación requerido en la enumeración [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat): PDF_A_1A o PDF_A_1B.

{{% alert color="primary" %}}

El formato XML de salida es un formato personalizado de Aspose. El XML contiene una colección de etiquetas con el nombre Problem; cada etiqueta contiene los detalles de un problema particular. El atributo ObjectID de la etiqueta Problem representa la ID del objeto particular al que está relacionado este problema. El atributo Clause representa una regla correspondiente en la especificación del PDF.

{{% /alert %}}

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1A.
El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1A.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validar PDF para PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1B.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validar PDF para PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

Aspose.PDF para .NET se puede utilizar para determinar si el documento cargado es un PDF válido y también [si está encriptado o no](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). Para ampliar aún más las capacidades de la clase Document, se ha añadido la propiedad *IsPdfaCompliant* para determinar si el archivo de entrada cumple con PDF/A y una propiedad llamada *PdfaFormat* para identificar el formato PDF/A introducido.

{{% /alert %}}

## Trabajando con TOC

### Agregar TOC a un PDF Existente

La API de Aspose.PDF le permite agregar una tabla de contenido ya sea al crear un PDF o a un archivo existente. La clase ListSection en el espacio de nombres Aspose.Pdf.Generator le permite crear una tabla de contenidos al crear un PDF desde cero. Para agregar encabezados, que son elementos del TOC, use la clase Aspose.Pdf.Generator.Heading.

Para agregar un TOC a un archivo PDF existente, use la clase Heading en el espacio de nombres Aspose.Pdf.
Para agregar un TOC a un archivo PDF existente, utilice la clase Heading en el espacio de nombres Aspose.Pdf.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Cargar un archivo PDF existente
Document doc = new Document(dataDir + "AddTOC.pdf");

// Obtener acceso a la primera página del archivo PDF
Page tocPage = doc.Pages.Insert(1);

// Crear objeto para representar la información de TOC
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Índice de Contenidos");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// Establecer el título para TOC
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// Crear objetos de cadena que se utilizarán como elementos de TOC
string[] titles = new string[4];
titles[0] = "Primera página";
titles[1] = "Segunda página";
titles[2] = "Tercera página";
titles[3] = "Cuarta página";
for (int i = 0; i < 2; i++)
{
    // Crear objeto Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // Especificar la página de destino para el objeto de encabezado
    heading2.DestinationPage = doc.Pages[i + 2];

    // Página de destino
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // Coordenada de destino
    segment2.Text = titles[i];

    // Añadir encabezado a la página que contiene TOC
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
```
### Establecer diferentes tipos de TabLeader para diferentes niveles de TOC

Aspose.PDF también permite establecer diferentes tipos de TabLeader para diferentes niveles de TOC. Necesitas configurar la propiedad LineDash de FormatArray con el valor apropiado del enumerado TabLeaderType como sigue.

```csharp
 string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

//establecer LeaderType
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("Tabla de Contenidos");
title.TextState.FontSize = 30;
tocInfo.Title = title;

//Añadir la sección de lista a la colección de secciones del documento Pdf
tocPage.TocInfo = tocInfo;
//Definir el formato de los cuatro niveles de lista configurando los márgenes izquierdos
//y
//configuraciones de formato de texto de cada nivel

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

//Crear una sección en el documento Pdf
Page page = doc.Pages.Add();

//Añadir cuatro encabezados en la sección
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "Encabezado de Muestra" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    //Añadir el encabezado en la Tabla de Contenidos.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// guardar el Pdf

doc.Save(outFile);
```
### Ocultar Números de Página en el TOC

En caso de que no desee mostrar los números de página, junto con los encabezados en el TOC, puede usar la propiedad [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) de la Clase [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) como false. Por favor, consulte el siguiente fragmento de código para ocultar los números de página en la tabla de contenidos:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Tabla de Contenidos");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
//Añadir la sección de lista a la colección de secciones del documento Pdf
tocPage.TocInfo = tocInfo;
//Definir el formato de los cuatro niveles de lista ajustando los márgenes izquierdos y
//configuraciones de formato de texto de cada nivel

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
//Añadir cuatro encabezados en la sección
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "este es un encabezado de nivel " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### Personalizar Números de Página al agregar TOC

Es común personalizar la numeración de páginas en el TOC al agregar un TOC en un documento PDF. Por ejemplo, podemos necesitar agregar algún prefijo antes del número de página como P1, P2, P3, etc. En tal caso, Aspose.PDF para .NET proporciona la propiedad PageNumbersPrefix de la clase TocInfo que se puede utilizar para personalizar los números de página como se muestra en el siguiente ejemplo de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// Cargar un archivo PDF existente
Document doc = new Document(inFile);
// Acceder a la primera página del archivo PDF
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// Crear objeto para representar la información de TOC
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Índice de Contenidos");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// Establecer el título para TOC
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i<doc.Pages.Count; i++)
{
    // Crear objeto Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // Especificar la página de destino para el objeto de encabezado
    heading2.DestinationPage = doc.Pages[i + 1];
    // Página de destino
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // Coordenada de destino
    segment2.Text = "Página " + i.ToString();
    // Agregar encabezado a la página que contiene TOC
    tocPage.Paragraphs.Add(heading2);
}

// Guardar el documento actualizado
doc.Save(outFile);
```
## Cómo establecer la fecha de caducidad del PDF

Aplicamos privilegios de acceso en archivos PDF para que un cierto grupo de usuarios pueda acceder a características/objetos particulares de documentos PDF. Con el fin de restringir el acceso al archivo PDF, generalmente aplicamos encriptación y podemos tener el requisito de establecer una fecha de caducidad del archivo PDF, de modo que el usuario que acceda/visualice el documento reciba un aviso válido respecto a la caducidad del archivo PDF.

Para lograr el requisito mencionado anteriormente, podemos usar el objeto *JavascriptAction*. Por favor, eche un vistazo al siguiente fragmento de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instanciar objeto Document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// Añadir página a la colección de páginas del archivo PDF
doc.Pages.Add();
// Añadir fragmento de texto a la colección de párrafos del objeto de página
doc.Pages[1].Paragraphs.Add(new TextFragment("Hola Mundo..."));
// Crear objeto JavaScript para establecer la fecha de caducidad del PDF
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('El archivo ha caducado. Necesitas uno nuevo.');");
// Establecer JavaScript como acción de apertura de PDF
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// Guardar documento PDF
doc.Save(dataDir);
```
## Determinar el Progreso de la Generación de Archivos PDF

Un cliente nos pidió agregar una característica que permita a los desarrolladores determinar el progreso de la generación de archivos PDF. Aquí está la respuesta a esa solicitud.

El campo [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) de la clase [DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) le permite determinar cómo va la generación del PDF. El manejador tiene los siguientes tipos:

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

Los fragmentos de código a continuación muestran cómo usar CustomerProgressHandler.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Progreso de conversión: {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - Página fuente {1} de {2} analizada.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Diseño de página resultado {1} de {2} creado.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Página resultado {1} de {2} exportada.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## Aplanar PDF Rellenable en C#

Los documentos PDF a menudo incluyen formularios con widgets rellenables interactivos como botones de radio, casillas de verificación, cajas de texto, listas, etc. Para hacerlo no editable para varios propósitos de aplicación, necesitamos aplanar el archivo PDF.
Aspose.PDF proporciona la función para aplanar tu PDF en C# con solo unas pocas líneas de código:

```csharp

// Cargar el formulario PDF fuente
Document doc = new Document(dataDir + "input.pdf");

// Aplanar PDF Rellenable
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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


