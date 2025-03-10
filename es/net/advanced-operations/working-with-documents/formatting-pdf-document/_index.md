---
title: Formateo de Documento PDF usando C#
linktitle: Formateo de Documento PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/formatting-pdf-document/
description: Crea y formatea el Documento PDF con Aspose.PDF for .NET. Usa el siguiente fragmento de código para resolver tus tareas.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting Document using C#",
    "alternativeHeadline": "Enhance PDF Formatting with Aspose.PDF for .NET",
    "abstract": "Descubre la poderosa nueva función de Aspose.PDF for .NET que permite a los usuarios crear y formatear documentos PDF sin problemas. Con un control completo sobre las propiedades del documento, como la configuración de visualización de la ventana, las opciones de incrustación de fuentes y los factores de zoom personalizables, los desarrolladores pueden mejorar la experiencia del usuario y mantener la integridad del documento en diferentes plataformas. Optimiza tus tareas de manipulación de PDF con esta funcionalidad robusta que mejora significativamente la eficiencia de tus aplicaciones .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Formatting PDF Document, Aspose.PDF for .NET, PDF document properties, embed fonts, font substitution, set zoom factor, document window properties, PDF manipulation library, PDF document generation, C# PDF formatting",
    "wordcount": "2526",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Crea y formatea el Documento PDF con Aspose.PDF for .NET. Usa el siguiente fragmento de código para resolver tus tareas."
}
</script>

## Formateo de Documento PDF

### Obtener Propiedades de Visualización de Ventana y Página del Documento

Este tema te ayuda a entender cómo obtener propiedades de la ventana del documento, la aplicación visualizadora y cómo se muestran las páginas. Para establecer estas propiedades:

Abre el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Ahora, puedes establecer las propiedades del objeto Document, tales como

- CenterWindow – Centrar la ventana del documento en la pantalla. Predeterminado: false.
- Direction – Orden de lectura. Esto determina cómo se disponen las páginas cuando se muestran una al lado de la otra. Predeterminado: de izquierda a derecha.
- DisplayDocTitle – Mostrar el título del documento en la barra de título de la ventana del documento. Predeterminado: false (el título se muestra).
- HideMenuBar – Ocultar o mostrar la barra de menú de la ventana del documento. Predeterminado: false (la barra de menú se muestra).
- HideToolBar – Ocultar o mostrar la barra de herramientas de la ventana del documento. Predeterminado: false (la barra de herramientas se muestra).
- HideWindowUI – Ocultar o mostrar elementos de la ventana del documento como las barras de desplazamiento. Predeterminado: false (los elementos de la interfaz de usuario se muestran).
- NonFullScreenPageMode – Cómo se muestra el documento cuando no se presenta en modo de pantalla completa.
- PageLayout – El diseño de la página.
- PageMode – Cómo se muestra el documento cuando se abre por primera vez. Las opciones son mostrar miniaturas, pantalla completa, mostrar panel de adjuntos.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El siguiente fragmento de código te muestra cómo obtener las propiedades usando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetDocumentWindow.pdf"))
    {
        // Get different document properties
        // Position of document's window - Default: false
        Console.WriteLine("CenterWindow : {0}", document.CenterWindow);

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        Console.WriteLine("Direction : {0}", document.Direction);

        // Whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        Console.WriteLine("DisplayDocTitle : {0}", document.DisplayDocTitle);

        // Whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        Console.WriteLine("FitWindow : {0}", document.FitWindow);

        // Whether to hide menu bar of the viewer application - Default: false
        Console.WriteLine("HideMenuBar : {0}", document.HideMenubar);

        // Whether to hide tool bar of the viewer application - Default: false
        Console.WriteLine("HideToolBar : {0}", document.HideToolBar);

        // Whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        Console.WriteLine("HideWindowUI : {0}", document.HideWindowUI);

        // Document's page mode. How to display document on exiting full-screen mode.
        Console.WriteLine("NonFullScreenPageMode : {0}", document.NonFullScreenPageMode);

        // The page layout i.e. single page, one column
        Console.WriteLine("PageLayout : {0}", document.PageLayout);

        // How the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        Console.WriteLine("PageMode : {0}", document.PageMode);
    }
}
```

### Establecer Propiedades de Visualización de Ventana y Página del Documento

Este tema explica cómo establecer las propiedades de la ventana del documento, la aplicación visualizadora y la visualización de la página. Para establecer estas diferentes propiedades:

1. Abre el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Establece las propiedades del objeto Document.
1. Guarda el archivo PDF actualizado usando el método Save.

Las propiedades disponibles son:

- CenterWindow.
- Direction.
- DisplayDocTitle.
- FitWindow.
- HideMenuBar.
- HideToolBar.
- HideWindowUI.
- NonFullScreenPageMode.
- PageLayout.
- PageMode.

Cada una se utiliza y se describe en el código a continuación. El siguiente fragmento de código te muestra cómo establecer las propiedades usando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetDocumentWindow.pdf"))
    {
        // Set different document properties
        // Specify to position document's window - Default: false
        document.CenterWindow = true;

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        document.Direction = Aspose.Pdf.Direction.R2L;

        // Specify whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        document.DisplayDocTitle = true;

        // Specify whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        document.FitWindow = true;

        // Specify whether to hide menu bar of the viewer application - Default: false
        document.HideMenubar = true;

        // Specify whether to hide tool bar of the viewer application - Default: false
        document.HideToolBar = true;

        // Specify whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        document.HideWindowUI = true;

        // Document's page mode. Specify how to display document on exiting full-screen mode.
        document.NonFullScreenPageMode = Aspose.Pdf.PageMode.UseOC;

        // Specify the page layout i.e. single page, one column
        document.PageLayout = Aspose.Pdf.PageLayout.TwoColumnLeft;

        // Specify how the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseThumbs;

        // Save PDF document
        document.Save(dataDir + "SetDocumentWindow_out.pdf");
    }
}
```

