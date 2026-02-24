---
title: Bandingkan dokumen PDF
linktitle: Bandingkan PDF
type: docs
weight: 130
url: /id/python-net/compare-pdf-documents/
description: Dimungkinkan untuk membandingkan konten dokumen PDF dengan tanda anotasi dan output berdampingan.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## Cara Membandingkan Dokumen PDF

Saat bekerja dengan dokumen PDF, ada kalanya Anda perlu membandingkan konten dua dokumen untuk mengidentifikasi perbedaan. Perpustakaan Aspose.PDF for Python via .NET menyediakan seperangkat alat yang kuat untuk tujuan ini. Dalam artikel ini, kami akan mengeksplorasi cara membandingkan dokumen PDF menggunakan beberapa cuplikan kode sederhana.

Fungsi perbandingan dalam Aspose.PDF memungkinkan Anda membandingkan dua dokumen PDF halaman per halaman. Anda dapat memilih untuk membandingkan halaman tertentu atau seluruh dokumen. Dokumen perbandingan yang dihasilkan menyoroti perbedaan, memudahkan identifikasi perubahan antara kedua file.

Berikut adalah daftar cara yang mungkin untuk membandingkan dokumen PDF menggunakan perpustakaan Aspose.PDF for Python via .NET:

1. **Membandingkan Halaman Tertentu** - Bandingkan halaman pertama dari dua dokumen PDF.
1. **Membandingkan Seluruh Dokumen** - Bandingkan seluruh konten dua dokumen PDF.
1. **Bandingkan dokumen PDF secara grafis**:

- Bandingkan PDF dengan metode 'comparer.get_difference' - gambar individual di mana perubahan ditandai.
- Bandingkan PDF dengan metode 'comparer.compare_documents_to_pdf' - dokumen PDF dengan gambar di mana perubahan ditandai.

## Membandingkan Halaman Tertentu

Cuplikan kode pertama menunjukkan cara membandingkan halaman pertama dari dua dokumen PDF menggunakan kelas SideBySidePdfComparer.

1. Inisialisasi Dokumen.
1. Buat fungsi untuk melakukan perbandingan.
1. Proses Perbandingan:

- document1.pages[1] dan document2.pages[1]: - ini menentukan halaman pertama dari masing-masing dokumen untuk perbandingan. Perhatikan bahwa pengindeksan halaman dimulai dari 1 di Aspose.PDF.
- SideBySideComparisonOptions - kelas ini memungkinkan kustomisasi perilaku perbandingan.
- additional_change_marks = True - mengaktifkan tampilan penanda perubahan tambahan, menyoroti perbedaan yang mungkin ada di halaman lain, bahkan jika tidak ada di halaman yang sedang dibandingkan.
- comparison_mode = ComparisonMode.IgnoreSpaces - mengatur mode perbandingan untuk mengabaikan spasi dalam teks, fokus hanya pada perubahan dalam kata.

1. Hasil perbandingan disimpan sebagai file PDF baru bernama ComparingSpecificPages_out.pdf di data_dir yang ditentukan.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## Membandingkan Seluruh Dokumen

Cuplikan kode kedua memperluas ruang lingkup untuk membandingkan seluruh konten dua dokumen PDF.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

Kode yang disediakan menunjukkan cara membandingkan dua dokumen PDF menggunakan Aspose.PDF for Python via .NET. Ia menggunakan kelas SideBySidePdfComparer untuk melakukan perbandingan halaman demi halaman, menghasilkan PDF baru yang menampilkan perbedaan berdampingan. Perbandingan dikonfigurasi dengan SideBySideComparisonOptions, di mana additional_change_marks diatur ke True untuk menyoroti perubahan tidak hanya pada halaman saat ini tetapi juga pada halaman lain, dan comparison_mode diatur ke IgnoreSpaces untuk fokus pada perbedaan konten yang berarti dengan mengabaikan variasi spasi.

