---
title: Usando Anotaciones de Texto para PDF
linktitle: Anotación de Texto
type: docs
weight: 10
url: /net/text-annotation/
description: Aspose.PDF para .NET te permite Agregar, Obtener y Eliminar Anotaciones de Texto de tu documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Usando Anotaciones de Texto para PDF",
    "alternativeHeadline": "Cómo agregar Anotaciones de Texto en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, anotación de texto",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET te permite Agregar, Obtener y Eliminar Anotaciones de Texto de tu documento PDF."
}
</script>
## Cómo agregar una anotación de texto en un archivo PDF existente

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Una Anotación de Texto es una anotación adjunta a una ubicación específica en un documento PDF. Cuando está cerrada, la anotación se muestra como un icono; cuando está abierta, debería mostrar una ventana emergente que contiene el texto de la nota en la fuente y tamaño elegidos por el lector.

Las anotaciones están contenidas por la colección [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) de una Página particular. Esta colección contiene las anotaciones para esa página individual solamente; cada página tiene su propia colección de Annotations.

Para agregar una anotación a una página en particular, añádela a la colección Annotations de esa página con el método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. Primero, crea una anotación que quieras agregar al PDF.
1. Luego abre el PDF de entrada.
1.
El siguiente fragmento de código muestra cómo agregar una anotación en una página PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// Crear anotación
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "Título de la Anotación de Ejemplo";
textAnnotation.Subject = "Asunto de Ejemplo";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "Contenidos de muestra para la anotación";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// Agregar anotación en la colección de anotaciones de la página
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// Guardar archivo de salida
pdfDocument.Save(dataDir);
```
## Cómo agregar Anotación Emergente

Una Anotación Emergente muestra texto en una ventana emergente para su entrada y edición. No debe aparecer sola sino que está asociada con una anotación de marcado, su anotación padre, y debe ser utilizada para editar el texto del padre.

No debe tener un flujo de apariencia ni acciones asociadas propias y debe ser identificada por la entrada Popup en el diccionario de anotaciones del padre.

El siguiente fragmento de código te muestra cómo agregar una [Anotación Emergente](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) en una página PDF usando un ejemplo de agregar una [Anotación de Línea](/pdf/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file) del padre.

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // La ruta al directorio de documentos.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // Cargar el archivo PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // Crear Anotación de Línea
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // Agregar anotación a la página
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## Cómo agregar (o crear) una nueva anotación de texto libre

Una anotación de texto libre muestra texto directamente en la página. El método [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) permite crear este tipo de anotación. En el siguiente fragmento, añadimos una anotación de texto libre sobre la primera aparición de la cadena.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Demostración de Texto Libre", 1); // el último parámetro es el número de página
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### Establecer propiedad de llamada para FreeTextAnnotation
### Establecer la Propiedad de Llamada para FreeTextAnnotation

Para una configuración más flexible de la anotación en el documento PDF, Aspose.PDF para .NET proporciona la propiedad [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) de la clase [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) que permite especificar un Array de puntos de la línea de llamada. El siguiente fragmento de código muestra cómo utilizar esta funcionalidad:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">Este es un ejemplo</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### Establecer Propiedad de Llamada para Archivo XFDF

Si usa importación desde archivo XFDF, por favor use el nombre de línea de llamada en lugar de solo Llamada. El siguiente fragmento de código muestra cómo usar esta funcionalidad:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

El siguiente método se utiliza para CrearXfdf:

```csharp
/// <summary>
/// Crear XFDF
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">Esto es una muestra</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### Hacer Invisible la Anotación de Texto Libre

