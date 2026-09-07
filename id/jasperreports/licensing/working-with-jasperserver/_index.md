---
title: Working with JasperServer
linktitle: Bekerja dengan JasperServer
type: docs
weight: 20
description: Jelajahi cara bekerja secara efisien dengan JasperServer menggunakan Aspose.PDF. Ekspor laporan ke PDF profesional dengan mudah.
lastmod: "2026-08-31"
---

## <ins>Tetapkan Parameter Pengekspor LicenseFile di applicationContext.xml

{{% alert color="primary" %}}

This method is used with JasperServer.

{{% /alert %}}

1. Unduh lisensi ke komputer Anda dan salin ke ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` folder, where  ```<InstallDir>``` singkatan dari direktori instalasi JasperServer.
2. Temukan file ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` dan tambahkan baris berikut:

```xml
 <bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
Catatan: Harap diperhatikan bahwa jalur instalasi tidak boleh mengandung spasi apa pun, misalnya C:/Program Files/JasperServer… karena dapat menyebabkan masalah saat mengakses file lisensi.
{{% /alert %}}

## Verifikasi bahwa Lisensi Berfungsi

Ekspor laporan apa pun ke format PDF dan periksa apakah laporan tersebut berisi pesan evaluasi. Jika tidak ada pesan evaluasi, maka lisensi berfungsi dengan baik.

Aspose.PDF for JasperReports memasukkan tanda air saat bekerja dalam mode evaluasi

![Integration with JasperServer_1](working-with-jasperserver_1.png)

Aspose.PDF for JasperReports memasukkan tanda air saat bekerja dalam mode evaluasi

![Integration with JasperServer_2](working-with-jasperserver_2.png)

