---
title: Trabajando con formularios XFA
linktitle: Formularios XFA
type: docs
weight: 20
url: /es/java/xfa-forms/
description: Aprenda cómo convertir formularios XFA a AcroForms estándar en documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convierta formularios PDF basados en XFA a AcroForms estándar con Java
Abstract: Este artículo explica cómo trabajar con formularios basados en XFA usando Aspose.PDF for Java. Cubre la conversión de un formulario XFA dinámico a un AcroForm estándar y el manejo de documentos XFA que requieren la opción ignore-needs-rendering antes de la conversión.
---
Los formularios XFA pueden convertirse en AcroForms estándar para que puedan procesarse con las API de formularios PDF habituales.

## Convertir un formulario XFA dinámico a un AcroForm

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceder al documento [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) y establecer lo requerido [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) propiedades.
1. Guardar el PDF actualizado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Convertir un formulario XFA con `ignoreNeedsRendering`

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceder al documento [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) y establecer lo requerido `ignoreNeedsRendering` y [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) propiedades.
1. Guardar el PDF actualizado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertXfaFormWithIgnoreNeedsRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (!document.getForm().getNeedsRendering() && document.getForm().hasXfa()) {
            document.getForm().setIgnoreNeedsRendering(true);
        }
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```
