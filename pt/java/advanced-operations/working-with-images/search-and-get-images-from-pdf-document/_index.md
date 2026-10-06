---
title: Obter e pesquisar imagens em PDF
linktitle: Obter e pesquisar imagens
type: docs
weight: 40
url: /pt/java/search-and-get-images-from-pdf-document/
description: Aprenda como pesquisar e inspecionar imagens em documentos PDF em Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Pesquisar e inspecionar imagens em arquivos PDF com Java
Abstract: Este artigo mostra como pesquisar e inspecionar imagens em documentos PDF usando Aspose.PDF for Java. Ele abrange a leitura da geometria de posicionamento da imagem, a detecção do tipo de cor, a extração de texto alternativo e o cálculo da resolução efetiva da imagem a partir dos operadores de página.
---
Aspose.PDF for Java pode inspecionar informações de posicionamento de imagens, bem como dados de desenho em nível inferior.

## Obter parâmetros de posicionamento da imagem

Use este exemplo quando precisar inspecionar a geometria da imagem e a resolução efetiva em uma página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Use [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para coletar posicionamentos de imagens.
1. Exiba o tamanho, as coordenadas e a resolução de cada imagem posicionada.

```java
public static void extractImageParams(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("image width: " + imagePlacement.getRectangle().getWidth());
            System.out.println("image height: " + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX: " + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY: " + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution: " + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution: " + imagePlacement.getResolution().getY());
        }
    }
}
```

## Detectar tipos de cor da imagem

Use este exemplo quando precisar contar imagens em tons de cinza e RGB em uma página PDF.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Use [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para iterar sobre as imagens das páginas.
1. Leia o [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) de cada imagem e exiba os totais.

```java
public static void extractImageTypesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        int grayscaled = 0;
        int rgb = 0;

        document.getPages().get_Item(1).accept(absorber);

        System.out.println("--------------------------------");
        System.out.println("Total Images = " + absorber.getImagePlacements().size());

        int imageCounter = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            ColorType colorType = imagePlacement.getImage().getColorType();
            if (colorType == ColorType.Grayscale) {
                grayscaled++;
                System.out.println("Image " + imageCounter + " is Grayscale...");
            } else if (colorType == ColorType.Rgb) {
                rgb++;
                System.out.println("Image " + imageCounter + " is RGB...");
            }
            imageCounter++;
        }

        System.out.println("--------------------------------");
        System.out.println("Grayscale Images = " + grayscaled);
        System.out.println("RGB Images = " + rgb);
    }
}
```

## Extrair texto alternativo da imagem

Use este exemplo quando precisar inspecionar o texto de acessibilidade associado às imagens da página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Use [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para coletar posicionamentos de imagens.
1. Leia o texto alternativo de cada imagem e exiba o resultado.

```java
public static void extractImageAltText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("Name in collection: " + imagePlacement.getImage().getNameInCollection());
            List<String> lines = imagePlacement.getImage().getAlternativeText(document.getPages().get_Item(1));
            if (!lines.isEmpty()) {
                System.out.println("Alt Text: " + lines.get(0));
            } else {
                System.out.println("Alt Text: ");
            }
        }
    }
}
```

## Calcular informações da imagem a partir dos operadores de página

Use este exemplo quando precisar derivar o tamanho efetivo da imagem e a resolução a partir dos operadores de conteúdo de página de baixo nível.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e colete nomes de recursos de imagem.
1. Acompanhe o estado gráfico enquanto itera pelos operadores de página.
1. Resolva cada operação de desenho de imagem e calcule suas dimensões e resolução efetivas.

```java
public static void extractImageInformationFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int defaultResolution = 72;
        List<Matrix> graphicsState = new ArrayList<>();
        List<String> imageNames = Arrays.asList(document.getPages().get_Item(1).getResources().getImages().getNames());

        graphicsState.add(new Matrix(1, 0, 0, 1, 0, 0));

        for (Operator operator : document.getPages().get_Item(1).getContents()) {
            if (operator instanceof GSave) {
                graphicsState.add(new Matrix(graphicsState.get(graphicsState.size() - 1)));
            } else if (operator instanceof GRestore) {
                graphicsState.remove(graphicsState.size() - 1);
            } else if (operator instanceof ConcatenateMatrix concatenateMatrix) {
                Matrix current = graphicsState.get(graphicsState.size() - 1);
                graphicsState.set(graphicsState.size() - 1, current.multiply(concatenateMatrix.getMatrix()));
            } else if (operator instanceof Do doOperator) {
                if (imageNames.contains(doOperator.getName())) {
                    Matrix lastCtm = graphicsState.get(graphicsState.size() - 1);
                    int index = imageNames.indexOf(doOperator.getName()) + 1;
                    XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(index);

                    double scaledWidth = Math.sqrt(Math.pow(lastCtm.getA(), 2) + Math.pow(lastCtm.getB(), 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCtm.getC(), 2) + Math.pow(lastCtm.getD(), 2));

                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    String info = String.format(
                            "%s image %s (%.2f:%.2f): res %.2f x %.2f",
                            inputFile,
                            doOperator.getName(),
                            scaledWidth,
                            scaledHeight,
                            resHorizontal,
                            resVertical);
                    System.out.println(info);
                }
            }
        }
    }
}
```
