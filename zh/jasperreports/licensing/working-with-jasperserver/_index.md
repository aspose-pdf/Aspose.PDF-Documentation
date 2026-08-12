---
title: 使用 JasperServer
linktitle: 使用 JasperServer
type: docs
weight: 20
description: 探索如何使用 Aspose.PDF 高效地使用 JasperServer。轻松将报告导出为专业 PDF。
lastmod: "2021-06-05"
---

## <ins>在applicationContext.xml中设置licenseFile Exporter参数

{{% alert color="primary" %}}

此方法与 JasperServer 一起使用。

{{% /alert %}}

1. 将许可证下载到您的计算机并将其复制到“`<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` folder, where  ```<InstallDir>```代表JasperServer安装目录。
2. 找到“`<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml`”文件并添加以下行：

```xml
 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  
    INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
注意：请注意安装路径不应包含任何空格，例如 C:/Program Files/JasperServer...，因为这会导致访问许可证文件时出现问题。
{{% /alert %}}

## 验证许可证是否有效

将任何报告导出为 PDF 格式并检查报告是否包含评估消息。如果没有评估消息，则许可证工作正常。

Aspose.PDF for JasperReports 在评估模式下工作时注入水印

![Integration with JasperServer_1](working-with-jasperserver_1.png)

Aspose.PDF for JasperReports 在评估模式下工作时注入水印

![Integration with JasperServer_2](working-with-jasperserver_2.png)

