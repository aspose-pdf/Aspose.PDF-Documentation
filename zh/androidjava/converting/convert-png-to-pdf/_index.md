---
title: 将 PNG 转换为 PDF
linktitle: 将 PNG 转换为 PDF
type: docs
weight: 200
url: /zh/androidjava/convert-png-to-pdf/
lastmod: "2026-07-01"
description: 本文展示了如何在 Android 的 Java 应用程序中使用 Aspose.PDF 库将 PNG 转换为 PDF。您可以通过简单的步骤将 PNG 图像转换为 PDF 格式。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 支持将 PNG 图像转换为 PDF 格式的功能。请检查下面的代码片段以实现您的任务。

<abbr title="Portable Network Graphics">PNG</abbr> 指的是一种使用无损压缩的光栅图像文件格式，这使其在用户中很受欢迎。

您可以使用以下步骤将 PNG 转换为 PDF 图像：

1. 加载输入 PNG 图像
1. 读取高度和宽度值
1. 创建新文档并添加页面
1. 设置页面尺寸
1. 保存输出文件

此外，下面的代码片段展示了如何在您的 Java 应用程序中将 PNG 转换为 PDF：

```java
    public void convertPNGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```

