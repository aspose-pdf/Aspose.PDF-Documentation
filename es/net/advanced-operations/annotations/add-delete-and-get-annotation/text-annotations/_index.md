---
title: Usando la Anotación de Texto para PDF
linktitle: Anotación de Texto
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/text-annotation/
description: Aspose.PDF for .NET te permite Agregar, Obtener y Eliminar Anotaciones de Texto de tu documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Text Annotation for PDF",
    "alternativeHeadline": "Enhance PDFs with Dynamic Text Annotations",
    "abstract": "Aspose.PDF for .NET introduce capacidades avanzadas de anotación de texto, permitiendo a los usuarios agregar, recuperar o eliminar anotaciones de texto dentro de documentos PDF sin esfuerzo. Esta característica mejora el proceso de edición de PDF al permitir la colocación precisa y la personalización de anotaciones, mejorando así la interacción y usabilidad del documento.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Text Annotation, PDF document generation, Aspose.PDF for .NET, Add Annotation, Delete Annotation, Free Text Annotation, Popup Annotation, StrikeOutAnnotation, AnnotationCollection, Aspose.PDF library",
    "wordcount": "2636",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET te permite Agregar, Obtener y Eliminar Anotaciones de Texto de tu documento PDF."
}
</script>

## Cómo agregar una Anotación de Texto en un archivo PDF existente

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

Una Anotación de Texto es una anotación adjunta a una ubicación específica en un documento PDF. Cuando está cerrada, la anotación se muestra como un ícono; cuando se abre, debe mostrar una ventana emergente que contenga el texto de la nota en la fuente y tamaño elegidos por el lector.

Las anotaciones están contenidas en la colección de [Annotations](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations) de una Página particular. Esta colección contiene las anotaciones solo para esa página individual; cada página tiene su propia colección de Annotations.

Para agregar una anotación a una página particular, agrégala a la colección de Annotations de esa página con el método [Add](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. Primero, crea una anotación que deseas agregar al PDF.
1. Luego abre el PDF de entrada.
1. Agrega la anotación a la colección de Annotations del objeto [Page](https://reference.aspose.com/pdf/es/net/aspose.pdf/page).

El siguiente fragmento de código te muestra cómo agregar una anotación en una página PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotationToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
        textAnnotation.Title = "Sample Annotation Title";
        textAnnotation.Subject = "Sample Subject";
        textAnnotation.SetReviewState(Aspose.Pdf.Annotations.AnnotationState.Accepted);
        textAnnotation.Contents = "Sample contents for the annotation";
        textAnnotation.Open = true;
        textAnnotation.Icon = Aspose.Pdf.Annotations.TextIcon.Key;

        // Set border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(textAnnotation);
        border.Width = 5;
        border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
        textAnnotation.Border = border;
        textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Add annotation to the annotations collection of the page
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddAnnotation_out.pdf");
    }
}
```

## Cómo agregar una Anotación Emergente

Una Anotación Emergente muestra texto en una ventana emergente para entrada y edición. No debe aparecer sola, sino que está asociada con una anotación de marcado, su anotación padre, y debe usarse para editar el texto del padre.

No debe tener un flujo de apariencia o acciones asociadas propias y debe ser identificada por la entrada Popup en el diccionario de anotaciones del padre.

El siguiente fragmento de código te muestra cómo agregar una [Anotación Emergente](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/popupannotation) en una página PDF usando un ejemplo de agregar una [anotación de Línea](/pdf/es/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file) del padre.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## Cómo agregar (o Crear) una nueva Anotación de Texto Libre

Una anotación de texto libre muestra texto directamente en la página. El método [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) permite crear este tipo de anotación. En el siguiente fragmento, agregamos una anotación de texto libre sobre la primera ocurrencia de la cadena.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotationDemo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Assuming tfa is an instance of TextFragmentAbsorber or similar
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber();
        tfa.Visit(document.Pages[1]);

        if (tfa.TextFragments.Count <= 0)
        {
            return;
        }

        // Define the rectangle for the free text annotation
        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Create free text annotation
        pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // Last param is the page number

        // Save PDF document
        pdfContentEditor.Save(dataDir + "pdf-sample-0.pdf");
    }
}
```

### Establecer la Propiedad de Llamada para FreeTextAnnotation

