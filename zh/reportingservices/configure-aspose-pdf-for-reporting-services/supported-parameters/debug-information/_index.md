---
title: 调试信息
type: docs
weight: 90
url: /zh/reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

渲染或渲染结果有问题是不可避免的。由于保密或隐私等原因，我们无法获得用户报告中使用的数据源，因此无法重现报告中的错误。为了让客户和开发人员之间的沟通更加轻松顺畅，我们添加了此参数。如果在使用 Aspose.PDF for Reporting Services 渲染报告时遇到问题，请设置此报告参数，然后您将获得 XML 格式的渲染文档。之后，请在产品论坛中发布 XML 文件给我们。

{{% /alert %}}

{{% alert color="primary" %}}
**参数名称**: SavingXmlFormat  
**数据类型**: Boolean  
**支持的值**: True, False (默认)  

**示例**
{{< highlight csharp >}}

<Render>
...

<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
```
<Configuration>
<SavingXmlFormat > 真 </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```