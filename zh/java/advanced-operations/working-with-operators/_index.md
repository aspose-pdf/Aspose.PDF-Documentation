---
title: 在 Java 中使用 PDF 运算符
linktitle: 与运营商合作
type: docs
weight: 90
url: /java/working-with-operators/
description: 了解如何在 Java 中使用低级 PDF 运算符进行内容流操作、图像放置、XForm 重用和图形清理。
lastmod: "2026-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中使用低级 PDF 运算符进行内容流控制
Abstract: 本文介绍如何在 Aspose.PDF for Java 中使用低级 PDF 运算符。了解如何精确放置图像、绘制可重用的 XForm 内容以及从 PDF 页面中删除图形运算符。
---
## PDF运算符及其用法简介

运算符是一个 PDF 关键字，指定应执行的某些操作，例如在页面上绘制图形形状。运算符关键字与命名对象的区别在于缺少初始斜线字符 (2Fh)。运算符仅在内容流内部才有意义。

内容流是一个 PDF 流对象，其数据由描述要在页面上绘制的图形元素的指令组成。有关 PDF 运算符的更多详细信息，请参阅 [PDF 规范](https://opensource.adobe.com/dc-acrobat-sdk-docs/)。

当您需要在 Java 中直接控制 PDF 内容流时，例如使用显式矩阵数学放置图像、通过 XForm 多次重复使用同一图形，或者从页面中删除低级绘图指令，请使用此页面。

## 使用 PDF 运算符添加图像

当必须在内容流级别而不是通过更高级别的布局 API 精确控制图像放置时，请使用低级别运算符。

1. 使用[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)打开源PDF并获取目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 将输入图像流添加到页面资源中，并保留返回的资源名称。
1. 创建一个定义目标区域的[矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)，并从其边界构建一个[矩阵](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/)。
1. 使用 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) 保留当前图形状态，使用 [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) 定位图像，使用 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) 绘制图像，使用 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) 恢复之前的状态。
1. 保存更新的 PDF 文档。

```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## 在页面上绘制可重用的 XForm 内容

当需要多次渲染同一图像或图形而不复制 PDF 文件中的资源时，请使用此方法。

1. 使用[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)打开源PDF，获取目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)，并访问其[OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/)。
1. 使用 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) 和 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) 包装现有页面内容，以便后续转换不会泄漏到原始内容流中。
1. 创建一个 [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) 资源，将图像添加到表单资源中，然后使用 [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) 加上 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) 在表单内绘制图像。
1. 通过添加转换矩阵并使用 `Do` 运算符执行表单名称，将相同的表单放置在多个页面坐标处。
1. 恢复图形状态并保存输出 PDF。

```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## 从页面中删除图形运算符

当页面包含应直接从内容流中删除的矢量绘图运算符时，请使用此示例。

1. 使用[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)打开源PDF并获取目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 迭代页面内容运算符并收集 [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/)、[ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/) 和 [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/) 的实例。
1. 从页面内容中删除收集的运算符并保​​存更新的 PDF。

该技术仅删除目标绘图指令。如果页面还包含相关文本标签或其他非图形运算符，则这些项目仍保留在内容流中，并且可能需要单独的清理过程。

```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## 相关主题

- [Java中的高级PDF操作](/pdf/java/advanced-operations/)
- [使用 Java 处理 PDF 中的图像](/pdf/java/working-with-images/)
- [在 Java 中处理 PDF 页面](/pdf/java/working-with-pages/)
- [在 Java 中使用矢量图形](/pdf/java/working-with-vector-graphics/)
