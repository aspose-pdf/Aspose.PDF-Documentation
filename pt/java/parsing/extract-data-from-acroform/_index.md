---
title: Extraia dados do AcroForm usando Java
linktitle: Extraia dados do AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: Aspose.PDF facilita a extração de dados de campos de formulário de arquivos PDF. Aprenda como extrair dados do AcroForms e salvá-los no formato JSON, XML ou FDF.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair dados do AcroForm via Java
Abstract: Este artigo explica como extrair e exportar dados AcroForm de arquivos PDF com Aspose.PDF para Java. Abrange a leitura de todos os campos do formulário, a recuperação de um valor de campo por nome, a exportação de dados do campo para JSON e a gravação de dados de formulário nos formatos XML, FDF e XFDF.
---
## Extraia todos os campos do formulário

Usar `com.aspose.pdf.facades.Form` para ler nomes e valores de campos sem trabalhar em todo o modelo de objeto do documento.

1. Abra o formulário PDF de origem com o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada para que os campos do AcroForm possam ser lidos sem percorrer todo o modelo de objeto do documento.
1. Chamar `getFieldNames()` para coletar todos os identificadores de campo presentes no formulário.
1. Itere através desses nomes de campo e chame `getField(fieldName)` para ler cada valor de campo.
1. Crie a string de saída a partir dos pares de valores-chave extraídos e imprima os dados agregados do formulário.
1. Feche o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada no `finally` bloquear.

```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## Recuperar um valor de campo por nome

1. Abra o formulário PDF de origem com o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada.
1. Chamar `getField(fieldName)` com o nome do campo solicitado para ler seu valor atual dos dados do AcroForm.
1. Imprima o valor do campo extraído.
1. Feche o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada no `finally` bloquear.

```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## Exportar campos de formulário para JSON

1. Abra o formulário PDF de origem com o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada.
1. Chamar `getFieldNames()` para coletar todos os identificadores de campo disponíveis no AcroForm.
1. Itere por esses campos, escape dos nomes e valores e crie uma string de objeto JSON.
1. Grave o resultado JSON no arquivo de saída.
1. Feche o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada no `finally` bloquear.

```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## Exporte dados de formulário para XML, FDF e XFDF

1. Crie o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sem vincular um documento ainda.
1. Abra um fluxo de saída para o arquivo XML e vincule o PDF de origem à fachada com `bindPdf(...)`.
1. Chamar `exportXml(stream)` portanto, os dados atuais do campo do formulário são serializados como XML.
1. Feche o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada após a conclusão da exportação.

```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

1. Crie o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sem vincular um documento ainda.
1. Abra um fluxo de saída para o arquivo FDF e vincule o PDF de origem à fachada com `bindPdf(...)`.
1. Chamar `exportFdf(stream)` portanto, os dados do campo do formulário são serializados no formato FDF.
1. Feche o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada após a conclusão da exportação.

```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

1. Crie o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sem vincular um documento ainda.
1. Abra um fluxo de saída para o arquivo XFDF e vincule o PDF de origem à fachada com `bindPdf(...)`.
1. Chamar `exportXfdf(stream)` portanto, os dados do campo do formulário são serializados no formato XFDF.
1. Feche o [Forma](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada após a conclusão da exportação.

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
