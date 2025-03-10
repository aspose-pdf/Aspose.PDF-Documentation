---
title: Anotación Multimedia en PDF usando C#
linktitle: Anotación Multimedia
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/multimedia-annotation/
description: Aspose.PDF for .NET te permite agregar, obtener y eliminar la anotación multimedia de tu documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Multimedia Annotation using C#",
    "alternativeHeadline": "Enable Multimedia Annotations in PDF with C#",
    "abstract": "Aspose.PDF for .NET introduce capacidades avanzadas de anotación multimedia, permitiendo a los usuarios agregar, recuperar y eliminar sin problemas varios tipos de multimedia en documentos PDF. Esta función admite anotaciones de pantalla, sonido y medios enriquecidos, mejorando la interactividad del documento y permitiendo la integración de contenido de video externo, notas de audio y medios incrustados, haciendo que los documentos PDF sean más dinámicos y atractivos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF multimedia annotation, Aspose.PDF, C# PDF features, screen annotation, sound annotation, rich media annotation, widget annotations, 3D annotation, document navigation, multimedia file embedding",
    "wordcount": "2247",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también enfrentar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

Las anotaciones en un documento PDF se encuentran en la colección Annotations de un objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Esta colección contiene todas las anotaciones para esa página individual solamente: cada página tiene su propia colección de Annotations. Para agregar una anotación a una página en particular, agrégala a la colección Annotations de esa página utilizando el método Add.

Utiliza la clase [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) en el espacio de nombres Aspose.PDF.InteractiveFeatures.Annotations para incluir archivos SWF como anotaciones en un documento PDF. Una anotación de pantalla especifica una región de una página sobre la cual se pueden reproducir clips multimedia.

