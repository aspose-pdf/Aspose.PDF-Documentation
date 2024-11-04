---
title: PHP via COM Interop
type: docs
weight: 50
url: /net/php-via-com-interop/
---

## Pré-requisitos

{{% alert color="primary" %}}
Configure seu PHP para trabalhar com COM. Veja <http://www.php.net/manual/en/ref.com.php>. Para mais informações, por favor, consulte o artigo chamado [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## Exemplo Hello World!

{{% alert color="primary" %}}
Esta é uma aplicação simples que mostra como criar um novo arquivo PDF e adicionar texto ao arquivo PDF usando [Aspose.PDF for .NET](/pdf/net/) em PHP via COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>Chamando Aspose.PDF for .NET a partir do PHP usando Interoperabilidade COM</h2>";
echo "<h3>Conversão de PDF para Excel</h3>";

//definir licença
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//Carregar Documento Pdf
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// Salve o documento PDF no formato de arquivo desejado passando o valor enum SaveFormat para o formato, neste caso, passamos 9 para excel.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

