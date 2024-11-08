---
title: 围绕中心点旋转印章
type: docs
weight: 10
url: /zh/net/rotating-stamp-about-the-center-point/
description: 本节介绍如何使用 Stamp 类围绕中心点旋转印章。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 在 [Aspose.PDF for .NET](/pdf/zh/net/) 中允许您在现有的 PDF 文件中添加印章。有时，用户确实需要旋转印章。在本文中，我们将看到如何围绕其中心点旋转印章。

{{% /alert %}}

## 实现细节

[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类允许您在 PDF 文件中添加水印。 你可以使用 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1) 方法指定要作为印章添加的图像。[SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/methods/setorigin) 方法允许您设置添加的印章的原点；此原点是印章的左下坐标。您还可以使用 [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/methods/setimagesize) 方法设置图像的大小。

现在，我们来看一下如何围绕印章的中心旋转印章。 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类提供了一个名为 Rotation 的属性。这个属性设置或获取印章内容从 0 到 360 的旋转角度。我们可以指定从 0 到 360 的任意旋转值。通过指定旋转值，我们可以围绕印章的中心点旋转它。如果 Stamp 是 Stamp 类型的对象，那么可以将旋转值指定为 aStamp.Rotation = 90。在这种情况下，印章将围绕其内容的中心点旋转 90 度。以下代码片段展示了如何围绕中心点旋转印章：

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}