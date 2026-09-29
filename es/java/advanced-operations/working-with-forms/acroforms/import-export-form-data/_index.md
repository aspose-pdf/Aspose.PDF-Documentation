---
title: Importar y Exportar Form datos
linktitle: Importar y Exportar Form datos
type: docs
weight: 80
url: /es/java/import-export-form-data/
description: Importar y exportar datos de campo AcroForm en formatos XML, FDF, XFDF y JSON usando Aspose.PDF for Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Importar y exportar datos de formularios PDF con Java
Abstract: Este artículo explica cómo intercambiar datos AcroForm con formatos externos usando Aspose.PDF for Java. Cubre la importación y exportación de datos XML, FDF y XFDF a través de la fachada Form y la extracción de valores de campos de formulario a JSON.
---
Aspose.PDF for Java soporta varios formatos de intercambio de datos comunes para Form interactivos.

## Importar datos de Form desde XML

Utilice este ejemplo cuando los valores del formulario se almacenan en un archivo XML y deben aplicarse a un formulario PDF.

1. Cree una fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) y vincule el PDF de origen.
1. Abra el flujo de entrada XML y importe los datos en el formulario.
1. Guarde el documento PDF actualizado.

```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Exportar datos del formulario a XML

Utilice este ejemplo cuando necesite almacenar los valores actuales de AcroForm en formato XML.

1. Cree una fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) y vincule el PDF de origen.
1. Abra el flujo de salida para el archivo XML.
1. Exporte los datos del formulario a XML.

```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## Importar datos del formulario desde FDF

Utilice este ejemplo cuando los valores del formulario llegan en el formato de intercambio FDF.

1. Cree una fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) y vincule el PDF de origen.
1. Abra el flujo de entrada FDF e importe los datos.
1. Guarde el documento PDF rellenado.

```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Exportar datos de formulario a FDF

Utilice este ejemplo cuando los valores del formulario PDF deban compartirse como un archivo FDF.

1. Cree una fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) y vincule el PDF de origen.
1. Abra el flujo de salida para el archivo FDF.
1. Exporte los datos del formulario en formato FDF.

```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## Importar datos del formulario desde XFDF

Utilice este ejemplo cuando los datos del formulario se proporcionan en formato XFDF y deben fusionarse en un PDF.

1. Cree una fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) y vincule el PDF de origen.
1. Abra la secuencia de entrada XFDF e importa los valores.
1. Guarde el documento PDF actualizado.

```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Exportar datos del formulario a XFDF

Utilice este ejemplo cuando necesite un archivo de intercambio basado en XML para los valores de AcroForm.

1. Cree una fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) y vincule el PDF de origen.
1. Abra el flujo de salida del archivo XFDF.
1. Exporte los valores actuales del formulario a XFDF.

```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## Extraer campos de formulario a JSON

Utilice este ejemplo cuando los valores del formulario deben exportarse a una representación JSON ligera.

1. Abra el PDF con la fachada [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Itere a través de los nombres de campo y serialice sus valores en texto JSON.
1. Escriba el contenido JSON en el archivo de destino.

```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
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

## Reutilizar el asistente de extracción JSON

Utilice este ejemplo cuando desee un método wrapper dedicado que delegue en la rutina principal de exportación JSON.

1. Llame al asistente de extracción JSON existente con el PDF de origen y la ruta de salida.
1. Reutilice la misma lógica de extracción sin duplicar el código de serialización.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
