---
title: 使用 Java 从 PDF 文件中提取矢量数据
linktitle: 从 PDF 中提取矢量数据
type: docs
weight: 80
url: /java/extract-vector-data-from-pdf/
description: Aspose.PDF 可以轻松地从 PDF 文件中提取矢量数据。您可以获得矢量数据，例如位置、矩形边界和 SVG 输出。
lastmod: "2026-06-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## 从 PDF 文档访问矢量数据

使用 `GraphicsAbsorber` 检查页面上的矢量图形元素并将其基本几何形状写入文本文件。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/)并访问目标[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)来收集矢量图形操作。
1. 迭代提取的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 对象并读取它们的矩形、位置和运算符集合。
1. 使用每个元素的几何和操作员计数详细信息构建输出文本。
1. 将提取的矢量数据写入输出文件。

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

## 将页面矢量图形保存为 SVG

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 从文档中获取目标[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 调用`page.trySaveVectorGraphics(outputFile.toString())`将该页面的矢量图形内容直接导出为SVG。

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## 将每个提取的元素保存到单独的 SVG

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/)并访问目标[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 在写入任何文件之前，为提取的子路径创建输出目录。
1. 迭代提取的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 对象并为每个元素调用 `saveToSvg(...)`。
1. 将每个提取的元素保存到单独的 SVG 文件中。

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

## 将提取的元素合并到单个 SVG 中

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/)并访问目标[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 创建将包含组合矢量片段的 SVG 包装器标记。
1. 迭代提取的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 对象并附加每个生成的 SVG 片段。
1. 将组合的 SVG 输出写入目标文件。

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

## 提取单个向量元素

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/)并访问目标[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 从提取的元素集合中获取所需的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/)。
1. 检查所选元素是否为 [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) 并在需要时下降到其嵌套元素。
1. 将选定的矢量元素保存到输出 SVG 文件。

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
