---
title: 如何使用 Aspose.Pdf for JasperReports 离线演示
type: docs
weight: 10
url: /jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports 包含多个演示项目，以帮助您开始从应用程序导出报告到 PDF 格式。这些演示是标准的 JasperReports 演示，已被修改以演示如何使用新的导出器。

{{% /alert %}}
### **运行 Aspose.PDF for JasperReports 演示**
要运行 Aspose.PDF for JasperReports 演示：

{{% alert color="primary" %}}

1. 从 <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579> 下载 JasperReports。确保下载包含源代码和演示的整个归档项目，而不仅仅是单个 JAR。
2. 将归档项目解压到硬盘上的某个位置，例如 C:\。
3. 1. 将 **Aspose.PDF.JasperReports.zip** 中的 \demo 文件夹中的所有演示文件夹复制到 ```<InstallDir>```\jasperreports\demo\samples，其中 ```<InstallDir>``` 是你解压 JasperReports 的位置。这一步是必要的，因为演示构建脚本依赖于 JasperReports 文件夹结构，否则你需要修改构建脚本。
2. 将 **Aspose.PDF.Jasperreports.jar** 文件从 **Aspose.PDF.JasperReports.zip** 中的 \lib 文件夹复制到 ```<InstallDir>```\jasperreports\lib。
3. 从 <http://ant.apache.org/bindownload.cgi> 下载 ANT 工具。
4. 解压 ANT 工具并按照工具手册中的说明设置环境变量。
5. 将当前目录更改为 ```<InstallDir>```\demo\hsqldb 并运行以下命令行：
   ant runServer
6. 打开新的命令提示符实例，并将当前目录更改为 Aspose.PDF for JasperReports 演示中的一个，例如 ```<InstallDir>```\demo\samples\charts.ap。
7. 在命令行上运行以下命令： ant javac – 编译测试应用程序的Java源文件。  
11. ant compile – 编译XML报告设计并生成.jasper文件  
12. ant fill – 用数据填充编译后的报告设计并生成.jrprint文件  
13. 在命令行中运行以下命令：  
   ant pdf – 从演示报告中生成PDF文件。  
14. 打开生成的文档之一进行查看，例如在Adobe Reader或其他应用程序中查看```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf。  

{{% /alert %}}