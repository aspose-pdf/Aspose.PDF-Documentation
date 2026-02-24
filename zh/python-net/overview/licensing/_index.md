---
title: Aspose PDF 许可证
linktitle: 许可与限制
type: docs
weight: 50
url: /zh/python-net/licensing/
description: Aspose.PDF for Python 邀请其客户获取经典许可证，并使用受限许可证以更好地探索产品。
lastmod: "2025-02-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python 的许可
Abstract: 本文讨论了 Aspose.PDF for Python 的限制和授权选项。它强调评估版允许完整功能测试，但会在生成的 PDF 上添加水印，显示 "Evaluation Only" 并附带版权信息。希望在无这些限制的情况下进行测试的用户可以使用 30 天的临时许可证。文章进一步说明了如何通过从文件或流加载来实现经典许可证，建议将许可证文件放置在与 Aspose.PDF.dll 相同的目录下，并使用 `Aspose.Pdf.License` 类设置许可证。提供了代码片段以演示授权过程。
---

## 评估版的限制

我们希望客户在购买前能够彻底测试我们的组件，因此评估版允许您像平常一样使用它。

- **带有评估水印的 PDF。** Aspose.PDF for Python 的评估版提供完整的产品功能，但生成的 PDF 文档的所有页面顶部都会加上水印，内容为 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd"。

>如果您想在不受评估版限制的情况下测试 Aspose.PDF，也可以申请 30 天的临时许可证。请参阅 [如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

许可证可以从文件或流对象加载。设置许可证的最简单方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并仅指定文件名而不使用路径，如下例所示。

如果您在使用 Aspose.PDF for Python 的同时使用了其他 Aspose for Python 组件，请像 [Aspose.Pdf.License 类]() 那样指定许可证的命名空间。

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```

