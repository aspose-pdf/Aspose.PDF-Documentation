---
title: Converter PDF para PDF/A, PDF/E e PDF/X em Java
linktitle: Converter PDF para PDF/A, PDF/E e PDF/X
type: docs
weight: 120
url: /pt/java/convert-pdf-to-pdf_x/
lastmod: "2026-10-06"
description: Aprenda como converter arquivos PDF para PDF/A, PDF/E e PDF/X em Java com Aspose.PDF para fluxos de trabalho de arquivamento, engenharia, acessibilidade e impressão.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Converter PDF para formatos PDF/x
Abstract: Este artigo explica como validar e converter documentos PDF para os formatos PDF/A, PDF/E e PDF/X usando Aspose.PDF for Java. Ele aborda a geração de logs, preservação de anexos para PDF/A-3, substituição de fontes ausentes, auto‑tagging, configuração de perfil ICC e configurações de intenção de saída.
---
Aspose.PDF for Java pode validar e converter arquivos PDF padrão em padrões PDF de arquivamento e intercâmbio.

## Converter PDF para PDF/A

Use este exemplo quando um PDF padrão deve ser convertido em um documento de arquivamento compatível com PDF/A.

1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `document.convert(...)` com [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` e [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Escreva o registro de validação em um arquivo XML sidecar para que os problemas de conformidade sejam registrados durante a conversão.
1. Salve a saída PDF/A validada.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Converter PDF para PDF/E

Use este exemplo quando um PDF deve ser convertido para o padrão PDF/E orientado à engenharia.

1. Crie [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) para [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` e o caminho do arquivo de log desejado.
1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `document.convert(options)`; assim, a conversão de conformidade é executada com o objeto de opções preparado.
1. Salve o arquivo PDF em conformidade resultante.

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

## Converter PDF para PDF/X

Use este exemplo quando um PDF deve ser convertido para o padrão PDF/X orientado para impressão.

1. Crie [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) para [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` e o caminho do arquivo de log desejado.
1. Configure um [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) como `FOGRA39`; assim, o perfil de cor de destino de impressão é incorporado nas configurações de conversão.
1. Abra o PDF de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e chamada `document.convert(options)`.
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