### Incrustar Fuentes en un archivo PDF existente

Los lectores de PDF admiten [un núcleo de 14 fuentes](https://en.wikipedia.org/wiki/PDF#Text) para que los documentos se puedan mostrar de la misma manera independientemente de la plataforma en la que se muestre el documento. Cuando un PDF contiene una fuente que no es una de las 14 fuentes principales, incrusta la fuente en el archivo PDF para evitar la sustitución de fuentes.

Aspose.PDF for .NET admite la incrustación de fuentes en archivos PDF existentes. Puedes incrustar una fuente completa o un subconjunto de la fuente. Para incrustar la fuente, abre el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Luego usa la clase [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) para incrustar la fuente en el archivo PDF. Para incrustar la fuente completa, usa la propiedad IsEmbeded de la clase Font; para usar un subconjunto de la fuente, usa la propiedad IsSubset.

{{% alert color="primary" %}}

Un subconjunto de fuente incrusta solo los caracteres que se utilizan y es útil donde las fuentes se utilizan para oraciones cortas o eslóganes, por ejemplo, donde se utiliza una fuente corporativa para un logotipo, pero no para el texto del cuerpo. Usar un subconjunto reduce el tamaño del archivo del PDF de salida. Sin embargo, si se utiliza una fuente personalizada para el texto del cuerpo, incrústala en su totalidad.

{{% /alert %}}

El siguiente fragmento de código muestra cómo incrustar una fuente en un archivo PDF.

### Incrustar Fuentes Estándar Tipo 1

Algunos documentos PDF tienen fuentes de un conjunto especial de fuentes de Adobe. Las fuentes de este conjunto se llaman “Fuentes Estándar Tipo 1”. Este conjunto incluye 14 fuentes y la incrustación de este tipo de fuentes requiere el uso de banderas especiales, es decir, [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). A continuación se muestra el fragmento de código que se puede utilizar para obtener un documento con todas las fuentes incrustadas, incluidas las Fuentes Estándar Tipo 1:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontsType1ToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set EmbedStandardFonts property of document
        document.EmbedStandardFonts = true;

        // Iterate through each page
        foreach (var page in document.Pages)
        {
            if (page.Resources.Fonts != null)
            {
                foreach (var pageFont in page.Resources.Fonts)
                {
                    // Check if font is already embedded
                    if (!pageFont.IsEmbedded)
                    {
                        pageFont.IsEmbedded = true;
                    }
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "EmbeddedFontsUpdated_out.pdf");
    }
}
```

### Incrustar Fuentes al crear PDF

Si necesitas usar alguna fuente que no sea una de las 14 fuentes principales admitidas por Adobe Reader, debes incrustar la descripción de la fuente mientras generas el archivo PDF. Si la información de la fuente no está incrustada, Adobe Reader la tomará del sistema operativo si está instalada en el sistema, o construirá una fuente sustituta de acuerdo con el descriptor de la fuente en el PDF.

> Ten en cuenta que la fuente incrustada debe estar instalada en la máquina anfitriona, es decir, en el caso del siguiente código, la fuente ‘Univers Condensed’ está instalada en el sistema.

Usamos la propiedad IsEmbedded de la clase Font para incrustar la información de la fuente en el archivo PDF. Establecer el valor de esta propiedad en ‘True’ incrustará el archivo de fuente completo en el PDF, sabiendo que aumentará el tamaño del archivo PDF. A continuación se muestra el fragmento de código que se puede utilizar para incrustar la información de la fuente en el PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontWhileCreatingPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create a section in the Pdf object
        var page = document.Pages.Add();

        // Create a TextFragment
        var fragment = new Aspose.Pdf.Text.TextFragment("");

        // Create a TextSegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");

        // Create and configure TextState
        var ts = new Aspose.Pdf.Text.TextState();
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        ts.Font.IsEmbedded = true;
        segment.TextState = ts;

        // Add the segment to the fragment
        fragment.Segments.Add(segment);

        // Add the fragment to the page
        page.Paragraphs.Add(fragment);

        // Save PDF Document
        document.Save(dataDir + "EmbedFontWhileDocCreation_out.pdf");
    }
}
```

### Establecer Nombre de Fuente Predeterminado al Guardar PDF

Cuando un documento PDF contiene fuentes que no están disponibles en el documento mismo y en el dispositivo, la API reemplaza estas fuentes con la fuente predeterminada. Cuando la fuente está disponible (está instalada en el dispositivo o está incrustada en el documento), el PDF de salida debe tener la misma fuente (no debe ser reemplazada por la fuente predeterminada). El valor de la fuente predeterminada debe contener el nombre de la fuente (no la ruta a los archivos de fuente). Hemos implementado una función para establecer el nombre de la fuente predeterminada al guardar un documento como PDF. El siguiente fragmento de código se puede utilizar para establecer la fuente predeterminada:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDefaultFontOnDocumentSave(string documentName, string newName)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var fs = new FileStream(dataDir + "GetDocumentWindow.pdf", FileMode.Open))
    {
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create PdfSaveOptions and specify Default Font Name
            var pdfSaveOptions = new Aspose.Pdf.PdfSaveOptions
            {
                DefaultFontName = newName
            };

            // Save PDF document
            document.Save(dataDir + "DefaultFont_out.pdf", pdfSaveOptions);
        }
    }
}
```

### Obtener Todas las Fuentes del Documento PDF

En caso de que desees obtener todas las fuentes de un documento PDF, puedes usar el método FontUtilities.GetAllFonts() proporcionado en la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Por favor, revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllFontsFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get all fonts used in the document
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through each font and print its name
        foreach (var font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```

