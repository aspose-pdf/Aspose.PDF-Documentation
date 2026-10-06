---
title: Recortar páginas PDF em Java
linktitle: Recortando páginas PDF
type: docs
weight: 70
url: /pt/java/crop-pages/
description: Aprenda como recortar páginas PDF e ajustar as caixas de recorte, aparar, sangria e mídia em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recorte páginas e ajuste as caixas de página em arquivos PDF com Java
Abstract: Este artigo explica como recortar páginas PDF usando Aspose.PDF for Java. Ele aborda a atribuição de um novo retângulo de recorte às caixas de recorte, aparar, arte e sangria, e o recorte de uma página automaticamente com base no conteúdo de imagem detectado.
---
Aspose.PDF for Java permite que você recorte páginas tanto por coordenadas de caixa explícitas quanto com base no conteúdo detectado.

## Cortar uma página definindo as caixas de página

Use este exemplo quando precisar aplicar a mesma área de corte às caixas de página principais.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar o novo corte [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
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

## Recortar uma página pelo conteúdo detectado

Use este exemplo quando a área de recorte deve ser derivada da primeira imagem detectada na página.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Usar [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para detectar posicionamentos de imagens.
1. Defina a caixa de recorte para o retângulo da imagem se uma for encontrada, então salve o documento.

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
