---
title: PHP via COM Interop
type: docs
weight: 50
url: es/net/php-via-com-interop/
---

## Prerrequisitos

{{% alert color="primary" %}}
Configura tu PHP para trabajar con COM. Consulta <http://www.php.net/manual/en/ref.com.php>. Para más información, por favor revisa el artículo titulado [Use Aspose.pdf for .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## Ejemplo de ¡Hola Mundo!

{{% alert color="primary" %}}
Esta es una aplicación simple que muestra cómo crear un nuevo archivo PDF y agregar texto al archivo PDF usando [Aspose.PDF for .NET](/pdf/net/) en PHP a través de COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>Llamando a Aspose.PDF for .NET desde PHP usando Interoperabilidad COM</h2>";
echo "<h3>Conversión de PDF a Excel</h3>";

//establecer licencia
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//Cargar documento PDF
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// Guardar el documento PDF en el formato de archivo deseado pasando el valor enum de SaveFormat para el formato en este caso pasamos 9 para excel.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

