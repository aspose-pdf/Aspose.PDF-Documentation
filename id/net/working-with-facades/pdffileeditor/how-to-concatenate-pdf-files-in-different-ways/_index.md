---
title: Menggabungkan file PDF menggunakan .NET 5 
linktitle: Cara menggabungkan PDF
type: docs
weight: 75
url: /id/net/how-to-concatenate-pdf-files-in-different-ways/
description: Artikel ini menjelaskan cara-cara untuk menggabungkan sejumlah file PDF yang ada menjadi satu file PDF tunggal.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Artikel ini menjelaskan bagaimana Anda dapat [Menggabungkan](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) beberapa Dokumen PDF menjadi satu Dokumen PDF dengan bantuan Komponen [Aspose.PDF for .NET](/pdf/id/net/). [Aspose.PDF for .NET](/pdf/id/net/) membuat pekerjaan ini menjadi sangat mudah.

{{% /alert %}}

Yang perlu Anda lakukan adalah memanggil metode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) dan semua file PDF input Anda akan digabungkan bersama dan satu file PDF tunggal akan dihasilkan. Mari kita buat aplikasi untuk berlatih menggabungkan file PDF. Kita akan membuat aplikasi menggunakan Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF untuk .NET dapat digunakan dalam jenis aplikasi apa pun yang berjalan di .NET Framework baik itu aplikasi web ASP.NET atau aplikasi Windows

{{% /alert %}}

## Cara Menggabungkan File PDF dengan Berbagai Cara

Dalam formulir, terdapat tiga Kotak Teks (textBox1, textBox2, textBox3) yang memiliki Label Tautan masing-masing (linkLabel1, linkLabel2, linkLabel3) untuk menjelajahi file PDF. Dengan mengklik Label Tautan "Browse", sebuah Dialog File Input (inputFileDialog1) akan muncul yang memungkinkan kita untuk memilih file PDF (yang akan digabungkan).

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

Tampilan aplikasi form windows ditunjukkan untuk demonstrasi kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) untuk Penggabungan File PDF.
![Concatenate PDF Files](how-to-concatenate-pdf-files-in-different-ways_1.png)

Setelah kita memilih file PDF dan mengklik tombol OK. Nama file lengkap dengan jalur ditugaskan ke Kotak Teks terkait.

![Choose the PDF file](how-to-concatenate-pdf-files-in-different-ways_2.png)

Demikian pula, kita dapat memilih dua atau tiga File PDF Masukan untuk digabungkan seperti yang ditunjukkan di bawah ini:

![Choose two or three Input PDF Files](how-to-concatenate-pdf-files-in-different-ways_3.png)

Kotak Teks terakhir (textBox4) akan mengambil Jalur Tujuan dari file PDF keluaran dengan namanya di mana file keluaran ini akan dibuat.

![Destination Path of the Output PDF file](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate method](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Concatenate() Method

Metode Concatenate() dapat digunakan dalam tiga cara. mari kita lihat lebih dekat masing-masing:

### Pendekatan 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Pendekatan ini bagus hanya jika Anda perlu menggabungkan hanya dua file PDF. Dua argumen pertama (firstInputFile dan secInputFile) memberikan nama file lengkap beserta jalur penyimpanan dari dua file PDF input yang akan digabungkan. Argumen ketiga (outputFile) memberikan nama file yang diinginkan beserta jalur dari file PDF keluaran.

![Gabungkan dua PDF menggunakan Nama File](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Pendekatan 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

Mirip dengan pendekatan di atas, pendekatan ini juga memungkinkan penggabungan dua file PDF. Dua argumen pertama (firstInputStream dan secInputStream) menyediakan dua file PDF input sebagai Stream (stream adalah array bit/byte) yang akan digabungkan. Argumen ketiga (outputStream) menyediakan representasi stream dari file PDF output yang diinginkan.

![Menggabungkan dua PDF menggunakan File Stream](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdf1,pdf2,outputPDF);
  outputPDF.Close();
}
```

### Pendekatan 3

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

Jika Anda ingin menggabungkan lebih dari dua file PDF maka pendekatan ini akan menjadi pilihan utama Anda. First argument (inputStreams[]) menyediakan file PDF input dalam bentuk Array of Streams yang akan digabungkan. Argument kedua (outputStream) menyediakan representasi stream dari file PDF keluaran yang diinginkan.

![Menggabungkan beberapa PDF menggunakan Array of Streams](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream pdf3 = new FileStream(textBox3.Text,FileMode.Open);
  Stream[] pdfStreams = new Stream[]{pdf1,pdf2,pdf3};
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdfStreams,outputPDF);
  outputPDF.Close();
}
```