---
title: PHP via COM Interop
type: docs
weight: 50
url: /net/php-via-com-interop/
---

## المتطلبات الأساسية

{{% alert color="primary" %}}
قم بتهيئة PHP الخاص بك للعمل مع COM. انظر <http://www.php.net/manual/en/ref.com.php>. لمزيد من المعلومات، يرجى مراجعة المقال بعنوان [استخدام Aspose.pdf لـ .NET عبر COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## مثال على برنامج Hello World!

{{% alert color="primary" %}}
هذا تطبيق بسيط يوضح كيفية إنشاء ملف PDF جديد وإضافة نص إلى ملف PDF باستخدام [Aspose.PDF لـ .NET](/pdf/net/) في PHP عبر COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>Calling Aspose.PDF for .NET from PHP using COM Interoperatibility</h2>";
echo "<h3>PDF to Excel Conversion</h3>";

//set license
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//Load Pdf Document
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// Save the PDF document  to desired file format by passing  SaveFormat enum value for the format in this case we pass 9 for excel.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

