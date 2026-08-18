---
title: Converta PDF em PDF/A, PDF/E e PDF/X em Java
linktitle: Converta PDF para PDF/A, PDF/E e PDF/X
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-16"
description: Aprenda como converter arquivos PDF em PDF/A, PDF/E e PDF/X em Java com Aspose.PDF para arquivamento, engenharia, acessibilidade e fluxos de trabalho de impressão.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF para formatos PDF/x
Abstract: Este artigo explica como validar e converter documentos PDF para os formatos PDF/A, PDF/E e PDF/X usando Aspose.PDF para Java. Abrange geração de log, preservação de anexos para PDF/A-3, substituição de fontes ausentes, marcação automática, configuração de perfil ICC e configurações de intenção de saída.
---
Aspose.PDF para Java pode validar e converter arquivos PDF padrão em padrões PDF orientados para arquivamento e troca.

## Converter PDF em PDF/A

Use este exemplo quando um PDF padrão precisar ser convertido em um documento de arquivo compatível com PDF/A.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ligue para `document.convert(...)` com [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` e [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Grave o log de validação em um arquivo XML secundário para que os problemas de conformidade sejam registrados durante a conversão.
1. Salve a saída PDF/A validada.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Converter PDF em PDF/E

Use este exemplo quando um PDF precisar ser convertido no padrão PDF/E orientado para engenharia.

1. Crie [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) para [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` e o caminho do arquivo de log desejado.
1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `document.convert(options)` para que a conversão de conformidade seja executada com o objeto de opções preparado.
1. Salve o arquivo PDF compatível resultante.

```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## Converter PDF em PDF/X

Use este exemplo quando um PDF precisar ser convertido no padrão PDF/X orientado para impressão.

1. Crie [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) para [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` e o caminho do arquivo de log desejado.
1. Configure um [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) como `FOGRA39` para que o perfil de cores do destino de impressão seja incorporado nas configurações de conversão.
1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e chame `document.convert(options)`.
1. Salve a saída PDF/X convertida.

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
