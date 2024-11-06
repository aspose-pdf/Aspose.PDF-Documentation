---
title: PHP via COM Interop
type: docs
weight: 50
url: fr/net/php-via-com-interop/
---

## Prérequis

{{% alert color="primary" %}}
Configurez votre PHP pour fonctionner avec COM. Voir <http://www.php.net/manual/en/ref.com.php>. Pour plus d'informations, veuillez consulter l'article intitulé [Utiliser Aspose.pdf pour .NET via COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)

{{% /alert %}}

## Exemple Hello World!

{{% alert color="primary" %}}
Ceci est une application simple qui vous montre comment créer un nouveau fichier PDF et ajouter du texte au fichier PDF en utilisant [Aspose.PDF pour .NET](/pdf/net/) dans PHP via COM Interop.

{{% /alert %}}

```php
<?php
echo "<h2>Appeler Aspose.PDF pour .NET depuis PHP en utilisant l'interopérabilité COM</h2>";
echo "<h3>Conversion de PDF en Excel</h3>";

//définir la licence
$lic = new COM("Aspose.PDF.License");
$lic->SetLicense("C:/temp/Aspose.Total.lic");

//Charger le document PDF
$input="C:/temp/HelloWorld.pdf";
$helper = new COM("Aspose.PDF.ComHelper");

$pdf = $helper->OpenFile($input);

// Enregistrer le document PDF dans le format de fichier souhaité en passant la valeur enum SaveFormat pour le format dans ce cas nous passons 9 pour excel.

$output = "C:/temp/test_php.xls";
$pdf->Save_4($output,9);
?>
```

