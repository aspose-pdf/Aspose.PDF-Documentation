---
title: Identificación de nombres de campos de formulario
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/identifying-form-fields-names/
description: Aspose.Pdf.Facades permite identificar los nombres de los campos de formulario utilizando la clase Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "La funcionalidad en Aspose.PDF for .NET simplifica el proceso de identificación de nombres de campos de formulario en documentos PDF. Al utilizar la clase Form y sus atributos, los usuarios pueden recuperar y mostrar fácilmente los nombres de los campos junto con sus campos correspondientes, agilizando el llenado y la edición de formularios PDF. Esta característica mejora la experiencia del usuario al garantizar una manipulación precisa de los campos, especialmente al trabajar con formularios creados en herramientas externas como Adobe Designer",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

[Aspose.PDF for .NET](/pdf/es/net/) proporciona la capacidad de crear, editar y llenar formularios PDF ya creados. El espacio de nombres [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) contiene la clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), que contiene la función llamada [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) y toma dos argumentos, es decir, el nombre del campo y el valor del campo. Por lo tanto, para llenar los campos del formulario, debes conocer el nombre exacto del campo del formulario.

## Detalles de implementación

A menudo nos encontramos con un escenario en el que necesitamos llenar un formulario creado en alguna herramienta, es decir, Adobe Designer, y no estamos seguros sobre los nombres de los campos del formulario. Por lo tanto, para llenar los campos del formulario, primero necesitamos leer los nombres de todos los campos del formulario PDF. La clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) proporciona la propiedad llamada [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) que devuelve todos los nombres de los campos y devuelve null si el PDF no contiene ningún campo. Sin embargo, al usar esta propiedad, obtenemos los nombres de todos los campos en el formulario PDF y podríamos no estar seguros de qué nombre corresponde a qué campo en el formulario.

Como solución a este problema, utilizaremos los atributos de apariencia de cada campo. La clase Form tiene una función llamada [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) que devuelve atributos, incluyendo ubicación, color, estilo de borde, fuente, elemento de lista, etc. Para guardar estos valores, necesitamos usar la clase [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), que se utiliza para registrar los atributos visuales de los campos. Una vez que tengamos estos atributos, podemos agregar un campo de texto debajo de cada campo que mostraría el nombre del campo.

{{% alert color="primary" %}}
En este punto, surge la pregunta "¿cómo determinaríamos la ubicación donde agregar el campo de texto?"
{{% /alert %}}

{{% alert color="primary" %}}
La solución a este problema es la propiedad Box en la clase [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), que contiene la ubicación del campo. Necesitamos guardar estos valores en un arreglo de tipo rectángulo y usar estos valores para identificar la posición donde agregar los nuevos campos de texto.
{{% /alert %}}

En el espacio de nombres [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) tenemos una clase llamada [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) que proporciona la capacidad de manipular formularios PDF. Abre un formulario PDF; agrega un campo de texto debajo de cada campo de formulario existente y guarda el formulario PDF con un nuevo nombre.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyFormFieldsNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location
        box[i] = facade.Box;
    }
    // Save PDF document
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
                "TextField" + i, allfields[i], 1, 
                box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "IdentifyFormFields_out.pdf");
        }
    }
}
```