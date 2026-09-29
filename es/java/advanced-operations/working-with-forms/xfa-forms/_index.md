---
title: Trabajar con formularios XFA
linktitle: Formularios XFA
type: docs
weight: 20
url: /es/java/xfa-forms/
description: Aprenda cómo convertir formularios XFA a AcroForms estándar en documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convierta formularios PDF basados en XFA a AcroForms estándar con Java
Abstract: Este artículo explica cómo trabajar con formularios basados en XFA usando Aspose.PDF for Java. Cubre la conversión de un formulario XFA dinámico a un AcroForm estándar y el manejo de documentos XFA que requieren la opción ignore-needs-rendering antes de la conversión.
---
Los formularios XFA pueden convertirse a AcroForms estándar para que puedan procesarse con las API de formularios PDF regulares.

## Convertir un formulario XFA dinámico a un AcroForm

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceda a [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) del documento y establezca las propiedades [`FormType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) requeridas.
1. Guarde el PDF actualizado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Convertir un formulario XFA con ignoreNeedsRendering

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceda a [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) del documento y establezca las propiedades `ignoreNeedsRendering` y [`FormType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) requeridas.
1. Guarde el PDF actualizado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
