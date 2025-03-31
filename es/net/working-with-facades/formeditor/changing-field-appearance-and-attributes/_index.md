---
title: Apariencia y atributos del campo
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/changing-field-appearance-and-attributes/
description: Esta sección explica cómo puedes cambiar la apariencia y los atributos del campo con la clase FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "La función introducida en la clase FormEditor del espacio de nombres Aspose.Pdf.Facades permite a los usuarios personalizar tanto la apariencia como los atributos de los campos de formulario en PDFs. Al utilizar métodos como SetFieldAppearance y SetFieldAttributes, los desarrolladores pueden modificar fácilmente los elementos visuales y comportamientos, incluidos los límites del campo, para mejorar la interacción del usuario y la eficiencia en la entrada de datos. Esta funcionalidad ofrece una mayor flexibilidad en el diseño de campos de formulario adaptados a necesidades específicas de la aplicación.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

La clase [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/FormEditor) del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades) te permite no solo cambiar la apariencia del campo de formulario, sino también el comportamiento del campo. En este artículo, veremos cómo podemos usar la clase FormEditor para cambiar la apariencia del campo, los atributos del campo y el límite del campo también.

{{% /alert %}}

## Detalles de implementación

El método [SetFieldAppearance](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) se utiliza para cambiar la apariencia de un campo de formulario. Toma AnnotationFlag como parámetro. AnnotationFlag es una enumeración que tiene diferentes miembros como Hidden o NoRotate, etc.

El método [SetFieldAttributes](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) se utiliza para cambiar el atributo de un campo de formulario. Un parámetro pasado a este método es la enumeración PropertyFlag que contiene miembros como ReadOnly o Required, etc.

La clase [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/FormEditor) también proporciona un método para establecer el límite del campo. Indica al campo cuántos caracteres se pueden llenar. El siguiente fragmento de código te muestra cómo se pueden usar todos estos métodos.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddFieldAndSetAttributes()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf"))
     {
         // Create an instance of FormEditor to manipulate form fields
         using (var formEditor = new Aspose.Pdf.Facades.FormEditor(doc))
         {
             // Add a new text field to the form on page 1 at the specified coordinates and size
             formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

             // Set the field attribute to make the text field required (user must fill it)
             formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

             // Set a character limit for the field (maximum 20 characters)
             formEditor.SetFieldLimit("text1", 20);

             // Save PDF document
             formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
         }
     }
 }
```