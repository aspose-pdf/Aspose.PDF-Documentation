---
title: Extraer Datos AcroForms
linktitle: Extraer Datos AcroForms
type: docs
weight: 30
url: /es/java/extract-form/
description: Esta sección explica cómo extraer formularios de su documento PDF con Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Valor de un Campo Individual del Documento PDF

El [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) del campo de formulario le permite obtener el valor de un campo en particular.

Para obtener el valor, obtenga el campo de formulario de la colección Form del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Este ejemplo selecciona un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) y recupera su valor utilizando el [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // Abrir un documento
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // Obtener un campo
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Obtener el nombre del campo
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // Obtener el valor del campo
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## Obtener Valores de Todos los Campos en un Documento PDF

Para obtener valores de todos los campos en un documento PDF, necesitas navegar a través de todos los campos de formulario y luego obtener el valor usando el [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--). Obtén cada campo de la colección Form usando el objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y su [método getForm()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) y obtén la lista de campos de formulario en un array Field usando getFields() y recorre el array para obtener el valor de los campos.

El siguiente fragmento de código muestra cómo obtener los valores de todos los campos en un documento PDF.

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // Abrir documento
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("Campo de formulario: " + fields[i].getFullName());
            System.out.println("Campo de formulario: " + fields[i].getValue());
        }

    }
}
```


## Obtener Campos de Formulario de una Región Específica de un Archivo PDF

En algunos casos, se requiere obtener datos no de todo el formulario, sino, por ejemplo, solo del cuarto superior izquierdo de la hoja impresa.
Con Aspose.PDF para Java, esto no es un problema. Puede especificar una región para filtrar los campos que están fuera de la región dada del archivo PDF. Para obtener campos de formulario de un área específica de un archivo PDF:

1. Abra el archivo PDF utilizando el objeto Document.
1. Obtenga el formulario de la colección Forms del documento.
1. Especifique la región rectangular y pásela al método [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) del objeto Form. Se devuelve una colección [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field).
1. Utilícelo para manipular los campos.

El siguiente fragmento de código muestra cómo obtener campos de formulario en una región rectangular específica de un archivo PDF.

```java
public static void GetValuesFromSpecificRegion() {
    // Abrir archivo PDF
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // Crear objeto rectángulo para obtener campos en esa área
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // Obtener el formulario PDF
    com.aspose.pdf.Form form = doc.getForm();

    // Obtener campos en el área rectangular
    Field[] fields = form.getFieldsInRect(rectangle);

    // Mostrar nombres y valores de los campos
    for (Field field : fields)
    {
        // Mostrar propiedades de colocación de imagen para todas las colocaciones
        System.out.println("Nombre del Campo: " + field.getFullName() + "-" + "Valor del Campo: " + field.getValue());
    }
}
```