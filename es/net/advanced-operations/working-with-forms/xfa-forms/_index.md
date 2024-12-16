---
title: Trabajando con Formularios XFA
linktitle: Formularios XFA
type: docs
weight: 20
url: /es/net/xfa-forms/
description: Aspose.PDF para .NET API le permite trabajar con campos XFA y XFA Acroform en un documento PDF. Las fachadas de Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con Formularios XFA",
    "alternativeHeadline": "Rellenar, Convertir y Obtener Formularios XFA en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, rellenar formulario xfa, obtener formulario xfa, convertir formulario xfa",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET API le permite trabajar con campos XFA y XFA Acroform en un documento PDF. Las fachadas de Aspose.PDF."
}
</script>
{{% alert color="primary" %}}

Los formularios dinámicos se basan en una especificación XML conocida como XFA, la "Arquitectura de Formularios XML". También puede convertir el formulario XFA dinámico en Acroform estándar. La información sobre el formulario (en lo que respecta al PDF) es muy vaga: especifica que existen campos, con propiedades y eventos de JavaScript, pero no especifica ningún renderizado. Los objetos del formulario XFA se dibujan en el momento de cargar el documento.

{{% /alert %}}

La clase Form proporciona la capacidad para tratar con AcroForm estático y puedes obtener una instancia de campo particular utilizando el método GetFieldFacade(..) de la clase Form. Sin embargo, los campos XFA no se pueden acceder mediante el método Form.GetFieldFacade(..). En su lugar, usa [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) para obtener/establecer valores de campos y manipular la plantilla de campo XFA (establecer propiedades de campo).

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Llenar campos XFA

El siguiente fragmento de código muestra cómo llenar campos en un formulario XFA.
El siguiente fragmento de código te muestra cómo llenar campos en un formulario XFA.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Cargar formulario XFA
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// Obtener nombres de los campos del formulario XFA
string[] names = doc.Form.XFA.FieldNames;

// Establecer valores de los campos
doc.Form.XFA[names[0]] = "Campo 0";
doc.Form.XFA[names[1]] = "Campo 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
```

## Convertir XFA a Acroform

{{% alert color="primary" %}}

Prueba en línea
Puedes verificar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace: [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

Los formularios dinámicos se basan en una especificación XML conocida como XFA, la "Arquitectura de Formularios XML".
Los formularios dinámicos se basan en una especificación XML conocida como XFA, la "Arquitectura de Formularios XML".

Actualmente, PDF admite dos métodos diferentes para integrar datos y formularios PDF:

- AcroForms (también conocidos como formularios Acrobat), introducidos e incluidos en la especificación del formato PDF 1.2.
- Formularios de Arquitectura de Formularios XML de Adobe (XFA), introducidos en la especificación del formato PDF 1.5 como una característica opcional (La especificación XFA no está incluida en la especificación PDF, solo se hace referencia a ella.)

No podemos extraer o manipular páginas de Formularios XFA, porque el contenido del formulario se genera en tiempo de ejecución (durante la visualización del formulario XFA) dentro de la aplicación que intenta mostrar o renderizar el formulario XFA. Aspose.PDF tiene una característica que permite a los desarrolladores convertir formularios XFA en AcroForms estándar.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Cargar formulario XFA dinámico
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// Establecer el tipo de campos de formulario como AcroForm estándar
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// Guardar el PDF resultante
document.Save(dataDir);
```
## Obtener propiedades de campo XFA

Para acceder a las propiedades del campo, primero usa Document.Form.XFA.Template para acceder a la plantilla del campo. El siguiente fragmento de código muestra los pasos para obtener las coordenadas X e Y de un campo de formulario XFA.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Cargar formulario XFA
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// Establecer valores de campo
doc.Form.XFA[names[0]] = "Campo 0";
doc.Form.XFA[names[1]] = "Campo 1";

// Obtener posición del campo
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// Obtener posición del campo
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
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


