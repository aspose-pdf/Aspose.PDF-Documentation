---
title: Trabalhar com Formulários XFA
linktitle: Formulários XFA
type: docs
weight: 20
url: /pt/java/xfa-forms/
description: Saiba como converter formulários XFA para AcroForms padrão em documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Converter formulários PDF baseados em XFA para AcroForms padrão com Java
Abstract: Este artigo explica como trabalhar com formulários baseados em XFA usando Aspose.PDF for Java. Ele aborda a conversão de um formulário XFA dinâmico para um AcroForm padrão e o tratamento de documentos XFA que exigem a opção ignore-needs-rendering antes da conversão.
---
Formulários XFA podem ser convertidos para AcroForms padrão para que possam ser processados com as APIs regulares de formulários PDF.

## Converter um formulário XFA dinâmico para um AcroForm

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acessar o documento [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) e definir o necessário [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) propriedades.
1. Salvar o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Converter um formulário XFA com `ignoreNeedsRendering`

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acessar o documento [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/form/) e definir o necessário `ignoreNeedsRendering` e [FormType](https://reference.aspose.com/pdf/java/com.aspose.pdf/formtype/) propriedades.
1. Salvar o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
