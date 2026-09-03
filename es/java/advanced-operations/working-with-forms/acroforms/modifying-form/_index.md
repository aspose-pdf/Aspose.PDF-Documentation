---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
weight: 45
url: /java/modifying-form/
description: Modifique los campos de AcroForm en documentos PDF utilizando Aspose.PDF para Java, lo que incluye borrar texto, establecer límites, diseñar campos y eliminar campos.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modifique y personalice los campos de formulario PDF con Java
Abstract: Este artículo explica cómo modificar el contenido de AcroForm usando Aspose.PDF para Java. Cubre la eliminación de texto de los recursos del formulario Typewriter, la configuración y la lectura de límites de longitud de los campos de texto, el cambio de la apariencia de la fuente del campo del formulario y la eliminación de campos específicos por nombre.
---
El mantenimiento de formularios a menudo implica tanto ediciones a nivel de campo como limpieza de recursos de página relacionados con el formulario.


## 
Borrar texto en recursos de formularios incrustados



Utilice este ejemplo cuando el contenido del formulario Typewriter deba vaciarse sin eliminar los objetos del formulario.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Recorra los recursos de formularios de página y localice formularios de máquina de escribir.
1. Borre los fragmentos de texto absorbidos y guarde el documento.


```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
Establecer un límite de longitud de campo de texto



Utilice este ejemplo cuando un campo de texto deba aceptar solo una cantidad limitada de caracteres.


1. Cree una fachada de [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) y vincule el PDF de origen.

1. Establezca la longitud máxima para el campo de destino.
1. Guarde el documento actualizado.


```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
Obtener un límite de longitud de campo de texto



Utilice este ejemplo cuando necesite inspeccionar la longitud máxima actual de un campo de texto.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda al campo de destino desde la colección de formularios.
1. Lea el límite de [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) y envíelo.


```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## 
Cambiar la fuente de un campo de formulario



Utilice este ejemplo cuando un campo de texto existente deba utilizar una fuente o apariencia diferente.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda al objetivo [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) y establezca una nueva apariencia predeterminada.
1. Guarde el PDF actualizado.


```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## 
Eliminar un campo de formulario por nombre



Utilice este ejemplo cuando deba eliminarse un campo específico de AcroForm.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Elimine el campo de destino del formulario por su nombre.
1. Guarde el documento actualizado.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
