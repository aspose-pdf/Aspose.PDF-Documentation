---
title: Eliminar formularios de PDF en Java
linktitle: Eliminar formularios
type: docs
weight: 70
url: /es/java/remove-form/
description: Eliminar objetos de Form de las páginas PDF usando Aspose.PDF for Java, incluyendo una limpieza completa y eliminación dirigida.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar recursos de Form de las páginas PDF con Java
Abstract: Este artículo explica cómo eliminar recursos de Form de documentos PDF usando Aspose.PDF for Java. Cubre la limpieza de todos los formularios de una página y la eliminación solo de los recursos de formulario Typewriter seleccionados después de filtrar la colección de formularios de la página.
---
Estos ejemplos eliminan recursos de Form de una página en lugar de solo cambiar los valores de los campos.

## Eliminar todos los recursos de formulario de una página

Utilice este ejemplo cuando todos los recursos de formulario en una página seleccionada deban eliminarse en una sola operación.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceda al [`XFormCollection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) para la página objetivo.
1. Elimine la colección y guarde el documento actualizado.

```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## Eliminar recursos de formulario específicos

Utilice este ejemplo cuando sólo se deben eliminar recursos de formulario seleccionados, como Typewriter forms.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceda al [`XFormCollection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) para la página objetivo.
1. Filtre los recursos [`XForm`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) que desea eliminar y elimínelos de la colección.
1. Guarde el PDF actualizado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```
