---
title: Trabajando con Acciones en PDF
linktitle: Acciones
type: docs
weight: 20
url: /net/actions/
description: Esta sección explica cómo agregar acciones al documento y a los campos de formulario programáticamente con C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Acciones en PDF",
    "alternativeHeadline": "Cómo agregar Acciones en PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, acciones en pdf",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección explica cómo agregar acciones al documento y a los campos de formulario programáticamente con C#."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Añadir Hipervínculo en un Archivo PDF

Es posible añadir hipervínculos a archivos PDF, ya sea para permitir a los lectores navegar a otra parte del PDF o a contenido externo.

Para añadir hipervínculos web a documentos PDF:

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Obtener la clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la que quieres añadir el enlace.
1. Crear un objeto [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) usando los objetos Page y [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle). El objeto rectángulo se utiliza para especificar la ubicación en la página donde se debe añadir el enlace.
1. Establecer la propiedad Action al objeto [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) que especifica la ubicación del URI remoto.
1. Para agregar un texto libre:

- Instancia un objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation). También acepta objetos Page y Rectangle como argumento, por lo que es posible proporcionar los mismos valores que se especifican contra el constructor de LinkAnnotation.
- Utilizando la propiedad Contents del objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), especifica la cadena que debe mostrarse en el PDF de salida.
- Opcionalmente, establece el ancho del borde de los objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) y FreeTextAnnotation a 0 para que no aparezcan en el documento PDF.
- Una vez que se hayan definido los objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) y [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), agrega estos enlaces a la colección de Anotaciones del objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Una vez que se han definido los objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) y [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), añade estos enlaces a la colección de Anotaciones del objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Finalmente, guarda el PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

El siguiente fragmento de código muestra cómo añadir un hipervínculo a un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Abrir documento
Document document = new Document(dataDir + "AddHyperlink.pdf");
// Crear página
Page page = document.Pages[1];
// Crear objeto de anotación de enlace
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// Crear objeto de borde para LinkAnnotation
Border border = new Border(link);
// Establecer el valor de ancho del borde como 0
border.Width = 0;
// Establecer el borde para LinkAnnotation
link.Border = border;
// Especificar el tipo de enlace como URI remoto
link.Action = new GoToURIAction("www.aspose.com");
// Añadir anotación de enlace a la colección de anotaciones de la primera página del archivo PDF
page.Annotations.Add(link);

// Crear anotación de texto libre
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// Cadena a añadir como texto libre
textAnnotation.Contents = "Enlace al sitio web de Aspose";
// Establecer el borde para la anotación de texto libre
textAnnotation.Border = border;
// Añadir anotación de texto libre a la colección de anotaciones de la primera página del documento
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// Guardar documento actualizado
document.Save(dataDir);
```
## Crear un hipervínculo a páginas en el mismo PDF

Aspose.PDF para .NET ofrece una excelente característica para la creación de PDF así como su manipulación. También ofrece la característica de añadir enlaces a páginas de PDF y un enlace puede dirigirse a páginas en otro archivo PDF, una URL web, enlace para lanzar una aplicación o incluso enlace a páginas en el mismo archivo PDF. Para agregar hipervínculos locales (enlaces a páginas en el mismo archivo PDF), se añade una clase llamada [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) al espacio de nombres de Aspose.PDF y esta clase tiene una propiedad llamada TargetPageNumber, que se utiliza para especificar la página de destino para el hipervínculo.

Para agregar el hipervínculo local, necesitamos crear un TextFragment para que el enlace pueda asociarse con el TextFragment. La clase [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) tiene una propiedad llamada Hyperlink que se utiliza para asociar la instancia de LocalHyperlink. El siguiente fragmento de código muestra los pasos para lograr este requisito.

```csharp
```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Crear instancia de Documento
Document doc = new Document();
// Añadir página a la colección de páginas del archivo PDF
Page page = doc.Pages.Add();
// Crear instancia de Fragmento de Texto
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("prueba de número de página de enlace a la página 7");
// Crear instancia de hipervínculo local
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// Establecer la página objetivo para la instancia de enlace
link.TargetPageNumber = 7;
// Establecer hipervínculo para TextFragment
text.Hyperlink = link;
// Añadir texto a la colección de párrafos de la Página
page.Paragraphs.Add(text);
// Crear nueva instancia de TextFragment
text = new TextFragment("prueba de número de página de enlace a la página 1");
// TextFragment debe ser añadido sobre nueva página
text.IsInNewPage = true;
// Crear otra instancia de hipervínculo local
link = new LocalHyperlink();
// Establecer página objetivo para el segundo hipervínculo
link.TargetPageNumber = 1;
// Establecer enlace para el segundo TextFragment
text.Hyperlink = link;
// Añadir texto a la colección de párrafos del objeto de página
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
```
## Obtener el destino del hipervínculo (URL) de un PDF

