---
title: JasperServer와 통합
linktitle: JasperServer와 통합
type: docs
weight: 30
url: /ko/jasperreports/integration-with-jasperserver/
description: Aspose.PDF를 JasperServer와 통합하는 방법을 배웁니다. 서버 보고서를 고품질 PDF 형식으로 쉽게 내보낼 수 있습니다.
lastmod: "2026-09-09"
---

{{% alert color="primary" %}}

아래에 Aspose.PDF for JasperReports와 JasperServer를 통합하는 방법이 설명됩니다.

{{% /alert %}}

다음 단계에서 <InstallDir> JasperServer 설치 디렉터리를 나타냅니다.

{{% alert color="primary" %}}

1. 다음 새로운 내보내기 속성을 추가합니다

**<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF\\flows\\viewReportBeans.xml** 파일.

{{% /alert %}}

```xml
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

2. 위치를 찾으세요 <util:map id=”exporterConfigMap> 그 안에 있는 요소 

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** 파일에 다음 줄을 추가하십시오:

{{% /alert %}}

```xml
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

3. **Aspose-pdf-jasperreports.zip**의 \lib 폴더에서 모든 GIF 이미지를 복사하여 <InstallDir>\apache-tomcat\webapps\jasperserver\images\.
4. 복사 **Aspose-pdf-jasperreports.jar**를 **Aspose.PDF.JasperReports.zip**의 \lib 폴더에서 <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.
5. 다음 줄을 **에 추가하십시오<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF\\applicationContext.xml** 파일.

   이 빈은 내보내기를 구성하기 위한 다양한 설정을 포함할 수 있습니다. 예를 들어, JasperReports 폰트 매핑 기능을 사용하거나 Aspose.Cells for JasperReports 라이선스 파일의 위치를 지정할 수 있습니다.
  
{{% /alert %}}

```xml
<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
<property name="localizedFontMap" ref="localePdfFontMap"/>

<!-- Uncomment to apply a license. Check the license path.
<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/
jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>
-->
</bean>

```

{{% alert color="primary" %}}

6. JasperServer를 실행하고 보고서를 하나 열어 보세요. 이전 단계가 올바르게 수행되었다면 사용 가능한 형식 목록에 Aspose.PDF for JasperReports를 통한 내보내기 아이콘이 표시됩니다.

   **Aspose.PDF for JasperReports가 통합되었습니다**

![JasperServer와 통합](integration-with-jasperserver_1.png)

{{% /alert %}}
