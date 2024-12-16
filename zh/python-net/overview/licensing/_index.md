---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 50
url: /zh/python-net/licensing/
description: Aspose. PDF for Python 邀请客户获取 Classic 许可证。以及使用有限许可证来更好地探索产品。
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 评估版本的限制

我们希望客户在购买前彻底测试我们的组件，因此评估版本允许您像正常使用一样使用它。

- **带有评估水印的 PDF。** Aspose.PDF for Python 的评估版本提供完整的产品功能，但生成的 PDF 文档中的所有页面都在顶部带有“仅限评估。由 Aspose.PDF 创建。版权 2002-2020 Aspose Pty Ltd”的水印。

>如果您希望测试 Aspose.PDF 而没有评估版本的限制，您也可以申请 30 天的临时许可证。
 请参考 [如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

许可证可以从文件或流对象加载。设置许可证的最简单方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并指定不带路径的文件名，如下面的示例所示。

如果您将任何其他 Aspose for Python 组件与 Aspose.PDF for Python 一起使用，请为许可证指定命名空间，例如 [Aspose.Pdf.License 类]()。

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```