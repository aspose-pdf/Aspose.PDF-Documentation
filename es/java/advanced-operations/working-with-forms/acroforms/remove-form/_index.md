---
title: Delete Forms from PDF in Java
linktitle: Eliminar formularios
type: docs
weight: 70
url: /java/remove-form/
description: Remove form objects from PDF pages using Aspose.PDF for Java, including full cleanup and targeted deletion.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar recursos de formulario de páginas PDF con Java
Abstract: Este artículo explica cómo eliminar recursos de formulario de documentos PDF usando Aspose.PDF para Java. Cubre la eliminación de todos los formularios de una página y la eliminación solo de los recursos de formularios de Typewriter seleccionados después de filtrar la colección de formularios de la página.
---
These examples remove form resources from a page rather than just changing field values.

## Remove all form resources from a page

Use this example when every form resource on a selected page should be removed in one operation.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Access the [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) for the target page.
1. Clear the collection and save the updated document.

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

Use this example when only selected form resources, such as Typewriter forms, should be deleted.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Access the [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) for the target page.
1. Filter the [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) resources you want to remove and delete them from the collection.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
