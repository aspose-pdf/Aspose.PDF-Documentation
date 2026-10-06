---
title: 在 Java 中使用 PDF 操作符
linktitle: 使用操作符
type: docs
weight: 90
url: /zh/java/working-with-operators/
description: 了解如何在 Java 中使用低级 PDF 操作符进行内容流操作、图像放置、XForm 重用以及图形清理。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中使用低级 PDF 操作符进行内容流控制
Abstract: 本文阐述了如何在 Aspose.PDF for Java 中使用低级 PDF 运算符。了解如何精确放置图像、绘制可重用的 XForm 内容以及从 PDF 页面中移除图形运算符。
aliases:
    - "/zh/java/operators/"
---
## PDF 运算符及其用法简介

运算符是指定应执行的某些操作的 PDF 关键字，例如在页面上绘制图形形状。运算符关键字与具名对象的区别在于缺少初始的斜杠字符 (2Fh)。运算符仅在内容流中才有意义。

内容流是一个 PDF 流对象，其数据由描述在页面上绘制的图形元素的指令组成。有关 PDF 运算符的更多详情可在以下位置找到： [PDF 规范](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

在需要直接控制 Java 中的 PDF 内容流时使用此页面，例如使用显式矩阵运算放置图像、通过 XForm 多次重用相同图形，或从页面删除低层次的绘图指令。

## 使用 PDF 运算符添加图像

在图像放置必须在内容流层面精确控制，而不是通过更高级别的布局 API 时，使用低层次运算符。

1. 打开源 PDF 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 将输入图像流添加到页面资源中，并保留返回的资源名称。
1. 创建一个 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 它定义目标区域并构建一个 [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) 从其边界。
1. 使用 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) 保留当前图形状态， [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) 定位图像， [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) 绘制它，并 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) 恢复先前的状态。
1. 保存更新后的 PDF 文档。

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

## 在页面上绘制可重复使用的 XForm 内容

当相同的图像或图形需要渲染多于一次且不在 PDF 文件中重复资源时，请使用此方法。

1. 打开源 PDF 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), 获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), 并访问其 [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. 用...包裹现有页面内容 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) 和 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) 以防后续的转换泄漏到原始内容流中。
1. 创建一个 [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) 资源，将图像添加到表单资源中，并使用 [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) 加 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) 在表单内部绘制图像。
1. 通过添加平移矩阵并执行表单名称，将相同的表单放置在多个页面坐标上 `Do` 操作员。
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

## 删除页面中的图形操作符

当页面包含应直接从内容流中删除的矢量绘图操作符时，请使用此示例。

1. 打开源 PDF 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. 遍历页面内容操作符并收集实例 [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/)，并且 [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. 从页面内容中删除收集的操作符并保存更新后的 PDF。

此技术仅删除目标绘图指令。如果页面还包含相关的文本标签或其他非图形操作符，这些项目将保留在内容流中，可能需要单独的清理步骤。

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

- [Java 中的高级 PDF 操作](/pdf/zh/java/advanced-operations/)
- [使用 Java 在 PDF 中处理图像](/pdf/zh/java/working-with-images/)
- [在 Java 中处理 PDF 页面](/pdf/zh/java/working-with-pages/)
- [在 Java 中使用矢量图形](/pdf/zh/java/working-with-vector-graphics/)
