```

 <property name="className" value="com.aspose.pdf.jr3_7_0.jasperreports.AsposeServerPdfExporter"/>

   <property name="parametersModelName" value="AsposeExportParameters"/>

</bean>

```



2. 然后在 **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\reportFlow.xml** 文件中添加以下条目来配置导出器。

```

<action id="AsposeExportAction" class="com.jaspersoft.jasperserver.war.action.AnticipatedExporter"/>

<property name="exporter" ref="AsposePdfExporter"/>

</action>

```



3. 在 **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\flowReportBeans.xml** 文件中，定义以下 bean：

```

<bean id="AsposeExportParameters" class="com.jaspersoft.jasperserver.war.action.AnticipatedExporterParameters">

   <property name="exporterConfiguration" ref="AsposePdfExporterConfiguration"/>

</bean>

```



4. 最后，重新启动 JasperServer，使更改生效。

```
<property name="iconSrc" value="/images/pdf.gif"/>

<property name="parameterDialogName" value="dlg"/>

<property name="exportParameters" ref="AsposeExportParameters"/>

<property name="currentExporter" ref="AsposePdfExporter"/>

</bean>

```

{{% alert color="primary" %}}

2. 找到 **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** 文件中的 <util:map id=”exporterConfigMap> 元素，并添加以下几行：

{{% /alert %}}

```

<util:map id="exporterConfigMap">

<entry key="pdf" value-ref="pdfExporterConfiguration"/>

<entry key="xls" value-ref="xlsExporterConfiguration"/>

<entry key="rtf" value-ref="rtfExporterConfiguration"/>

<entry key="csv" value-ref="csvExporterConfiguration"/>

<entry key="swf" value-ref="swfExporterConfiguration"/>

<!-- START of ADDED LINES -->

<entry key="Aspose_pdf" value-ref="AsposePdfExporterConfiguration"/>

<!-- END of NEW LINES -->

</util:map>

```

{{% alert color="primary" %}}

3. 将所有 GIF 图像从 **Aspose-pdf-jasperreports.zip** 的 \lib 文件夹复制到 <InstallDir>\apache-tomcat\webapps\jasperserver\images\。

4. 将 **Aspose-pdf-jasperreports.jar** 从 **Aspose.PDF.JasperReports.zip** 的 \lib 文件夹复制到 <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\。

5. 将以下行添加到 **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** 文件中。
{{% /alert %}}

   这个 bean 可能包含各种配置设置，用于配置导出。例如，您可以使用 JasperReports 字体映射功能或指定 Aspose.Cells for JasperReports 许可证文件的位置。

```
<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

<property name="localizedFontMap" ref="localePdfFontMap"/>

<!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/

jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>

```

{{% alert color="primary" %}}



6. 运行 JasperServer 并打开任何报告进行查看。如果前面的步骤执行正确，您将在可用格式列表中看到通过 Aspose.PDF for JasperReports 导出的图标。



   **Aspose.PDF for JasperReports 已集成**



![todo:image_alt_text](integration-with-jasperserver_1.png)



{{% /alert %}}

```