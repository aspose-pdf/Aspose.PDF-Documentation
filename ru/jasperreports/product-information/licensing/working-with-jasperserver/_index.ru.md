---

title: Работа с JasperServer

type: docs

weight: 20

url: /jasperreports/working-with-jasperserver/

lastmod: "2021-06-05"

---



#### <ins>**Установите параметр licenseFile Exporter в applicationContext.xml**

{{% alert color="primary" %}}



Этот метод используется с JasperServer.



{{% /alert %}}



1. Скачайте лицензию на ваш компьютер и скопируйте её в папку ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF```, где ```<InstallDir>``` обозначает директорию установки JasperServer.

2. Найдите файл ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` и добавьте следующие строки:



```

 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  

    INF/Aspose.Total.JasperReports.lic"/>

</bean>

```

{{% alert color="primary" %}}


Примечание: Обратите внимание, что путь установки не должен содержать пробелов, например C:/Program Files/JasperServer… так как это вызывает проблемы при доступе к файлу лицензии.

{{% /alert %}}



#### **Проверьте, что лицензия работает**

Экспортируйте любой отчет в формат PDF и проверьте, содержит ли отчет сообщение об оценке. Если сообщения об оценке нет, значит, лицензия работает правильно.



**Aspose.PDF for JasperReports добавляет водяной знак при работе в режиме оценки**



![todo:image_alt_text](working-with-jasperserver_1.png)







**Aspose.PDF for JasperReports добавляет водяной знак при работе в режиме оценки**



![todo:image_alt_text](working-with-jasperserver_2.png)