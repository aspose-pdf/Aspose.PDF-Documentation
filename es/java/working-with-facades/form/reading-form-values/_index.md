---
title: Lectura de valores de formulario
linktitle: Lectura de valores de formulario
type: docs
weight: 60
url: /es/java/reading-form-values/
description: Aprenda cómo inspeccionar los nombres y valores de los campos de formulario PDF en Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Leer nombres y valores de campos de formulario PDF en Java
Abstract: Esta sección cubre los flujos de trabajo de lectura de formularios en Java implementados en el conjunto actual de ejemplos de la fachada Form para Aspose.PDF for Java. El repositorio proporciona un ejemplo general de inspección de campos y utiliza notas de alcance explícitas para páginas especializadas que aún no tienen muestras de Java correspondientes.
---
El Java `FormExamples` La clase demuestra los principales flujos de trabajo de procesamiento de formularios expuestos por la API de Facades.

## Obtener valores de campos

Usar `FormExamples.inspectFormFields(...)` para inspeccionar los nombres de los campos y sus valores actuales.

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
