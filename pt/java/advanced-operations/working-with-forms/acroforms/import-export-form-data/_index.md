---
title: Importar e exportar dados de Form
linktitle: Importar e exportar dados de Form
type: docs
weight: 80
url: /pt/java/import-export-form-data/
description: Importar e exportar dados de campo AcroForm em formatos XML, FDF, XFDF e JSON usando Aspose.PDF for Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Importar e exportar dados de formulário PDF com Java
Abstract: Este artigo explica como trocar dados AcroForm com formatos externos usando Aspose.PDF for Java. Ele cobre a importação e exportação de dados XML, FDF e XFDF através da fachada Form e a extração de valores de campos de formulário para JSON.
---
Aspose.PDF for Java suporta vários formatos comuns de troca de dados para formulários interativos.

## Importar dados de formulário de XML

Use este exemplo quando os valores do formulário são armazenados em um arquivo XML e devem ser aplicados a um formulário PDF.

1. Crie um [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada e vincule o PDF de origem.
1. Abra o fluxo de entrada XML e importe os dados para o formulário.
1. Salve o documento PDF atualizado.

```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Exportar dados do Form para XML

Use este exemplo quando precisar armazenar os valores atuais do AcroForm em formato XML.

1. Crie um [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada e vincule o PDF de origem.
1. Abra o fluxo de saída para o arquivo XML.
1. Exporte os dados do formulário para XML.

```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## Importar dados de formulário do FDF

Use este exemplo quando os valores de formulário chegarem no formato de intercâmbio FDF.

1. Crie um [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada e vincule o PDF de origem.
1. Abra o fluxo de entrada FDF e importe os dados.
1. Salve o documento PDF preenchido.

```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Exportar dados do formulário para FDF

Use este exemplo quando os valores do formulário PDF devem ser compartilhados como um arquivo FDF.

1. Crie um [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada e vincule o PDF de origem.
1. Abra o fluxo de saída para o arquivo FDF.
1. Exporte os dados do formulário em formato FDF.

```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## Importar dados de formulário a partir de XFDF

Use este exemplo quando os dados do formulário são fornecidos no formato XFDF e devem ser mesclados em um PDF.

1. Crie um [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada e vincule o PDF de origem.
1. Abra o fluxo de entrada XFDF e importe os valores.
1. Salve o documento PDF atualizado.

```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Exportar dados do formulário para XFDF

Use este exemplo quando precisar de um arquivo de intercâmbio baseado em XML para valores de AcroForm.

1. Crie um [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) fachada e vincule o PDF de origem.
1. Abra o fluxo de saída para o arquivo XFDF.
1. Exporte os valores do formulário atual para XFDF.

```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## Extrair campos de formulário para JSON

Use este exemplo quando os valores do formulário devem ser exportados para uma representação JSON leve.

1. Abra o PDF com a fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Itere pelos nomes dos campos e serialize seus valores em texto JSON.
1. Escreva o conteúdo JSON no arquivo de destino.

```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
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

## Reutilize o assistente de extração JSON

Use este exemplo quando quiser um método wrapper dedicado que delega para a rotina principal de exportação JSON.

1. Chame o helper de extração JSON existente com o PDF de origem e o caminho de saída.
1. Reutilize a mesma lógica de extração sem duplicar o código de serialização.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
