---

title: Bekerja dengan JasperServer

type: docs

weight: 20

url: id/jasperreports/working-with-jasperserver/

lastmod: "2021-06-05"

---



#### <ins>**Mengatur Parameter Exporter licenseFile di applicationContext.xml**

{{% alert color="primary" %}}



Metode ini digunakan dengan JasperServer.



{{% /alert %}}



1. Unduh lisensi ke komputer Anda dan salin ke folder ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF```, di mana ```<InstallDir>``` adalah direktori instalasi JasperServer.

2. Temukan file ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` dan tambahkan baris berikut:



```

 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  

    INF/Aspose.Total.JasperReports.lic"/>

</bean>

```

{{% alert color="primary" %}}


Catatan: Harap dicatat bahwa jalur instalasi tidak boleh mengandung spasi, misalnya C:/Program Files/JasperServer… karena itu menyebabkan masalah ketika mengakses file lisensi.

{{% /alert %}}



#### **Verifikasi bahwa Lisensi Berfungsi**

Ekspor laporan apapun ke format PDF dan periksa apakah laporan tersebut mengandung pesan evaluasi. Jika tidak ada pesan evaluasi, maka lisensi berfungsi dengan baik.



**Aspose.PDF untuk JasperReports menyisipkan watermark saat bekerja dalam mode evaluasi**



![todo:image_alt_text](working-with-jasperserver_1.png)







**Aspose.PDF untuk JasperReports menyisipkan watermark saat bekerja dalam mode evaluasi**



![todo:image_alt_text](working-with-jasperserver_2.png)