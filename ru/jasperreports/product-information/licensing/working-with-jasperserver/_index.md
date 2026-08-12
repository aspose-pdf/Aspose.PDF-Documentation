---
title: Работа с Джасперсервером
linktitle: Работа с Джасперсервером
type: docs
weight: 20
description: Узнайте, как эффективно работать с JasperServer с помощью Aspose.PDF. Легко экспортируйте отчеты в профессиональные PDF-файлы.
lastmod: "2021-06-05"
---

## <ins>Задайте параметр LicenseFile Exporter в applicationContext.xml.

{{% alert color="primary" %}}

Этот метод используется с JasperServer.

{{% /alert %}}

1. Загрузите лицензию на свой компьютер и скопируйте ее в папку ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF```, где ```<InstallDir>``` обозначает каталог установки JasperServer.
2. Найдите файл ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` и добавьте следующие строки:

```xml
 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  
    INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
Примечание. Обратите внимание, что путь установки не должен содержать пробелов, например C:/Program Files/JasperServer…, поскольку это вызывает проблемы при доступе к файлу лицензии.
{{% /alert %}}

## Убедитесь, что лицензия работает

Экспортируйте любой отчет в формат PDF и проверьте, содержит ли отчет оценочное сообщение. Если сообщение об оценке отсутствует, значит, лицензия работает правильно.

Aspose.PDF для JasperReports вставляет водяной знак при работе в ознакомительном режиме.

![Integration with JasperServer_1](working-with-jasperserver_1.png)

Aspose.PDF для JasperReports вставляет водяной знак при работе в ознакомительном режиме.

![Integration with JasperServer_2](working-with-jasperserver_2.png)

