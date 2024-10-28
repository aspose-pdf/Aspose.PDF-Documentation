title: Integrasi dengan JasperServer

type: docs

weight: 30

url: /jasperreports/integration-with-jasperserver/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Mengintegrasikan Aspose.PDF untuk JasperReports dengan JasperServer dijelaskan di bawah ini.

{{% /alert %}}

Dalam langkah-langkah berikut <InstallDir> merupakan direktori instalasi JasperServer.

{{% alert color="primary" %}}

1. Tambahkan properti eksportir baru berikut ke file **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**.

{{% /alert %}}

```
<bean id="AsposePdfExporter" class="com.aspose.pdf.jr3_7_0.jasperreports.AsposeServerPdfExporter" parent="baseReportExporter">

   <property name="exportParameters" ref="AsposeExportParameters"/>

   <property name="setResponseContentLength" value="true"/>

</bean>

<bean id="AsposePdfExporterConfiguration" class="com.jaspersoft.jasperserver.war.action.ExporterConfigurationBean">

   <property name="descriptionKey" value="Pdf - PDF via Aspose.PDF for JasperReports"/>
```


<property name="iconSrc" value="/images/pdf.gif"/>

<property name="parameterDialogName" value="dlg"/>

<property name="exportParameters" ref="AsposeExportParameters"/>

<property name="currentExporter" ref="AsposePdfExporter"/>

</bean>
```

{{% alert color="primary" %}}

2. Temukan elemen <util:map id=”exporterConfigMap> di file **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** dan tambahkan baris berikut:

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

3. Salin semua gambar GIF dari folder \lib dalam **Aspose-pdf-jasperreports.zip** ke <InstallDir>\apache-tomcat\webapps\jasperserver\images\.

4. Salin **Aspose-pdf-jasperreports.jar** dari folder \lib dalam **Aspose.PDF.JasperReports.zip** ke <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.

5. Tambahkan baris berikut ke file **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.



   Bean ini mungkin mengandung berbagai pengaturan konfigurasi yang dimaksudkan untuk mengonfigurasi ekspor. Misalnya, Anda dapat menggunakan fitur pemetaan font JasperReports atau menentukan lokasi file lisensi Aspose.Cells for JasperReports.



```

<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

<property name="localizedFontMap" ref="localePdfFontMap"/>



<!-- Hapus komentar untuk menerapkan lisensi. Periksa jalur lisensi.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/


jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>

```
{{% alert color="primary" %}}
```

6. Jalankan JasperServer dan buka laporan apa pun untuk melihat. Jika langkah-langkah sebelumnya dilakukan dengan benar, Anda akan melihat ikon untuk ekspor melalui Aspose.PDF untuk JasperReports dalam daftar format yang tersedia.

   **Aspose.PDF untuk JasperReports terintegrasi**

![todo:image_alt_text](integration-with-jasperserver_1.png)

{{% /alert %}}