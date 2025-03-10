---
title: Reemplazar Texto - Fachadas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/replace-text-facades/
description: Esta sección explica cómo trabajar con Texto - Fachadas utilizando la clase PdfContentEditor.
lastmod: "2021-06-24"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text - Facades",
    "alternativeHeadline": "Effortless Text Replacement in PDF Files",
    "abstract": "La función Reemplazar Texto en la clase PdfContentEditor permite a los usuarios modificar de manera eficiente el contenido textual dentro de documentos PDF existentes. Al utilizar métodos simples como BindPdf y ReplaceText, los usuarios pueden actualizar texto sin problemas, ajustar tamaños de fuente y personalizar el formato del texto, incluyendo negrita y color, todo mientras mantienen la integridad del documento original. Esta funcionalidad mejora las capacidades de edición de PDF, facilitando la gestión dinámica del contenido.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "550",
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
    "url": "/net/replace-text-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Reemplazar Texto en un Archivo PDF Existente

Para reemplazar texto en un archivo PDF existente, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y vincular un archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Después de eso, necesitas llamar al método [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index). Debes guardar el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). El siguiente fragmento de código te muestra cómo reemplazar texto en un archivo PDF existente.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo01_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor Object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo01_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Verifica cómo se ve en el documento original:

![Reemplazar Texto](replace_text1.png)

Y verifica el resultado después de reemplazar el texto:

![Resultado de reemplazar Texto](replace_text2.png)

En el segundo ejemplo, verás cómo, además de reemplazar el texto, también puedes aumentar o disminuir el tamaño de la fuente:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo02_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label", 12);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo02_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Para más posibilidades avanzadas de trabajar con nuestro texto, utilizaremos el método [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate). Con este método, podemos hacer que el texto sea negrita, cursiva, de color, y así sucesivamente.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        var textState = new Aspose.Pdf.Text.TextState
        {
            ForegroundColor = Aspose.Pdf.Color.Red,
            FontSize = 12,
        };

        editor.ReplaceText("Value", "Label", textState);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo03_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");

    var textState = new Aspose.Pdf.Text.TextState
    {
        ForegroundColor = Aspose.Pdf.Color.Red,
        FontSize = 12,
    };

    editor.ReplaceText("Value", "Label", textState);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo03_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

En caso de que necesites reemplazar todo el texto especificado en el documento, utiliza el siguiente fragmento de código. Es decir, el reemplazo del texto ocurrirá donde sea que se encuentre el texto especificado para el reemplazo, y también contará el número de tales reemplazos.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        int count = 0;

        while (editor.ReplaceText("Value", "Label"))
        {
            count++;
        }

        Console.WriteLine($"{count} occurrences have been replaced.");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo04_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    int count = 0;

    while (editor.ReplaceText("Value", "Label"))
    {
        count++;
    }

    Console.WriteLine($"{count} occurrences have been replaced.");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo04_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

![Reemplazar todo el Texto](replace_text3.png)

El siguiente fragmento de código muestra cómo realizar todos los reemplazos de texto pero en una página específica de tu documento.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        int count = 0;

        while (editor.ReplaceText("9999", 2, "ABCDE"))
        {
            count++;
        }

        Console.WriteLine($"{count} occurrences have been replaced.");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo05_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    int count = 0;

    while (editor.ReplaceText("9999", 2, "ABCDE"))
    {
        count++;
    }

    Console.WriteLine($"{count} occurrences have been replaced.");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo05_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

En el siguiente fragmento de código, mostraremos cómo reemplazar, por ejemplo, un número dado con las letras que necesitamos.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText06()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor
           {
               ReplaceTextStrategy = new Aspose.Pdf.Facades.ReplaceTextStrategy
               {
                   IsRegularExpressionUsed = true,
                   ReplaceScope = Aspose.Pdf.Facades.ReplaceTextStrategy.Scope.ReplaceAll
               }
           })
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("\\d{4}", "ABCDE");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo06_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText06()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor
    {
        ReplaceTextStrategy = new Aspose.Pdf.Facades.ReplaceTextStrategy
        {
            IsRegularExpressionUsed = true,
            ReplaceScope = Aspose.Pdf.Facades.ReplaceTextStrategy.Scope.ReplaceAll
        }
    };

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("\\d{4}", "ABCDE");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo06_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}