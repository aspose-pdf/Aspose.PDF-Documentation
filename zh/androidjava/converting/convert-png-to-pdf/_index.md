---
title: 将PNG转换为PDF 
linktitle: 将PNG转换为PDF
type: docs
weight: 200
url: zh/androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: 本文展示了如何在您的Android应用程序中通过Aspose.PDF库将PNG转换为PDF。您可以使用简单的步骤将PNG图像转换为PDF格式。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** 支持将PNG图像转换为PDF格式的功能。查看下一个代码片段以实现您的任务。

<abbr title="Portable Network Graphics">PNG</abbr> 是一种使用无损压缩的光栅图像文件格式，这使得它在用户中很受欢迎。

您可以使用以下步骤将PNG转换为PDF图像：

1. 加载输入的PNG图像
1. 读取高度和宽度值
1. 创建新文档并添加页面
1. 设置页面尺寸
1. 保存输出文件

此外，下面的代码片段展示了如何在您的Java应用程序中将PNG转换为PDF：

```java
    public void convertPNGtoPDF () {
        // 初始化文档对象
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