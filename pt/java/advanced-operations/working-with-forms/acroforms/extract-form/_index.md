---
title: Extrair AcroForm - extrair dados de formulário de PDF em Java
linktitle: Extrair AcroForm
type: docs
weight: 30
url: /pt/java/extract-form/
description: Extrair valores dos campos AcroForm em documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair valores de campos de formulário de arquivos PDF com Java
Abstract: Este artigo mostra como extrair dados dos campos AcroForm usando Aspose.PDF for Java. O exemplo percorre os nomes dos campos com a fachada Form, lê cada valor atual e armazena o resultado em um mapa para processamento subsequente.
---
Use a fachada `Form` quando precisar de um fluxo simples de extração de nome de campo para valor de campo.

## Extrair valores de todos os campos AcroForm

1. Abra o documento de formulário PDF com o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade.
1. Itere pelos nomes dos campos a partir do [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade e leia cada valor de campo atual em um mapa.

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
