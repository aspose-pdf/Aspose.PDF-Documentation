---
title: Importar e exportar dados de formulário
linktitle: Importar e exportar dados de formulário
type: docs
weight: 80
url: /java/import-export-form-data/
description: Importe e exporte dados de campo AcroForm nos formatos XML, FDF, XFDF e JSON usando Aspose.PDF para Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importe e exporte dados de formulários PDF com Java
Abstract: Este artigo explica como trocar dados AcroForm com formatos externos usando Aspose.PDF para Java. Abrange a importação e exportação de dados XML, FDF e XFDF por meio da fachada do formulário e a extração de valores de campos de formulário para JSON.
---
Aspose.PDF para Java oferece suporte a vários formatos comuns de troca de dados para formulários interativos.

## Importar dados de formulário de XML

Use este exemplo quando os valores do formulário são armazenados em um arquivo XML e devem ser aplicados a um formulário PDF.

1. Crie uma fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) e vincule o PDF de origem.
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

## Exportar dados do formulário para XML

Use este exemplo quando precisar armazenar valores atuais do AcroForm em formato XML.

1. Crie uma fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) e vincule o PDF de origem.
1. Abra o fluxo de saída do arquivo XML.
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

Use este exemplo quando os valores do formulário chegarem no formato de intercâmbio FDF.

1. Crie uma fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) e vincule o PDF de origem.
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

1. Crie uma fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) e vincule o PDF de origem.
1. Abra o fluxo de saída do arquivo FDF.
1. Exporte os dados do formulário no formato FDF.

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

## Importe dados de formulário do XFDF

Use este exemplo quando os dados do formulário forem fornecidos no formato XFDF e precisarem ser mesclados em um PDF.

1. Crie uma fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) e vincule o PDF de origem.
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

## Exportar dados de formulário para XFDF

Use este exemplo quando precisar de um arquivo de intercâmbio baseado em XML para valores do AcroForm.

1. Crie uma fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) e vincule o PDF de origem.
1. Abra o fluxo de saída do arquivo XFDF.
1. Exporte os valores atuais do formulário para XFDF.

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

## Extraia campos de formulário para JSON

Use este exemplo quando os valores do formulário devem ser exportados para uma representação JSON leve.

1. Abra o PDF com a fachada [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Itere pelos nomes dos campos e serialize seus valores em texto JSON.
1. Grave o conteúdo JSON no arquivo de destino.

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

## Reutilize o auxiliar de extração JSON

Use este exemplo quando desejar um método wrapper dedicado que delegue para a rotina principal de exportação JSON.

1. Chame o auxiliar de extração JSON existente com o PDF de origem e o caminho de saída.
1. Reutilize a mesma lógica de extração sem duplicar o código de serialização.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
