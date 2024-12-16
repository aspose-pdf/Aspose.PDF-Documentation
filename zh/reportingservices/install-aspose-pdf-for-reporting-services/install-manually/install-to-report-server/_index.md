---
title: 安装到报表服务器
type: docs
weight: 10
url: /zh/reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

只有在手动安装 Aspose.PDF for Reporting Services 而不是使用 MSI 安装程序时，才需要按照这些步骤操作。MSI 安装程序会自动执行所有必要的安装和注册操作。

{{% /alert %}}

在以下步骤中，您需要复制和修改 Microsoft SQL Server Reporting Services 所安装目录中的文件。SSRS 2016 程序集位于 zip 包的 \Bin\SSRS2016 目录中；SSRS 2017 程序集位于 \Bin\SSRS2017 目录中；SSRS 2019 程序集位于 \Bin\SSRS2019 目录中；SSRS 2022 程序集位于 \Bin\SSRS2022 目录中；Power BI 报表服务器程序集位于 \Bin\PowerBI 目录中。

{{% alert color="primary" %}}

**步骤 1.** 找到报表服务器安装目录。 Microsoft SQL Server 的根目录通常是 C:\Program Files\Microsoft SQL Server。进一步的过程对于 Reporting Services 2016、Reporting Services 2017 及更高版本以及 Power BI Report Server 略有不同：

- 默认情况下，Report Server 2016 安装在 C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer 目录中。如果您使用自定义命名实例而不是默认实例，默认路径将是 C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- 默认情况下，Report Server 2017 及更高版本安装在 C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer 目录中。
- 默认情况下，Power BI Report Server 安装在 C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer 目录中。

在以下文本中，Reporting Services 的安装目录（上述路径之一）将被称为 ```<Instance>```。
**步骤 2.** 将适用于相应 SSRS 版本的 Aspose.Pdf.ReportingServices.dll 复制到 ```<Instance>```\bin 文件夹中。
{{% /alert %}}

{{% alert color="primary" %}}
**步骤 3.** 将 Aspose.Pdf for Reporting Services 注册为渲染扩展。打开 ```<Instance>```\rsreportserver.config 文件，并在 ```<Render>``` 元素中添加以下行：
{{% /alert %}}

**示例**

{{< highlight csharp >}}

<Render>
...
<!--从这里开始。-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**步骤 4.** 为 Aspose.Pdf for Reporting Services 提供执行权限。打开 ```<Instance>```\rssrvpolicy.config 文件，并在第二个最外层的 ```<CodeGroup>``` 元素中添加以下文本作为最后一项（应为 ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```

{{% /alert %}}

**示例**

{{< highlight csharp >}}

<CodeGroup>
...

<CodeGroup>
...

<!--从这里开始。-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="此代码组授予对 AP4SSRS 程序集的完全信任。">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--到这里结束。-->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

{{% alert color="primary" %}}
**步骤5。** 验证 Aspose.Pdf for Reporting Services 是否成功安装。 打开 Reporting Services Web 门户并查看报表可用的导出格式列表。您可以通过启动 web 浏览器并在地址栏中键入 Reporting Services Web 门户 URL 来启动 Web 门户（默认情况下为 http://```<Reporting_Services_server_name>```/reports/）。选择 Web 门户中可用的报表之一并拉出导出下拉列表。您应该会看到导出格式列表，包括由 Aspose.Pdf for Reporting Services 扩展提供的格式。选择通过 Aspose.PDF 的 PDF 项目。

点击所选项目。它将在所选格式中生成报表，将其发送给客户端，并根据您的 web 浏览器设置，显示保存文件对话框以选择保存导出报表的位置，或自动将文件下载到您的下载文件夹。
{{% /alert %}}
