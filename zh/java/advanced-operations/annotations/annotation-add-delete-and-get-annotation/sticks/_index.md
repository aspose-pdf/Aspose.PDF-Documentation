---
title: PDF 粘性注释
linktitle: 粘性注释
type: docs
weight: 50
url: zh/java/sticky-annotations/
description: 本主题关于粘性注释，以水印注释为例展示在文本中。它用于在页面上表示图形。查看代码片段以解决此任务。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 添加水印注释

水印注释用于表示将在页面上以固定大小和位置打印的图形，而不考虑打印页面的尺寸。

您可以在 PDF 页面的特定位置使用 [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) 添加水印文本。水印的透明度也可以通过使用透明度属性来控制。

请查看以下代码片段以添加 WatermarkAnnotation。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // 创建注释
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        // 将注释添加到页面的注释集合中
        page.getAnnotations().add(wa);

        // 创建 TextState 以进行字体设置
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        // 设置注释文本的透明度级别
        wa.setOpacity(0.5);

        // 向注释添加文本
        wa.setTextAndState(new String[] { "Aspose.PDF", "Watermark", "Demo" }, ts);

        // 保存文档
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## 获取水印注释

```java
    public static void GetWatermarkAnnotation() {
        // 加载PDF文件
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // 使用AnnotationSelector过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## 删除水印注释

```java
    public static void DeleteWatermarkAnnotation() {
         // 加载PDF文件
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // 使用AnnotationSelector过滤注释
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // 删除注释
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```