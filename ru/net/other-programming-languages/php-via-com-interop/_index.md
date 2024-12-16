---
title: PHP через COM Interop
type: docs
weight: 50
url: /ru/net/php-via-com-interop/
---

## Предварительные требования

{{% alert color="primary" %}}
Настройте ваш PHP для работы с COM. Смотрите <http://www.php.net/manual/en/ref.com.php>. Для получения дополнительной информации, пожалуйста, ознакомьтесь со статьей [Использование Aspose.pdf для .NET через COM Interop](/pdf/ru/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## Пример "Hello World!"

{{% alert color="primary" %}}
Это простое приложение, которое показывает, как создать новый PDF файл и добавить текст в PDF файл с помощью [Aspose.PDF для .NET](/pdf/ru/net/) в PHP через COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>Вызов Aspose.PDF для .NET из PHP с использованием COM Interoperatibility</h2>";
echo "<h3>Конвертация PDF в Excel</h3>";

//установка лицензии
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//Загрузка документа PDF
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// Сохранение документа PDF в желаемом формате файла, передав значение перечисления SaveFormat для формата, в этом случае мы передаем 9 для excel.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

