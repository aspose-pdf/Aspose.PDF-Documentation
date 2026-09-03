---
title: Extraer datos de AcroForm usando Java
linktitle: Extraer datos de AcroForm
type: docs
weight: 50
url: /es/java/extract-data-from-acroform/
description: Aspose.PDF facilita la extracción de datos de campos de formulario de archivos PDF. Aprenda cómo extraer datos de AcroForms y guardarlos en formato JSON, XML o FDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer datos de AcroForm mediante Java
Abstract: Este artículo explica cómo extraer y exportar datos de AcroForm de archivos PDF con Aspose.PDF for Java. Cubre la lectura de todos los campos de formulario, la obtención del valor de un campo por nombre, la exportación de datos de campos a JSON y la escritura de datos de formulario a formatos XML, FDF y XFDF.
---

## Extraer campos de formulario de un documento PDF

Usar `com.aspose.pdf.facades.Form` para leer nombres de campos y valores sin recorrer todo el modelo de objeto del documento.

1. Abra el PDF Form de origen con el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada para que los campos AcroForm se puedan leer sin recorrer todo el modelo de objetos del documento.
1. Llamar `getFieldNames()` para recopilar todos los identificadores de campo presentes en el formulario.
1. Itera a través de esos nombres de campo y llama `getField(fieldName)` para leer el valor de cada campo.
1. Construye la cadena de salida a partir de los pares clave-valor extraídos y muestra los datos del formulario agregados.
1. Cerrar el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada en el `finally` bloque.

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

## Recuperar el valor del campo del formulario por nombre

Cuando conoces el nombre exacto del campo definido en el formulario PDF, puedes obtener su valor directamente con `getField(fieldName)`
sin iterar a través de toda la colección de campos.

1. Abra el PDF Form de origen con el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada.
1. Llamar `getField(fieldName)` con el nombre de campo solicitado para leer su valor actual de los datos del AcroForm.
1. Imprima el valor del campo extraído.
1. Cerrar el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada en el `finally` bloque.

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

## Extraer campos de formulario de un documento PDF a JSON

Los valores de los campos del formulario también pueden extraerse y almacenarse como JSON. Esto es útil cuando los datos del formulario PDF necesitan ser consumidos por
aplicaciones web, APIs o otros sistemas que trabajan con JSON.

1. Abra el PDF Form de origen con el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada.
1. Llamar `getFieldNames()` para recopilar todos los identificadores de campo disponibles del AcroForm.
1. Itera a través de esos campos, escapa los nombres y valores, y construye una cadena de objeto JSON.
1. Escribe el resultado JSON en el archivo de salida.
1. Cerrar el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada en el `finally` bloque.

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

## Exportar datos de formulario a XML desde un archivo PDF

La exportación XML es útil cuando los datos del formulario PDF deben ser consumidos por sistemas que trabajan con datos XML estructurados.

1. Crear el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sin vincular un documento todavía.
1. Abra un flujo de salida para el archivo XML y vincule el PDF de origen a la fachada con `bindPdf(...)`.
1. Llamar `exportXml(stream)` Así que los datos actuales del campo de formulario se serializan como XML.
1. Cerrar el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada después de que la exportación se complete.

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

## Exportar datos a FDF desde un archivo PDF

FDF (Formato de datos de formularios) se usa comúnmente para intercambiar datos de campos AcroForm independientemente del documento PDF.

1. Crear el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sin vincular un documento todavía.
1. Abrir un flujo de salida para el archivo FDF y vincular el PDF de origen a la fachada con `bindPdf(...)`.
1. Llamar `exportFdf(stream)` Así que los datos del campo de formulario se serializan en formato FDF.
1. Cerrar el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada después de que la exportación se complete.

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

## Exportar datos a XFDF desde un archivo PDF

XFDF es la representación basada en XML del Formato de datos de formularios y es conveniente para intercambiar datos de formulario con sistemas que trabajan con XML.

1. Crear el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sin vincular un documento todavía.
1. Abra un flujo de salida para el archivo XFDF y vincule el PDF de origen a la fachada con `bindPdf(...)`.
1. Llamar `exportXfdf(stream)` por lo tanto, los datos del campo de formulario se serializan en formato XFDF.
1. Cerrar el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada después de que la exportación se complete.

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