Para una configuración más flexible de la anotación en el documento PDF, Aspose.PDF for .NET proporciona la propiedad [Callout](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/freetextannotation/properties/callout) de la clase [FreeTextAnnotation](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/freetextannotation) que permite especificar un Array de puntos de la línea de llamada. El siguiente fragmento de código muestra cómo usar esta funcionalidad:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextCalloutAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create default appearance for the annotation
        var da = new Aspose.Pdf.Annotations.DefaultAppearance();
        da.TextColor = System.Drawing.Color.Red;
        da.FontSize = 10;

        // Create free text annotation with callout
        var fta = new Aspose.Pdf.Annotations.FreeTextAnnotation(page, new Aspose.Pdf.Rectangle(422.25, 645.75, 583.5, 702.75), da);
        fta.Intent = Aspose.Pdf.Annotations.FreeTextIntent.FreeTextCallout;
        fta.EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow;
        fta.Callout = new Aspose.Pdf.Point[]
        {
            new Aspose.Pdf.Point(428.25, 651.75),
            new Aspose.Pdf.Point(462.75, 681.375),
            new Aspose.Pdf.Point(474, 681.375)
        };

        // Add the annotation to the page
        page.Annotations.Add(fta);

        // Set rich text for the annotation
        fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";

        // Save PDF document
        document.Save(dataDir + "SetCalloutProperty_out.pdf");
    }
}
```

### Establecer la Propiedad de Llamada para el Archivo XFDF

Si usas la importación desde un archivo XFDF, por favor usa el nombre de la línea de llamada en lugar de solo Callout. El siguiente fragmento de código muestra cómo usar esta funcionalidad:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationsFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create an XFDF string builder
        var xfdf = new StringBuilder();
        xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");

        // Call the method to create XFDF content
        CreateXfdf(ref xfdf);

        xfdf.AppendLine("</annots></xfdf>");

        // Import annotations from the XFDF string
        document.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(xfdf.ToString())));

        // Save PDF document
        document.Save(dataDir + "SetCalloutPropertyXfdf_out.pdf");
    }
}
```

El siguiente método se utiliza para CreateXfdf:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```

### Hacer que la Anotación de Texto Libre sea Invisible

A veces, es necesario crear una marca de agua que no sea visible en el documento al verlo, pero que deba ser visible cuando se imprima el documento. Usa las banderas de anotación para este propósito. El siguiente fragmento de código muestra cómo hacerlo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInvisibleAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create a free text annotation
        var annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(50, 600, 250, 650),
            new Aspose.Pdf.Annotations.DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red)
        );

        annotation.Contents = "ABCDEFG";
        annotation.Characteristics.Border = System.Drawing.Color.Red;
        annotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print | Aspose.Pdf.Annotations.AnnotationFlags.NoView;

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(annotation);

        // Save PDF document
        document.Save(dataDir + "InvisibleAnnotation_out.pdf");
    }
}
```

### Establecer el Formato de FreeTextAnnotation

Esta parte analiza cómo formatear el texto en una anotación de texto libre.

Las anotaciones están contenidas en la colección [AnnotationCollection](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/annotationcollection) del objeto [Page](https://reference.aspose.com/pdf/es/net/aspose.pdf/page). Al agregar una [FreeTextAnnotation](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/freetextannotation) a un documento PDF, puedes especificar la información de formato como fuente, tamaño, color, etc., utilizando la clase [DefaultAppearance](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/defaultappearance/methods/index). También es posible especificar la información de formato utilizando la propiedad TextStyle. Además, puedes actualizar el formato de cualquier FreeTextAnnotation que ya esté en el documento PDF.

La clase [TextStyle](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/textstyle) admite trabajar con la entrada de estilo predeterminado. Esta clase te permite establecer color, tamaño de fuente y nombre de fuente:

- La propiedad FontName obtiene o establece el nombre de la fuente (cadena).
- La propiedad FontSize obtiene y establece el tamaño de texto predeterminado (doble).
- La propiedad System.Drawing.Color obtiene y establece el color del texto (color).
- La propiedad TextAlignment obtiene y establece la alineación del texto de la anotación (alineación).

El siguiente fragmento de código muestra cómo agregar una FreeTextAnnotation con un formato de texto específico.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Instantiate DefaultAppearance object
        var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Arial", 28, System.Drawing.Color.Red);

        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600), defaultAppearance);

        // Specify the contents of annotation
        freetext.Contents = "Free Text";

        // Add annotation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation(string fontName = "Arial", float fontSize = 28)
{
     // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Set default values
        var textColor = System.Drawing.Color.Red;
        var position = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Instantiate DefaultAppearance object
        Aspose.Pdf.Annotations.DefaultAppearance defaultAppearance = new(fontName, fontSize, textColor);
        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], position, defaultAppearance)
        {
            // Specify the contents of annotation
            Contents = "Free Text"
        };
        // Add anootation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

