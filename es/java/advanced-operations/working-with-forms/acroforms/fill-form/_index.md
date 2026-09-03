---
title: Complete AcroForm - Complete un formulario PDF usando Java
linktitle: Rellenar AcroForm
type: docs
weight: 20
url: /java/fill-form/
description: Complete los campos de AcroForm en un documento PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Complete los campos de AcroForm en archivos PDF con Java
Abstract: Este artículo explica cómo completar campos de AcroForm usando Aspose.PDF para Java. El ejemplo carga un PDF a través de la fachada del formulario, compara los nombres de los campos con un mapa de valores, actualiza los campos coincidentes y guarda el documento completo.
---
La fachada `Form` se puede utilizar para automatizar el llenado de campos en un AcroForm existente.


## 
Rellene los campos de AcroForm con nuevos valores


1. Abra el documento de formulario PDF con la fachada [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).

1. Recorra los campos del formulario y actualice las entradas coincidentes con los valores proporcionados.

1. Guarde el documento PDF actualizado.

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
