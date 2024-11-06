---
title: 下载和配置 Aspose.Pdf 在 Struts 1.3
type: docs
weight: 10
url: zh/java/downloads-and-configure-aspose-pdf-in-struts-1-3/
lastmod: "2021-06-05"
---

## 下载适用于 Struts 1.3 的 Aspose.PDF Java

您可以从以下位置下载/检出项目源代码：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_for_Struts)

## 从源代码构建适用于 Struts 1.3 的 Aspose.PDF Java

从上述任何一个代码库检出源代码后，应用以下 mvn 命令：

{{< highlight java >}}

 $ mvn -U clean package

{{< /highlight >}}

这将在目标文件夹中生成 "Strutsbookapp.war"。

要部署 .war 文件，只需将其复制到正在运行的 Apache tomcat 服务器的 webapp 目录。