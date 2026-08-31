---
title: Работа с JasperReports
linktitle: Работа с JasperReports
type: docs
weight: 10
url: /ru/jasperreports/working-with-jasperreports/
description: Освойте работу с JasperReports с использованием Aspose.PDF. Создавайте и экспортируйте подробные отчеты в формате PDF с расширенными функциями.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports доступен для бесплатного ознакомления без ограничения по времени со страницы загрузки. Оценочная и лицензионная версии продукта загружаются одинаково.

Если вас устраивает ознакомительная версия, [купите лицензию](https://purchase.aspose.com/buy?ppId=98899). Убедитесь, что вы понимаете и согласны с условиями лицензии.

{{% /alert %}}

Лицензия доступна для скачивания на странице заказа после оплаты заказа. Лицензия представляет собой XML-файл в виде открытого текста с цифровой подписью. Лицензия содержит такую ​​информацию, как имя клиента, приобретенный продукт и тип лицензии. Не изменяйте содержимое файла лицензии: это сделает лицензию недействительной.

Активировать лицензию можно несколькими способами:

- [Вызов setLicense](/pdf/ru/jasperreports/working-with-jasperreports/#call-setlicense).
- [Установите параметр экспортера в коде](/pdf/ru/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [Установите параметр экспортера в **applicationContext.xml**](/pdf/ru/jasperreports/working-with-jasperserver/).

Первые два используются с JasperReports, последний — с JasperServer.

## Вызовите `setLicense`

Этот метод используется с JasperReports.

1. Загрузите лицензию на свой компьютер и скопируйте ее в соответствующую папку (например, в папку вашего приложения или JasperReports\lib).
2. Добавьте в свой проект следующий код:

```java
import com.Aspose.PDF.jr3_7_0.jasperreports.*;
try
{ 
    // create a stream object containing the license file
   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // Set the license through the stream object
 
   License license = new License();
   license.setLicense(fstream);
}
catch(Exception ex)
{
   System.out.println(ex.toString());
}

```

## Задайте параметр `LicenseFile Exporter` в коде

Этот метод используется с JasperReports.

1. Загрузите лицензию на свой компьютер и скопируйте ее в соответствующую папку (например, в папку вашего приложения или JasperReports\lib).
2. Добавьте в свой проект следующий код:

```java

import com.Aspose.PDF.jr3_7_0.jasperreports.*;

com.Aspose.PDF.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.Aspose.PDF.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```