## Bandingkan Menggunakan GraphicalPdfComparer

Saat berkolaborasi pada dokumen, terutama di lingkungan profesional, Anda sering berakhir dengan banyak versi dari file yang sama.
Kode yang disediakan menunjukkan cara membandingkan secara visual halaman tertentu dari dua dokumen PDF menggunakan Aspose.PDF for Python via .NET. Dengan menggunakan kelas `GraphicalPdfComparer`, ia menyoroti perbedaan antara halaman pertama dari kedua PDF dan menghasilkan gambar yang sesuai untuk merepresentasikan perbedaan tersebut.

Anda dapat mengatur properti kelas berikut:

- Resolution - resolusi dalam satuan DPI untuk gambar output, serta untuk gambar yang dihasilkan selama perbandingan.
- Color - warna penanda perubahan.
- Threshold - ambang perubahan dalam persen. Nilai default adalah nol. Menetapkan nilai selain nol memungkinkan Anda mengabaikan perubahan grafis yang tidak signifikan bagi Anda.

Dengan Aspose.PDF for Python via .NET, dimungkinkan untuk membandingkan dokumen dan halaman serta mengeluarkan hasil perbandingan ke dokumen PDF atau file gambar.

Kelas `GraphicalPdfComparer` memiliki metode yang memungkinkan Anda mendapatkan perbedaan gambar halaman dalam bentuk yang cocok untuk pemrosesan lebih lanjut: `get_difference(document1.pages[1], document2.pages[1])`.

Metode ini mengembalikan objek tipe `images_difference`, yang berisi gambar halaman pertama yang dibandingkan dan array perbedaan.

Objek `images_difference` memungkinkan Anda menghasilkan gambar yang berbeda dan mendapatkan gambar halaman kedua yang dibandingkan dengan menerapkan array perbedaan pada gambar asli. Untuk melakukannya, gunakan metode `difference_to_image` dan `get_destination_image`.

### Bandingkan PDF dengan Metode Get Difference

Kode yang disediakan mendefinisikan metode `get_difference` yang membandingkan dua dokumen PDF dan menghasilkan representasi visual dari perbedaan di antara keduanya.

Metode ini membandingkan halaman pertama dari dua file PDF dan menghasilkan dua gambar PNG:

- Satu gambar menyoroti perbedaan antara halaman-halaman dalam warna merah.
- Gambar lain adalah representasi visual dari halaman PDF tujuan (kedua).

Proses ini dapat berguna untuk membandingkan secara visual perubahan atau perbedaan antara dua versi dokumen.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### Bandingkan PDF dengan Metode CompareDocumentsToPdf

Potongan kode yang disediakan menggunakan metode `compare_documents_to_pdf`, yang membandingkan dua dokumen dan menghasilkan laporan PDF dari hasil perbandingan.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

Contoh ini menunjukkan cara melakukan perbandingan grafis dari dua dokumen PDF lengkap menggunakan Aspose.PDF untuk Python melalui .NET. Dengan memanfaatkan kelas `GraphicalPdfComparer`, ia menghasilkan file PDF baru yang menyoroti perbedaan secara visual antara dokumen-dokumen tersebut.

- Properti threshold diatur ke 3.0, yang berarti perbedaan kecil di bawah persentase ini diabaikan selama perbandingan, fokus pada perubahan yang lebih signifikan.
- Perbedaan ditandai dengan warna biru dengan mengatur properti warna ke ap.Color.blue, memungkinkan perbedaan visual yang jelas.
- Perbandingan dilakukan dengan resolusi 300 DPI dengan mengatur properti resolusi, memastikan output yang detail dan jelas.

Metode `compare_documents_to_pdf` membandingkan semua halaman dari kedua dokumen dan menghasilkan hasilnya ke file PDF baru, compareDocumentsToPdf_out.pdf, dengan perbedaan yang disorot secara visual.