Cuando necesites agregar un enlace de video externo en el documento PDF, puedes usar [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
Una Anotación de Película contiene gráficos animados y sonido que se presentarán en la pantalla de la computadora y a través de los altavoces.

Una [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) es análoga a una anotación de texto, excepto que en lugar de una nota de texto, contiene sonido grabado desde el micrófono de la computadora o importado desde un archivo. Cuando se activa la anotación, se reproducirá el sonido. La anotación se comportará como una anotación de texto en la mayoría de los aspectos, con un ícono diferente (por defecto, un altavoz) para indicar que representa un sonido.

Sin embargo, cuando hay un requisito para incrustar medios dentro del documento PDF, necesitas usar [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

Los siguientes métodos/properties de la clase RichMediaAnnotation pueden ser utilizados.

- Stream CustomPlayer { set; }: Permite establecer el reproductor utilizado para reproducir video.
- string CustomFlashVariables { set; }: Permite establecer variables que se pasan a la aplicación flash. Esta línea es un conjunto de pares “clave=valor” que están separados por ‘&'.
- void AddCustomData(strig name, Stream data): Agregar datos adicionales para el reproductor. Por ejemplo source=video.mp4&autoPlay=true&scale=100.
- ActivationEvent ActivateOn { get; set}: El evento activa el reproductor; los valores posibles son Click, PageOpen, PageVisible.
- void SetContent(Stream stream, string name): Establecer datos de video/audio a reproducir.
- void Update(): Crear una estructura de datos de la anotación. Este método debe ser llamado al final.
- void SetPoster(Stream): Establecer el póster del video, es decir, la imagen mostrada cuando el reproductor no está activo.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Agregar Anotación de Pantalla

El siguiente fragmento de código muestra cómo agregar una Anotación de Pantalla a un archivo PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddScreenAnnotationWithMedia()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (cument = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Path to the media file (SWF)
        var mediaFile = dataDir + "input.swf";

        // Create Screen Annotation
        var screenAnnotation = new Aspose.Pdf.Annotations.ScreenAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(170, 190, 470, 380),
            mediaFile);

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(screenAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddScreenAnnotationWithMedia_out.pdf");
    }
}
```

## Agregar Anotación de Sonido

El siguiente fragmento de código muestra cómo agregar una Anotación de Sonido a un archivo PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSoundAnnotation()
{
    // Open PDF document
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        var mediaFile = dataDir + "file_example_WAV_1MG.wav";

        // Create Sound Annotation
        var soundAnnotation = new Aspose.Pdf.Annotations.SoundAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(20, 700, 60, 740),
            mediaFile)
        {
            Color = Aspose.Pdf.Color.Blue,
            Title = "John Smith",
            Subject = "Sound Annotation demo",
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(20, 700, 60, 740))
        };

        document.Pages[1].Annotations.Add(soundAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddSoundAnnotation_out.pdf");
    }
}
```

## Agregar RichMediaAnnotation

El siguiente fragmento de código muestra cómo agregar RichMediaAnnotation a un archivo PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRichMediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
        Page page = document.Pages.Add();

        // Define video and poster names
        const string videoName = "file_example_MP4_480_1_5MG.mp4";
        const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        string skinName = "SkinOverAllNoFullNoCaption.swf";

        // Create RichMediaAnnotation
        var rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600));

        // Specify the stream containing the video player code
        rma.CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp, "Players", "Videoplayer.swf"), FileMode.Open, FileAccess.Read);

        // Compose flash variables line for the player
        rma.CustomFlashVariables = $"source={videoName}&skin={skinName}";

        // Add skin code
        rma.AddCustomData(skinName, new FileStream(Path.Combine(pathToAdobeApp, skinName), FileMode.Open, FileAccess.Read));

        // Set poster for the video
        rma.SetPoster(new FileStream(Path.Combine(dataDir, posterName), FileMode.Open, FileAccess.Read));

        // Set video content
        using (Stream fs = new FileStream(Path.Combine(dataDir, videoName), FileMode.Open, FileAccess.Read))
        {
            rma.SetContent(videoName, fs);
        }

        // Set type of the content (video)
        rma.Type = RichMediaAnnotation.ContentType.Video;

        // Activate player by click
        rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

        // Update annotation data
        rma.Update();

        // Add annotation to the page
        page.Annotations.Add(rma);

        // Save PDF document
        document.Save(dataDir + "RichMediaAnnotation_out.pdf");
    }
}
```

### Obtener MultimediaAnnotation

Por favor, intenta usar el siguiente fragmento de código para Obtener MultimediaAnnotation del documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMultimediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get multimedia annotations (Screen, Sound, RichMedia)
        var mediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Screen
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Sound
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.Annotation>();

        // Iterate through the annotations and print their details
        foreach (var ma in mediaAnnotations)
        {
            Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
        }
    }
}
```

### Eliminar MultimediaAnnotation

