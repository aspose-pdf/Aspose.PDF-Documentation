---
title: Extraer AcroForm: extraer datos de formularios de PDF en Java
linktitle: Extraer AcroForm
type: docs
weight: 30
url: /java/extract-form/
description: Extraiga valores de campos de AcroForm en documentos PDF utilizando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga valores de campos de formulario de archivos PDF con Java
Abstract: Este artículo muestra cómo extraer datos de campos de AcroForm usando Aspose.PDF para Java. El ejemplo recorre en iteración los nombres de los campos con la fachada del formulario, lee cada valor actual y almacena el resultado en un mapa para su procesamiento posterior.
---
Utilice la fachada `Form` cuando necesite un flujo de extracción de nombre de campo simple para valor de campo.


## 
Extraiga valores de todos los campos de AcroForm


1. 
Abra el documento de formulario PDF con la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. 
Repita los nombres de los campos de la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) y lea cada valor de campo actual en un mapa.

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
