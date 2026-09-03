---
title: Extraer AcroForm - Extraer datos de formulario de PDF en Java
linktitle: Extraer AcroForm
type: docs
weight: 30
url: /es/java/extract-form/
description: Extraer valores de los campos AcroForm en documentos PDF utilizando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer valores de campos de formulario de archivos PDF con Java
Abstract: Este artículo muestra cómo extraer datos de los campos AcroForm utilizando Aspose.PDF for Java. El ejemplo itera a través de los nombres de campo con el Form facade, lee cada valor actual y almacena el resultado en un mapa para procesamiento posterior.
---
Utiliza el `Form` fachada cuando necesitas un flujo simple de extracción de nombre de campo a valor de campo.

## Extraer valores de todos los campos AcroForm

1. Abra el documento de formulario PDF con el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada.
1. Itere a través de los nombres de campo del [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada y lea cada valor de campo actual en un mapa.

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
