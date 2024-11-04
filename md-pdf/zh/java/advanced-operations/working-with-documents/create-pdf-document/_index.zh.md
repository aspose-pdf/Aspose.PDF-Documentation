---
title: 创建文档
type: docs
weight: 10
url: /java/create-pdf-document/
description: Aspose.PDF for Java 帮助您在几个简单的步骤中创建 PDF 文档和可搜索的 PDF 文件。
lastmod: "2021-06-05"
---

在本文中，我们将展示如何使用 Aspose.PDF for Java API 在 Java 应用程序中轻松生成和读取 PDF 文件。

Aspose.PDF for Java API 让 Java 应用程序开发人员能够在他们的应用程序中嵌入 PDF 文档处理功能。它可以用于创建和读取 PDF 文件，而无需在底层机器上安装任何其他软件。Aspose.PDF for Java 可用于各种 Java 应用程序类型，如桌面应用程序、JSP 和 JSF 应用程序。

## 如何使用 Java 创建 PDF 文件

要使用 Java 创建 PDF 文件，可以使用以下步骤。

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 类的对象

1. 将 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) 对象添加到 Document 对象的 Pages 集合中
1. 将 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) 添加到页面的 [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) 集合中
1. 保存生成的 PDF 文档

```java
package com.aspose.pdf.examples;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.Document.CallBackGetHocr;

public class ExampleCreate {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    
    public static void Create() {        
        Document document = new Document();
 
        //添加页面
        Page page = document.getPages().add();
         
        // 向新页面添加文本
        page.getParagraphs().add(new TextFragment("Hello World!"));
         
        // 保存更新的 PDF
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


在这种情况下，我们创建一个A4页面大小、纵向方向的PDF单页文档。我们的页面将在页面的左上部分包含一个“Hello, World”。

此外，Aspose.PDF for Java提供了创建可搜索PDF的能力。让我们学习下一个代码片段：

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // 创建回调 - 逻辑识别PDF图像的文本。使用外部OCR支持HOCR标准(http://en.wikipedia.org/wiki/HOCR)。
        // 我们使用了免费的谷歌tesseract OCR(http://en.wikipedia.org/wiki/Tesseract_%28software%29)
        
        CallBackGetHocr cbgh = new CallBackGetHocr() {
            @Override
            public String invoke(java.awt.image.BufferedImage img) {
                File outputfile = new File(_dataDir + "test.jpg");
                try {
                    ImageIO.write(img, "jpg", outputfile);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        
                try {
                    java.lang.Process process = Runtime.getRuntime().exec("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    System.out.println("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    process.waitFor();
        
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
        
                // 将out.html读取为字符串
                File file = new File(_dataDir + "out.hocr");
                StringBuilder fileContents = new StringBuilder((int) file.length());
                Scanner scanner = null;
                try {
                    scanner = new Scanner(file);
                    String lineSeparator = System.getProperty("line.separator");
        
                    while (scanner.hasNextLine()) {
                        fileContents.append(scanner.nextLine() + lineSeparator);
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } finally {
                    if (scanner != null)
                        scanner.close();
                }
        
                // 删除临时文件
                File fileOut = new File(_dataDir + "out.hocr");
                if (fileOut.exists()) {
                    fileOut.delete();
                }
                File fileTest = new File(_dataDir + "test.jpg");
                if (fileTest.exists()) {
                    fileTest.delete();
                }
        
                return fileContents.toString();
            }
        };
        // 结束回调
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```