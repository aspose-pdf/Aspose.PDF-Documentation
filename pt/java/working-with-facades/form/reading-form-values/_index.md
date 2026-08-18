---
title: Lendo Valores do Formulário
linktitle: Lendo Valores do Formulário
type: docs
weight: 60
url: /java/reading-form-values/
description: Aprenda como inspecionar nomes e valores de campos de formulário PDF em Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Leia nomes e valores de campos de formulário PDF em Java
Abstract: Esta seção aborda os fluxos de trabalho de leitura de formulário Java implementados no exemplo atual de fachada de formulário definido para Aspose.PDF para Java. O repositório fornece um exemplo geral de inspeção de campo e usa notas de escopo explícitas para páginas especializadas que ainda não possuem amostras Java correspondentes.
---
A classe Java `FormExamples` demonstra os principais fluxos de trabalho de processamento de formulários expostos pela API Facades.

## Obtenha valores de campo

Use `FormExamples.inspectFormFields(...)` para inspecionar nomes de campos e seus valores atuais.

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
