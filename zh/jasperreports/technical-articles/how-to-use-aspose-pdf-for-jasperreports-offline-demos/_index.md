---
title: 如何 - 使用 Aspose.PDF 进行 JasperReports 离线演示
linktitle: 如何 - 使用 Aspose.PDF 进行 JasperReports 离线演示
type: docs
weight: 10
url: /zh/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: 探索 Aspose.PDF for JasperReports 的离线演示。以亲身实践的方式学习实际的实现和功能。
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports includes a number of demo projects to help you get started exporting reports to PDF formats from your application. The demos are standard JasperReports demos that have been modified to demonstrate how to use new exporters.

{{% /alert %}}

## 为 JasperReports 演示运行 Aspose.PDF

要为 JasperReports 演示运行 Aspose.PDF：

{{% alert color="primary" %}}

1. 从 <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. 下载 JasperReports 确保下载包含源代码和演示的整个存档项目，而不仅仅是单个 JAR。
2. 将存档项目解压到硬盘上的某个位置，例如C:\.
3. 将 **Aspose.PDF.JasperReports.zip** 中的 \demo 文件夹中的所有演示文件夹复制到“`<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>``` 是您将 JasperReports 解压到的位置。此步骤是必需的，因为演示构建脚本依赖于 JasperReports 文件夹结构，否则您必须修改构建脚本。
4. 将 **aspose.pdf.jasperreports.jar** 文件从 **Aspose.PDF.JasperReports.zip** 中的 \lib 文件夹复制到“`<InstallDir>`”\jasperreports\lib。
5. 从<http://ant.apache.org/bindownload.cgi>.下载ANT工具
6. 解压 ANT 工具并按照工具手册中的说明设置环境变量。
7. Change the current directory to ```<InstallDir>```\demo\hsqldb and run the following command line:
   ant运行服务器
8. 打开新的命令提示符实例并将当前目录更改为 JasperReports 演示的 Aspose.PDF 之一，例如```<InstallDir>```\demo\samples\charts.ap。
9. 在命令行中运行以下命令：
10. ant javac – 编译测试应用程序的 Java 源文件。
11. ant compile – 编译 XML 报告设计并生成 .jasper 文件
12. ant fill – 用数据填充已编译的报告设计并生成 .jrprint 文件
13. 在命令行中运行以下命令：
   ant pdf – 从演示报告生成 PDF 文件。
14. 打开生成的文档之一进行查看，例如在 Adob​​e Reader 或其他应用程序中打开```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf。

{{% /alert %}}