### Obtener Advertencias sobre la Sustitución de Fuentes

Aspose.PDF for .NET proporciona métodos para obtener notificaciones sobre la sustitución de fuentes para manejar casos de sustitución de fuentes. Los fragmentos de código a continuación muestran cómo usar la funcionalidad correspondiente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void NotificationFontSubstitution()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Attach the FontSubstitution event handler
        document.FontSubstitution += OnFontSubstitution;
        // You can use lambda
        // (oldFont, newFont) => Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        //                                                                        oldFont.FontName, newFont.FontName));

        // Save PDF document
        document.Save(dataDir + "NotificationFontSubstitution_out.pdf");
    }
}
```

El método **OnFontSubstitution** se enumera a continuación.

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### Mejorar la Incrustación de Fuentes usando FontSubsetStrategy

La función para incrustar las fuentes como un subconjunto se puede lograr utilizando la propiedad IsSubset, pero a veces deseas reducir un conjunto de fuentes completamente incrustadas a solo subconjuntos que se utilizan en el documento. Aspose.Pdf.Document tiene la propiedad FontUtilities que incluye el método SubsetFonts(FontSubsetStrategy subsetStrategy). En el método SubsetFonts(), el parámetro subsetStrategy ayuda a ajustar la estrategia de subconjunto. FontSubsetStrategy admite dos variantes siguientes de subconjuntos de fuentes.

- SubsetAllFonts - Esto incluirá todos los subconjuntos de fuentes utilizadas en un documento.
- SubsetEmbeddedFontsOnly - Esto incluirá solo aquellas fuentes que están completamente incrustadas en el documento.

El siguiente fragmento de código muestra cómo establecer FontSubsetStrategy:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFontSubsetStrategy()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // All fonts will be embedded as subset into document in case of SubsetAllFonts.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetAllFonts);

        // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetEmbeddedFontsOnly);

        // Save PDF document
        document.Save(dataDir + "SetFontSubsetStrategy_out.pdf");
    }
}
```

