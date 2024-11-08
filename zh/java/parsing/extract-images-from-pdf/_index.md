---
title: 从 PDF 中提取图像
linktitle: 提取图像
type: docs
weight: 20
url: /zh/java/extract-images-from-the-pdf-file/
description: 如何使用 Aspose.PDF for Java 从 PDF 中提取部分图像
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 文档中的每一页都包含资源（图像、表单和字体）。我们可以通过调用 [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 方法访问这些资源。[Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) 类包含 [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection)，我们可以通过调用 [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) 方法获取图像列表。

因此，要从页面中提取图像，我们需要获取页面的引用，接着是页面资源，最后是图像集合。
我们可以通过索引来提取特定的图像。

图像的索引返回一个 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) 对象。
该对象提供一个 [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) 方法，可以用来保存提取的图像。以下代码片段展示了如何从 PDF 文件中提取图像。

```java
public static void Extract_Images(){
        // 文档目录的路径。
        String _dataDir = "/home/admin1/pdf-examples/Samples/";
        String filePath = _dataDir + "ExtractImages.pdf";

        // 加载 PDF 文档
        com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

        com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
        // 提取特定图像
        com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

        try {
            java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
            // 保存输出图像
            xImage.save(outputImage);
            outputImage.close();
        } catch (java.io.FileNotFoundException e) {
            // TODO: 处理异常
            e.printStackTrace();
        } catch (java.io.IOException e) {
            // TODO: 处理异常
            e.printStackTrace();
        }
    }
```