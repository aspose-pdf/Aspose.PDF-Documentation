---
title: ¿Cuál es la diferencia entre los formatos FDF, XML y XFDF?
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Esta sección diferencia entre los formularios XML, FDF y XFDF con las fachadas de Aspose.PDF utilizando la clase Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "Descubre las diferencias entre los formatos FDF, XML y XFDF en la manipulación de datos de formularios PDF a través de Aspose.PDF for .NET. Esta función permite a los desarrolladores exportar sin problemas los valores de los campos de formularios interactivos en varios formatos, cada uno con su propia sintaxis, mientras se mejora la comprensión y el uso de estos tipos de archivos esenciales en el procesamiento de PDF. Optimiza el manejo de formularios PDF con información detallada sobre cómo representar campos de formularios en diferentes formatos de datos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
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
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

Hemos mezclado muchos términos diferentes como FDF, XML y XFDF. Todos estos términos están relacionados entre sí de alguna manera. Este artículo explora estos conceptos y su relación entre ellos.

{{% /alert %}}

## Desentrañando Formularios

Aspose.PDF for .NET se utiliza para manipular documentos PDF estandarizados por Adobe. Y los documentos PDF contienen formularios interactivos llamados AcroForms. Estos formularios interactivos tienen una serie de campos de formulario, como combo, cuadro de texto y botón de opción. Los formularios interactivos de Adobe y los campos de formulario funcionan de la misma manera que un formulario HTML y sus campos de formulario.

Es posible almacenar los valores de los campos de formulario en un archivo separado: un archivo FDF (Formato de Datos de Formularios). Este contiene los valores de los campos de formulario en forma de clave/valor. Los archivos FDF todavía se utilizan para este propósito. Pero Adobe también proporciona un tipo de FDF codificado en XML llamado XFDF. Un archivo XFDF almacena los valores de los campos de formulario de manera jerárquica utilizando etiquetas XML.

Con Aspose.PDF, los desarrolladores no solo pueden exportar los valores de los campos de formulario PDF a un archivo FDF o XFDF, sino también a un archivo XML. Todos estos archivos utilizan diferentes sintaxis para guardar los valores de los campos de formulario PDF. El siguiente ejemplo explica las diferencias.

Supongamos que hay algunos campos de formulario PDF cuyos valores necesitan ser presentados en formatos FDF, XML y XFDF. Estos campos de formulario supuestos con sus nombres y valores se muestran a continuación:

|**Nombre del Campo**|**Valor del Campo**|
| :- | :- |
|Empresa|Aspose.com|
|Dirección.1|Sídney, Australia|
|Dirección.2|Línea de dirección adicional|
Veamos cómo representar estos valores en formatos FDF, XML y XFDF.

### ¿Qué es el formato FDF?

Como sabemos, el archivo FDF almacena datos en forma de clave/valor donde /T representa una clave, /V representa el valor y los datos entre paréntesis () representan el contenido de una clave o un valor. Por ejemplo, /T(Company) significa que Company es la clave del campo y /V(Aspose.com) está destinado a un valor de campo.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Línea de dirección adicional)

### ¿Qué es el formato XML? 

Los desarrolladores pueden representar cada campo de formulario PDF en forma de una etiqueta de campo, `<field>`. Cada etiqueta de campo tiene un atributo, name que muestra el nombre del campo y una subetiqueta, `<value>` que representa el valor del campo como se muestra a continuación:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### ¿Qué es el formato XFDF?  

La representación de los datos anteriores en forma XFDF es similar a la forma XML, excepto por algunas diferencias. En los archivos XFDF, agregamos su espacio de nombres XML, que es <http://ns.adpbe.com/xfdf/> y hay una etiqueta adicional, `<f>` que se utiliza para señalar el documento PDF que contiene estos campos de formulario PDF. Al igual que XML, XFDF también contiene campos en forma de etiquetas de campo, `<field>` como se muestra a continuación:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### Identificando los nombres de los campos de formulario

Aspose.PDF for .NET proporciona la capacidad de crear, editar y llenar formularios PDF ya creados. Contiene la clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form), que tiene la función llamada [FillField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/fillfield/index), y toma dos parámetros, es decir, el nombre del campo que necesita ser llenado y el valor del campo. Por lo tanto, para llenar los campos de formulario, debes conocer el nombre exacto del campo de formulario.
A menudo nos encontramos con el escenario en el que necesitamos llenar un formulario que fue creado en alguna herramienta, es decir, Adobe Designer, y no estamos seguros sobre los nombres de los campos de formulario. Para cumplir con nuestro requisito, necesitamos leer los nombres de todos los campos de formulario PDF. La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form) proporciona la propiedad llamada [FieldsNames](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/properties/fieldnames) que devuelve todos los nombres de los campos y devuelve nulo si el PDF no tiene campo. Pero esta propiedad devolverá todos los nombres de los campos de formulario PDF y no estaremos seguros de qué nombre corresponde a qué campo en el formulario.

Como solución a este problema, necesitaríamos los atributos de apariencia de cada campo. La clase [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) tiene una función llamada GetFieldFacade que devuelve atributos, incluyendo ubicación, color, estilo de borde, fuente, elemento de lista, etc. Para guardar estos valores, utilizaremos la clase [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade), que se utiliza para registrar los atributos visuales de los campos. Una vez que tengamos estos atributos, podemos agregar un campo de texto debajo de cada campo que mostraría el nombre del campo. Aquí surge la pregunta de cómo determinaríamos la ubicación donde agregar el campo de texto. La solución a este problema es la propiedad Box en la clase [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade), que contiene la ubicación del campo. Guardaríamos estos valores en un arreglo de tipo rectángulo y usaríamos estos valores para identificar la posición donde agregar los nuevos campos de texto.
En el espacio de nombres Aspose.Pdf.Facades, tenemos una clase llamada [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor) que proporciona la capacidad de manipular formularios PDF. Abre un formulario PDF, agrega un campo de texto debajo de cada campo de formulario existente y guarda el formulario PDF con un nuevo nombre.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```