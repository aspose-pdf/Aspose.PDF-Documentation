---
title: Trabajar con formularios XFA
linktitle: Formularios XFA
type: docs
weight: 20
url: /java/xfa-forms/
description: Aprenda a convertir formularios XFA a AcroForms estándar en documentos PDF utilizando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convierta formularios PDF basados en XFA a AcroForms estándar con Java
Abstract: Este artículo explica cómo trabajar con formularios basados en XFA usando Aspose.PDF para Java. Cubre la conversión de un formulario XFA dinámico a un AcroForm estándar y el manejo de documentos XFA que requieren la opción de ignorar necesidades de procesamiento antes de la conversión.
---
Los formularios XFA se pueden convertir a AcroForms estándar para que puedan procesarse con las API de formularios PDF habituales.


## 
Convierta un formulario XFA dinámico en un AcroForm


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda al documento [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) y establezca las propiedades requeridas de [Tipo de formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/).

1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Convierta un formulario XFA con `ignoreNeedsRendering`


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda al documento [Formulario](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) y establezca las propiedades `ignoreNeedsRendering` y [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) requeridas.

1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
