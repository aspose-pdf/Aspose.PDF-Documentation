---
title: Extrair AcroForm - Extrair dados de formulário de PDF em Java
linktitle: Extrair AcroForm
type: docs
weight: 30
url: /java/extract-form/
description: Extraia valores de campos AcroForm em documentos PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia valores de campos de formulário de arquivos PDF com Java
Abstract: Este artigo mostra como extrair dados de campos AcroForm usando Aspose.PDF para Java. O exemplo itera pelos nomes dos campos com a fachada Form, lê cada valor atual e armazena o resultado em um mapa para processamento posterior.
---
Use a fachada `Form` quando precisar de um fluxo simples de extração de nome de campo para valor de campo.

## Extraia valores de todos os campos do AcroForm

1. Abra o documento PDF com a fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Itere pelos nomes dos campos da fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) e leia cada valor de campo atual em um mapa.

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```
