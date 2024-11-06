---
title: Anotación Multimedia PDF usando C#
linktitle: Anotación Multimedia
type: docs
weight: 40
url: es/net/multimedia-annotation/
description: Aspose.PDF para .NET te permite agregar, obtener y eliminar la anotación multimedia de tu documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotación Multimedia PDF usando C#",
    "alternativeHeadline": "Cómo agregar Anotación Multimedia en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, anotación multimedia, anotación en pantalla, anotación de sonido, anotación de widget, anotación 3D",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET te permite agregar, obtener y eliminar la anotación multimedia de tu documento PDF."
}
</script>

Las anotaciones en un documento PDF están contenidas en la colección de Anotaciones de un objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Esta colección contiene todas las anotaciones para esa página individual solamente: cada página tiene su propia colección de Anotaciones. Para agregar una anotación a una página en particular, agréguela a la colección de Anotaciones de esa página utilizando el método Add.

Utilice la clase [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) en el espacio de nombres Aspose.PDF.InteractiveFeatures.Annotations para incluir archivos SWF como anotaciones en un documento PDF en su lugar. Una anotación de pantalla especifica una región de una página sobre la cual se pueden reproducir clips de medios.

Cuando necesite agregar un enlace de video externo en el documento PDF, puede usar [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
Una Anotación de Película contiene gráficos animados y sonido para ser presentados en la pantalla del computador y a través de los altavoces.

Una [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) será análoga a una anotación de texto excepto que en lugar de una nota de texto, contiene sonido grabado desde el micrófono del computador o importado de un archivo.
Una [Anotación de Sonido](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) debe ser análoga a una anotación de texto, excepto que en lugar de una nota de texto, contiene sonido grabado desde el micrófono de la computadora o importado desde un archivo.

Sin embargo, cuando existe un requisito para incrustar medios dentro de un documento PDF, necesitas usar [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

Los siguientes métodos/propiedades de la clase RichMediaAnnotation pueden ser utilizados.

- Stream CustomPlayer { set; }: Permite establecer el reproductor utilizado para reproducir video.
- string CustomFlashVariables { set; }: Permite establecer variables que se pasan a la aplicación flash. Esta línea es un conjunto de pares "clave=valor" que están separados con '&'.
- void AddCustomData(strig name, Stream data): Agrega datos adicionales para el reproductor. Por ejemplo, source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: El evento activa el reproductor; los valores posibles son Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Establece datos de video/audio para ser reproducidos.
- void SetContent(Stream stream, string name): Establecer datos de vídeo/audio para ser reproducidos.
- void Update(): Crear una estructura de datos de la anotación. Este método debe ser llamado al final.
- void SetPoster(Stream): Establecer el póster del video, es decir, la imagen mostrada cuando el reproductor no está activo.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Añadir Anotación de Pantalla

El siguiente fragmento de código muestra cómo añadir una Anotación de Pantalla a un archivo PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // La ruta al directorio de documentos.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // Cargar el archivo PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // Crear Anotación de Pantalla
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## Añadir Anotación de Sonido

El siguiente fragmento de código muestra cómo añadir una Anotación de Sonido a un archivo PDF:

```csharp
        public static void AddSoundAnnotation()
        {
            // Cargar el archivo PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // Crear Anotación de Sonido
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "Demostración de Anotación de Sonido",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## Añadir RichMediaAnnotation

El siguiente fragmento de código muestra cómo añadir RichMediaAnnotation a un archivo PDF:
El siguiente fragmento de código muestra cómo agregar RichMediaAnnotation a un archivo PDF:

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //dar nombre a los datos del video. Estos datos se incrustarán en el documento con este nombre y se harán referencia desde las variables flash por este nombre.
            //videoName no debe contener la ruta al archivo; esto es más bien una "clave" para acceder a los datos dentro del documento PDF
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //también usamos un skin para el reproductor de video
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //aquí debemos especificar el stream que contiene el código del reproductor de video
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //componer la línea de variables flash para el reproductor. tenga en cuenta que diferentes reproductores pueden tener diferentes formatos de la línea de variables flash. Consulte la documentación de su reproductor.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //agregar código de skin.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //establecer póster para el video
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //establecer contenido de video
            rma.SetContent(videoName, fs);

            //establecer tipo del contenido (video)
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //activar reproductor al hacer clic
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //actualizar datos de la anotación. Este método debe ser llamado después de todas las asignaciones/configuraciones. Este método inicializa la estructura de datos de la anotación e incrusta los datos requeridos.
            rma.Update();

            //agregar anotación en la página.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### Obtener MultimediaAnnotation

Por favor, intenta utilizar el siguiente fragmento de código para obtener MultimediaAnnotation de un documento PDF.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // Cargar el archivo PDF
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### Eliminar MultimediaAnnotation

El siguiente fragmento de código muestra cómo eliminar MultimediaAnnotation de un archivo PDF.

```csharp
        public static void DeletePolyAnnotation()
        {
            // Cargar el archivo PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```
## Agregar Anotaciones de Widget

Los formularios interactivos utilizan [Anotaciones de Widget](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) para representar la apariencia de los campos y para gestionar las interacciones del usuario.
Utilizamos estos elementos de formulario que se agregan a un PDF para facilitar la entrada, el envío de información o realizar alguna otra interacción del usuario.

Las Anotaciones de Widget son una representación gráfica de un campo de formulario en páginas específicas, por lo que no podemos crearlas directamente como una anotación.

Cada Anotación de Widget tendrá gráficos apropiados (apariencia) dependiendo de su tipo. Después de la creación, ciertos aspectos visuales pueden cambiarse, como el estilo del borde y el color de fondo.
Otras propiedades como el color del texto y la fuente pueden cambiarse a través del campo, una vez adjunto a uno.

En algunos casos, es posible que desees que un campo aparezca en más de una página, repitiendo el mismo valor.
En algunos casos, es posible que desee que un campo aparezca en más de una página, repitiendo el mismo valor.
Alguien que llene el formulario puede usar cualquiera de esos widgets para actualizar el valor del campo, y esto se refleja en todos los demás widgets también.

Cada campo del formulario para cada lugar en el documento representa una Anotación de Widget. Los datos específicos de la ubicación de la Anotación de Widget se agregan a la página particular. Cada campo del formulario tiene varias variaciones. Un botón puede ser un botón de radio, una casilla de verificación o un botón de pulsación. Un widget de elección puede ser un cuadro de lista o un cuadro combinado.

En este ejemplo, aprenderemos cómo agregar los botones de navegación en el documento.

### Añadir botón al documento

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "Imprimir documento actual",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "Imprimir documento"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
Este botón tiene borde y establece un fondo. También configuramos un nombre de botón (Nombre), un tooltip (NombreAlternativo), una etiqueta (LeyendaNormal) y un color del texto de la etiqueta (Color).

### Usando acciones de navegación de documentos

Existe un ejemplo más complejo del uso de Anotaciones de Widget - navegación de documentos en un documento PDF. Esto puede ser necesario para preparar una presentación de documentos PDF.

Este ejemplo muestra cómo crear 4 botones:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "Ir a la primera página", "Ir a la página anterior", "Ir a la siguiente página", "Ir a la última página" };
var normalCaptions = new[] { "Primera", "Anterior", "Siguiente", "Última" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

Deberíamos crear los botones sin adjuntarlos a la página.
Deberíamos crear los botones sin adjuntarlos a la página.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

Deberíamos duplicar este arreglo de botones en cada página del documento.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

Llamamos al [método Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) con los siguientes parámetros: campo, nombre y el índice de las páginas a las que se añadirá este campo.
Llamamos al [método Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) con los siguientes parámetros: campo, nombre e índice de las páginas donde se añadirá este campo.

Y para obtener el resultado completo, necesitamos desactivar los botones "First" y "Prev" en la primera página y los botones "Next" y "Last" en la última página.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

Para obtener más información detallada y posibilidades de estas características, consulte también [Trabajando con Formularios](/pdf/net/acroforms/).

En documentos PDF, puedes ver y gestionar contenido 3D de alta calidad creado con software CAD 3D o de modelado 3D e incrustado en el documento PDF. Puedes rotar elementos 3D en todas las direcciones como si los tuvieras en tus manos.

¿Por qué necesitas en absoluto una visualización 3D de imágenes?

En los últimos años, la tecnología ha logrado enormes avances en todas las áreas gracias a la impresión 3D.
En los últimos años, la tecnología ha logrado enormes avances en todas las áreas gracias a la impresión 3D.
y profesores.

La tarea principal de la modelación 3D es la idea de un objeto futuro o un objeto porque, para liberar un objeto, se necesita una comprensión de sus características de diseño en todo detalle para la regeneración sucesiva en diseño industrial o arquitectura.

## Añadir Anotación 3D

La anotación 3D se añade utilizando un modelo creado en formato U3D.

1. Crear un nuevo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Cargar los datos del modelo 3D deseado (en nuestro caso "Ring.u3d") para crear [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)
1. Crear objeto [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) y vincularlo al documento y 3DContent
1. Ajustar objeto pdf3dArtWork:

    - 3DLightingScheme - (estableceremos `CAD` en el ejemplo)
    - 3DRenderMode - (estableceremos `Solid` en el ejemplo)
    - Llenar `ViewArray`, crear al menos una [Vista 3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) y añadirla al array.
- Rellenar `ViewArray`, crear al menos una [Vista 3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) y añadirla al array.

1. Establecer 3 parámetros básicos en la anotación:
    - la `página` en la que se colocará la anotación,
    - el `rectángulo`, dentro del cual la anotación,
    - y el objeto `3dArtWork`.
1. Para una mejor presentación del objeto 3D, establecer el marco del borde
1. Establecer la vista predeterminada (por ejemplo - TOP)
1. Añadir algunos parámetros adicionales: nombre, póster de vista previa, etc.
1. Añadir Anotación a la [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. Guardar el resultado

### Ejemplo

Por favor, revise el siguiente fragmento de código para añadir una Anotación 3D.

```csharp
    public static void Add3dAnnotation()
    {
    // Cargar el archivo PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Name = "Ring.u3d";
    //establecer imagen de vista previa si es necesario
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
Este ejemplo de código nos mostró un modelo así:

![Demostración de anotación 3D](3d_demo.png)

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

