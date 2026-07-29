---
title: Penjajaran Teks Justify FullJustify
linktitle: Penjajaran Teks Justify FullJustify
type: docs
weight: 40
url: /id/reportingservices/justify-fulljustify-text-alignment/
description: Capai penjajaran teks yang sempurna dalam laporan PDF dengan Aspose.PDF for Reporting Services. Mendukung opsi justify dan full justify.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Report builder tidak mendukung kemampuan untuk menentukan penjajaran teks untuk kotak teks “Justify” dan “FullJustify”. Dengan Aspose.PDF for Reporting Services, Anda dapat melakukannya dengan mudah dengan menambahkan properti khusus.

{{% /alert %}}

{{% alert color="primary" %}}
**Nama Properti Kustom** : TextAlignment  
**Tipe Properti Kustom** : String  
**Nilai Properti Kustom** : Justify, FullJustify  

Dalam laporan, kode harus seperti berikut:

**Contoh**

{{< highlight csharp >}}
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>Perataan Teks</Name>
     <Value>Ratakan</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}
