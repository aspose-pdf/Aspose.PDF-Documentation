---
title: Работа с Джасперсервером
linktitle: Работа с Джасперсервером
type: docs
weight: 20
url: /ru/jasperreports/working-with-jasperserver/
description: Узнайте, как эффективно работать с JasperServer с помощью Aspose.PDF. Легко экспортируйте отчеты в профессиональные PDF-файлы.
lastmod: "2021-06-05"
---

## Задайте параметр `LicenseFile Exporter` в `applicationContext.xml`

{{% alert color="primary" %}}

Этот метод используется с JasperServer.

{{% /alert %}}

1. Загрузите лицензию на свой компьютер и скопируйте ее в каталог ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF```, где ```<InstallDir>``` обозначает каталог установки JasperServer.
2. Найдите файл ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` и добавьте следующие строки:

```xml
 <bean id="AsposeExportParameters" class="com.Aspose.PDF.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  
    INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
Примечание. Обратите внимание, что путь установки не должен содержать пробелов, например C:/Program Files/JasperServer…, поскольку это вызывает проблемы при доступе к файлу лицензии.
{{% /alert %}}

## Убедитесь, что лицензия работает

Экспортируйте любой отчет в формат PDF и проверьте, содержит ли отчет оценочное сообщение. Если сообщение об оценке отсутствует, значит, лицензия работает правильно.

Aspose.PDF for JasperReports вставляет водяной знак при работе в ознакомительном режиме.

![Integration with JasperServer_1](working-with-jasperserver_1.png)

Aspose.PDF for JasperReports вставляет водяной знак при работе в ознакомительном режиме.

![Integration with JasperServer_2](working-with-jasperserver_2.png)
