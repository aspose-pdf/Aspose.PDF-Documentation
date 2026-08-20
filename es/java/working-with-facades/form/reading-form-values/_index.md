---
title: Lectura de valores de formulario
linktitle: Lectura de valores de formulario
type: docs
weight: 60
url: /java/reading-form-values/
description: Aprenda a inspeccionar nombres y valores de campos de formularios PDF en Java utilizando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Leer nombres y valores de campos de formularios PDF en Java
Abstract: Esta sección cubre los flujos de trabajo de lectura de formularios Java implementados en el ejemplo actual de fachada de formulario establecido para Aspose.PDF para Java. El repositorio proporciona un ejemplo de inspección de campo general y utiliza notas de alcance explícitas para páginas especializadas que aún no tienen ejemplos de Java coincidentes.
---
La clase Java `FormExamples` demuestra los principales flujos de trabajo de procesamiento de formularios expuestos por la API de Fachadas.


## 
Obtener valores de campo



Utilice `FormExamples.inspectFormFields(...)` para inspeccionar los nombres de los campos y sus valores actuales.

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
