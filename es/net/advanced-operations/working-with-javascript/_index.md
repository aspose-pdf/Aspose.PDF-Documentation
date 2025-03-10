---
title: Trabajando con JavaScript
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /es/net/working-with-javascript/
description: Aprende cómo agregar, modificar y ejecutar JavaScript en documentos PDF usando Aspose.PDF for .NET. Mejora la interactividad y la automatización.
lastmod: "2025-02-07"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with JavaScript",
    "alternativeHeadline": "Enhance PDF with Custom JavaScript Actions",
    "abstract": "Descubre las capacidades mejoradas de integrar JavaScript dentro de documentos PDF a través de Aspose.PDF for .NET. Esta nueva característica permite a los desarrolladores agregar y gestionar acciones de JavaScript tanto a nivel de documento como de página, habilitando experiencias PDF interactivas y dinámicas orientadas a mejorar la participación y funcionalidad del usuario. Desbloquea el potencial de JavaScript para crear formularios PDF sofisticados que imitan comportamientos similares a los de la web, elevando tus flujos de trabajo de generación de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "JavaScript, Acrobat JavaScript, PDF document generation, JavaScript collection, document level JavaScript, JavaScript Action, interactive PDF forms, manipulate PDF files, HTML JavaScript, Aspose.PDF for .NET",
    "wordcount": "423",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Agregando JavaScript (DOM)

### ¿Qué es Acrobat JavaScript?

Acrobat JavaScript es un lenguaje basado en el núcleo de JavaScript versión 1.5 de ISO-16262, anteriormente conocido como ECMAScript, un lenguaje de scripting orientado a objetos desarrollado por Netscape Communications. JavaScript fue creado para descargar el procesamiento de páginas web de un servidor a un cliente en aplicaciones basadas en la web. Acrobat JavaScript implementa extensiones, en forma de nuevos objetos y sus métodos y propiedades acompañantes, al lenguaje JavaScript. Estos objetos específicos de Acrobat permiten a un desarrollador gestionar la seguridad del documento, comunicarse con una base de datos, manejar archivos adjuntos, manipular un archivo PDF para que se comporte como un formulario interactivo habilitado para la web, y así sucesivamente. Debido a que los objetos específicos de Acrobat se agregan sobre el JavaScript básico, aún tienes acceso a sus clases estándar, incluyendo Math, String, Date, Array y RegExp.

### Acrobat JavaScript vs HTML (Web) JavaScript

Los documentos PDF tienen una gran versatilidad ya que pueden ser mostrados tanto dentro del software Acrobat como en un navegador web. Por lo tanto, es importante ser consciente de las diferencias entre Acrobat JavaScript y JavaScript utilizado en un navegador web, también conocido como HTML JavaScript:

- Acrobat JavaScript no tiene acceso a objetos dentro de una página HTML. De manera similar, HTML JavaScript no puede acceder a objetos dentro de un archivo PDF.
- HTML JavaScript puede manipular objetos como Window. Acrobat JavaScript no puede acceder a este objeto en particular, pero puede manipular objetos específicos de PDF.

Puedes agregar JavaScript tanto a nivel de documento como de página usando [Aspose.PDF for .NET](/pdf/net/). Para agregar JavaScript:

### Agregando JavaScript a la Acción de Documento o Página

1. Declara e instancia un objeto JavascriptAction con la declaración de JavaScript deseada como argumento del constructor.
1. Asigna el objeto JavascriptAction a la acción deseada del documento o página PDF.

El siguiente ejemplo aplica el OpenAction a un documento específico.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Adding JavaScript at Document Level
        // Instantiate JavascriptAction with desired JavaScript statement
        var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

        // Assign JavascriptAction object to desired action of Document
        document.OpenAction = javaScript;

        // Adding JavaScript at Page Level
        document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
        document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

        // Save PDF Document
        document.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Adding JavaScript at Document Level
    // Instantiate JavascriptAction with desired JavaScript statement
    var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // Assign JavascriptAction object to desired action of Document
    document.OpenAction = javaScript;

    // Adding JavaScript at Page Level
    document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
    document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

    // Save PDF Document
    document.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Agregando/Eliminando JavaScript a Nivel de Documento

Se ha agregado una nueva propiedad llamada JavaScript en la clase Document que tiene tipo de colección de JavaScript y proporciona acceso a escenarios de JavaScript por su clave. Esta propiedad se utiliza para agregar JavaScript a nivel de documento. La colección de JavaScript tiene las siguientes propiedades y métodos:

