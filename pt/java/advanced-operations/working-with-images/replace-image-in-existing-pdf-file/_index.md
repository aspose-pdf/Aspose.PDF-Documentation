---
title: Substituir imagem em arquivo PDF existente usando Java
linktitle: Substituir imagem
type: docs
weight: 70
url: /pt/java/replace-image-in-existing-pdf-file/
description: Aprenda como substituir imagens incorporadas em arquivos PDF existentes em Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Substituir imagens em arquivos PDF existentes com Java
Abstract: Este artigo mostra como substituir imagens em documentos PDF usando Aspose.PDF for Java. Ele aborda a substituição de uma imagem por seu índice de recurso e a substituição da primeira posição de imagem correspondida encontrada com ImagePlacementAbsorber.
---
Use a coleção de imagens da página ou a busca baseada em posicionamento, dependendo de quão precisamente você precisa direcionar a imagem.

## Substituir uma imagem por índice de recurso

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse os recursos de imagem no destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Substitua o recurso de imagem de destino pelo novo arquivo de imagem.
1. Salve o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## Substituir uma imagem usando `ImagePlacementAbsorber`

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) e visite o destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Obtenha o destino [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) e substitua-o pelo novo fluxo de imagem.
1. Salve o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```
