---
title: Extrair dados do AcroForm usando Java
linktitle: Extrair dados do AcroForm
type: docs
weight: 50
url: /pt/java/extract-data-from-acroform/
description: Aspose.PDF facilita a extração de dados de campos de formulário de arquivos PDF. Aprenda como extrair dados de AcroForms e salvá‑los em formato JSON, XML ou FDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair dados de AcroForm via Java
Abstract: Este artigo explica como extrair e exportar dados de AcroForm de arquivos PDF com Aspose.PDF for Java. Ele cobre a leitura de todos os campos de formulário, a recuperação de um valor de campo por nome, a exportação de dados de campo para JSON e a gravação de dados de formulário nos formatos XML, FDF e XFDF.
---

## Extrair campos de formulário de um documento PDF

Usar `com.aspose.pdf.facades.Form` para ler nomes de campos e valores sem percorrer todo o modelo de objeto do documento.

1. Abra o formulário PDF de origem com o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada para que os campos AcroForm possam ser lidos sem percorrer todo o modelo de objeto do documento.
1. Chamar `getFieldNames()` para coletar todos os identificadores de campo presentes no formulário.
1. Itere pelos nomes desses campos e chame `getField(fieldName)` para ler o valor de cada campo.
1. Construa a string de saída a partir dos pares chave-valor extraídos e imprima os dados de formulário agregados.
1. Feche o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada na `finally` bloco.

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

## Recuperar valor do campo de formulário por Nome

Quando você conhece o nome exato do campo definido no formulário PDF, pode recuperar seu valor diretamente com `getField(fieldName)`
sem percorrer toda a coleção de campos.

1. Abra o formulário PDF de origem com o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada.
1. Chamar `getField(fieldName)` com o nome do campo solicitado para ler seu valor atual dos dados do AcroForm.
1. Imprima o valor do campo extraído.
1. Feche o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada na `finally` bloco.

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

## Extrair campos de formulário de documento PDF para JSON

Os valores dos campos de formulário também podem ser extraídos e armazenados como JSON. Isso é útil quando os dados do formulário PDF precisam ser consumidos por
aplicações web, APIs ou outros sistemas que trabalham com JSON.

1. Abra o formulário PDF de origem com o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada.
1. Chamar `getFieldNames()` para coletar todos os identificadores de campo disponíveis do AcroForm.
1. Itere pelos campos, escape os nomes e valores e construa uma string de objeto JSON.
1. Escreva o resultado JSON no arquivo de saída.
1. Feche o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada na `finally` bloco.

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

## Exportar dados de formulário para XML de um arquivo PDF

A exportação XML é útil quando os dados de formulário PDF precisam ser consumidos por sistemas que trabalham com dados XML estruturados.

1. Criar o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sem vincular um documento ainda.
1. Abra um fluxo de saída para o arquivo XML e vincule o PDF de origem à fachada com `bindPdf(...)`.
1. Chamar `exportXml(stream)` então os dados atuais do campo de formulário são serializados como XML.
1. Feche o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada após a exportação ser concluída.

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

## Exportar Dados para FDF a partir de um Arquivo PDF

FDF (Forms Data Format) é comumente usado para trocar dados de campos AcroForm independentemente do documento PDF.

1. Criar o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sem vincular um documento ainda.
1. Abra um fluxo de saída para o arquivo FDF e vincule o PDF de origem à fachada com `bindPdf(...)`.
1. Chamar `exportFdf(stream)` então os dados do campo de formulário são serializados no formato FDF.
1. Feche o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada após a exportação ser concluída.

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

## Exportar Dados para XFDF a partir de um Arquivo PDF

XFDF é a representação baseada em XML do Forms Data Format e é conveniente para a troca de dados de formulário com sistemas que trabalham com XML.

1. Criar o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada sem vincular um documento ainda.
1. Abra um fluxo de saída para o arquivo XFDF e vincule o PDF de origem à fachada com `bindPdf(...)`.
1. Chamar `exportXfdf(stream)` então os dados do campo de formulário são serializados no formato XFDF.
1. Feche o [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada após a exportação ser concluída.

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
