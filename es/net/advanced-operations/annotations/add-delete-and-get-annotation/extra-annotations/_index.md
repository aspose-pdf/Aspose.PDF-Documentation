---
title: Anotaciones Adicionales usando C#
linktitle: Anotaciones Adicionales
type: docs
weight: 60
url: es/net/extra-annotations/
description: Esta sección describe cómo agregar, obtener y eliminar tipos adicionales de anotaciones de su documento PDF.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotaciones Adicionales usando C#",
    "alternativeHeadline": "Cómo agregar Anotaciones Adicionales en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, anotación de enlace, anotación de cuidado",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección describe cómo agregar, obtener y eliminar tipos adicionales de anotaciones de su documento PDF."
}
</script>

## Cómo agregar anotación de intercalación en un archivo PDF existente

La anotación de intercalación es un símbolo que indica edición de texto. La anotación de intercalación también es una anotación de marcado, por lo que la clase Caret se deriva de la clase Markup y también proporciona funciones para obtener o establecer propiedades de la anotación de intercalación y restablecer el flujo de la apariencia de la anotación de intercalación.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Pasos con los que creamos la anotación de intercalación:

1. Cargar el archivo PDF - nuevo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Crear una nueva [Anotación de Intercalación](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) y establecer los parámetros de Caret (nuevo Rectángulo, título, Asunto, Banderas, color, ancho, Estilo de inicio y Estilo de finalización). Esta anotación se utiliza para indicar la inserción de texto.
1. Crea una nueva [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) y establece parámetros (nuevo Rectangle, título, color, nuevos QuadPoints y nuevos puntos, Asunto, InReplyTo, Tipo de Respuesta).
1. Después podemos añadir anotaciones a la página.

El siguiente fragmento de código muestra cómo agregar una Anotación de Cuidado a un archivo PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // La ruta al directorio de documentos.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // Cargar el archivo PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // Esta anotación se usa para indicar la inserción de texto
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "Usuario de Aspose",
                Subject = "Texto insertado 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // Esta anotación se usa para indicar el reemplazo de texto
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "Texto insertado 2",
                Title = "Usuario de Aspose",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "Tachado",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```

### Obtener Anotación de Cuidado

Por favor intenta usar el siguiente fragmento de código para obtener una Anotación de Cuidado en un documento PDF

```csharp
public static void GetCaretAnnotation()
{
    // Cargar el archivo PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### Eliminar Anotación de Cuidado

El siguiente fragmento de código muestra cómo eliminar una Anotación de Cuidado de un archivo PDF.

```csharp
public static void DeleteCaretAnnotation()
{
    // Cargar el archivo PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## Redactar cierta región de la página con la Anotación de Redacción usando Aspose.PDF para .NET

Aspose.PDF para .NET soporta la característica de añadir y manipular Anotaciones en un archivo PDF existente. Recientemente, algunos de nuestros clientes solicitaron redactar (eliminar texto, imagen, etc. de) ciertas regiones de una página de un documento PDF. Para cumplir con este requerimiento, se proporciona una clase llamada RedactionAnnotation, que puede ser utilizada para redactar ciertas regiones de la página o puede ser utilizada para manipular RedactionAnnotations existentes y redactarlas (es decir, aplanar la anotación y eliminar el texto debajo de ella).

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document doc = new Document(dataDir + "input.pdf");

// Crear instancia de RedactionAnnotation para una región específica de la página
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// Texto a imprimir en la anotación de redacción
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Repetir texto de superposición sobre la anotación de redacción
annot.Repeat = true;
// Añadir anotación a la colección de anotaciones de la primera página
doc.Pages[1].Annotations.Add(annot);
// Aplana la anotación y redacta el contenido de la página (es decir, elimina texto e imagen
// Bajo la anotación redactada)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### Enfoque de Fachadas

El espacio de nombres Aspose.PDF.Facades también tiene una clase llamada [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) que proporciona la función de manipular Anotaciones existentes dentro del archivo PDF. Esta clase contiene un método llamado [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) que ofrece la capacidad de eliminar ciertas regiones de la página.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// Redactar cierta región de la página
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save(dataDir + "FacadesApproach_out.pdf");
```

<script type="application/ld+json">

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
    "applicationCategory": "Biblioteca de Manipulación PDF para .NET",
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

