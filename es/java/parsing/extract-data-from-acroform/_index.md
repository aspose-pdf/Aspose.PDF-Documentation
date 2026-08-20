---
title: Extraer datos de AcroForm usando Java
linktitle: Extraer datos de AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: Aspose.PDF facilita la extracción de datos de campos de formulario de archivos PDF. Aprenda a extraer datos de AcroForms y guardarlos en formato JSON, XML o FDF.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer datos de AcroForm a través de Java
Abstract: Este artículo explica cómo extraer y exportar datos AcroForm de archivos PDF con Aspose.PDF para Java. Cubre la lectura de todos los campos del formulario, la recuperación de un valor de campo por nombre, la exportación de datos de campo a JSON y la escritura de datos de formulario en formatos XML, FDF y XFDF.
---
## Extraer todos los campos del formulario



Utilice `com.aspose.pdf.facades.Form` para leer nombres y valores de campos sin trabajar en el modelo de objetos del documento completo.


1. 
Abra el formulario PDF de origen con la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) para que los campos de AcroForm se puedan leer sin atravesar el modelo de objetos del documento completo.

1. 
Llame a `getFieldNames()` para recopilar todos los identificadores de campo presentes en el formulario.

1. 
Repita esos nombres de campo y llame a `getField(fieldName)` para leer cada valor de campo.
1. Cree la cadena de salida a partir de los pares clave-valor extraídos e imprima los datos agregados del formulario.

1. 
Cierre la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) en el bloque `finally`.


```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## 
Recuperar un valor de campo por nombre


1. 
Abra el formulario PDF de origen con la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. 
Llame a `getField(fieldName)` con el nombre del campo solicitado para leer su valor actual de los datos de AcroForm.
1. Imprima el valor del campo extraído.

1. 
Cierre la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) en el bloque `finally`.


```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## 
Exportar campos de formulario a JSON


1. 
Abra el formulario PDF de origen con la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. 
Llame a `getFieldNames()` para recopilar todos los identificadores de campo disponibles en AcroForm.
1. Itere a través de esos campos, escape los nombres y valores y cree una cadena de objeto JSON.

1. 
Escriba el resultado JSON en el archivo de salida.

1. 
Cierre la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) en el bloque `finally`.


```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## 
Exportar datos de formulario a XML, FDF y XFDF


1. 
Cree la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sin vincular ningún documento todavía.
1. Abra una secuencia de salida para el archivo XML y vincule el PDF de origen a la fachada con `bindPdf(...)`.

1. 
Llame a `exportXml(stream)` para que los datos del campo del formulario actual se serialicen como XML.

1. 
Cierre la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) una vez completada la exportación.


```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

1. 
Cree la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sin vincular ningún documento todavía.

1. 
Abra una secuencia de salida para el archivo FDF y vincule el PDF de origen a la fachada con `bindPdf(...)`.
1. Llame a `exportFdf(stream)` para que los datos del campo del formulario se serialicen en formato FDF.

1. 
Cierre la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) una vez completada la exportación.


```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

1. 
Cree la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sin vincular ningún documento todavía.

1. 
Abra una secuencia de salida para el archivo XFDF y vincule el PDF de origen a la fachada con `bindPdf(...)`.

1. 
Llame a `exportXfdf(stream)` para que los datos del campo del formulario se serialicen en formato XFDF.
1. Cierre la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) una vez completada la exportación.

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
