---
title: Menggabungkan Dokumen PDF
type: docs
weight: 10
url: id/java/concatenate-pdf-documents/
description: Bagian ini menjelaskan cara menggabungkan dokumen PDF dengan com.aspose.pdf.facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Menggabungkan File PDF Menggunakan Jalur File (Facades)

metode concatenate dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) dapat digunakan untuk menggabungkan dua file PDF. Metode concatenate memungkinkan Anda untuk memasukkan tiga parameter: PDF input pertama, PDF input kedua, dan PDF output. PDF output akhir berisi kedua file PDF input.

Cuplikan kode berikut menunjukkan kepada Anda cara menggabungkan file PDF menggunakan jalur file.

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // Buat objek PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Gabungkan file
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


Dalam beberapa kasus, ketika terdapat banyak outline, pengguna dapat menonaktifkannya dengan mengatur **CopyOutlines** ke false dan meningkatkan performa dari penggabungan.

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // Buat objek PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Menggabungkan file
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## Menggabungkan beberapa file PDF menggunakan MemoryStreams

[Concatenate]https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) mengambil file PDF sumber dan file PDF tujuan sebagai parameter.
 These parameters can be either paths to the PDF files on the disk or they could be MemoryStreams. Now, for this example, we’ll first create two files streams to read the PDF files from the disk. Then we’ll convert these files into byte arrays. These byte arrays of the PDF files will be converted to MemoryStreams. Once we get the MemoryStreams out of PDF files, we’ll be able to pass them on to the concatenate method and merge into a single output file.

Parameter ini bisa berupa path ke file PDF di disk atau bisa juga berupa MemoryStreams. Sekarang, untuk contoh ini, kita akan membuat dua file stream untuk membaca file PDF dari disk. Kemudian kita akan mengonversi file-file ini menjadi array byte. Array byte dari file PDF ini akan dikonversi menjadi MemoryStreams. Setelah kita mendapatkan MemoryStreams dari file PDF, kita bisa meneruskannya ke metode concatenate dan menggabungkannya menjadi satu file output.

The following code snippet shows you how to concatenate multiple PDF files using MemoryStreams:

Cuplikan kode berikut menunjukkan cara menggabungkan beberapa file PDF menggunakan MemoryStreams:

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // Create two file streams to read pdf files
            // Membuat dua file stream untuk membaca file pdf
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // Create byte arrays to keep the contents of PDF files
            // Membuat array byte untuk menyimpan isi file PDF
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.le)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // Read PDF file contents into byte arrays
            // Membaca isi file PDF ke dalam array byte
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            // Sekarang, pertama-tama ubah array byte menjadi MemoryStreams dan kemudian gabungkan stream tersebut
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        // Membuat instance dari kelas PdfFileEditor untuk menggabungkan stream
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to putput MemoryStream
                        // Gabungkan kedua MemoryStreams input dan simpan ke MemoryStream output
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        // Mengonversi MemoryStream kembali ke array byte
                        byte[] data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        // Membuat FileStream untuk menyimpan file PDF keluaran
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // Write byte array contents in the output file stream
                        // Menulis isi array byte ke dalam file stream keluaran
                        output.Write(data, 0, data.Length);
                        // Close output file
                        // Menutup file keluaran
                        output.Close();
                    }
                }
            }
            // Close input files
            // Menutup file input
            fs1.Close();
            fs2.Close();
        }
```

## Menggabungkan Array File PDF Menggunakan Jalur File (Fasad)

Jika Anda ingin menggabungkan beberapa file PDF, Anda dapat menggunakan overload dari metode concatenate, yang memungkinkan Anda untuk memberikan array jalur file PDF. Output akhir disimpan sebagai file gabungan yang dibuat dari semua file dalam array.

Cuplikan kode berikut menunjukkan kepada Anda cara menggabungkan array file PDF menggunakan jalur file.

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // Buat objek PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Array file
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // Gabungkan file
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## Menggabungkan Array File PDF Menggunakan Stream (Fasad)

Menggabungkan array file PDF tidak terbatas hanya pada file yang berada di disk.
 Anda juga dapat menggabungkan array file PDF dari aliran. Jika Anda ingin menggabungkan beberapa file PDF, Anda dapat menggunakan overload yang sesuai dari metode Concatenate. Pertama, Anda perlu membuat array aliran input dan satu aliran untuk output PDF dan kemudian memanggil metode Concatenate. Hasilnya akan disimpan dalam aliran output.

Cuplikan kode berikut menunjukkan cara menggabungkan array file PDF menggunakan aliran.

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // Buat objek PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Array dari aliran
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // Aliran keluaran
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // Menggabungkan file
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## Menggabungkan Formulir PDF dan menjaga nama bidang tetap unik

Kelas [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) dalam namespace [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) menawarkan kemampuan untuk menggabungkan file PDF.
 Sekarang, jika file Pdf yang akan digabungkan memiliki form field dengan nama field yang serupa, Aspose.PDF menyediakan fitur untuk menjaga field dalam file Pdf hasil sebagai unik dan juga Anda dapat menentukan akhiran untuk membuat nama field menjadi unik. Metode [KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) dari PdfFileEditor sebagai true akan membuat nama field unik ketika form Pdf digabungkan. Selain itu, metode [UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) dari PdfFileEditor dapat digunakan untuk menentukan format yang ditentukan pengguna dari akhiran yang ditambahkan ke nama field agar menjadi unik ketika form digabungkan. String ini harus mengandung substring %NUM% yang akan digantikan dengan angka di file hasil.

Silakan lihat potongan kode sederhana berikut untuk mencapai fungsionalitas ini.

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // Tetapkan jalur file input dan output

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // Instansiasi objek PdfFileEditor
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // Untuk menjaga Id field unik untuk semua field
                KeepFieldsUnique = true,
                // Format akhiran yang ditambahkan ke nama field agar menjadi unik ketika form digabungkan.
                UniqueSuffix = "_%NUM%"
            };

            // Menggabungkan file ke dalam file Pdf hasil
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## Menggabungkan Menyisipkan halaman kosong

Setelah file PDF digabungkan, kita dapat menyisipkan halaman kosong di awal dokumen di mana kita dapat membuat Daftar Isi. Untuk memenuhi persyaratan ini, kita dapat memuat file yang sudah digabungkan ke dalam objek Dokumen dan kita perlu memanggil metode Page.Insert(…) untuk menyisipkan halaman kosong.

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // Buat objek PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // Menggabungkan file
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```