### Obtener-Establecer Factor de Zoom del Archivo PDF

A veces, deseas determinar cuál es el factor de zoom actual de un documento PDF. Con Aspose.Pdf, puedes averiguar el valor actual así como establecer uno.

La propiedad Destination de la clase [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) te permite obtener el valor de zoom asociado con un archivo PDF. De manera similar, se puede usar para establecer el factor de zoom de un archivo.

#### Establecer Factor de Zoom

El siguiente fragmento de código muestra cómo establecer el factor de zoom de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetZoomFactor.pdf"))
    {
        // Create GoToAction with a specific zoom factor
        var action = new Aspose.Pdf.Annotations.GoToAction(new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 0, 0, 0.5));
        document.OpenAction = action;

        // Save PDF document
        document.Save(dataDir + "ZoomFactor_out.pdf");
    }
}
```

#### Obtener Factor de Zoom

El siguiente fragmento de código muestra cómo obtener el factor de zoom de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Zoomed_pdf.pdf"))
    {
        // Create GoToAction object
        if (document.OpenAction is Aspose.Pdf.Annotations.GoToAction action)
        {
            // Get the Zoom factor of PDF file
            if (action.Destination is Aspose.Pdf.Annotations.XYZExplicitDestination destination)
            {
                System.Console.WriteLine(destination.Zoom); // Document zoom value;
            }
        }
    }
}
```

### Establecer Propiedades de Preset del Diálogo de Impresión

Aspose.PDF permite establecer las propiedades de preset del diálogo de impresión de un documento PDF. Te permite cambiar la propiedad DuplexMode para un documento PDF que está configurado en simplex por defecto. Esto se puede lograr utilizando dos metodologías diferentes como se muestra a continuación.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Set duplex printing to DuplexFlipLongEdge
        document.Duplex = Aspose.Pdf.PrintDuplex.DuplexFlipLongEdge;

        // Save PDF document
        document.Save(dataDir + "SetPrintDlgPresetProperties_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

### Establecer Propiedades de Preset del Diálogo de Impresión usando el Editor de Contenido PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetPropertiesUsingPdfContentEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    string inputFile = dataDir + "input.pdf";

    using (var ed = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        ed.BindPdf(inputFile);

        // Check if the file has duplex flip short edge
        if ((ed.GetViewerPreference() & Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge) > 0)
        {
            Console.WriteLine("The file has duplex flip short edge");
        }

        // Change the viewer preference to duplex flip short edge
        ed.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge);

        // Save PDF document
        ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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