El siguiente fragmento de código muestra cómo Eliminar MultimediaAnnotation de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolyAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get RichMedia annotations
        var richMediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.RichMediaAnnotation>();

        // Delete each RichMedia annotation
        foreach (var rma in richMediaAnnotations)
        {
            document.Pages[1].Annotations.Delete(rma);
        }

        // Save PDF document
        document.Save(dataDir + "DeletePolyAnnotation_out.pdf");
    }
}
```

## Agregar Anotaciones de Widget

Los formularios interactivos utilizan [Widget Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) para representar la apariencia de los campos y gestionar las interacciones del usuario.
Utilizamos estos elementos de formulario que se agregan a un PDF para facilitar la entrada, envío de información o realizar alguna otra interacción del usuario.

Las Anotaciones de Widget son una representación gráfica de un campo de formulario en páginas específicas, por lo que no podemos crearlo directamente como una anotación.

Cada Anotación de Widget tendrá gráficos apropiados (apariencia) dependiendo de su tipo. Después de la creación, ciertos aspectos visuales pueden ser cambiados, como el estilo del borde y el color de fondo.
Otras propiedades como el color del texto y la fuente pueden ser cambiadas a través del campo, una vez que esté adjunto a uno.

En algunos casos, es posible que desees que un campo aparezca en más de una página, repitiendo el mismo valor. En ese caso, los campos que normalmente tienen solo un widget pueden tener múltiples widgets adjuntos: un TextField, ListBox, ComboBox y CheckBox generalmente tienen exactamente uno, mientras que el RadioGroup tiene múltiples widgets, uno para cada botón de radio.
Alguien que complete el formulario puede usar cualquiera de esos widgets para actualizar el valor del campo, y esto se refleja en todos los otros widgets también.

Cada campo de formulario para cada lugar en el documento representa una Anotación de Widget. Los datos específicos de ubicación de la Anotación de Widget se agregan a la página particular. Cada campo de formulario tiene varias variaciones. Un botón puede ser un botón de radio, una casilla de verificación o un botón pulsador. Un widget de elección puede ser un cuadro de lista o un cuadro combinado.

En este ejemplo, aprenderemos cómo agregar los botones de pulsar para la navegación en el documento.

### Agregar Botón al Documento

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPrintButton()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Define the rectangle for the button
        var rect = new Aspose.Pdf.Rectangle(72, 748, 164, 768);

        // Create a button field
        var printButton = new Aspose.Pdf.Forms.ButtonField(page, rect)
        {
            AlternateName = "Print current document",
            Color = Aspose.Pdf.Color.Black,
            PartialName = "printBtn1",
            NormalCaption = "Print Document"
        };

        // Set the border style for the button
        var border = new Aspose.Pdf.Annotations.Border(printButton)
        {
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
            Width = 2
        };
        printButton.Border = border;

        // Set the border and background color characteristics
        printButton.Characteristics.Border = System.Drawing.Color.FromArgb(255, 0, 0, 255);
        printButton.Characteristics.Background = System.Drawing.Color.FromArgb(255, 0, 191, 255);

        // Add the button to the form
        document.Form.Add(printButton);

        // Save PDF document
        document.Save(dataDir + "PrintButton_out.pdf");
    }
}
```

Este botón tiene borde y establece un fondo. También establecemos un nombre de botón (Name), un tooltip (AlternateName), una etiqueta (NormalCaption) y un color del texto de la etiqueta (Color).

### Usando acciones de navegación del documento

Existe un ejemplo más complejo del uso de las Anotaciones de Widget: navegación de documentos en el documento PDF. Esto puede ser necesario para preparar una presentación de documento PDF.