- string this(string key)– Obtiene o establece JavaScript por su nombre.
- IList Keys – proporciona una lista de claves existentes en la colección de JavaScript.
- bool Remove(string key) – elimina JavaScript por su clave.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        document.JavaScript["func1"] = "function func1() { hello(); }";
        document.JavaScript["func2"] = "function func2() { hello(); }";
        document.Save(dataDir + "AddJavascript.pdf");
    }

    // Remove Document level JavaScript
    using (var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf"))
    {
        var keys = (IList)document1.JavaScript.Keys;

        Console.WriteLine("=============================== ");

        foreach (string key in keys)
        {
            Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
        }

        document1.JavaScript.Remove("func1");

        Console.WriteLine("Key 'func1' removed ");
        Console.WriteLine("=============================== ");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    document.JavaScript["func1"] = "function func1() { hello(); }";
    document.JavaScript["func2"] = "function func2() { hello(); }";
    document.Save(dataDir + "AddJavascript.pdf");

    // Remove Document level JavaScript
    using var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf");
    IList keys = (IList)document1.JavaScript.Keys;

    Console.WriteLine("=============================== ");

    foreach (string key in keys)
    {
        Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
    }

    document1.JavaScript.Remove("func1");

    Console.WriteLine("Key 'func1' removed ");
    Console.WriteLine("=============================== ");
}
```
{{< /tab >}}
{{< /tabs >}}

### Estableciendo la Fecha de Expiración de un Documento PDF Usando Acciones de JavaScript

Aspose.PDF te permite establecer una fecha de expiración para un documento PDF al incrustar Acciones de JavaScript. Esta funcionalidad asegura que el PDF se vuelva inaccesible después de una fecha y hora especificadas, mejorando la seguridad y el control del documento. Al aprovechar las Acciones de JavaScript, puedes definir condiciones de expiración precisas hasta el segundo, asegurando que la accesibilidad del documento esté estrictamente regulada.

**Puedes lograr esto siguiendo estos pasos**

1. **Inicializar Documento:** Crea un nuevo documento PDF y agrega una página en blanco o abre un documento PDF existente.
2. **Definir Fecha y Hora de Expiración:** Establece la fecha y hora después de las cuales el documento expirará.
3. **Preparar Código JavaScript:** 
    - Recupera la fecha y hora actuales.
    - Define la fecha y hora exactas de expiración, considerando que los meses son basados en cero en JavaScript.
    - Compara la fecha y hora actuales con la fecha y hora de expiración.
    - Si la fecha y hora actuales superan la fecha y hora de expiración, muestra una alerta y cierra el documento.
4. **Establecer Acción de Apertura:** Asocia la acción de JavaScript con la acción de apertura del documento.
5. **Guardar Documento:** Guarda el PDF con el JavaScript incrustado que impone la condición de expiración.

A continuación se presentan fragmentos de código que demuestran esta funcionalidad tanto en C# (.NET) como en Java.

El siguiente fragmento de código en C# demuestra cómo establecer una fecha y hora de expiración para un documento PDF utilizando Acciones de JavaScript con Aspose.PDF:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();

        // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
        DateTime expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

        // Create JavaScript code to enforce the expiry date and time
        string jsCode =
            // Get the current date and time
            "var rightNow = new Date();\n" +
            // Set the expiry date and time
            "var endDate = new Date(" +
            $"{expiryDateTime.Year}," +
            $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
            $"{expiryDateTime.Day}," +
            $"{expiryDateTime.Hour}," +
            $"{expiryDateTime.Minute}," +
            $"{expiryDateTime.Second}" +
            ");\n" +
            "if(rightNow > endDate)\n" +
            "{\n" +
            "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
            "    this.closeDoc();\n" +
            "}";

        // Create a JavascriptAction with the defined JavaScript code
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

        // Set the JavaScript action to execute when the document is opened
        document.OpenAction = javaScript;

        // Save PDF document
        document.Save(dataDir + "PDFExpiry_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();

    // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
    var expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

    // Create JavaScript code to enforce the expiry date and time
    string jsCode =
        // Get the current date and time
        "var rightNow = new Date();\n" +
        // Set the expiry date and time
        "var endDate = new Date(" +
        $"{expiryDateTime.Year}," +
        $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
        $"{expiryDateTime.Day}," +
        $"{expiryDateTime.Hour}," +
        $"{expiryDateTime.Minute}," +
        $"{expiryDateTime.Second}" +
        ");\n" +
        "if(rightNow > endDate)\n" +
        "{\n" +
        "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
        "    this.closeDoc();\n" +
        "}";

    // Create a JavascriptAction with the defined JavaScript code
    var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

    // Set the JavaScript action to execute when the document is opened
    document.OpenAction = javaScript;

    // Save PDF document
    document.Save(dataDir + "PDFExpiry_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

- **Objeto Date de JavaScript:** En JavaScript, el índice del mes comienza en `0` para enero y termina en `11` para diciembre. Asegúrate de que el valor del mes se ajuste adecuadamente al establecer la fecha y hora de expiración.
  
- **Consideraciones de Seguridad:** Si bien las acciones de JavaScript pueden controlar el comportamiento de un documento PDF, dependen del soporte del visor de PDF para JavaScript. No todos los visores de PDF pueden honrar estos scripts, y los usuarios pueden tener deshabilitada la ejecución de JavaScript por razones de seguridad.

- **Personalización:** Modifica el código JavaScript para realizar acciones adicionales al expirar, como deshabilitar ciertas funciones, redirigir a una página específica o registrar el evento. Además, si es necesario, puedes verificar solo la fecha de expiración sin especificar la hora.

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