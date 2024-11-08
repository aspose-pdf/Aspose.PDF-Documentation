---
title: Apa perbedaan antara format FDF, XML, dan XFDF
type: docs
weight: 30
url: /id/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Bagian ini membahas perbedaan antara formulir XML, FDF, dan XFDF dengan Aspose.PDF Facades menggunakan Kelas Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Kami mencampurkan banyak istilah berbeda seperti FDF, XML, dan XFDF. Semua istilah ini terkait satu sama lain. Artikel ini mengeksplorasi konsep-konsep ini dan hubungan mereka satu sama lain.

{{% /alert %}}

## Mengungkap Formulir

Aspose.PDF untuk .NET digunakan untuk memanipulasi dokumen PDF yang distandarisasi oleh Adobe. Dan dokumen PDF berisi formulir interaktif yang disebut AcroForms. Formulir interaktif ini memiliki sejumlah bidang formulir, seperti kombo, kotak teks, dan tombol radio. Formulir interaktif Adobe, dan bidang formulir, bekerja dengan cara yang sama seperti formulir HTML dan bidang formulirnya.

Dimungkinkan untuk menyimpan nilai-nilai bidang formulir dalam file terpisah: file FDF (Format Data Formulir). Ini berisi nilai-nilai dari bidang formulir dalam bentuk pasangan kunci/nilai. File FDF masih digunakan untuk tujuan ini. Namun Adobe juga menyediakan jenis FDF yang dikodekan XML yang disebut XFDF. File XFDF menyimpan nilai-nilai dari bidang formulir secara hierarkis menggunakan tag XML.

Dengan Aspose.PDF pengembang tidak hanya dapat mengekspor nilai-nilai dari bidang formulir PDF ke dalam file FDF atau XFDF tetapi juga ke dalam file XML. Semua file ini menggunakan sintaks yang berbeda untuk menyimpan nilai bidang formulir PDF. Contoh di bawah ini menjelaskan perbedaannya.

Mari kita anggap bahwa ada beberapa bidang formulir PDF yang nilainya perlu disajikan dalam bentuk FDF, XML, dan XFDF. Bidang formulir yang diasumsikan ini dengan nama dan nilainya ditunjukkan di bawah ini:

|**Nama Bidang**|**Nilai Bidang**|
| :- | :- |
|Company|Aspose.com|
|Address.1|Sydney, Australia|
|Address.2|Baris Alamat Tambahan|
Mari kita lihat bagaimana mewakili nilai-nilai ini dalam format FDF, XML dan XFDF.

### Apa itu format FDF?

Seperti yang kita ketahui bahwa file FDF menyimpan data dalam bentuk Pasangan Kunci di mana /T mewakili Kunci, /V mewakili Nilai dan data dalam tanda kurung () mewakili konten dari Kunci atau Nilai. Untuk contoh, /T(Company) berarti Company adalah kunci bidang dan /V(Aspose.com) dimaksudkan untuk nilai bidang.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### Apa itu format XML? 

Pengembang dapat merepresentasikan setiap bidang formulir PDF dalam bentuk tag bidang, `<field>`. Setiap tag bidang memiliki atribut, nama yang menunjukkan nama bidang dan sub tag, `<value>` yang merepresentasikan nilai bidang seperti yang ditunjukkan di bawah ini:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### ### Apa itu format XFDF?  

Representasi data di atas dalam bentuk XFDF mirip dengan bentuk XML kecuali dengan beberapa perbedaan. Dalam file XFDF, kami menambahkan XML Namespace mereka, yaitu <http://ns.adpbe.com/xfdf/> dan ada tag tambahan, `<f>` yang digunakan untuk menunjuk ke dokumen PDF yang berisi bidang formulir PDF tersebut. Seperti XML, XFDF juga berisi bidang dalam bentuk tag bidang, `<field>` seperti yang ditunjukkan di bawah ini:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### Mengidentifikasi nama bidang formulir

Aspose.PDF untuk .NET menyediakan kemampuan untuk membuat, mengedit, dan mengisi formulir PDF yang sudah dibuat. Itu mengandung kelas [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), yang memiliki fungsi bernama [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index), dan ini mengambil dua parameter yaitu nama Field yang perlu diisi, dan nilai field. Jadi untuk mengisi field formulir, Anda harus mengetahui nama field formulir yang tepat. Kami sering menghadapi skenario di mana kami perlu mengisi formulir yang dibuat dalam beberapa alat yaitu. Adobe Designer, dan kami tidak yakin tentang nama-nama bidang formulir. Untuk memenuhi kebutuhan kami, kami perlu membaca nama-nama semua bidang formulir PDF. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) kelas menyediakan properti bernama [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) yang mengembalikan semua nama bidang dan mengembalikan null jika PDF tidak memiliki bidang. Tetapi properti ini akan mengembalikan semua nama bidang formulir PDF dan kami tidak akan yakin, nama mana yang sesuai dengan bidang mana di atas formulir.

Sebagai solusi untuk masalah ini, kami memerlukan atribut tampilan dari setiap bidang. Kelas [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) memiliki fungsi bernama GetFieldFacade yang mengembalikan atribut, termasuk lokasi, warna, gaya batas, font, item daftar, dan sebagainya. Untuk menyimpan nilai-nilai ini, kita akan menggunakan kelas [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), yang digunakan untuk merekam atribut visual dari bidang. Setelah kita memiliki atribut-atribut ini, kita dapat menambahkan bidang teks di bawah setiap bidang yang akan menampilkan nama bidang tersebut. Di sini muncul pertanyaan bagaimana kita akan menentukan lokasi di mana menambahkan bidang teks? Solusi untuk masalah ini adalah properti Box dalam kelas [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade), yang menyimpan lokasi bidang. Kita akan menyimpan nilai-nilai ini ke dalam array tipe persegi panjang dan menggunakan nilai-nilai ini untuk mengidentifikasi posisi di mana menambahkan bidang teks baru. Dalam namespace Aspose.Pdf.Facades, kita memiliki kelas bernama [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) yang menyediakan kemampuan untuk memanipulasi formulir PDF. Buka formulir PDF, tambahkan bidang teks di bawah setiap bidang formulir yang ada, dan simpan formulir PDF dengan nama baru.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}