---
title: Apa perbedaan antara format FDF, XML, dan XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: Bagian ini menjelaskan perbedaan antara formulir XML, FDF, dan XFDF dengan menggunakan Aspose.PDF Facades melalui Kelas Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "Temukan perbedaan antara format FDF, XML, dan XFDF dalam manipulasi data formulir PDF melalui Aspose.PDF for .NET. Fitur ini memungkinkan pengembang untuk mengekspor nilai bidang formulir interaktif dalam berbagai format masing-masing dengan sintaksnya sendiri sambil meningkatkan pemahaman dan penggunaan jenis file penting ini dalam pemrosesan PDF. Optimalkan penanganan formulir PDF Anda dengan wawasan mendetail tentang cara merepresentasikan bidang formulir di berbagai format data",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Kami mencampur banyak istilah berbeda seperti FDF, XML, dan XFDF. Semua istilah ini saling terkait dengan cara tertentu. Artikel ini mengeksplorasi konsep-konsep ini dan hubungan mereka satu sama lain.

{{% /alert %}}

## Mengurai Formulir

Aspose.PDF for .NET digunakan untuk memanipulasi dokumen PDF yang distandarisasi oleh Adobe. Dan dokumen PDF mengandung formulir interaktif yang disebut AcroForms. Formulir interaktif ini memiliki sejumlah bidang formulir, seperti combo, kotak teks, dan tombol radio. Formulir interaktif Adobe, dan bidang formulir, bekerja dengan cara yang sama seperti formulir HTML dan bidang formulirnya.

Adalah mungkin untuk menyimpan nilai bidang formulir dalam file terpisah: file FDF (Forms Data Format). Ini berisi nilai bidang formulir dalam format kunci/pasangan. File FDF masih digunakan untuk tujuan ini. Tetapi Adobe juga menyediakan jenis FDF yang dikodekan dalam XML yang disebut XFDF. File XFDF menyimpan nilai bidang formulir dengan cara hierarkis menggunakan tag XML.

Dengan Aspose.PDF, pengembang tidak hanya dapat mengekspor nilai bidang formulir PDF ke file FDF atau XFDF tetapi juga ke file XML. Semua file ini menggunakan sintaks yang berbeda untuk menyimpan nilai bidang formulir PDF. Contoh di bawah ini menjelaskan perbedaannya.

Mari kita anggap ada beberapa bidang formulir PDF yang nilainya perlu disajikan dalam format FDF, XML, dan XFDF. Bidang formulir yang diasumsikan dengan nama dan nilai bidangnya ditunjukkan di bawah ini:

|**Nama Bidang**|**Nilai Bidang**|
| :- | :- |
|Perusahaan|Aspose.com|
|Alamat.1|Sydney, Australia|
|Alamat.2|Baris Alamat Tambahan|
Mari kita lihat bagaimana cara merepresentasikan nilai-nilai ini dalam format FDF, XML, dan XFDF.

### Apa itu format FDF?

Seperti yang kita ketahui bahwa file FDF menyimpan data dalam format Kunci/Pasangan di mana /T mewakili Kunci, /V mewakili Nilai dan data dalam tanda kurung () mewakili konten dari Kunci atau Nilai. Misalnya, /T(Company) berarti Company adalah kunci bidang dan /V(Aspose.com) dimaksudkan untuk nilai bidang.

```
/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)
```

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

### Apa itu format XFDF?  

Representasi data di atas dalam bentuk XFDF mirip dengan bentuk XML kecuali dengan beberapa perbedaan. Dalam file XFDF, kami menambahkan Namespace XML mereka, yaitu <http://ns.adpbe.com/xfdf/> dan ada tag tambahan, `<f>` yang digunakan untuk menunjuk ke dokumen PDF yang berisi bidang formulir PDF ini. Seperti XML, XFDF juga berisi bidang dalam bentuk tag bidang, `<field>` seperti yang ditunjukkan di bawah ini:

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

Aspose.PDF for .NET menyediakan kemampuan untuk membuat, mengedit, dan mengisi formulir PDF yang sudah dibuat. Ini berisi kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form), yang memiliki fungsi bernama [FillField](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/methods/fillfield/index), dan mengambil dua parameter yaitu nama bidang yang perlu diisi, dan nilai bidang. Jadi untuk mengisi bidang formulir, Anda harus mengetahui nama bidang formulir yang tepat.
Kami sering menemui skenario di mana kami perlu mengisi formulir yang dibuat di beberapa alat yaitu Adobe Designer, dan kami tidak yakin tentang nama bidang formulir. Untuk memenuhi kebutuhan kami, kami perlu membaca nama semua bidang formulir PDF. Kelas [Form](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form) menyediakan properti bernama [FieldsNames](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/form/properties/fieldnames) yang mengembalikan semua nama bidang dan mengembalikan null jika PDF tidak memiliki bidang. Tetapi properti ini akan mengembalikan semua nama bidang formulir PDF dan kami tidak akan yakin, nama mana yang sesuai dengan bidang mana di formulir.

Sebagai solusi untuk masalah ini, kami memerlukan atribut penampilan dari setiap bidang. Kelas [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) memiliki fungsi bernama GetFieldFacade yang mengembalikan atribut, termasuk lokasi, warna, gaya batas, font, item daftar, dan seterusnya. Untuk menyimpan nilai-nilai ini, kami akan menggunakan kelas [FormFieldFacade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formfieldfacade) yang digunakan untuk mencatat atribut visual dari bidang. Setelah kami memiliki atribut ini, kami dapat menambahkan bidang teks di bawah setiap bidang yang akan menampilkan nama bidang. Di sini muncul pertanyaan bagaimana kami akan menentukan lokasi di mana menambahkan bidang teks? Solusi untuk masalah ini adalah properti Box dalam kelas [FormFieldFacade](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formfieldfacade) yang menyimpan lokasi bidang. Kami akan menyimpan nilai-nilai ini ke dalam array tipe persegi panjang dan menggunakan nilai-nilai ini untuk mengidentifikasi posisi di mana menambahkan bidang teks baru.
Dalam namespace Aspose.Pdf.Facades, kami memiliki kelas bernama [FormEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/formeditor) yang menyediakan kemampuan untuk memanipulasi formulir PDF. Buka formulir PDF, tambahkan bidang teks di bawah setiap bidang formulir yang ada dan simpan formulir PDF dengan nama baru.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```