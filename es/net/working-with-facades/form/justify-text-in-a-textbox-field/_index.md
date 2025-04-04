---
title: Justificar texto en un campo de cuadro de texto
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/justify-text-in-a-textbox-field/
description: Este artículo te muestra cómo justificar texto en un campo de cuadro de texto utilizando la clase Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Justify Text in a Textbox Field",
    "alternativeHeadline": "Justify Text in PDF Textbox Fields Effortlessly",
    "abstract": "La función permite a los usuarios justificar texto dentro de un campo de cuadro de texto en documentos PDF utilizando la clase FormEditor del espacio de nombres Aspose.Pdf.Facades. Al utilizar la opción AlignJustified, los usuarios pueden lograr una alineación de texto visualmente atractiva mientras mantienen la funcionalidad, aunque la alineación justificada no es compatible durante la entrada activa. Esto mejora la presentación de los datos del formulario en archivos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "283",
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
    "url": "/net/justify-text-in-a-textbox-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/justify-text-in-a-textbox-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

En este artículo, te mostraremos cómo justificar texto en un campo de cuadro de texto en un archivo PDF.

{{% /alert %}}

## Detalles de implementación

La clase [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor) en el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades) ofrece la capacidad de decorar un campo de formulario PDF. Ahora, si tu requisito es justificar el texto en un campo de cuadro de texto, puedes lograrlo fácilmente utilizando el valor [AlignJustified](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) de la enumeración [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade) y llamando al método [FormEditor.DecorateField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). En el siguiente ejemplo, primero llenaremos un campo de cuadro de texto utilizando el método [FillField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/fillfield/index) de la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form). Después de eso, utilizaremos la clase FormEditor para justificar el texto en el campo de cuadro de texto. El siguiente fragmento de código te muestra cómo justificar texto en un campo de cuadro de texto.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void JustifyTextInTextboxField()
{
    // The path to the documents directory 
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Open PDF document
    using (var source = File.Open(dataDir + "JustifyText.pdf", FileMode.Open))
    {
        using (var ms = new MemoryStream())
        {
            // Create Form Object
            var form = new Aspose.Pdf.Facades.Form();
            // Bind PDF document
            form.BindPdf(source);
            // Fill Text Field
            form.FillField("Text1", "Thank you for using Aspose");
            // Save PDF document in Memory Stream
            form.Save(ms);
            ms.Seek(0, SeekOrigin.Begin);

            using (var dest = new FileStream(dataDir + "JustifyText_out.pdf", FileMode.Create))
            {
                // Create formEditor Object
                using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
                {
                    // Open PDF from memory stream
                    formEditor.BindPdf(ms);
                    // Set Text Alignment as Justified
                    formEditor.Facade.Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignJustified;
                    // Decorate form field
                    formEditor.DecorateField();
                    // Save PDF document
                    formEditor.Save(dest);
                }
            }
        }
    }
}
```
Ten en cuenta que la alineación justificada no es compatible con PDF, por lo que el texto se alineará a la izquierda cuando ingreses el texto en el campo de cuadro de texto. Pero cuando el campo no está activo, el texto está justificado.