---
title: Formateo de Documentos PDF usando C#
linktitle: Formateo de Documentos PDF
type: docs
weight: 11
url: /net/formatting-pdf-document/
description: Crea y formatea el Documento PDF con Aspose.PDF para .NET. Utiliza el siguiente fragmento de código para resolver tus tareas.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formateo de Documentos PDF usando C#",
    "alternativeHeadline": "Cómo formatear un Documento PDF en .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, dotnet, formatear documento pdf",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Crea y formatea el Documento PDF con Aspose.PDF para .NET. Utiliza el siguiente fragmento de código para resolver tus tareas."
}
</script>
## Formateo de Documento PDF

### Obtener Propiedades de la Ventana del Documento y de Visualización de Páginas

Este tema te ayuda a entender cómo obtener propiedades de la ventana del documento, la aplicación de visualización y cómo se muestran las páginas. Para establecer estas propiedades:

Abre el archivo PDF utilizando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Ahora, puedes configurar las propiedades del objeto Document, tales como

- CenterWindow – Centra la ventana del documento en la pantalla. Predeterminado: false.
- Direction – Orden de lectura. Esto determina cómo se disponen las páginas cuando se muestran lado a lado. Predeterminado: de izquierda a derecha.
- DisplayDocTitle – Muestra el título del documento en la barra de título de la ventana del documento. Predeterminado: false (el título se muestra).
- HideMenuBar – Oculta o muestra la barra de menú de la ventana del documento. Predeterminado: false (la barra de menú se muestra).
- HideToolBar – Oculta o muestra la barra de herramientas de la ventana del documento. Predeterminado: false (la barra de herramientas se muestra).
- HideWindowUI – Oculta o muestra elementos de la ventana del documento como las barras de desplazamiento. Predeterminado: false (los elementos de la ventana se muestran).
- HideWindowUI – Ocultar o mostrar elementos de la ventana del documento como barras de desplazamiento.
- NonFullScreenPageMode – Cómo se muestra el documento cuando no está en modo de página completa.
- PageLayout – El diseño de la página.
- PageMode – Cómo se muestra el documento cuando se abre por primera vez. Las opciones son mostrar miniaturas, pantalla completa, mostrar panel de adjuntos.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente fragmento de código muestra cómo obtener las propiedades usando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// Obtener diferentes propiedades del documento
// Posición de la ventana del documento - Predeterminado: false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);
  
// Orden de lectura predominante; determina la posición de la página
// Cuando se muestra lado a lado - Predeterminado: L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// Si la barra de título de la ventana debe mostrar el título del documento
// Si es falso, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// Si redimensionar la ventana del documento para ajustarse al tamaño de
// La primera página mostrada - Predeterminado: false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// Si ocultar la barra de menú de la aplicación visor - Predeterminado: false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// Si ocultar la barra de herramientas de la aplicación visor - Predeterminado: false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// Si ocultar elementos de la interfaz de usuario como barras de desplazamiento
// Y dejar solo los contenidos de la página mostrados - Predeterminado: false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// Modo de página del documento. Cómo mostrar el documento al salir del modo de pantalla completa.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// El diseño de página, es decir, página única, una columna
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// Cómo debería mostrarse el documento cuando se abre
// Es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### Establecer las Propiedades de la Ventana del Documento y la Visualización de Página

Este tema explica cómo establecer las propiedades de la ventana del documento, la aplicación de visualización y la visualización de página. Para configurar estas diferentes propiedades:

1. Abre el archivo PDF utilizando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Establece las propiedades del objeto Document.
1. Guarda el archivo PDF actualizado utilizando el método Save.

Las propiedades disponibles son:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Cada una se utiliza y se describe en el código a continuación. El siguiente fragmento de código te muestra cómo establecer las propiedades utilizando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// Establecer diferentes propiedades del documento
// Especificar para posicionar la ventana del documento - Predeterminado: false
pdfDocument.CenterWindow = true;

// Orden de lectura predominante; determina la posición de la página
// Cuando se muestra lado a lado - Predeterminado: L2R
pdfDocument.Direction = Direction.R2L;

// Especificar si la barra de título de la ventana debe mostrar el título del documento
// Si es falso, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
pdfDocument.DisplayDocTitle = true;

// Especificar si redimensionar la ventana del documento para ajustar el tamaño de
// La primera página mostrada - Predeterminado: false
pdfDocument.FitWindow = true;

