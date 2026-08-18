---
title: 用 Java 优化 PDF 文件
linktitle: 优化 PDF
type: docs
weight: 30
url: /java/optimize-pdf/
description: 了解如何使用 Aspose.PDF 在 Java 中优化、压缩和减小 PDF 文件大小。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 压缩 PDF 资源并减小文件大小
Abstract: 本文介绍如何使用 Aspose.PDF for Java 优化 PDF 文件。它涵盖整个文档优化、资源压缩、图像质量降低、删除未使用的对象和流、链接重复流、取消嵌入字体、扁平化注释和表单、灰度转换以及扁平化图像压缩。
---
Aspose.PDF for Java 通过`Document.optimize`、`optimizeResources` 和`OptimizationOptions` 公开优化功能。

## 通过一般文档优化来优化 PDF

当您希望 Aspose.PDF 应用内置的整个文档优化例程时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 对文档调用`optimize()`。
1. 保存优化后的文件并比较原始大小和输出大小。

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

此示例重点关注资源级优化，无需手动配置各个选项。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 运行`optimizeResources()`来优化内部资源。
1. Save the result and print the input and output file sizes.

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

当图像较多的文档需要较小的文件大小并且可以接受一定程度的图像质量降低时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
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

此示例删除编辑或合并后可能保留在文档结构中的未使用对象。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 并启用删除未使用的对象。
1. 优化资源并保存更新的文件。
1. 打印原始文件和缩小后的文件大小。

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

当您想要丢弃文档不再引用的流数据时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 配置 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 以删除未使用的流。
1. 优化资源、保存输出文档并比较文件大小。

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

此示例对重复的流进行重复数据删除，因此相同的内容只能存储一次。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 并启用重复流链接。
1. 优化资源、保存输出文档并打印文件大小。

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

当减小文件大小比在输出中保留嵌入字体数据更重要时，请使用此选项。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 配置 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 以取消嵌入字体。
1. 优化资源、保存文档并比较文件大小。

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

## 拼合 PDF 中的注释

此示例将注释转换为静态页面内容，以便它们不再保留交互式对象。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代每个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 及其 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 集合。
1. 拼合每个注释并保存更新的文档。

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

当可填写的表单字段在分发或存档之前应成为固定内容时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 检查文档是否包含表单小部件。
1. 展平由 [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/) 表示的每个 [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/)。
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

此示例将每个页面更改为灰度，这有助于降低颜色复杂性并标准化存档或打印工作流程的输出。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历文档中的每个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 在每个页面上调用`makeGrayscale()`并保存输出文件。

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

当您想要在 PDF 资源优化期间对图像应用基于 Flate 的压缩时，请使用此模式。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) 并将图像编码设置为 [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`。
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

## 打印原始文件和优化文件大小

此辅助方法报告源文件和优化输出文件之间的大小差异。

1. 读取输入文件的大小。
1. 读取输出文件的大小。
1. 在一条状态消息中打印这两个值。

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
