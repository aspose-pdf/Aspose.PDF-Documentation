---
title: PDF Tooltip usando C#
linktitle: PDF Tooltip
type: docs
weight: 20
url: /es/net/pdf-tooltip/
description: Aprende cómo agregar un tooltip al fragmento de texto en PDF usando C# y Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip usando C#",
    "alternativeHeadline": "Agregar PDF Tooltip al Texto",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, agregar pdf tooltip",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2022-02-04",
    "description": "Aprende cómo agregar un tooltip al fragmento de texto en PDF usando C# y Aspose.PDF"
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Agregar Tooltip al Texto Buscado añadiendo un Botón Invisible

A menudo es necesario agregar algunos detalles a una frase o palabra específica como un tooltip en el documento PDF para que se muestre cuando el usuario coloca el cursor del ratón sobre el texto. Aspose.PDF para .NET proporciona esta característica para crear tooltips agregando un botón invisible sobre el texto buscado. El siguiente fragmento de código te mostrará cómo lograr esta funcionalidad:

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// Crear documento de muestra con texto
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Mueva el cursor del ratón aquí para mostrar un tooltip"));
doc.Pages[1].Paragraphs.Add(new TextFragment("Mueva el cursor del ratón aquí para mostrar un tooltip muy largo"));
doc.Save(outputFile);

// Abrir documento con texto
Document document = new Document(outputFile);
// Crear objeto TextAbsorber para encontrar todas las frases que coincidan con la expresión regular
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Mueva el cursor del ratón aquí para mostrar un tooltip");
// Aceptar el absorber para las páginas del documento
document.Pages.Accept(absorber);
// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragments = absorber.TextFragments;

// Bucle a través de los fragmentos
foreach (TextFragment fragment in textFragments)
{
    // Crear botón invisible en la posición del fragmento de texto
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // El valor AlternateName se mostrará como tooltip por una aplicación visor
    field.AlternateName = "Tooltip para texto.";
    // Agregar campo de botón al documento
    document.Form.Add(field);
}

// A continuación será un ejemplo de tooltip muy largo
absorber = new TextFragmentAbsorber("Mueva el cursor del ratón aquí para mostrar un tooltip muy largo");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // Establecer texto muy largo
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// Guardar documento
document.Save(outputFile);
```
{{% alert color="primary" %}}

En relación con la longitud del tooltip, el texto del tooltip está contenido en el documento PDF como tipo de cadena PDF, fuera del flujo de contenido. No hay una restricción efectiva sobre dichas cadenas en los archivos PDF (Ver Apéndice C de Referencia PDF.). Sin embargo, un lector conforme (por ejemplo, Adobe Acrobat) que funcione en un procesador particular y en un entorno operativo específico sí tiene dicho límite. Por favor, consulte la documentación de su aplicación lectora de PDF.

{{% /alert %}}

## Crear un Bloque de Texto Oculto y Mostrarlo al Pasar el Ratón

En Aspose.PDF, se implementa una característica para ocultar acciones con la cual es posible mostrar/ocultar un campo de cuadro de texto (u otro tipo de anotación) al entrar/salir el ratón sobre algún botón invisible. Para este propósito, se utiliza la Clase Aspose.Pdf.Annotations.HideAction para asignar la acción de mostrar/ocultar al bloque de texto. Por favor, use el siguiente fragmento de código para Mostrar/Ocultar un Bloque de Texto al Entrar/Salir del Ratón.

También tenga en cuenta que las acciones PDF en los documentos funcionan bien en los lectores conformes (por ejemplo,
Tenga en cuenta que las acciones PDF en los documentos funcionan correctamente en los lectores conformes (por ejemplo,

- Todas las implementaciones de la acción de ocultar en documentos PDF funcionan correctamente en Internet Explorer v.11.0.
- Todas las implementaciones de la acción de ocultar también funcionan en Opera v.12.14, pero notamos cierto retraso en la respuesta en la primera apertura del documento.
- Solo la implementación utilizando el constructor HideAction que acepta el nombre del campo funciona si Google Chrome v.61.0 navega por el documento; Por favor, use los constructores correspondientes si navegar en Google Chrome es significativo:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// Crear documento de muestra con texto
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Mueva el cursor del ratón aquí para mostrar texto flotante"));
doc.Save(outputFile);

// Abrir documento con texto
Document document = new Document(outputFile);
// Crear objeto TextAbsorber para encontrar todas las frases que coinciden con la expresión regular
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Mueva el cursor del ratón aquí para mostrar texto flotante");
// Aceptar el absorber para las páginas del documento
document.Pages.Accept(absorber);
// Obtener el primer fragmento de texto extraído
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// Crear campo de texto oculto para texto flotante en el rectángulo especificado de la página
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// Establecer texto para mostrar como valor del campo
floatingField.Value = "Este es el \"campo de texto flotante\".";
// Recomendamos hacer el campo 'solo lectura' para este escenario
floatingField.ReadOnly = true;
// Establecer la bandera 'oculto' para hacer el campo invisible al abrir el documento
floatingField.Flags |= AnnotationFlags.Hidden;

// Establecer un nombre de campo único no es necesario pero está permitido
floatingField.PartialName = "FloatingField_1";

// Establecer características de la apariencia del campo no es necesario pero lo mejora
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// Agregar campo de texto al documento
document.Form.Add(floatingField);

// Crear botón invisible en la posición del fragmento de texto
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// Crear nueva acción de ocultar para el campo especificado (anotación) y bandera de invisibilidad.
// (También puede referir al campo flotante por el nombre si lo especificó anteriormente.)
// Agregar acciones al entrar/salir del ratón en el campo de botón invisible
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// Agregar campo de botón al documento
document.Form.Add(buttonField);

// Guardar documento
document.Save(outputFile);
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