Este ejemplo muestra cómo crear 4 botones:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNavigationButtons()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "JSON Fundamenals.pdf"))
    {
        // Create an array of button fields
        var buttons = new Aspose.Pdf.Forms.ButtonField[4];

        // Define alternate names and normal captions for the buttons
        var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
        var normalCaptions = new[] { "First", "Prev", "Next", "Last" };

        // Define predefined actions for the buttons
        PredefinedAction[] actions = {
            PredefinedAction.FirstPage,
            PredefinedAction.PrevPage,
            PredefinedAction.NextPage,
            PredefinedAction.LastPage
        };

        // Define border and background colors
        var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
        var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);

        // We should create the buttons without attaching them to the page.
        for (var i = 0; i < 4; i++)
        {
            buttons[i] = new Aspose.Pdf.Forms.ButtonField(document, new Aspose.Pdf.Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
            {
                AlternateName = alternateNames[i],
                Color = Aspose.Pdf.Color.White,
                NormalCaption = normalCaptions[i],
                OnActivated = new Aspose.Pdf.Annotations.NamedAction(actions[i])
            };

            // Set the border style for the button
            buttons[i].Border = new Aspose.Pdf.Annotations.Border(buttons[i])
            {
                Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
                Width = 2
            };

            // Set the border and background color characteristics
            buttons[i].Characteristics.Border = clrBorder;
            buttons[i].Characteristics.Background = clrBackGround;
        }

        // Duplicate the array of buttons on each page in the document
        for (var pageIndex = 1; pageIndex <= document.Pages.Count; pageIndex++)
        {
            for (var i = 0; i < 4; i++)
            {
                document.Form.Add(buttons[i], $"btn{pageIndex}_{i + 1}", pageIndex);
            }
        }

        // Save PDF document
        document.Save(dataDir + "NavigationButtons_out.pdf");

        // We call Form.Add method with the following parameters: field, name, and the index of the pages that this field will be added to.
        // And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

        document.Form["btn1_1"].ReadOnly = true;
        document.Form["btn1_2"].ReadOnly = true;

        document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
        document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
    }
}
```

Para obtener información más detallada y posibilidades de estas características, consulta también [Trabajando con Formularios](/pdf/net/acroforms/).

En los documentos PDF, puedes ver y gestionar contenido 3D de alta calidad creado con software CAD 3D o de modelado 3D e incrustado en el documento PDF. Puedes rotar elementos 3D en todas las direcciones como si los estuvieras sosteniendo en tus manos.

¿Por qué necesitas una visualización 3D de imágenes?

En los últimos años, la tecnología ha logrado grandes avances en todas las áreas gracias a la impresión 3D. Las tecnologías de impresión 3D pueden aplicarse para enseñar habilidades tecnológicas en construcción, ingeniería mecánica, diseño como herramienta principal. Estas tecnologías, gracias a la aparición de dispositivos de impresión personal, pueden contribuir a la introducción de nuevas formas de organización del proceso educativo, aumentar la motivación y la formación de las competencias necesarias de los graduados y profesores.

La tarea principal del modelado 3D es la idea de un objeto futuro porque, para liberar un objeto, necesitas una comprensión de sus características de diseño en todos los detalles para la regeneración sucesiva en diseño industrial o arquitectura.

## Agregar Anotación 3D

La anotación 3D se agrega utilizando un modelo creado en el formato U3D.

1. Crea un nuevo [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Carga los datos del modelo 3D deseado (en nuestro caso "Ring.u3d") para crear [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent).
1. Crea un objeto [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) y vincúlalo al documento y al 3DContent.
1. Ajusta el objeto pdf3dArtWork:

    - 3DLightingScheme - (estableceremos `CAD` en el ejemplo)
    - 3DRenderMode - (estableceremos `Solid` en el ejemplo)
    - Rellena `ViewArray`, crea al menos una [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) y agrégala al array.

1. Establece 3 parámetros básicos en la anotación:
    - la `página` en la que se colocará la anotación.
    - el `rectángulo`, dentro del cual estará la anotación.
    - y el objeto `3dArtWork`.
1. Para una mejor presentación del objeto 3D, establece el marco del borde.
1. Establece la vista predeterminada (por ejemplo - TOP).
1. Agrega algunos parámetros adicionales: nombre, póster de vista previa, etc.
1. Agrega la Anotación a la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Guarda el resultado.

### Ejemplo

Por favor, revisa el siguiente fragmento de código para agregar una Anotación 3D.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Add3dAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Load 3D content
        var pdf3DContent = new Aspose.Pdf.Annotations.PDF3DContent(dataDir + "Ring.u3d");

        // Create 3D artwork
        var pdf3dArtWork = new Aspose.Pdf.Annotations.PDF3DArtwork(document, pdf3DContent)
        {
            LightingScheme = new Aspose.Pdf.Annotations.PDF3DLightingScheme(Aspose.Pdf.Annotations.LightingSchemeType.CAD),
            RenderMode = new Aspose.Pdf.Annotations.PDF3DRenderMode(Aspose.Pdf.Annotations.RenderModeType.Solid),
        };

        // Define matrices for different views
        var topMatrix = new Aspose.Pdf.Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Aspose.Pdf.Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);

        // Add views to the 3D artwork
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        // Add page
        var page = document.Pages.Add();

        // Create a 3D annotation
        var pdf3dAnnotation = new Aspose.Pdf.Annotations.PDF3DAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.Border = new Aspose.Pdf.Annotations.Border(pdf3dAnnotation);
        pdf3dAnnotation.SetDefaultViewIndex(1);
        pdf3dAnnotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.NoZoom;
        pdf3dAnnotation.Name = "Ring.u3d";

        // Set preview image if needed
        // pdf3dAnnotation.SetImagePreview(dataDir + "sample_3d.png");

        // Add the 3D annotation to the page
        document.Pages[1].Annotations.Add(pdf3dAnnotation);

        // Save PDF document
        document.Save(dataDir + "Add3dAnnotation_out.pdf");
    }
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