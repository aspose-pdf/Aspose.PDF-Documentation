---

title: Integração com JasperServer

type: docs

weight: 30

url: /jasperreports/integration-with-jasperserver/

lastmod: "2021-06-05"

---



{{% alert color="primary" %}}



A integração do Aspose.PDF para JasperReports com o JasperServer é descrita abaixo.



{{% /alert %}}



Nos passos seguintes, <InstallDir> representa o diretório de instalação do JasperServer.



{{% alert color="primary" %}}



1. Adicione as seguintes novas propriedades de exportador ao arquivo **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**.



{{% /alert %}}



```

<bean id="AsposePdfExporter" class="com.aspose.pdf.jr3_7_0.jasperreports.AsposeServerPdfExporter" parent="baseReportExporter">

   <property name="exportParameters" ref="AsposeExportParameters"/>

   <property name="setResponseContentLength" value="true"/>

</bean>



<bean id="AsposePdfExporterConfiguration" class="com.jaspersoft.jasperserver.war.action.ExporterConfigurationBean">


   <property name="descriptionKey" value="Pdf - PDF via Aspose.PDF for JasperReports"/>


<property name="iconSrc" value="/images/pdf.gif"/>

<property name="parameterDialogName" value="dlg"/>

<property name="exportParameters" ref="AsposeExportParameters"/>

<property name="currentExporter" ref="AsposePdfExporter"/>

</bean>
```

{{% alert color="primary" %}}

2. Localize o elemento <util:map id=”exporterConfigMap> no arquivo **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** e adicione as seguintes linhas:

{{% /alert %}}


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


3. Copie todas as imagens GIF da pasta \lib de **Aspose-pdf-jasperreports.zip** para <InstallDir>\apache-tomcat\webapps\jasperserver\images\.

4. Copie **Aspose-pdf-jasperreports.jar** da pasta \lib no **Aspose.PDF.JasperReports.zip** para <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.

5. Adicione as seguintes linhas ao arquivo **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.



   Este bean pode conter várias configurações destinadas a configurar a exportação. Por exemplo, você pode usar o recurso de mapeamento de fontes do JasperReports ou especificar a localização do arquivo de licença do Aspose.Cells para JasperReports.

  

{{% /alert %}}



```

<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

<property name="localizedFontMap" ref="localePdfFontMap"/>



<!-- Descomente para aplicar uma licença. Verifique o caminho da licença.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/


jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>

-->

</bean>



```

{{% alert color="primary" %}}



6. Execute o JasperServer e abra qualquer relatório para visualizar. Se as etapas anteriores foram realizadas corretamente, você verá um ícone para exportar via Aspose.PDF para JasperReports na lista de formatos disponíveis.



   **Aspose.PDF para JasperReports está integrado**



![todo:image_alt_text](integration-with-jasperserver_1.png)



{{% /alert %}}