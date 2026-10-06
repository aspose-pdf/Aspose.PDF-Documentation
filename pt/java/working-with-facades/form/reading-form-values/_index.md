---
title: Leitura de Valores de Formulário
linktitle: Leitura de Valores de Formulário
type: docs
weight: 60
url: /pt/java/reading-form-values/
description: Aprenda como inspecionar nomes e valores de campos de formulário PDF em Java usando o Form facade no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Ler nomes e valores de campos de formulário PDF em Java
Abstract: Esta seção cobre os fluxos de trabalho de leitura de formulários Java implementados no conjunto atual de exemplos do Form facade para Aspose.PDF for Java. O repositório fornece um exemplo geral de inspeção de campos e usa notas de escopo explícitas para páginas especializadas que ainda não possuem amostras Java correspondentes.
---
O Java `FormExamples` classe demonstra os principais fluxos de trabalho de processamento de formulários expostos pela API Facades.

## Obter Valores de Campo

Usar `FormExamples.inspectFormFields(...)` para inspecionar nomes de campo e seus valores atuais.

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
