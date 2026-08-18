---
title: Cortar páginas PDF em Java
linktitle: Cortar páginas PDF
type: docs
weight: 70
url: /java/crop-pages/
description: Aprenda como cortar páginas PDF e ajustar caixas de corte, corte, sangramento e mídia em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cortar páginas e ajustar caixas de páginas em arquivos PDF com Java
Abstract: Este artigo explica como cortar páginas PDF usando Aspose.PDF para Java. Ele abrange a atribuição de um novo retângulo de corte às caixas de corte, corte, arte e sangramento, e o corte automático de uma página com base no conteúdo da imagem detectada.
---
Aspose.PDF para Java permite cortar páginas por coordenadas de caixa explícitas ou com base no conteúdo detectado.

## Cortar uma página definindo caixas de página

Use este exemplo quando precisar aplicar a mesma área de corte às caixas da página principal.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o novo corte [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Aplique o retângulo às caixas de página relacionadas ao corte e salve o documento.

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## Cortar uma página por conteúdo detectado

Use este exemplo quando a área de corte precisar ser derivada da primeira imagem detectada na página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Use [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para detectar posicionamentos de imagens.
1. Defina a caixa de corte para o retângulo da imagem, se for encontrado, e salve o documento.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
