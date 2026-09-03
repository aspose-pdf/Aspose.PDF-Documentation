---
title: Rellenar AcroForm - Rellenar formulario PDF usando Java
linktitle: Rellenar AcroForm
type: docs
weight: 20
url: /es/java/fill-form/
description: Rellenar campos AcroForm en un documento PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rellenar campos AcroForm en archivos PDF con Java
Abstract: Este artículo explica cómo rellenar campos AcroForm usando Aspose.PDF for Java. El ejemplo carga un PDF a través de la fachada Form, compara los nombres de los campos con un mapa de valores, actualiza los campos coincidentes y guarda el documento completado.
---
El `Form` La fachada puede usarse para automatizar la población de campos en un AcroForm existente.

## Rellenar campos AcroForm con nuevos valores

1. Abra el documento PDF Form con el [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada.
1. Iterar a través de los campos del Form y actualizar las entradas coincidentes con los valores proporcionados.
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
