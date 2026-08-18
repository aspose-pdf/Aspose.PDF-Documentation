---
title: Extraia dados vetoriais de um arquivo PDF usando Java
linktitle: Extraia dados vetoriais de PDF
type: docs
weight: 80
url: /java/extract-vector-data-from-pdf/
description: Aspose.PDF facilita a extração de dados vetoriais de um arquivo PDF. Você pode obter os dados vetoriais, como posição, limites do retângulo e saída SVG.
lastmod: "2026-06-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## Acesse dados vetoriais de um documento PDF

Use `GraphicsAbsorber` para inspecionar elementos gráficos vetoriais em uma página e escrever sua geometria básica em um arquivo de texto.

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) e visite a [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino para coletar operações de gráficos vetoriais.
1. Itere pelos objetos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraídos e leia suas coleções de retângulo, posição e operador.
1. Crie o texto de saída com detalhes de geometria e contagem de operadores para cada elemento.
1. Grave os dados vetoriais extraídos no arquivo de saída.

```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## Salvar gráficos vetoriais de página em SVG

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtenha o alvo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) do documento.
1. Chame `page.trySaveVectorGraphics(outputFile.toString())` para exportar o conteúdo gráfico vetorial dessa página diretamente para SVG.

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## Salve cada elemento extraído em um SVG separado

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) e visite a [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie o diretório de saída para os subcaminhos extraídos antes de gravar qualquer arquivo.
1. Itere através dos objetos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraídos e chame `saveToSvg(...)` para cada elemento.
1. Salve cada elemento extraído em um arquivo SVG separado.

```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## Combine elementos extraídos em um único SVG

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) e visite a [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie a marcação do wrapper SVG que conterá os fragmentos do vetor combinados.
1. Itere através dos objetos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraídos e anexe cada fragmento SVG gerado.
1. Grave a saída SVG combinada no arquivo de destino.

```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## Extraia um único elemento vetorial

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) e visite a [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Obtenha o [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) necessário da coleção de elementos extraídos.
1. Verifique se o elemento selecionado é um [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) e desça até seus elementos aninhados quando necessário.
1. Salve o elemento vetorial selecionado no arquivo SVG de saída.

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```
