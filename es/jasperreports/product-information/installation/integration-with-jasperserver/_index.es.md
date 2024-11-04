```
   <property name="contentType" value="application/pdf"/>

   <property name="titleKey" value="exporters.Pdf"/>

   <property name="iconClass" value="fa fa-file-pdf-o"/>

</bean>

```

{{% alert color="primary" %}}

2. Agregar el siguiente nuevo exportador a la **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\exporters.xml** archivo.

{{% /alert %}}

```
<bean id="pdfExporter" class="com.jaspersoft.jasperserver.war.action.AwsPdfExporter" parent="baseReportExporter">

   <property name="exportParameters" ref="AsposeExportParameters"/>

   <property name="setResponseContentLength" value="true"/>

</bean>

```

{{% alert color="primary" %}}

3. Reiniciar el servidor de aplicaciones JasperServer.

{{% /alert %}}

   <property name="iconSrc" value="/images/pdf.gif"/>

   <property name="parameterDialogName" value="dlg"/>

   <property name="exportParameters" ref="AsposeExportParameters"/>

   <property name="currentExporter" ref="AsposePdfExporter"/>

</bean>



```

{{% alert color="primary" %}}



2. Localiza el elemento <util:map id=”exporterConfigMap> en el archivo **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** y añade las siguientes líneas:



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

3. Copia todas las imágenes GIF de la carpeta \lib de **Aspose-pdf-jasperreports.zip** a <InstallDir>\apache-tomcat\webapps\jasperserver\images\.

4. Copia **Aspose-pdf-jasperreports.jar** de la carpeta \lib en **Aspose.PDF.JasperReports.zip** a <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.

5. Agrega las siguientes líneas al archivo **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.



   Este bean puede contener varias configuraciones destinadas a configurar la exportación. Por ejemplo, puedes usar la función de mapeo de fuentes de JasperReports o especificar la ubicación del archivo de licencia de Aspose.Cells para JasperReports.

  

{{% /alert %}}



```

<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

<property name="localizedFontMap" ref="localePdfFontMap"/>



<!-- Descomenta para aplicar una licencia. Verifica la ruta de la licencia.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/


jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>

```

{{% alert color="primary" %}}



6. Ejecute JasperServer y abra cualquier informe para ver. Si los pasos anteriores se realizaron correctamente, verá un icono para exportar a través de Aspose.PDF para JasperReports en la lista de formatos disponibles.



   **Aspose.PDF para JasperReports está integrado**



![todo:image_alt_text](integration-with-jasperserver_1.png)



{{% /alert %}}

```