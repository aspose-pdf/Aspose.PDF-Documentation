---

title: 与 JasperServer 一起工作

type: docs

weight: 20

url: /jasperreports/working-with-jasperserver/

lastmod: "2021-06-05"

---



#### <ins>**在 applicationContext.xml 中设置 licenseFile Exporter 参数**

{{% alert color="primary" %}}



此方法用于 JasperServer。



{{% /alert %}}



1. 下载许可证到你的计算机并将其复制到 ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` 文件夹，其中 ```<InstallDir>``` 代表 JasperServer 的安装目录。

2. 找到 ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` 文件并添加以下行：



```

 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  

    INF/Aspose.Total.JasperReports.lic"/>

</bean>

```

{{% alert color="primary" %}}


注意: 请注意，安装路径中不应包含任何空格，例如 C:/Program Files/JasperServer…，因为这会导致访问许可证文件时出现问题。

{{% /alert %}}



#### **验证许可证是否有效**

将任何报告导出为 PDF 格式，并检查报告中是否包含评估消息。如果没有评估消息，则表示许可证正常工作。



**Aspose.PDF for JasperReports 在评估模式下工作时会注入水印**



![todo:image_alt_text](working-with-jasperserver_1.png)







**Aspose.PDF for JasperReports 在评估模式下工作时会注入水印**



![todo:image_alt_text](working-with-jasperserver_2.png)