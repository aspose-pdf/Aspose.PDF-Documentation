---
title: Page Orientation
linktitle: 页面方向
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: 在 Aspose.PDF for Reporting Services 中配置 PDF 报告的页面方向。自定义布局以获得更好的呈现效果。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

报告定义语言不允许明确指定报告中页面的方向。使用 Aspose.PDF for Reporting Services，您可以轻松指示导出器生成横向页面方向的 PDF 文档。默认方向是纵向。

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## 例子

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>
```

