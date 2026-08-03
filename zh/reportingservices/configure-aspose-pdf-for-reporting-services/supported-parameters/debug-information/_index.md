---
title: 调试信息
linktitle: 调试信息
type: docs
weight: 90
url: /reportingservices/debug-information/
description: 访问和分析 Aspose.PDF for Reporting Services 中 PDF 渲染的调试信息，以有效地解决问题。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

渲染或者渲染结果出现问题是在所难免的。由于保密或隐私等原因，我们无法获取用户报告中使用的数据源，因此无法重现报告中的错误。为了让客户和开发者之间的沟通更加轻松、顺畅，我们添加了这个参数。如果您在使用 Aspose.PDF for Reporting Services 渲染报表时遇到问题，请设置此报表参数，然后您将获得 XML 格式的渲染文档。之后，请在产品论坛中为我们发布 XML 文件。

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## 例子

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}
