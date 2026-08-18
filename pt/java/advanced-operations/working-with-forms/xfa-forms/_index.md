---
title: Trabalhando com formulários XFA
linktitle: Formulários XFA
type: docs
weight: 20
url: /java/xfa-forms/
description: Aprenda como converter formulários XFA em AcroForms padrão em documentos PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Converta formulários PDF baseados em XFA em AcroForms padrão com Java
Abstract: Este artigo explica como trabalhar com formulários baseados em XFA usando Aspose.PDF para Java. Ele cobre a conversão de um formulário XFA dinâmico em um AcroForm padrão e o tratamento de documentos XFA que exigem a opção ignorar necessidade de renderização antes da conversão.
---
Os formulários XFA podem ser convertidos em AcroForms padrão para que possam ser processados ​​com as APIs regulares de formulários PDF.

## Converter um formulário XFA dinâmico em um AcroForm

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o documento [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) e defina as propriedades [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) necessárias.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Converta um formulário XFA com `ignoreNeedsRendering`

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o documento [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) e defina as propriedades `ignoreNeedsRendering` e [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) necessárias.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
