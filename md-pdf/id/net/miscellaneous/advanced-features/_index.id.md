---
title: Fitur Lanjutan
type: docs
weight: 210
url: /net/advanced-features/
---

## Mengirim Pdf ke Browser untuk Diunduh

Terkadang ketika Anda mengembangkan aplikasi ASP.NET, Anda perlu mengirim file PDF ke browser web untuk diunduh tanpa menyimpannya secara fisik. Untuk mencapai itu, Anda dapat menyimpan dokumen PDF ke dalam objek MemoryStream setelah menghasilkannya dan mengirimkan byte dari MemoryStream tersebut ke objek Response. Melakukan ini akan membuat browser mengunduh dokumen PDF yang dihasilkan.

Potongan kode berikut menunjukkan fungsionalitas di atas:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-Examples.Web-SendPdfToBrowserForDownload.aspx-1.cs" >}}

## Mengekstrak file yang tertanam dari file PDF

Aspose.PDF menonjol saat datang ke fitur lanjutan untuk bekerja dengan file format PDF. Ini mengekstrak file yang tertanam jauh lebih baik daripada alat lain yang menawarkan fitur ini.

Dengan Aspose.PDF untuk .NET, Anda dapat secara efisien mengekstrak file yang tertanam apa pun yang mungkin merupakan font yang tertanam, gambar, video, atau audio.
Dengan Aspose.PDF untuk .NET, Anda dapat secara efisien mengekstrak file yang tertanam apapun yang mungkin berupa font tertanam, gambar, video, atau audio.

Potongan kode berikut mengekstrak semua file yang tertanam dari file PDF:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-DocumentConversion-PDFToXML-PDFToXML.cs" >}}

## Penggunaan Skrip Latex untuk Menambahkan Ekspresi Matematika

Dengan Aspose.PDF, Anda dapat menambahkan ekspresi atau rumus matematika di dalam dokumen PDF menggunakan skrip latex. Contoh berikut menunjukkan bagaimana fitur ini dapat digunakan dalam dua cara yang berbeda, untuk menambahkan rumus matematika di dalam sel tabel:

### Tanpa preamble dan lingkungan dokumen

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript-WithoutPreambleanddocument.cs" >}}

### Dengan preamble dan lingkungan dokumen

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript2-WithPreambleanddocument.cs" >}}

### Dukungan untuk Tag Latex
### Dukungan untuk Tag Latex

Lingkungan align didefinisikan dalam paket amsmath, dan lingkungan proof didefinisikan dalam paket amsthm. Oleh karena itu, Anda harus menentukan paket-paket ini menggunakan perintah \usepackage dalam bagian awal dokumen. Dan ini berarti bahwa Anda harus menyertakan teks LaTeX ke dalam lingkungan dokumen seperti yang ditunjukkan dalam contoh kode berikut.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Text-UseLatexScript3-UseLatexScript3.cs" >}}
