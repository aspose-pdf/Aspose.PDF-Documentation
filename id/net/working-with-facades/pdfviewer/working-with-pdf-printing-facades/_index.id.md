---
title: Bekerja dengan Pencetakan PDF - Facades
type: docs
weight: 10
url: /net/working-with-pdf-printing-facades/
description: Bagian ini menjelaskan cara mencetak file PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Mencetak File PDF ke Printer Default menggunakan Pengaturan Printer dan Halaman

Pertama, dokumen dikonversi menjadi gambar dan kemudian dicetak pada printer. Kami membuat instance dari kelas [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) yang memungkinkan Anda mencetak file PDF ke printer default, menggunakan metode BindPdf untuk dokumen tersebut, dan membuat pengaturan tertentu. Dalam contoh kami, kami menggunakan format A4, orientasi potret. Dalam printerSettings, pertama-tama, kami menunjukkan nama printer yang akan kami gunakan untuk mencetak. Atau jika tidak, akan mencetak ke printer default. Selanjutnya, tentukan jumlah salinan yang kami butuhkan.

```csharp
 public static void PrintingPDFFile()
        {
            // Buat objek PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Buka file PDF input
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Tetapkan atribut untuk pencetakan
            viewer.AutoResize = true;         // Cetak file dengan ukuran yang disesuaikan
            viewer.AutoRotate = true;         // Cetak file dengan rotasi yang disesuaikan
            viewer.PrintPageDialog = false;   // Jangan tampilkan dialog nomor halaman saat mencetak

            // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // Tetapkan nama printer
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // Tetapkan Ukuran Halaman (jika diperlukan)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Tetapkan Margin Halaman (jika diperlukan)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Cetak dokumen menggunakan pengaturan printer dan halaman
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Tutup file PDF setelah mencetak
            viewer.Close();
        }
```

Untuk menampilkan dialog cetak, coba gunakan potongan kode berikut:

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // Membuat objek PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Buka file PDF input
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Tetapkan atribut untuk pencetakan
            viewer.AutoResize = true;         // Cetak file dengan ukuran yang disesuaikan
            viewer.AutoRotate = true;         // Cetak file dengan rotasi yang disesuaikan

            // Membuat objek untuk pengaturan printer dan halaman serta PrintDocument

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // Tetapkan UkuranHalaman (jika diperlukan)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // Tetapkan MarginHalaman (jika diperlukan)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // Kode pencetakan dokumen ada di sini
                // Cetak dokumen menggunakan pengaturan printer dan halaman
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // Tutup file PDF setelah pencetakan
            viewer.Close();
        }
```

## Cetak PDF ke Printer Lunak

Ada printer yang mencetak ke file. Kami mengatur nama printer virtual, dan, dengan analogi dengan contoh sebelumnya, kami membuat pengaturan.

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // Buat objek PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Buka file PDF input
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Atur atribut untuk mencetak
            viewer.AutoResize = true;         // Cetak file dengan ukuran yang disesuaikan
            viewer.AutoRotate = true;         // Cetak file dengan rotasi yang disesuaikan
            viewer.PrintPageDialog = false;   // Tidak menampilkan dialog nomor halaman saat mencetak

            viewer.PrintAsImage = false;

            // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Atur nama printer
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Atau atur printer PDF
            //ps.PrinterName = "Adobe PDF";

            // Atur UkuranHalaman (jika diperlukan)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Atur MarginHalaman (jika diperlukan)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Cetak dokumen menggunakan pengaturan printer dan halaman
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Tutup file PDF setelah mencetak
            viewer.Close();
        }
```

## Menyembunyikan Dialog Cetak

Aspose.PDF untuk .NET memungkinkan Anda untuk menyembunyikan dialog cetak. Untuk ini gunakan metode [PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog).

Cuplikan kode berikut menunjukkan cara menyembunyikan dialog cetak.

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // Buat objek PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Buka file PDF input
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Setel atribut untuk pencetakan
            viewer.AutoResize = true;         // Cetak file dengan ukuran yang disesuaikan
            viewer.AutoRotate = true;         // Cetak file dengan rotasi yang disesuaikan

            viewer.PrintPageDialog = false;   // Jangan tampilkan dialog nomor halaman saat mencetak

            // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Setel nama printer XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // Setel UkuranHalaman (jika diperlukan)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Setel MarginHalaman (jika diperlukan)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Cetak dokumen menggunakan pengaturan printer dan halaman
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Tutup file PDF setelah mencetak
            viewer.Close();
        }
```

## Mencetak PDF Berwarna ke File XPS sebagai Grayscale

Dokumen PDF berwarna dapat dicetak ke printer XPS sebagai grayscale, menggunakan [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Untuk mencapai hal tersebut, Anda perlu menggunakan properti PdfViewer.PrintAsGrayscale dan mengaturnya ke *true*. Cuplikan kode berikut menunjukkan implementasi dari Properti PdfViewer.PrintAsGrayscale.

```csharp
public static void PrintingPDFasGrayscale()
        {
            // Buat objek PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Buka file PDF input
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Atur atribut untuk pencetakan
            viewer.AutoResize = true;         // Cetak file dengan ukuran yang disesuaikan
            viewer.AutoRotate = true;         // Cetak file dengan rotasi yang disesuaikan

            viewer.PrintPageDialog = false;   // Jangan tampilkan dialog nomor halaman saat mencetak
            viewer.PrintAsGrayscale = false;

            // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Atur nama printer XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // Atur UkuranHalaman (jika diperlukan)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Atur MarginHalaman (jika diperlukan)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Cetak dokumen menggunakan pengaturan printer dan halaman
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Tutup file PDF setelah mencetak
            viewer.Close();
        }
