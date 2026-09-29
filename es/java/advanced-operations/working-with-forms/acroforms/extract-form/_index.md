---
title: Extraer AcroForm - extraer datos de formulario de PDF en Java
linktitle: Extraer AcroForm
type: docs
weight: 30
url: /es/java/extract-form/
description: Extraer valores de los campos AcroForm en documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer valores de campos de formulario de archivos PDF con Java
Abstract: Este artículo muestra cómo extraer datos de los campos AcroForm usando Aspose.PDF for Java. El ejemplo itera a través de los nombres de los campos con la fachada Form, lee cada valor actual y almacena el resultado en un mapa para el procesamiento posterior.
---
Utilice la fachada `Form` cuando necesita un flujo de extracción simple de nombre de campo a valor de campo.

## Extraer valores de todos los campos AcroForm

1. Abra el documento PDF Form con el [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade.
1. Itere a través de los nombres de campo del [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade y lea cada valor de campo actual en un mapa.

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```
