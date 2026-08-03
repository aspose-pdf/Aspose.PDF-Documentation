---
title: Justify FullJustify Perataan Teks
linktitle: Justify FullJustify Text Alignment
type: docs
weight: 40
url: /reportingservices/justify-fulljustify-text-alignment/
description: Raih perataan teks sempurna dalam laporan PDF dengan Aspose.PDF untuk Layanan Pelaporan. Dukungan untuk opsi pembenaran dan pembenaran penuh.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Pembuat laporan tidak mendukung kemampuan untuk menentukan perataan teks untuk kotak teks `Justify` Dan `FullJustify`. Dengan Aspose.PDF untuk Layanan Pelaporan, Anda dapat melakukannya dengan mudah dengan menambahkan properti khusus.

{{% /alert %}}

```text
Custom Property `Name`: TextAlignment  
Custom Property `Type`: String  
Custom Property `Values`: Justify, FullJustify  
```

Dalam laporan, kodenya harus seperti berikut:

## Contoh

```xml
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
```
