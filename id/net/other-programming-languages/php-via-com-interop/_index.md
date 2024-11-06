---
title: PHP via COM Interop
type: docs
weight: 50
url: id/net/php-via-com-interop/
---

## Prasyarat

{{% alert color="primary" %}}
Konfigurasikan PHP Anda untuk bekerja dengan COM. Lihat <http://www.php.net/manual/en/ref.com.php>. Untuk informasi lebih lanjut, silakan periksa artikel yang bernama [Menggunakan Aspose.pdf untuk .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## Contoh Hello World!

{{% alert color="primary" %}}
Ini adalah aplikasi sederhana yang menunjukkan cara membuat file PDF baru dan menambahkan teks ke file PDF menggunakan [Aspose.PDF for .NET](/pdf/net/) di PHP melalui COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>Memanggil Aspose.PDF untuk .NET dari PHP menggunakan Interoperabilitas COM</h2>";
echo "<h3>Konversi PDF ke Excel</h3>";

//setel lisensi
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//Muat Dokumen Pdf
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// Simpan dokumen PDF ke format file yang diinginkan dengan melewati nilai enum SaveFormat untuk format dalam hal ini kita lewatkan 9 untuk excel.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

