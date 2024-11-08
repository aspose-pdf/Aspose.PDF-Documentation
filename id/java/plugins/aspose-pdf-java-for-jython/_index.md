---
title: Aspose.PDF Java untuk Jython
type: docs
weight: 60
url: /id/java/aspose-pdf-java-for-jython/
lastmod: "2021-06-05"
---

## Pengenalan

### Apa itu Jython?

Jython adalah implementasi Java dari Python yang menggabungkan kekuatan ekspresif dengan kejelasan. Jython tersedia secara gratis untuk penggunaan komersial dan non-komersial dan didistribusikan dengan kode sumber. Jython melengkapi Java dan sangat cocok untuk tugas-tugas berikut:

- **Skrip tertanam** - Pemrogram Java dapat menambahkan pustaka Jython ke sistem mereka untuk memungkinkan pengguna akhir menulis skrip sederhana atau rumit yang menambahkan fungsionalitas ke aplikasi.
- **Eksperimen interaktif** - Jython menyediakan interpreter interaktif yang dapat digunakan untuk berinteraksi dengan paket Java atau dengan aplikasi Java yang sedang berjalan. Ini memungkinkan pemrogram untuk bereksperimen dan men-debug sistem Java apa pun menggunakan Jython.
- **Pengembangan aplikasi cepat** - Program Python biasanya 2-10X lebih pendek daripada program Java yang setara.
 Ini secara langsung diterjemahkan menjadi peningkatan produktivitas programmer. Interaksi yang mulus antara Python dan Java memungkinkan pengembang untuk bebas mencampur kedua bahasa tersebut baik selama pengembangan maupun dalam produk yang dikirimkan.

### Aspose.PDF untuk Java

Aspose.PDF untuk Java adalah komponen pembuatan dokumen PDF yang memungkinkan aplikasi Java Anda untuk membaca, menulis, dan memanipulasi dokumen PDF tanpa menggunakan Adobe Acrobat.

Aspose.PDF untuk Java adalah komponen dengan harga terjangkau yang menawarkan kekayaan fitur yang luar biasa, termasuk: opsi kompresi PDF, pembuatan dan manipulasi tabel, dukungan grafis, fungsi gambar, fungsionalitas hyperlink yang luas, kontrol keamanan yang diperluas, dan penanganan font khusus.

Aspose.PDF untuk Java memungkinkan Anda membuat file PDF secara langsung melalui API dan template XML yang disediakan. Menggunakan Aspose.PDF untuk Java juga akan memungkinkan Anda menambahkan kemampuan PDF ke aplikasi Anda dalam waktu singkat.

### Aspose.PDF Java untuk Jython

Aspose.PDF Java untuk Jython adalah proyek yang menunjukkan / menyediakan contoh penggunaan API Aspose.PDF untuk Java dalam Jython.
## Persyaratan Sistem dan Platform yang Didukung

### Persyaratan Sistem

Berikut adalah persyaratan sistem untuk menggunakan Aspose.PDF Java untuk Jython:

- Java 1.5 atau lebih tinggi terinstal
- Komponen Aspose.PDF yang diunduh
- Jython 2.7.0

### Platform yang Didukung

Berikut adalah platform yang didukung:

- Aspose.PDF 15.4 dan di atasnya.
- IDE Java (Eclipse, NetBeans ...)

## Unduh Instalasi dan Penggunaan

### Mengunduh

Rilis contoh berjalan berikut tersedia untuk diunduh dari GitHub:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Unduh komponen Aspose.PDF untuk Java:

- [Aspose.PDF untuk Java](https://downloads.aspose.com/pdf/java)

### Menginstal

- Tempatkan file jar Aspose.PDF untuk Java yang telah diunduh ke dalam direktori "lib".
- Ganti "your-lib" dengan nama file jar yang diunduh dalam file _*init*_.py.

### Menggunakan

Anda dapat mengonversi dokumen Pdf ke dokumen doc menggunakan contoh kode berikut:

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'


        # Buka dokumen target
        pdf = Document(dataDir + 'input1.pdf')

        # Simpan file keluaran yang digabungkan (dokumen target)
        pdf.save(dataDir + "output.doc")

        print "Dokumen telah berhasil dikonversi"


if __name__ == '__main__':       

    PdfToDoc()
```


## Dukungan, Perluasan, dan Kontribusi

### Dukungan

Sejak hari pertama Aspose, kami tahu bahwa hanya memberikan produk yang baik kepada pelanggan kami tidaklah cukup. Kami juga perlu memberikan layanan yang baik. Kami adalah pengembang sendiri dan mengerti betapa frustrasinya ketika masalah teknis atau keanehan dalam perangkat lunak menghentikan Anda melakukan apa yang perlu Anda lakukan. Kami di sini untuk memecahkan masalah, bukan menciptakannya.

Inilah mengapa kami menawarkan dukungan gratis. Siapapun yang menggunakan produk kami, baik yang telah membelinya atau menggunakan evaluasi, berhak mendapatkan perhatian dan rasa hormat penuh dari kami.

Anda dapat mencatat masalah atau saran apa pun terkait Aspose.PDF Java untuk Jython menggunakan salah satu platform berikut:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Perluasan dan Kontribusi

Aspose.PDF Java untuk Jython adalah sumber terbuka dan kode sumbernya tersedia di situs web pemrograman sosial utama yang tercantum di bawah ini.
 Developers didorong untuk mengunduh kode sumber dan berkontribusi dengan menyarankan atau menambahkan fitur baru atau meningkatkan yang sudah ada, sehingga orang lain juga dapat merasakannya.

### Kode Sumber

Anda dapat mendapatkan kode sumber terbaru dari salah satu lokasi berikut

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)