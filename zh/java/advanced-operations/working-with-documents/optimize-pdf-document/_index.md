---
title: 在 Java 中优化 PDF 文件
linktitle: 优化 PDF
type: docs
weight: 30
url: /zh/java/optimize-pdf/
description: 了解如何在 Java 中使用 Aspose.PDF 优化、压缩并减小 PDF 文件大小。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 压缩 PDF 资源并减小文件大小。
Abstract: 本文解释了如何使用 Aspose.PDF for Java 对 PDF 文件进行优化。它涵盖了全文档优化、资源压缩、图像质量降低、移除未使用的对象和流、链接重复流、取消嵌入字体、扁平化注释和表单、灰度转换以及 Flate 图像压缩。
---
Aspose.PDF for Java 通过 `Document.optimize`, `optimizeResources`，和 `OptimizationOptions`.

## 使用通用文档优化来优化 PDF

当您希望 Aspose.PDF 应用内置的整个文档优化例程时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 调用 `optimize()` 在文档上。
1. 保存优化后的文件，并比较原始文件和输出文件的大小。

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 通过优化资源减小 PDF 大小

此示例专注于资源级优化，而无需手动配置各个选项。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 运行 `optimizeResources()` 优化内部资源。
1. 保存结果并打印输入文件和输出文件的大小。

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 压缩 PDF 中的所有图像

当文档中图片较多且需要更小的文件尺寸且可以接受一定的图像质量降低时，使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 并启用具有所需质量级别的图像压缩。
1. 使用这些设置优化文档资源。
1. 保存优化后的文件并比较文件大小。

```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 从 PDF 中删除未使用的对象

此示例会删除在编辑或合并后可能仍保留在文档结构中的未使用对象。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 并启用删除未使用的对象。
1. 优化资源并保存更新后的文件。
1. 打印原始和压缩后的文件大小。

```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 从 PDF 中删除未使用的流

当您想要丢弃文档中不再被引用的流数据时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 配置 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 删除未使用的流。
1. 优化资源，保存输出文档，并比较文件大小。

```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 链接 PDF 中的重复流

此示例对重复的流进行去重，以便相同的内容只存储一次。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 并启用重复流链接。
1. 优化资源，保存输出文档，并打印文件大小。

```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 从 PDF 中取消嵌入字体

当减小文件大小比在输出中保留嵌入的字体数据更重要时，请使用此选项。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 配置 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 取消嵌入字体。
1. 优化资源，保存文档，并比较文件大小。

```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 在 PDF 中展平注释

此示例将注释转换为静态页面内容，使它们不再保持交互式对象。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 遍历每个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 和它的 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 集合。
1. 将所有注释扁平化并保存更新后的文档。

```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 展平 PDF 表单字段

在可填写的表单字段在分发或存档之前应转换为固定内容时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 检查文档是否包含表单小部件。
1. 扁平化每个 [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) 由 a 表示 [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. 保存输出文件并打印文件大小。

```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 将 PDF 转换为灰度

此示例将每页转换为灰度，这有助于降低颜色复杂度，并为归档或打印工作流标准化输出。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 遍历每个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 在文档中。
1. 调用 `makeGrayscale()` 在每页上并保存输出文件。

```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## 使用 FlateDecode 图像压缩

当您想在 PDF 资源优化期间对图像使用基于 Flate 的压缩时，请使用此模式。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 并将图像编码设置为 [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.
1. 优化文档资源并保存输出文件。

```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## 打印原始和优化后的文件大小

此辅助方法报告源文件与优化后输出文件之间的大小差异。

1. 读取输入文件的大小。
1. 读取输出文件的大小。
1. 在单个状态消息中打印两个值。

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
