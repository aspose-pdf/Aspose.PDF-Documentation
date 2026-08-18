---
title: Compare documentos PDF em Java
linktitle: Comparar PDF
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: Aprenda como comparar documentos PDF em Java usando saída lado a lado e diferença gráfica com Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compare páginas PDF e documentos completos com saída de diferença visual em Java
Abstract: Este artigo explica como comparar documentos PDF usando Aspose.PDF para Java. Aprenda como comparar páginas específicas ou arquivos PDF inteiros com saída lado a lado, gerar relatórios gráficos de diferenças em PDF e exportar diferenças de imagens em nível de página.
---
Aspose.PDF para Java fornece APIs de comparação lado a lado e gráfica para detectar diferenças entre arquivos PDF.

## Compare páginas e exporte imagens diferentes

Use este exemplo quando precisar de saída de diferença baseada em imagem para um par específico de páginas PDF.

1. Abra os dois objetos PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de origem.
1. Use [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) para obter o nível de página [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/).
1. Use 'GraphicalPdfComparer' para obter o 'ImagesDifference' no nível da página.
1. Exporte as imagens de diferença geradas e descarte o resultado da comparação.

```java
public static void comparePdfWithGetDifferenceMethod(
        Path inputFile1, Path inputFile2, Path diffOutputFile, Path destinationOutputFile) throws Exception {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer comparer = new GraphicalPdfComparer();
        ImagesDifference imagesDifference = comparer.getDifference(document1.getPages().get_Item(1),
                document2.getPages().get_Item(1));

        ImageIO.write(imagesDifference.differenceToImage(Color.getRed(), Color.getWhite()),
                "png", diffOutputFile.toFile());
        ImageIO.write(imagesDifference.getDestinationImage(), "png", destinationOutputFile.toFile());
        imagesDifference.dispose();
    }
    System.out.println("Difference images saved to " + diffOutputFile + " and " + destinationOutputFile);
}
```

## Compare páginas específicas lado a lado

Use este exemplo quando apenas as páginas selecionadas devem ser comparadas e salvas como um resultado PDF lado a lado.

1. Abra os dois objetos PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de origem.
1. Configure [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) para o modo de comparação necessário.
1. Compare as páginas selecionadas e salve o PDF de saída.

```java
public static void comparingSpecificPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1.getPages().get_Item(1), document2.getPages().get_Item(1),
                outputFile.toString(), options);
    }
    System.out.println("Specific pages comparison saved to " + outputFile);
}
```

## Compare graficamente documentos PDF completos

Este exemplo gera um relatório gráfico em PDF que destaca as diferenças visuais em todos os documentos.

1. Abra os dois objetos PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de origem.
1. Configure o limite, a cor e a resolução do [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/).
1. Compare os documentos completos e salve o PDF da saída gráfica.

```java
public static void comparePdfWithCompareDocumentsToPdfMethod(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer pdfComparer = new GraphicalPdfComparer();
        pdfComparer.setThreshold(3.0);
        pdfComparer.setColor(Color.getBlue());
        pdfComparer.setResolution(new Resolution(300));
        pdfComparer.compareDocumentsToPdf(document1, document2, outputFile.toString());
    }
    System.out.println("Graphical comparison saved to " + outputFile);
}
```

## Compare documentos inteiros lado a lado

Use este exemplo quando todos os documentos devem ser comparados página por página em uma saída PDF lado a lado.

1. Abra os dois objetos PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de origem.
1. Configure [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) para o comportamento de comparação desejado.
1. Compare os documentos completos e salve o resultado como PDF.

```java
public static void comparingEntireDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1, document2, outputFile.toString(), options);
    }
    System.out.println("Entire document comparison saved to " + outputFile);
}
```