// Especificar si ocultar la barra de menú de la aplicación de visualización - Predeterminado: false
pdfDocument.HideMenubar = true;

// Especificar si ocultar la barra de herramientas de la aplicación de visualización - Predeterminado: false
pdfDocument.HideToolBar = true;

// Especificar si ocultar elementos de la interfaz de usuario como barras de desplazamiento
// Y dejar solo los contenidos de la página mostrados - Predeterminado: false
pdfDocument.HideWindowUI = true;

// Modo de página del documento. especificar cómo mostrar el documento al salir del modo de pantalla completa.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// Especificar el diseño de página, es decir, página única, una columna
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// Especificar cómo se debe mostrar el documento al abrirse
// Es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// Guardar archivo PDF actualizado
pdfDocument.Save(dataDir);
```
### Incrustación de fuentes en un archivo PDF existente

Los lectores de PDF admiten [un núcleo de 14 fuentes](https://en.wikipedia.org/wiki/PDF#Text) para que los documentos se muestren de la misma manera, independientemente de la plataforma en la que se visualice el documento. Cuando un PDF contiene una fuente que no es una de las 14 fuentes principales, incrusta la fuente en el archivo PDF para evitar la sustitución de fuentes.

Aspose.PDF para .NET admite la incrustación de fuentes en archivos PDF existentes. Puedes incrustar una fuente completa o un subconjunto de la fuente. Para incrustar la fuente, abre el archivo PDF utilizando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Luego usa la clase [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) para incrustar la fuente en el archivo PDF. Para incrustar la fuente completa, usa la propiedad IsEmbeded de la clase Font; para usar un subconjunto de la fuente, usa la propiedad IsSubset.

{{% alert color="primary" %}}

Un subconjunto de fuente incrusta solo los caracteres que se utilizan y es útil donde las fuentes se usan para frases cortas o eslóganes, por ejemplo, donde una fuente corporativa se usa para un logotipo, pero no para el texto principal.
Un subconjunto de fuentes incrusta solo los caracteres que se utilizan y es útil donde las fuentes se utilizan para frases cortas o lemas, por ejemplo, donde una fuente corporativa se utiliza para un logotipo, pero no para el texto principal.

{{% /alert %}}

El siguiente fragmento de código muestra cómo incrustar una fuente en un archivo PDF.

### Incrustando Fuentes Estándar Tipo 1

Algunos documentos PDF tienen fuentes de un conjunto especial de fuentes de Adobe. Las fuentes de este conjunto se denominan "Fuentes Estándar Tipo 1". Este conjunto incluye 14 fuentes y la incrustación de este tipo de fuentes requiere el uso de banderas especiales, es decir [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). A continuación se muestra el fragmento de código que se puede utilizar para obtener un documento con todas las fuentes incrustadas, incluidas las Fuentes Estándar Tipo 1:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Cargar un Documento PDF existente
Document pdfDocument = new Document(dataDir + "input.pdf");
// Establecer la propiedad EmbedStandardFonts del documento
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// Comprobar si la fuente ya está incrustada
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### Incrustación de fuentes al crear PDF

Si necesita usar una fuente que no sea una de las 14 fuentes básicas que admite Adobe Reader, debe incrustar la descripción de la fuente al generar el archivo Pdf. Si la información de la fuente no está incrustada, Adobe Reader la tomará del Sistema Operativo si está instalada en el sistema, o construirá una fuente sustituta de acuerdo con el descriptor de la fuente en el Pdf.

>Tenga en cuenta que la fuente incrustada debe estar instalada en la máquina host, es decir, en el caso del siguiente código, la fuente 'Univers Condensed' está instalada en el sistema.

Usamos la propiedad IsEmbedded de la clase Font para incrustar la información de la fuente en el archivo Pdf. Establecer el valor de esta propiedad en 'True' incrustará el archivo de fuente completo en el Pdf, sabiendo el hecho de que aumentará el tamaño del archivo Pdf. A continuación se muestra el fragmento de código que se puede usar para incrustar la información de la fuente en Pdf.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instanciar el objeto Pdf llamando a su constructor vacío
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// Crear una sección en el objeto Pdf
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" Este es un texto de muestra usando fuente personalizada.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// Guardar documento PDF
doc.Save(dataDir);
```
### Establecer el Nombre de la Fuente Predeterminada al Guardar PDF

