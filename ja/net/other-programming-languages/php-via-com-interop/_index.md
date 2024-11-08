---
title: PHP via COM Interop
type: docs
weight: 50
url: /ja/net/php-via-com-interop/
---

## 前提条件

{{% alert color="primary" %}}
COMを使用して動作するようにPHPを設定してください。詳細については、<http://www.php.net/manual/en/ref.com.php>を参照してください。さらに情報が必要な場合は、[Use Aspose.pdf for .NET via COM Interop](/pdf/ja/net/use-aspose-pdf-for-net-via-com-interop/)という記事をご覧ください。

{{% /alert %}}

## Hello World! 例

{{% alert color="primary" %}}
これは、[Aspose.PDF for .NET](/pdf/ja/net/)をPHP経由でCOM Interopを使用して新しいPDFファイルを作成し、PDFファイルにテキストを追加する方法を示すシンプルなアプリケーションです。

{{% /alert %}}

```php
<?php
echo "<h2>PHPからCOM相互運用を使用してAspose.PDF for .NETを呼び出す</h2>";
echo "<h3>PDFからExcelへの変換</h3>";

//ライセンス設定
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//PDFドキュメントをロード
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// SaveFormat列挙値を使って望むファイル形式でPDFドキュメントを保存します。この場合、Excelのために9を渡します。

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

