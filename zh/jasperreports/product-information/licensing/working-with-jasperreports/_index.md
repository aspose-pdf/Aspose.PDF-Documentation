---
title: 使用 JasperReports
linktitle: 使用 JasperReports
type: docs
weight: 10
url: /zh/jasperreports/working-with-jasperreports/
description: 精通使用 Aspose.PDF 处理 JasperReports。使用高级功能创建和导出 PDF 格式的详细报告。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.Words for JasperReports 可从下载页面免费、无时间限制地进行评估。该产品的评估版和许可版是相同的下载。

当您对评估版感到满意时， [购买许可证](http://www.aspose.com/purchase/default.aspx)。确保您理解并同意许可条款。

{{% /alert %}}

订单付款后，可以从订单页面下载许可证。该许可证是经过数字签名的明文 XML 文件。许可证包含客户名称、购买的产品和许可证类型等信息。请勿修改许可证文件的内容：这会使许可证失效。

激活许可证有多种方法：

- [调用设置许可证](/pdf/zh/jasperreports/working-with-jasperreports/#call-setlicense).
- [在代码中设置导出器参数](/pdf/zh/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [在 **applicationContext.xml** 中设置导出器参数](/pdf/zh/jasperreports/working-with-jasperserver/).

前两个与 JasperReports 一起使用，最后一个与 JasperServer 一起使用。

## 调用设置许可证

此方法与 JasperReports 一起使用。

1. 将许可证下载到您的计算机并将其复制到适当的文件夹（例如应用程序的文件夹或 JasperReports\lib）。
2. 将以下代码添加到您的项目中：

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;
try
{ 
    // create a stream object containing the license file
   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // Set the license through the stream object
 
   License license = new License();
   license.setLicense(fstream);
}
catch(Exception ex)
{
   System.out.println(ex.toString());
}

```

## 在代码中设置licenseFile Exporter参数

此方法与 JasperReports 一起使用。

1. 将许可证下载到您的计算机并将其复制到适当的文件夹（例如应用程序的文件夹或 JasperReports\lib）。
2. 将以下代码添加到您的项目中：

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```