Los enlaces están representados como anotaciones en un archivo PDF y pueden ser añadidos, actualizados o eliminados. Aspose.PDF para .NET también admite obtener el destino (URL) del hipervínculo en un archivo PDF.

Para obtener la URL de un enlace:

1. Crea un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Obtén la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) de la que deseas extraer los enlaces.
3. Usa la clase [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) para extraer todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) de la página especificada.
4. Pasa el objeto [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) al método Accept del objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Finalmente, extraiga la acción de LinkAnnotation como GoToURIAction.

El siguiente fragmento de código muestra cómo obtener destinos de hipervínculos (URL) de un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Cargar el archivo PDF
Document document = new Document(dataDir + "input.pdf");

// Recorrer todas las páginas del PDF
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // Obtener las anotaciones de enlace de una página en particular
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // Crear lista que contiene todos los enlaces
    IList<Annotation> list = selector.Selected;
    // Iterar a través de cada elemento dentro de la lista
    foreach (LinkAnnotation a in list)
    {
        // Imprimir la URL de destino
        Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## Obtener el Texto del Hipervínculo

Un hipervínculo tiene dos partes: el texto que se muestra en el documento y la URL de destino. En algunos casos, es el texto y no la URL lo que necesitamos.

El texto y las anotaciones/acciones en un archivo PDF están representados por diferentes entidades. El texto en una página es solo un conjunto de palabras y caracteres, mientras que las anotaciones aportan cierta interactividad, como la inherente en un hipervínculo.

Para encontrar el contenido de la URL, necesitas trabajar tanto con la anotación como con el texto. El objeto [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) no tiene el texto en sí, pero se sitúa debajo del texto en la página. Por lo tanto, para obtener el texto, la Anotación proporciona los límites de la URL, mientras que el objeto Texto proporciona los contenidos de la URL. Por favor, consulta el siguiente fragmento de código.

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // La ruta al directorio de documentos.
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // Cargar el archivo PDF
                Document document = new Document(dataDir + "input.pdf");
                // Iterar a través de cada página del PDF
                foreach (Page page in document.Pages)
                {
                    // Mostrar anotación de enlace
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // Imprimir la URL de cada Anotación de Enlace
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // Imprimir el texto asociado con el hipervínculo
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## Eliminar la Acción de Abrir Documento de un Archivo PDF

[Cómo Especificar la Página del PDF al Visualizar el Documento](#how-to-specify-pdf-page-when-viewing-document) explicó cómo indicar que un documento se abra en una página diferente a la primera. Al concatenar varios documentos, y uno o más tienen establecida una acción GoTo, probablemente quieras eliminarlas. Por ejemplo, si combinas dos documentos y el segundo tiene una acción GoTo que te lleva a la segunda página, el documento resultante se abrirá en la segunda página del segundo documento en lugar de en la primera página del documento combinado. Para evitar este comportamiento, elimina el comando de acción de apertura.

Para eliminar una acción de apertura:

1. Establece la propiedad [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) a null.
1. Guarda el PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) del objeto Document.

El siguiente fragmento de código muestra cómo eliminar una acción de abrir documento del archivo PDF.
El siguiente fragmento de código muestra cómo eliminar una acción de apertura de documentos de un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Abrir documento
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// Eliminar la acción de apertura del documento
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// Guardar el documento actualizado
document.Save(dataDir);
```

## Cómo especificar la página PDF al visualizar el documento {#how-to-specify-pdf-page-when-viewing-document}

Al visualizar archivos PDF en un visor de PDF como Adobe Reader, los archivos generalmente se abren en la primera página. Sin embargo, es posible configurar el archivo para que se abra en una página diferente.

La clase [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) le permite especificar una página en un archivo PDF que desea abrir.
La clase [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) te permite especificar una página en un archivo PDF que deseas abrir.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Cargar el archivo PDF
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// Obtener la instancia de la segunda página del documento
Page page2 = doc.Pages[2];
// Crear la variable para establecer el factor de zoom de la página objetivo
double zoom = 1;
// Crear una instancia de GoToAction
GoToAction action = new GoToAction(doc.Pages[2]);
// Ir a la página 2
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// Establecer la acción de apertura del documento
doc.OpenAction = action;
// Guardar el documento actualizado
doc.Save(dataDir + "goto2page_out.pdf");
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