{{% alert color="primary" %}}

Cuando cambias el contenido o el estilo de texto de una anotación de texto libre, la apariencia de la anotación se regenera para reflejar los cambios.

{{% /alert %}}

### Tachar Palabras usando StrikeOutAnnotation

Aspose.PDF for .NET te permite agregar, eliminar y actualizar anotaciones en documentos PDF. Una de las clases también te permite tachar anotaciones. Esto es útil cuando deseas tachar uno o más fragmentos de texto en un documento. Las anotaciones se mantienen en la colección [AnnotationCollection](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/annotationcollection) del objeto [Page](https://reference.aspose.com/pdf/es/net/aspose.pdf/page). Se puede usar una clase llamada [StrikeOutAnnotation](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/strikeoutannotation) para agregar anotaciones de tachado a un documento PDF.

Para tachar un cierto TextFragment:

1. Busca un TextFragment en el archivo PDF.
1. Obtén las coordenadas del objeto TextFragment.
1. Usa las coordenadas para instanciar un objeto StrikeOutAnnotation.

El siguiente fragmento de código muestra cómo buscar un TextFragment particular y agregar una StrikeOutAnnotation a ese objeto.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void StrikeOutTextInDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        // Create TextFragment Absorber instance to search for a particular text fragment
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Estoque");

        // Iterate through pages of PDF document
        foreach (var page in document.Pages)
        {
            // Accept the absorber for the current page
            page.Accept(textFragmentAbsorber);
        }

        // Get the collection of absorbed text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Iterate through the collection of text fragments
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Get rectangular dimensions of the TextFragment object
            var rect = new Aspose.Pdf.Rectangle(
                (float)textFragment.Position.XIndent,
                (float)textFragment.Position.YIndent,
                (float)textFragment.Position.XIndent + (float)textFragment.Rectangle.Width,
                (float)textFragment.Position.YIndent + (float)textFragment.Rectangle.Height);

            // Instantiate StrikeOut Annotation instance
            var strikeOut = new Aspose.Pdf.Annotations.StrikeOutAnnotation(textFragment.Page, rect)
            {
                // Set opacity for annotation
                Opacity = 0.80f,

                // Set the color of annotation
                Color = Aspose.Pdf.Color.Red
            };

            // Set the border for annotation instance
            strikeOut.Border = new Aspose.Pdf.Annotations.Border(strikeOut);

            // Add annotation to the annotations collection of the TextFragment's page
            textFragment.Page.Annotations.Add(strikeOut);
        }

        // Save PDF document
        document.Save(dataDir + "StrikeOutWords_out.pdf");
    }
}
```

## Eliminar Todas las Anotaciones de la Página de un Archivo PDF

La colección [AnnotationCollection](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/annotationcollection) del objeto [Page](https://reference.aspose.com/pdf/es/net/aspose.pdf/page) contiene todas las anotaciones para esa página particular. Para eliminar todas las anotaciones de una página, llama al método *Delete* de la colección AnnotationCollectoin.

El siguiente fragmento de código te muestra cómo eliminar todas las anotaciones de una página particular.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotationsFromPage.pdf"))
    {
        // Delete all annotations from the first page
        document.Pages[1].Annotations.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
    }
}
```

## Eliminar una Anotación Particular de un Archivo PDF

{{% alert color="primary" %}}

Puedes verificar la calidad de Aspose.PDF y obtener los resultados en línea en este enlace:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF te permite eliminar una Anotación particular de un archivo PDF. Este tema explica cómo.

