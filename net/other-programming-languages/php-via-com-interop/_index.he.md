---
title: PHP דרך COM Interop
type: docs
weight: 50
url: /net/php-via-com-interop/
---

## דרישות מוקדמות

{{% alert color="primary" %}}
הגדר את ה-PHP שלך לעבוד עם COM. ראה <http://www.php.net/manual/en/ref.com.php>. למידע נוסף, אנא בדוק את המאמר בשם [שימוש ב-Aspose.pdf ל-.NET דרך COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## דוגמת Hello World!

{{% alert color="primary" %}}
זו יישום פשוט שמראה לך איך ליצור קובץ PDF חדש ולהוסיף טקסט לקובץ ה-PDF באמצעות [Aspose.PDF ל-.NET](/pdf/net/) ב-PHP דרך COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>קריאה ל-Aspose.PDF ל-.NET מ-PHP באמצעות יכולת תאימות COM</h2>";
echo "<h3>המרת PDF ל-Excel</h3>";

//set license
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//טען מסמך PDF
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// שמור את מסמך ה-PDF לפורמט הקובץ הרצוי על ידי העברת ערך enum של SaveFormat לפורמט, במקרה זה אנו מעבירים 9 ל-Excel.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

