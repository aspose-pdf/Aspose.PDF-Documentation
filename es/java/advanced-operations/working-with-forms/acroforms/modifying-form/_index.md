---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
weight: 45
url: /es/java/modifying-form/
description: Modifique los campos AcroForm en documentos PDF usando Aspose.PDF for Java, incluyendo borrar texto, establecer límites, estilizar campos y eliminar campos.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modifique y personalice los campos de formulario PDF con Java
Abstract: Este artículo explica cómo modificar el contenido AcroForm usando Aspose.PDF for Java. Cubre la eliminación de texto de los recursos de formulario Typewriter, la configuración y lectura de los límites de longitud de los campos de texto, el cambio de la apariencia de la fuente del campo de formulario y la eliminación de campos específicos por nombre.
---
El mantenimiento de Form a menudo implica tanto ediciones a nivel de campo como la limpieza de recursos de página relacionados con Form.

## Borrar texto en recursos de Form incrustados.

Utilice este ejemplo cuando el contenido del formulario Typewriter deba vaciarse sin eliminar los objetos de Form en sí.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de los recursos del formulario de página y localizar formularios de máquina de escribir.
1. Borrar los fragmentos de texto absorbidos y guardar el documento.

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

## Establecer un límite de longitud del campo de texto

Utilice este ejemplo cuando un campo de texto debe aceptar solo un número limitado de caracteres.

1. Crear un [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) fachada y enlazar el PDF de origen.
1. Establecer la longitud máxima para el campo de destino.
1. Guardar el documento actualizado.

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

## Obtener un límite de longitud de campo de texto

Utilice este ejemplo cuando necesite inspeccionar la longitud máxima actual de un campo de texto.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceda al campo objetivo desde la colección de formularios.
1. Lea el límite desde el [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) y mostrarlo.

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

## Cambiar la fuente de un campo de formulario

Utilice este ejemplo cuando un campo de texto existente deba usar una fuente o apariencia diferente.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceder al objetivo [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) y establecer una nueva apariencia predeterminada.
1. Guardar el PDF actualizado.

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

## Eliminar un campo de formulario por nombre

Utilice este ejemplo cuando se deba eliminar un campo específico del AcroForm.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Elimine el campo objetivo del formulario por su nombre.
1. Guardar el documento actualizado.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
