---

title: Работа с JasperReports

type: docs

weight: 10

url: ru/jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---



{{% alert color="primary" %}}



Aspose.Words для JasperReports доступен бесплатно для неограниченной по времени оценки с страницы загрузки. Оценочная и лицензированная версии продукта являются одной и той же загрузкой.



Когда вы будете довольны оценочной версией, [приобретите лицензию](http://www.aspose.com/purchase/default.aspx). Убедитесь, что вы понимаете и соглашаетесь с условиями лицензии.



{{% /alert %}}





Лицензия доступна для загрузки со страницы заказа после оплаты. Лицензия представляет собой текстовый XML файл с цифровой подписью. Лицензия содержит информацию, такую как имя клиента, приобретенный продукт и тип лицензии. Не изменяйте содержание файла лицензии: это аннулирует лицензию.



Есть несколько способов активировать лицензию:



- [Вызвать setLicense](/pdf/jasperreports/working-with-jasperreports/#call-setlicense).


- [Установить параметр экспортера в коде](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).

- [Установите параметр экспортера в **applicationContext.xml**](/pdf/jasperreports/working-with-jasperserver/).



Первые два используются с JasperReports, последний с JasperServer.

#### **Вызовите setLicense**

<ins> **Этот метод используется с JasperReports.**



1. Загрузите лицензию на свой компьютер и скопируйте ее в соответствующую папку (например, в папку вашего приложения или JasperReports\lib).

2. Добавьте следующий код в ваш проект:



```

import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // создайте объект потока, содержащий файл лицензии

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  



    // Установите лицензию через объект потока

 

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}



```



#### **Установите параметр экспортера licenseFile в коде**



<ins> **Этот метод используется с JasperReports.**



1. Скачайте лицензию на ваш компьютер и скопируйте ее в соответствующую папку (например, папку вашего приложения или JasperReports\lib).

2. Добавьте следующий код в ваш проект:

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");

exporter.exportReport();
```