A veces, es necesario crear una marca de agua que no sea visible en el documento al visualizarlo, pero que debería ser visible al imprimir el documento. Utiliza las banderas de anotación para este propósito. El siguiente fragmento de código muestra cómo hacerlo.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// Guardar archivo de salida
doc.Save(dataDir);
```
### Formato de FreeTextAnnotation

Esta parte examina cómo formatear el texto en una anotación de texto libre.

Las anotaciones están contenidas en la colección [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) de un objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Al agregar una [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) a un documento PDF, puede especificar la información de formato como la fuente, tamaño, color, etc., utilizando la clase [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index). También es posible especificar la información de formato usando la propiedad TextStyle. Además, puede actualizar el formato de cualquier FreeTextAnnotation ya en el documento PDF.

La clase [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) admite trabajar con la entrada de estilo predeterminado.
La clase [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) soporta trabajar con la entrada de estilo predeterminado.

- La propiedad FontName obtiene o establece el nombre de la fuente (cadena).
- La propiedad FontSize obtiene y establece el tamaño de texto predeterminado (doble).
- La propiedad System.Drawing.Color obtiene y establece el color del texto (color).
- La propiedad TextAlignment obtiene y establece la alineación del texto de la anotación (alineación).

El siguiente fragmento de código muestra cómo agregar una FreeTextAnnotation con un formato de texto específico.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

Cuando cambias el contenido o el estilo de texto de una anotación de texto libre, la apariencia de la anotación se regenera para reflejar los cambios.

{{% /alert %}}

### Tachar palabras usando StrikeOutAnnotation

Aspose.PDF para .NET te permite agregar, eliminar y actualizar anotaciones en documentos PDF.
Aspose.PDF para .NET le permite agregar, eliminar y actualizar anotaciones en documentos PDF.

Para tachar un TextFragment específico:

1. Buscar un TextFragment en el archivo PDF.
1. Obtener las coordenadas del objeto TextFragment.
1. Usar las coordenadas para instanciar un objeto StrikeOutAnnotation.

El siguiente fragmento de código muestra cómo buscar un TextFragment particular y agregar un StrikeOutAnnotation a ese objeto.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

Esta característica es compatible con la versión 19.6 o superior.

{{% /alert %}}

## Eliminar Todas las Anotaciones de una Página del Archivo PDF

La colección [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) de un objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) contiene todas las anotaciones de esa página en particular.
Una colección [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) de un objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) contiene todas las anotaciones de esa página en particular.

El siguiente fragmento de código te muestra cómo eliminar todas las anotaciones de una página en particular.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// Eliminar una anotación particular
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// Guardar documento actualizado
pdfDocument.Save(dataDir);
```

## Eliminar una anotación particular de un archivo PDF

{{% alert color="primary" %}}

Puedes verificar la calidad de Aspose.PDF y obtener los resultados en línea en este enlace:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF permite eliminar una Anotación específica de un archivo PDF. Este tema explica cómo hacerlo.

Para eliminar una anotación específica de un PDF, llama al método Delete de la [colección AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). Esta colección pertenece al objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). El método Delete requiere el índice de la anotación que deseas eliminar. Luego, guarda el archivo PDF actualizado. El siguiente fragmento de código muestra cómo eliminar una anotación específica.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// Eliminar anotación específica
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// Guardar documento actualizado
pdfDocument.Save(dataDir);
```
## Obtener Todas las Anotaciones de una Página de un Documento PDF

Aspose.PDF permite obtener anotaciones de un documento completo o de una página específica. Para obtener todas las anotaciones de una página en un documento PDF, recorra la colección [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) de los recursos de la página deseada. El siguiente fragmento de código muestra cómo obtener todas las anotaciones de una página.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// Recorrer todas las anotaciones
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // Obtener propiedades de la anotación
    Console.WriteLine("Título : {0} ", annotation.Title);
    Console.WriteLine("Asunto : {0} ", annotation.Subject);
    Console.WriteLine("Contenidos : {0} ", annotation.Contents);
}
```
Tenga en cuenta que para obtener todas las anotaciones de todo el PDF, debe recorrer la colección de la clase PageCollection del documento antes de navegar por la colección de la clase AnnotationCollection. Puede obtener cada anotación de la colección en un tipo de anotación base llamado clase MarkupAnnotation y luego mostrar sus propiedades.

## Obtener una Anotación Particular del Archivo PDF

Las anotaciones están asociadas con páginas individuales y se almacenan en la colección [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) del objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
Las anotaciones están asociadas con páginas individuales y almacenadas en la colección [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) de un objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// Obtener una anotación particular
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// Obtener propiedades de la anotación
Console.WriteLine("Title : {0} ", textAnnotation.Title);
Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
```

## Obtener Recurso de Anotación

Aspose.PDF permite obtener un recurso de anotación de un documento entero, o de una página dada.
Aspose.PDF le permite obtener un recurso de anotación de un documento completo o de una página dada.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document doc = new Document(dataDir + "AddAnnotation.pdf");
//Crear anotación
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// Guardar Documento
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Abrir documento
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

//Obtener acción de la anotación
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

//Obtener rendición de la acción de rendición
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

//Clip de medios
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
//Los datos de los medios están accesibles en FileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
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
Por supuesto, necesitaré ver el contenido del documento para poder traducirlo al español manteniendo el formato markdown original. Por favor, proporcione el texto o el fragmento del documento que necesita ser traducido.
