---
title: Modificando AcroForms
linktitle: Modificando AcroForms
type: docs
weight: 40
url: /es/java/modifing-form/
description: Esta sección explica cómo modificar formularios en su documento PDF con Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Establecer Fuente Personalizada para Campo de Formulario

Los campos de formulario en archivos PDF de Adobe pueden configurarse para usar fuentes predeterminadas específicas. Aspose.PDF permite a los desarrolladores aplicar cualquier fuente como fuente predeterminada del campo, ya sea una de las 14 fuentes básicas o una fuente personalizada. Para establecer y actualizar la fuente predeterminada utilizada para los campos de formulario, Aspose.PDF tiene la clase DefaultAppearance (Font font, double size, Color color). Esta clase puede ser accedida utilizando com.aspose.pdf.DefaultAppearance. Para usar este objeto, utilice el método setDefaultAppearance(..) de la clase Field.

El siguiente fragmento de código muestra cómo establecer la fuente predeterminada para el campo de formulario PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // Obtener campo de formulario particular del documento
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // Crear objeto de fuente
        Font font = FontRepository.findFont("ComicSansMS");

        // Establecer la información de la fuente para el campo de formulario
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // Guardar documento actualizado
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## Obtener/Establecer Límite de Campo

El método SetFieldLimit de la clase FormEditor te permite establecer un límite de campo, el número máximo de caracteres que se pueden ingresar en un campo.

```java
    public static void ObtenerLimiteMaximoDeCampo()
    {
        // Obtener el límite máximo de campo usando DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("Límite: " +field.getMaxLen());
    }
```

También puedes obtener el mismo valor usando el espacio de nombres Aspose.PDF.Facades usando el siguiente fragmento de código.

```java
    public static void ObtenerLimiteMaximoDeCampoFacades()
    {
        // Obtener el límite máximo de campo usando Facades
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("Límite: " + form.getFieldLimit("textbox1"));
    }
```

De manera similar, Aspose.PDF tiene un método que obtiene el límite de campo usando el enfoque DOM.
 El siguiente fragmento de código muestra los pasos.

```java
    public static void SettingMaximumFieldLimit()
    {
        // Obtener el límite máximo de campo usando DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Límite: " +field.getMaxLen());       
    }
```

## Eliminar un Campo de Formulario Particular de un Documento PDF

Todos los campos de formulario están contenidos en la colección Form del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Esta colección proporciona diferentes métodos que gestionan los campos de formulario, incluido el método de eliminación. Si deseas eliminar un campo en particular, pasa el nombre del campo como parámetro al método de eliminación y luego guarda el documento PDF actualizado.

El siguiente fragmento de código muestra cómo eliminar un campo con nombre de un documento PDF.

```java
    public static void DeleteParticularFormField()
    {    
        // Abrir un documento
        Document pdfDocument = new Document("input.pdf");

        // Eliminar un campo con nombre por su nombre
        pdfDocument.getForm().delete("textbox1");

        // Guardar el PDF modificado
        pdfDocument.save("output.pdf");
    }
```

## Modificar un Campo de Formulario en un Documento PDF

La colección Form del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) te permite gestionar campos de formulario en un documento PDF.

Para modificar un campo de formulario, obtén el campo de la colección Form y establece sus propiedades. Luego guarda el documento PDF actualizado.

El siguiente fragmento de código muestra cómo modificar un campo de formulario existente en un documento PDF.

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // Obtener un campo
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modificar el valor del campo
        textBoxField.setValue("Valor Actualizado");

        // Establecer el campo como solo lectura
        textBoxField.setReadOnly(true);

        // Guardar el documento actualizado
        pdfDocument.save("output.pdf");
    }
```

### Mover un Campo de Formulario a una Nueva Ubicación en un Archivo PDF

Si deseas mover un campo de formulario a una nueva ubicación en una página PDF, primero obtén el objeto del campo y luego especifica un nuevo valor para su método setRect.
 Un objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) con nuevas coordenadas se asigna al método setRect(..). Luego guarde el PDF actualizado utilizando el método save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código le muestra cómo mover un campo de formulario a una nueva ubicación.

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // Abrir un documento
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // Obtener un campo
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modificar la ubicación del campo
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // Guardar el documento modificado
        pdfDocument.save("output.pdf");
    }
}
```