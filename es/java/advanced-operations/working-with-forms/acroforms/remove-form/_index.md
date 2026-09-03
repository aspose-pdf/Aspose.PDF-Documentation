---
title: Eliminar formularios de PDF en Java
linktitle: Eliminar formularios
type: docs
weight: 70
url: /java/remove-form/
description: Elimine objetos de formulario de páginas PDF utilizando Aspose.PDF para Java, incluida la limpieza completa y la eliminación selectiva.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar recursos de formulario de páginas PDF con Java
Abstract: Este artículo explica cómo eliminar recursos de formulario de documentos PDF usando Aspose.PDF para Java. Cubre la eliminación de todos los formularios de una página y la eliminación solo de los recursos de formularios de Typewriter seleccionados después de filtrar la colección de formularios de la página.
---
Estos ejemplos eliminan recursos de formulario de una página en lugar de simplemente cambiar los valores de los campos.


## 
Eliminar todos los recursos de formulario de una página



Utilice este ejemplo cuando todos los recursos de formulario en una página seleccionada deban eliminarse en una sola operación.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda a [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) para la página de destino.
1. Borre la colección y guarde el documento actualizado.


```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## 
Eliminar recursos de formulario específicos



Utilice este ejemplo cuando solo deban eliminarse los recursos de formulario seleccionados, como los formularios de máquina de escribir.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda a [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) para la página de destino.
1. Filtre los recursos [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) que desea eliminar y elimínelos de la colección.

1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
