---
title: 安装到报表服务器
linktitle: 安装到报表服务器
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

如果您手动安装 Aspose.PDF for Reporting Services，而不是使用 MSI 安装程序，则只需执行这些步骤。 MSI 安装程序自动执行所有必要的安装和注册操作。

{{% /alert %}}

在以下步骤中，您将需要复制并修改 Microsoft SQL Server Reporting Services 安装目录中的文件。 SSRS 2016程序集位于zip包的\Bin\SSRS2016目录下； SSRS 2017 程序集位于 \Bin\SSRS2017 目录中； SSRS 2019 程序集位于 \Bin\SSRS2019 目录中； SSRS 2022 程序集位于 \Bin\SSRS2022 目录中； Power BI 报表服务器程序集位于 \Bin\PowerBI 目录中。

**步骤 1.** 找到报表服务器安装目录。 Microsoft SQL Server 的根目录通常为C:\Program Files\Microsoft SQL Server。 Reporting Services 2016、Reporting Services 2017 及更高版本以及 Power BI 报表服务器的进一步流程略有不同：

- 默认情况下，Report Server 2016 安装在 C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer 目录中。如果您使用自定义命名实例而不是默认实例，则默认路径将为 C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- 默认情况下，Report Server 2017 及更高版本安装在 C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer 目录中。
- Power BI 报表服务器默认安装在 C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer 目录中。

在下文中，Reporting Services 的安装目录（上述路径之一）将被引用为 `<Instance>`。

**步骤2.** 将相应SSRS版本的Aspose.Pdf.ReportingServices.dll复制到`<Instance>\bin`文件夹。

**步骤 3.** 将 Aspose.PDF for Reporting Services 注册为渲染扩展。打开 `<Instance>\rsreportserver.config` 文件并将以下行添加到 `<Render>` 元素中：

## 例子

```xml
<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>
</Render>
```

**步骤 4.** 为 Aspose.PDF for Reporting Services 提供执行权限。打开`<Instance>\rssrvpolicy.config` 文件并将以下文本添加为​​第二个外部`<CodeGroup>` 元素中的最后一项，该元素应为`<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):`

## 例子

```xml

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>
```

**步骤 5.** 验证 Aspose.PDF for Reporting Services 是否已成功安装。打开 Reporting Services Web 门户并检查报表的可用导出格式列表。您可以通过启动 Web 浏览器并在地址栏中键入 Reporting Services Web 门户 URL（默认情况下为http://@@KEEP_0@@/reports/).）来启动 Web 门户。选择 Web 门户中可用的报告之一并拉出“导出”下拉列表。您应该看到导出格式列表，包括 Aspose.PDF for Reporting Services 扩展提供的格式。通过 Aspose.PDF 项选择 PDF。

![Install to report server](install-to-report-server_1.png)

单击所选项目。它将以所选格式生成报告，将其发送到客户端，并且根据您的 Web 浏览器设置，显示“保存文件”对话框以选择保存导出报告的位置，或自动将文件下载到您的“下载”文件夹。

恭喜，您已成功安装 Aspose.PDF for Reporting Services 并将报告导出为 PDF 文档！


