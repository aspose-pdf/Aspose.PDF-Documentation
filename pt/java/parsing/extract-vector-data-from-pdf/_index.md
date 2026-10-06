---
title: Extrair Dados Vetoriais de um arquivo PDF usando Java
linktitle: Extrair Dados Vetoriais de PDF
type: docs
weight: 80
url: /pt/java/extract-vector-data-from-pdf/
description: Aspose.PDF facilita a extração de dados vetoriais de um arquivo PDF. Você pode obter os dados vetoriais, como posição, limites retangulares e saída SVG.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## Acessar dados vetoriais de um documento PDF

Usar `GraphicsAbsorber` inspecionar elementos gráficos vetoriais em uma página e gravar sua geometria básica em um arquivo de texto.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) e visite o alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) para coletar operações de gráficos vetoriais.
1. Iterar através dos extraídos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) objetos e ler suas coleções de retângulo, posição e operador.
1. Construa o texto de saída com detalhes de geometria e contagem de operadores para cada elemento.
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

## Salvar gráficos vetoriais da página em SVG

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Obter o destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) do documento.
1. Chamada `page.trySaveVectorGraphics(outputFile.toString())` para exportar o conteúdo gráfico vetorial dessa página diretamente para SVG.

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## Salve cada elemento extraído em um SVG separado

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) e visite o alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie o diretório de saída para os subcaminhos extraídos antes de gravar quaisquer arquivos.
1. Iterar através dos extraídos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) objetos e chamada `saveToSvg(...)` para cada elemento.
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

## Combine os elementos extraídos em um único SVG

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) e visite o alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie a marcação de contêiner SVG que conterá os fragmentos vetoriais combinados.
1. Iterar através dos extraídos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) objetos e anexe cada fragmento SVG gerado.
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

## Extrair um único elemento vetorial

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar um [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) e visite o alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Obter o necessário [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) da coleção de elementos extraídos.
1. Verifique se o elemento selecionado é um [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) e desça para seus elementos aninhados quando necessário.
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
