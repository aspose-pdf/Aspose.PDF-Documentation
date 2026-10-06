---
title: 使用 Java 从 PDF 文件提取矢量数据
linktitle: 从 PDF 提取矢量数据
type: docs
weight: 80
url: /zh/java/extract-vector-data-from-pdf/
description: Aspose.PDF 使从 PDF 文件中提取矢量数据变得简单。您可以获取矢量数据，例如位置、矩形边界和 SVG 输出。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## 从 PDF 文档访问矢量数据

使用 `GraphicsAbsorber` 检查页面上的矢量图形元素并将其基本几何信息写入文本文件。

1. 在 a 中打开源 PDF。 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) 并访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 收集矢量图形操作。
1. 遍历提取的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 对象并读取它们的矩形、位置和操作符集合。
1. 为每个元素构建包含几何形状和运算符计数细节的输出文本。
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

1. 在 a 中打开源 PDF。 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 从文档中。
1. 调用 `page.trySaveVectorGraphics(outputFile.toString())` 将该页面的矢量图形内容直接导出为 SVG。

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## 将每个提取的元素保存为单独的 SVG

1. 在 a 中打开源 PDF。 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) 并访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 在写入任何文件之前，为提取的子路径创建输出目录。
1. 遍历提取的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 对象和调用 `saveToSvg(...)` 对于每个元素。
1. 将每个提取的元素保存为单独的 SVG 文件。

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

## 合并提取的元素为单个 SVG

1. 在 a 中打开源 PDF。 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) 并访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 创建将容纳合并矢量片段的 SVG 包装标记。
1. 遍历提取的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) objects 并追加每个生成的 SVG 片段。
1. 将合并后的 SVG 输出写入目标文件。

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

## 提取单个矢量元素

1. 在 a 中打开源 PDF。 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 创建一个 [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) 并访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 获取所需的 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 从提取的元素集合中。
1. 检查所选元素是否为一个 [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) 并在需要时深入其嵌套元素。
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