Cuando un documento PDF contiene fuentes que no están disponibles en el documento mismo ni en el dispositivo, la API reemplaza estas fuentes con la fuente predeterminada. Cuando la fuente está disponible (está instalada en el dispositivo o está incrustada en el documento), el PDF resultante debería tener la misma fuente (no debería ser reemplazada por la fuente predeterminada). El valor de la fuente predeterminada debe contener el nombre de la fuente (no la ruta a los archivos de la fuente). Hemos implementado una característica para establecer el nombre de la fuente predeterminada al guardar un documento como PDF. El siguiente fragmento de código se puede utilizar para establecer la fuente predeterminada:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Cargar un documento PDF existente con fuente faltante
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // Especificar el Nombre de la Fuente Predeterminada
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### Obtener Todas las Fuentes de un Documento PDF

En caso de que quieras obtener todas las fuentes de un documento PDF, puedes utilizar el método FontUtilities.GetAllFonts() proporcionado en la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Por favor, revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### Obtener Advertencias para la Sustitución de Fuentes

Aspose.PDF para .NET proporciona métodos para obtener notificaciones sobre la sustitución de fuentes para manejar casos de sustitución de fuentes. Los fragmentos de código a continuación muestran cómo usar la funcionalidad correspondiente.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
El método **OnFontSubstitution** se enumera a continuación.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Console.WriteLine(string.Format("La fuente '{0}' fue sustituida por otra fuente '{1}'",
oldFont.FontName, newFont.FontName));
```

### Mejorar la incrustación de fuentes utilizando FontSubsetStrategy

La característica de incrustar las fuentes como un subconjunto se puede lograr utilizando la propiedad IsSubset, pero a veces deseas reducir un conjunto de fuentes completamente incrustado a solo los subconjuntos que se utilizan en el documento. Aspose.Pdf.Document tiene la propiedad FontUtilities que incluye el método SubsetFonts(FontSubsetStrategy subsetStrategy). En el método SubsetFonts(), el parámetro subsetStrategy ayuda a ajustar la estrategia de subconjunto. FontSubsetStrategy admite las siguientes dos variantes de subconjunto de fuentes.

- SubsetAllFonts - Esto subconjuntará todas las fuentes, usadas en un documento.
- SubsetEmbeddedFontsOnly - Esto subconjuntará solo aquellas fuentes que están completamente incrustadas en el documento.

El siguiente fragmento de código muestra cómo establecer FontSubsetStrategy:
### Configurar la Estrategia de Subconjunto de Fuentes

El siguiente fragmento de código muestra cómo configurar FontSubsetStrategy:

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// Todas las fuentes se incrustarán como subconjunto en el documento en caso de SubsetAllFonts.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// El subconjunto de fuentes se incrustará para las fuentes completamente incrustadas, pero las fuentes que no están incrustadas en el documento no se verán afectadas.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### Obtener y Establecer el Factor de Zoom de un Archivo PDF

A veces, deseas determinar cuál es el factor de zoom actual de un documento PDF. Con Aspose.Pdf, puedes descubrir el valor actual y configurar uno.

La propiedad Destination de la clase [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) te permite obtener el valor de zoom asociado con un archivo PDF.
La propiedad Destination de la clase [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) te permite obtener el valor de zoom asociado con un archivo PDF.

#### Establecer factor de Zoom

El siguiente fragmento de código muestra cómo establecer el factor de zoom de un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor ir a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// El camino al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instanciar nuevo objeto Document
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// Guardar el documento
doc.Save(dataDir);
```

#### Obtener factor de Zoom

El siguiente fragmento de código muestra cómo obtener el factor de zoom de un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor ir a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// El camino al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instanciar nuevo objeto Document
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// Crear objeto GoToAction
GoToAction action = doc.OpenAction as GoToAction;

// Obtener el factor de Zoom del archivo PDF
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // Valor de zoom del documento;
```
### Configuración de Propiedades Preestablecidas del Diálogo de Impresión

Aspoose.PDF permite configurar las propiedades preestablecidas del diálogo de impresión de un documento PDF. Te permite cambiar la propiedad DuplexMode de un documento PDF que está configurada por defecto en simplex. Esto se puede lograr utilizando dos metodologías diferentes como se muestra a continuación.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### Configuración de Propiedades Preestablecidas del Diálogo de Impresión usando Editor de Contenido PDF

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("El archivo tiene doble cara en el borde corto");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
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