```

## Konversi PDF ke PostScript

Kelas [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) menyediakan kemampuan untuk mencetak dokumen PDF dan dengan bantuan kelas ini, kita juga dapat mengonversi file PDF ke format PostScript. Untuk mengonversi file PDF ke PostScript, pertama-tama instal printer PS apa pun dan cukup cetak ke file dengan bantuan PdfViewer.

Cuplikan kode berikut menunjukkan cara mencetak dan mengonversi PDF ke format PostScript.

```csharp
public static void PrintingPDFToPostScript()
        {
            // Buat objek PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Buka file PDF input
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Tetapkan atribut untuk pencetakan
            viewer.AutoResize = true;         // Cetak file dengan ukuran yang disesuaikan
            viewer.AutoRotate = true;         // Cetak file dengan rotasi yang disesuaikan
            viewer.PrintPageDialog = false;   // Jangan tampilkan dialog nomor halaman saat mencetak

            viewer.PrintAsImage = false;

            // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Tetapkan nama printer XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Tetapkan nama file output dan atribut PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Tetapkan PageSize (jika diperlukan)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Tetapkan PageMargins (jika diperlukan)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Cetak dokumen menggunakan pengaturan printer dan halaman
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Tutup file PDF setelah mencetak
            viewer.Close();
        }
```

## Memeriksa Status Pekerjaan Cetak

File PDF dapat dicetak ke printer fisik maupun ke Microsoft XPS Document Writer, tanpa menampilkan dialog cetak, menggunakan kelas [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Ketika mencetak file PDF besar, prosesnya mungkin memakan waktu lama sehingga pengguna mungkin tidak yakin apakah proses pencetakan selesai atau mengalami masalah. Untuk mengetahui status pekerjaan cetak, gunakan properti PrintStatus. Kode berikut menunjukkan cara mencetak file PDF ke file XPS dan mendapatkan status pencetakan.

```csharp
public static void CheckingPrintJobStatus()
        {
            // Buat objek PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Buka file PDF masukan
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // Atur atribut untuk pencetakan
            viewer.AutoResize = true;         // Cetak file dengan ukuran yang disesuaikan
            viewer.AutoRotate = true;         // Cetak file dengan rotasi yang disesuaikan
            viewer.PrintPageDialog = false;   // Jangan tampilkan dialog nomor halaman saat mencetak

            viewer.PrintAsImage = false;

            // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Atur nama printer XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Atur nama file keluaran dan atribut PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Atur PageSize (jika diperlukan)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Atur PageMargins (jika diperlukan)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Cetak dokumen menggunakan pengaturan printer dan halaman
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Periksa status cetak
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // Tidak ditemukan kesalahan. Pekerjaan pencetakan telah selesai dengan sukses
                Console.WriteLine("Pencetakan selesai tanpa masalah..");
            }

            // Tutup file PDF setelah mencetak
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## Mencetak halaman dalam mode Simpleks dan Dupleks

Dalam pekerjaan pencetakan tertentu, halaman dokumen PDF dapat dicetak dalam mode Dupleks atau Simpleks, tetapi Anda tidak dapat mencetak beberapa halaman sebagai simpleks dan beberapa halaman sebagai dupleks dalam satu pekerjaan cetak. Namun untuk memenuhi persyaratan tersebut, rentang halaman yang berbeda dan objek PrintingJobSettings dapat digunakan. Cuplikan kode berikut menunjukkan cara mencetak beberapa halaman file PDF dalam mode Simpleks dan beberapa halaman dalam mode Dupleks.

```csharp
 public static void PrintingPagesInSimplexAndDuplexMode()
        {
            int printingJobIndex = 0;
            string inPdf = _dataDir + "sample-8page.pdf";
            string output = _dataDir;
            IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

            PrintingJobSettings printingJob1 = new PrintingJobSettings
            {
                FromPage = 1,
                ToPage = 3,
                OutputFile = output + "sample_1_3.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob1);

            PrintingJobSettings printingJob2 = new PrintingJobSettings
            {
                FromPage = 4,
                ToPage = 6,
                OutputFile = output + "sample_4_6.xps",
                Mode = Duplex.Simplex
            };

            printingJobs.Add(printingJob2);

            PrintingJobSettings printingJob3 = new PrintingJobSettings
            {
                FromPage = 7,
                ToPage = 7,
                OutputFile = output + "sample_7.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob3);

            PdfViewer viewer = new PdfViewer();

            viewer.BindPdf(inPdf);
            viewer.AutoResize = true;
            viewer.AutoRotate = true;
            viewer.PrintPageDialog = false;

            PrinterSettings ps = new PrinterSettings();
            PageSettings pgs = new PageSettings();

            ps.PrinterName = "Microsoft XPS Document Writer";
            ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.PrintToFile = true;
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;
            ps.PrintRange = PrintRange.SomePages;

            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
            ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            viewer.EndPrint += (sender, args) =>
            {
                if (++printingJobIndex < printingJobs.Count)
                {
                    ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                    ps.FromPage = printingJobs[printingJobIndex].FromPage;
                    ps.ToPage = printingJobs[printingJobIndex].ToPage;
                    ps.Duplex = printingJobs[printingJobIndex].Mode;
                    viewer.PrintDocumentWithSettings(pgs, ps);
                }
            };

            viewer.PrintDocumentWithSettings(pgs, ps);
        }
```