---
title: Substituir imagem em arquivo PDF existente usando Java
linktitle: Substituir imagem
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: Aprenda como substituir imagens incorporadas em arquivos PDF existentes em Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Substitua imagens em arquivos PDF existentes por Java
Abstract: Este artigo mostra como substituir imagens em documentos PDF usando Aspose.PDF para Java. Abrange a substituição de uma imagem por seu índice de recursos e a substituição do primeiro posicionamento de imagem correspondente encontrado por ImagePlacementAbsorber.
---
Use a coleção de imagens da página ou a pesquisa baseada em posicionamento, dependendo da precisão com que você precisa direcionar a imagem.

## Substitua uma imagem por índice de recursos

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse os recursos de imagem na [página] de destino (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Substitua o recurso de imagem de destino pelo novo arquivo de imagem.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## Substitua uma imagem usando `ImagePlacementAbsorber`

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) e visite a [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Obtenha o alvo [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) e substitua-o pelo novo fluxo de imagem.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
