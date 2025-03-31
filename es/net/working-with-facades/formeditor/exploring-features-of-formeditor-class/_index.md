---
title: Explorando las características de la clase FormEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/exploring-features-of-formeditor-class/
description: Puedes aprender detalles sobre la exploración de las características de la clase FormEditor con la biblioteca Aspose.PDF para .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exploring features of FormEditor class",
    "alternativeHeadline": "Enhancing PDF Forms with FormEditor Class",
    "abstract": "Descubre las capacidades mejoradas de la clase FormEditor dentro de la biblioteca Aspose.PDF for .NET, diseñada para la manipulación sin esfuerzo de formularios PDF interactivos. Esta característica permite a los desarrolladores agregar, editar y configurar campos de formulario de manera fluida, con métodos fáciles de usar para agilizar el proceso de modificación. Optimiza el manejo de tus formularios PDF aprovechando las funcionalidades integrales de FormEditor para elevar tus flujos de trabajo de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "358",
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
    "url": "/net/exploring-features-of-formeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/exploring-features-of-formeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

Los documentos PDF a veces contienen formularios interactivos, que se conocen como AcroForm. Es como un formulario utilizado en las páginas web. Estos formularios contienen diferentes tipos de controles, es decir, cuadros de texto, casillas de verificación y botones, etc. Un desarrollador que trabaja con archivos PDF a veces puede tener que editar estos formularios. En este artículo, analizaremos los detalles de cómo el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades) nos permite hacer eso.

{{% /alert %}}

## Detalles de implementación

Los desarrolladores pueden usar el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades) no solo para agregar nuevos formularios y campos de formulario en un documento PDF, sino también para permitirte editar campos existentes. El alcance de este artículo se limita a las características de [Aspose.PDF for .NET](/pdf/es/net/) que tratan con la edición de formularios.

[FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor) es la clase que contiene la mayoría de los métodos y propiedades que permiten a los desarrolladores editar campos de formulario. No solo puedes agregar nuevos campos, sino también eliminar campos existentes, mover un campo a otra posición, cambiar el nombre del campo o atributos, etc. La lista de características proporcionadas por esta clase es bastante completa, y es muy fácil trabajar con los campos de formulario utilizando esta clase.

Estos métodos se pueden dividir en dos categorías principales, una de las cuales se utiliza para manipular los campos, y la otra se utiliza para establecer los nuevos atributos de estos campos. Los métodos que podemos agrupar bajo la primera categoría incluyen AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField y RenameField, etc. En la segunda categoría de métodos se pueden incluir SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript. El siguiente fragmento de código te muestra algunos de los métodos de la clase FormEditor en funcionamiento:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExploringFormEditorFeatures()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "inFile.pdf"))
    {
        // Create instance of FormEditor
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            // Add field in the PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "field1", 1, 300, 500, 350, 525);

            // Add List field in PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225);

            // Add list items
            editor.AddListItem("field2", "item 1");
            editor.AddListItem("field2", "item 2");

            // Add submit button
            editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http:// Testwebsite.com/testpage", 200, 200, 250, 225);

            // Delete list item
                editor.DelListItem("field2", "item 1");

            // Move field to new position
            editor.MoveField("field1", 10, 10, 50, 50);

            // Remove existing field from the PDF
            editor.RemoveField("field1");

            // Rename an existing field
            editor.RenameField("field1", "newfieldname");

            // Reset all visual attributes to empty value
            editor.ResetFacade();

            // Set the alignment style of a text field
            editor.SetFieldAlignment("field1", Aspose.Pdf.Facades.FormFieldFacade.AlignLeft);

            // Set appearance of the field
            editor.SetFieldAppearance("field1", Aspose.Pdf.Annotations.AnnotationFlags.NoRotate);

            // Set field attributes i.e. ReadOnly, Required
            editor.SetFieldAttribute("field1", Aspose.Pdf.Facades.PropertyFlag.ReadOnly);

            // Set field limit
            editor.SetFieldLimit("field1", 25);

            // Save modifications in the output file
            editor.Save(dataDir + "FormEditorFeatures2_out.pdf");                    
        }
    }
}
```