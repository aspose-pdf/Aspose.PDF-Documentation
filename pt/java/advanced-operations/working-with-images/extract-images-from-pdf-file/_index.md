---
title: Extrair Imagens de Arquivo PDF usando Java
linktitle: Extrair Imagens
type: docs
weight: 30
url: /pt/java/extract-images-from-pdf-file/
description: Aprenda como extrair imagens incorporadas de arquivos PDF em Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Extrair imagens de arquivos PDF com Java
Abstract: Este artigo mostra como extrair imagens de documentos PDF usando Aspose.PDF for Java. Ele cobre salvar um recurso de imagem específico de uma página e exportar imagens que se encontram dentro de uma região retangular selecionada.
---
Aspose.PDF for Java suporta extração direta de recursos de imagem e filtragem baseada em posicionamento.

## Extrair uma imagem incorporada por índice

Use este exemplo quando precisar salvar um recurso de imagem específico de uma página PDF.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acessar o destino [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) dos recursos da página.
1. Salve o fluxo de imagem em um arquivo de saída.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## Extrair imagens de uma região específica da página

Use este exemplo quando somente as imagens posicionadas dentro de um retângulo selecionado devem ser exportadas.

1. Defina o destino [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) e abra o PDF de origem.
1. Usar [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para inspeccionar a colocação de imagens na página.
1. Salve apenas as imagens cuja colocação se encaixa dentro da região selecionada.

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```
