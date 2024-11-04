---
title: 获取嵌入图像的分辨率和尺寸
linktitle: 获取分辨率和尺寸
type: docs
weight: 40
url: /java/get-resolution-and-dimensions-of-embedded-images/
description: 本节展示了如何获取嵌入图像的分辨率和尺寸的详细信息
lastmod: "2021-06-05"
---

本主题解释了如何使用 Aspose.PDF 命名空间中的操作类，它们提供了在不提取图像的情况下获取图像分辨率和尺寸信息的功能。

有不同的方法可以实现这一点。本文解释了如何使用 `arraylist` 和 [图像放置类](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement)。

1. 首先，加载源 PDF 文件（包含图像）。
1. 然后创建一个 ArrayList 对象来保存文档中任何图像的名称。
1. 使用 Page.Resources.Images 属性获取图像。
1. 创建一个堆栈对象来保存图像的图形状态，并使用它来跟踪不同的图像状态。

1. 创建一个定义当前变换的ConcatenateMatrix对象。它还支持缩放、旋转和倾斜任何内容。它将新矩阵与先前的矩阵连接起来。请注意，我们不能从头开始定义变换，只能修改现有的变换。

1. 因为我们可以使用ConcatenateMatrix修改矩阵，所以我们可能还需要恢复到原始图像状态。使用GSave和GRestore操作符。这些操作符是成对的，因此它们应该一起调用。例如，如果您在进行一些复杂变换的图形工作并最终将变换返回到初始状态，方法将是这样的：

```java
// 绘制一些文本
GSave

ConcatenateMatrix  // 在操作符之后旋转内容

// 一些图形工作

ConcatenateMatrix // 在操作符之后缩放（带有先前的旋转）内容

// 其他一些图形工作

GRestore

// 绘制一些文本
```

结果是，文本以常规形式绘制，但在文本操作符之间执行了一些变换。
 为了显示图像或绘制表单对象和图像，我们需要使用 Do 操作符。

我们还有一个名为 XImage 的类，它提供了两个属性，宽度和高度，可以用来获取图像尺寸。

1. 执行一些计算来计算图像分辨率。
2. 在命令提示符中显示图像名称及其信息。

以下代码片段展示了如何在不从 PDF 文档中提取图像的情况下获取图像的尺寸和分辨率。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // 加载源 PDF 文件
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // 定义图像的默认分辨率
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // 定义保存图像名称的数组列表对象
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // 将对象插入堆栈
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // 获取文档第一页的所有操作符
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // 使用 GSave/GRestore 操作符恢复之前设置的转换
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // 实例化 ConcatenateMatrix 对象，因为它定义了当前的转换矩阵。
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // 创建 Do 操作符，用于从资源中绘制对象。它绘制表单对象和图像对象
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // 保存上一个状态并将当前状态推到堆栈的顶部
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // 丢弃当前状态并恢复上一个状态
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // 将当前矩阵与状态矩阵相乘
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // 如果这是一个图像绘制操作符
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // 创建 XImage 对象以保存 PDF 第一页的图像
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // 获取图像尺寸
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // 获取图像的高度和宽度信息
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // 基于上述信息计算分辨率
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // 显示每个图像的尺寸和分辨率信息
                    System.out.printf(_dataDir + "image %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // 保存输出文档
                doc.save(_dataDir);
            }
        }
    }
}
```