---
title: ¿Cuál es la diferencia entre los formatos FDF, XML y XFDF?
type: docs
weight: 30
url: /net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Esta sección diferencia entre formularios XML, FDF y XFDF con Aspose.PDF Facades usando la Clase Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Mezclamos muchos términos diferentes como FDF, XML y XFDF. Todos estos términos están relacionados entre sí de alguna manera. Este artículo explora estos conceptos y su relación entre sí.

{{% /alert %}}

## Desentrañando Formularios

Aspose.PDF para .NET se utiliza para manipular documentos PDF estandarizados por Adobe. Y los documentos PDF contienen formularios interactivos llamados AcroForms. Estos formularios interactivos tienen una serie de campos de formulario, como combo, cuadro de texto y botón de opción. Los formularios interactivos de Adobe y los campos de formulario funcionan de la misma manera que un formulario HTML y sus campos de formulario.

Es posible almacenar los valores de los campos de formulario en un archivo separado: un archivo FDF (Formato de Datos de Formularios). Esto contiene los valores de los campos del formulario en formato clave/par. Los archivos FDF todavía se utilizan para este propósito. Pero Adobe también proporciona un tipo de FDF codificado en XML llamado XFDF. Un archivo XFDF almacena los valores de los campos del formulario de manera jerárquica utilizando etiquetas XML.

Con Aspose.PDF, los desarrolladores no solo pueden exportar los valores de los campos del formulario PDF a un archivo FDF o XFDF, sino también a un archivo XML. Todos estos archivos utilizan diferentes sintaxis para guardar los valores de los campos del formulario PDF. El ejemplo a continuación explica las diferencias.

Supongamos que hay algunos campos de formulario PDF cuyos valores necesitan ser presentados en formas FDF, XML y XFDF. Estos campos de formulario asumidos con sus nombres de campo y valores se muestran a continuación:

|**Field Name**|**Field Value**|
| :- | :- |
|Company|Aspose.com|
|Address.1|Sydney, Australia|
|Address.2|Additional Address Line|
Veamos cómo representar estos valores en formatos FDF, XML y XFDF.

### ¿Qué es el formato FDF?

Como sabemos, el archivo FDF almacena datos en formato Clave/Par donde /T representa una Clave, /V representa el Valor y los datos entre paréntesis () representan el contenido de una Clave o un Valor. Por ejemplo, /T(Company) significa que Company es la clave del campo y /V(Aspose.com) se refiere a un valor del campo.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### ¿Qué es el formato XML?

Los desarrolladores pueden representar cada campo de formulario PDF en forma de una etiqueta de campo, `<field>`. Cada etiqueta de campo tiene un atributo, nombre que muestra el nombre del campo y una subetiqueta, `<value>` que representa el valor del campo como se muestra a continuación:

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

### ### ¿Qué es el formato XFDF?

La representación de los datos anteriores en forma XFDF es similar a la forma XML, excepto con algunas diferencias. En los archivos XFDF, añadimos su Espacio de Nombres XML, que es <http://ns.adpbe.com/xfdf/> y hay una etiqueta adicional, `<f>` que se utiliza para apuntar hacia el documento PDF que contiene estos campos de formulario PDF. Al igual que XML, XFDF también contiene campos en forma de etiquetas de campo, `<field>` como se muestra a continuación:

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

Aspose.PDF para .NET proporciona la capacidad de crear, editar y completar formularios PDF ya creados. Contiene la clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), que tiene la función llamada [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index), y toma dos parámetros, es decir, el nombre del campo que necesita ser llenado y el valor del campo. Por lo tanto, para llenar los campos del formulario, debe conocer el nombre exacto del campo del formulario. A menudo nos encontramos con el escenario en el que necesitamos llenar el formulario que se crea en alguna herramienta, es decir. Adobe Designer, y no estamos seguros sobre los nombres de los campos del formulario. Para cumplir con nuestro requisito, necesitamos leer los nombres de todos los campos del formulario PDF. La clase [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) proporciona la propiedad llamada [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) que devuelve todos los nombres de los campos y devuelve null si el PDF no tiene campos. Pero esta propiedad devolverá todos los nombres de los campos del formulario PDF y no estaremos seguros de qué nombre corresponde a qué campo en el formulario.

Como solución a este problema, necesitaríamos los atributos de apariencia de cada campo. [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) la clase tiene una función llamada GetFieldFacade que devuelve atributos, incluyendo ubicación, color, estilo de borde, fuente, elemento de lista, etc. Para guardar estos valores utilizaremos la clase [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), que se usa para registrar atributos visuales de los campos. Una vez que tenemos estos atributos, podemos añadir un campo de texto debajo de cada campo que mostraría el nombre del campo. Aquí surge una pregunta: ¿cómo determinaríamos la ubicación donde añadir el campo de texto? La solución a este problema es la propiedad Box en la clase [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), que contiene la ubicación del campo. Guardaríamos estos valores en un array de tipo rectángulo y usaríamos estos valores para identificar la posición donde añadir los nuevos campos de texto. En el espacio de nombres Aspose.Pdf.Facades, tenemos una clase llamada [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) que proporciona la capacidad de manipular formularios PDF. Open a PDF form add a text field beneath every existing form field and save the PDF form with new name.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}