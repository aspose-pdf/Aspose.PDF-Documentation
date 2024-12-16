---
title: Justify FullJustify Text Alignment
type: docs
weight: 40
url: /id/reportingservices/justify-fulljustify-text-alignment/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Pembuat laporan tidak mendukung kemampuan untuk menentukan perataan teks untuk kotak teks “Justify” dan “FullJustify”. Dengan Aspose.Pdf untuk Layanan Pelaporan, Anda dapat melakukannya dengan mudah dengan menambahkan properti kustom.

{{% /alert %}}

{{% alert color="primary" %}}
**Nama Properti Kustom** : TextAlignment  
**Tipe Properti Kustom** : String  
**Nilai Properti Kustom** : Justify, FullJustify  

Dalam laporan, kode harus seperti berikut ini:

**Contoh**

{{< highlight csharp >}}
<Textbox Name="textbox1">
<value> AsposePdf4RS </value>     
  <CustomProperties>
   <CustomProperty>
     <Name>TextAlignment</Name>
     <Value>Justify</Value>
   </CustomProperty>
  </CustomProperties>
</Textbox>
{{< /highlight >}}
{{% /alert %}}