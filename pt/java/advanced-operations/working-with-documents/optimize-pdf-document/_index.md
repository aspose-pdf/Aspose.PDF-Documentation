---
title: Otimizar arquivos PDF em Java
linktitle: Otimizar PDF
type: docs
weight: 30
url: /pt/java/optimize-pdf/
description: Aprenda como otimizar, comprimir e reduzir o tamanho do arquivo PDF em Java usando Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comprima recursos PDF e reduza o tamanho do arquivo com Java
Abstract: Este artigo explica como otimizar arquivos PDF usando Aspose.PDF for Java. Ele cobre otimização de todo o documento, compressão de recursos, redução da qualidade de imagem, remoção de objetos e streams não utilizados, vinculação de streams duplicados, desincorporação de fontes, achatamento de anotações e formulários, conversão para escala de cinza e compressão de imagem Flate.
---
Aspose.PDF for Java expõe recursos de otimização através `Document.optimize`, `optimizeResources`, e `OptimizationOptions`.

## Otimizar um PDF com otimização geral de documento

Use este exemplo quando você quiser que o Aspose.PDF aplique a rotina de otimização de documento inteiro incorporada.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `optimize()` no documento.
1. Salve o arquivo otimizado e compare os tamanhos original e de saída.

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Reduza o tamanho do PDF otimizando recursos

Este exemplo foca na otimização ao nível de recurso sem configurar manualmente opções individuais.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Execute `optimizeResources()` para otimizar recursos internos.
1. Salve o resultado e imprima os tamanhos dos arquivos de entrada e saída.

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Compactar todas as imagens em um PDF

Use esta abordagem quando documentos com muitas imagens precisam de um tamanho de arquivo menor e alguma redução na qualidade da imagem é aceitável.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) e habilite a compactação de imagem com o nível de qualidade necessário.
1. Otimize os recursos do documento com essas configurações.
1. Salve o arquivo otimizado e compare os tamanhos dos arquivos.

```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Remover objetos não utilizados de um PDF

Este exemplo remove objetos não utilizados que podem permanecer na estrutura do documento após edições ou mesclagens.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) e habilite a remoção de objetos não utilizados.
1. Otimize os recursos e salve o arquivo atualizado.
1. Imprima os tamanhos do arquivo original e do reduzido.

```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Remover fluxos não utilizados de um PDF

Use esta abordagem quando quiser descartar dados de fluxo que não são mais referenciados pelo documento.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configure [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) para remover fluxos não utilizados.
1. Otimize os recursos, salve o documento de saída e compare os tamanhos dos arquivos.

```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Vincular fluxos duplicados em um PDF

Este exemplo deduplica fluxos repetidos para que o conteúdo idêntico possa ser armazenado apenas uma vez.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) e habilite o vínculo de fluxo duplicado.
1. Otimize os recursos, salve o documento de saída e imprima os tamanhos dos arquivos.

```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Desincorporar fontes de um PDF

Use esta opção quando reduzir o tamanho do arquivo for mais importante do que manter os dados de fontes incorporadas na saída.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configure [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) para desincorporar fontes.
1. Otimize os recursos, salve o documento e compare os tamanhos dos arquivos.

```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Achatar anotações em um PDF

Este exemplo converte anotações em conteúdo de página estático, de modo que elas não permanecem mais como objetos interativos.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere através de cada [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e seu [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) coleção.
1. Aplanar todas as anotações e salvar o documento atualizado.

```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Aplanar campos de formulário PDF

Use esta abordagem quando os campos de formulário preenchíveis devem se tornar conteúdo fixo antes da distribuição ou arquivamento.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Verifique se o documento contém widgets de formulário.
1. Achatar cada [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) representado por um [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Salve o arquivo de saída e imprima os tamanhos dos arquivos.

```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Converter um PDF para escala de cinza

Este exemplo altera cada página para tons de cinza, o que pode ajudar a reduzir a complexidade de cores e padronizar a saída para fluxos de trabalho de arquivamento ou impressão.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere através de cada [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) no documento.
1. Chame `makeGrayscale()` em cada página e salve o arquivo de saída.

```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## Usar compressão de imagem FlateDecode

Use este padrão quando quiser aplicar compressão baseada em Flate a imagens durante a otimização de recursos PDF.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) e defina a codificação da imagem para [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.
1. Otimize os recursos do documento e salve o arquivo de saída.

```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## Imprimir tamanhos de arquivos original e otimizado

Este método auxiliar relata a diferença de tamanho entre o arquivo de origem e o arquivo de saída otimizado.

1. Leia o tamanho do arquivo de entrada.
1. Leia o tamanho do arquivo de saída.
1. Imprima ambos os valores em uma única mensagem de status.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
