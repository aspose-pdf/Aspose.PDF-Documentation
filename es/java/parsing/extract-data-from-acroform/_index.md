---
title: Extraer datos de AcroForm usando Java
linktitle: Extraer datos de AcroForm
type: docs
weight: 50
url: /es/java/extract-data-from-acroform/
description: Aspose.PDF facilita la extracción de datos de campos de formulario de archivos PDF. Aprenda cómo extraer datos de AcroForms y guardarlos en formato JSON, XML o FDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer datos de AcroForm mediante Java
Abstract: Este artículo explica cómo extraer y exportar datos de AcroForm de archivos PDF con Aspose.PDF for Java. Cubre la lectura de todos los campos de formulario, la obtención del valor de un campo por su nombre, la exportación de datos de campos a JSON y la escritura de datos de formulario en formatos XML, FDF y XFDF.
---

## Extraer campos de formulario de un documento PDF

Utilice `com.aspose.pdf.facades.Form` para leer los nombres y valores de los campos sin recorrer todo el modelo de objetos del documento.

1. Abra el formulario PDF de origen con la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) para que los campos AcroForm puedan leerse sin recorrer todo el modelo de objetos del documento.
1. Llame `getFieldNames()` para recopilar todos los identificadores de campo presentes en el formulario.
1. Itere a través de esos nombres de campo y llame `getField(fieldName)` para leer el valor de cada campo.
1. Construya la cadena de salida a partir de los pares clave-valor extraídos e imprima los datos agregados del Form.
1. Cierre la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) en el bloque `finally`.

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

## Recuperar el valor del campo de formulario por nombre

Cuando conoce el nombre exacto del campo definido en el formulario PDF, puede recuperar su valor directamente con `getField(fieldName)`
sin iterar sobre toda la colección de campos.

1. Abra el formulario PDF de origen con la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Llame `getField(fieldName)` con el nombre de campo solicitado para leer su valor actual de los datos del AcroForm.
1. Imprima el valor del campo extraído.
1. Cierre la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) en el bloque `finally`.

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

## Extraer campos de formulario de documento PDF a JSON

Los valores de los campos de formulario también pueden extraerse y almacenarse como JSON. Esto es útil cuando los datos del formulario PDF necesitan ser consumidos por
aplicaciones web, APIs u otros sistemas que trabajan con JSON.

1. Abra el formulario PDF de origen con la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Llame `getFieldNames()` para recopilar todos los identificadores de campo disponibles del AcroForm.
1. Itere a través de esos campos, escapa los nombres y valores, y construya una cadena de objeto JSON.
1. Escriba el resultado JSON en el archivo de salida.
1. Cierre la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) en el bloque `finally`.

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

1. Cree la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sin enlazar aún un documento.
1. Abra un flujo de salida para el archivo XML y vincule el PDF de origen a la fachada con `bindPdf(...)`.
1. Llame `exportXml(stream)` por lo tanto, los datos actuales del campo de formulario se serializan como XML.
1. Cierre la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) después de que se complete la exportación.

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

FDF (Formato de datos de formularios) se usa comúnmente para intercambiar datos de campos AcroForm de forma independiente del documento PDF.

1. Cree la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sin enlazar aún un documento.
1. Abra un flujo de salida para el archivo FDF y vincule el PDF de origen a la fachada con `bindPdf(...)`.
1. Llame `exportFdf(stream)` por lo tanto, los datos del campo de formulario se serializan en formato FDF.
1. Cierre la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) después de que se complete la exportación.

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

XFDF es la representación basada en XML del Forms Data Format y es conveniente para intercambiar datos de formularios con sistemas que trabajan con XML.

1. Cree la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sin enlazar aún un documento.
1. Abra un flujo de salida para el archivo XFDF y vincule el PDF fuente a la fachada con `bindPdf(...)`.
1. Llame `exportXfdf(stream)` por lo que los datos del campo del formulario se serializan en formato XFDF.
1. Cierre la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) después de que se complete la exportación.

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