Para eliminar una anotación particular de un PDF, llama al [método Delete de la colección AnnotationCollection](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). Esta colección pertenece al objeto [Page](https://reference.aspose.com/pdf/es/net/aspose.pdf/page). El método Delete requiere el índice de la anotación que deseas eliminar. Luego, guarda el archivo PDF actualizado. El siguiente fragmento de código muestra cómo eliminar una anotación particular.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularAnnotation.pdf"))
    {
        // Delete a particular annotation by index (e.g., the first annotation on the first page)
        document.Pages[1].Annotations.Delete(1);

        // Save PDF document
        document.Save(dataDir + "DeleteParticularAnnotation_out.pdf");
    }
}
```

## Obtener Todas las Anotaciones de la Página de un Documento PDF

Aspose.PDF te permite obtener anotaciones de un documento completo o de una página dada. Para obtener todas las anotaciones de la página en un documento PDF, recorre la colección [AnnotationCollection](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/annotationcollection) de los recursos de la página deseada. El siguiente fragmento de código te muestra cómo obtener todas las anotaciones de una página.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAllAnnotationsFromPage.pdf"))
    {
        // Loop through all the annotations on the first page
        foreach (Aspose.Pdf.Annotations.MarkupAnnotation annotation in document.Pages[1].Annotations)
        {
            // Get annotation properties
            Console.WriteLine("Title : {0} ", annotation.Title);
            Console.WriteLine("Subject : {0} ", annotation.Subject);
            Console.WriteLine("Contents : {0} ", annotation.Contents);
        }
    }
}
```

Ten en cuenta que para obtener todas las anotaciones del PDF completo, debes recorrer la colección de la clase PageCollection del documento antes de navegar a través de la colección de la clase AnnotationCollection. Puedes obtener cada anotación de la colección en un tipo de anotación base llamado clase MarkupAnnotation y luego mostrar sus propiedades.

## Obtener una Anotación Particular de un Archivo PDF

Las anotaciones están asociadas con páginas individuales y se almacenan en la colección [AnnotationCOllection](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/annotationcollection) del objeto [Page](https://reference.aspose.com/pdf/es/net/aspose.pdf/page). Para obtener una anotación particular, especifica su índice. Esto devuelve un objeto [Annotation](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/annotation) que necesita ser convertido a un tipo de anotación particular, por ejemplo [TextAnnotation](https://reference.aspose.com/pdf/es/net/aspose.pdf.annotations/textannotation). El siguiente fragmento de código muestra cómo obtener una anotación particular y sus propiedades.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetParticularAnnotation.pdf"))
    {
        // Get a particular annotation by index (e.g., the first annotation on the first page)
        var textAnnotation = (Aspose.Pdf.Annotations.TextAnnotation)document.Pages[1].Annotations[1];

        // Get annotation properties
        Console.WriteLine("Title : {0} ", textAnnotation.Title);
        Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
        Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
    }
}
```

## Obtener el Recurso de la Anotación

Aspose.PDF te permite obtener un recurso de anotación de un documento completo o de una página dada. El siguiente fragmento de código te muestra cómo obtener el recurso de anotación como un objeto [FileSpecification](https://reference.aspose.com/pdf/es/net/aspose.pdf/filespecification) del archivo PDF de entrada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAndGetResourceOfAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create a screen annotation with a SWF file
        var sa = new Aspose.Pdf.Annotations.ScreenAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
        document.Pages[1].Annotations.Add(sa);

        // Save PDF document with the new annotation
        document.Save(dataDir + "GetResourceOfAnnotation_out.pdf");

        // Open the updated document
        var document1 = new Aspose.Pdf.Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

        // Get the action of the annotation
        var action = (document1.Pages[1].Annotations[1] as Aspose.Pdf.Annotations.ScreenAnnotation).Action as Aspose.Pdf.Annotations.RenditionAction;

        // Get the rendition of the rendition action
        var rendition = action.Rendition;

        // Get the media clip
        var clip = (rendition as Aspose.Pdf.Annotations.MediaRendition).MediaClip;
        var data = (clip as Aspose.Pdf.Annotations.MediaClipData).Data;

        // Read the media data
        using (var ms = new MemoryStream())
        {
            byte[] buffer = new byte[1024];
            int read = 0;

            // Data of media are accessible in FileSpecification.Contents
            using (var source = data.Contents)
            {
                while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
                {
                    ms.Write(buffer, 0, read);
                }
            }

            Console.WriteLine(rendition.Name);
            Console.WriteLine(action.RenditionOperation);
        }
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