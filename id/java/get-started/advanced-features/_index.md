---
title: Fitur Lanjutan
linktitle: Fitur Lanjutan
type: docs
weight: 120
url: id/java/advanced-features/
description: Bagian ini menunjukkan bagaimana Anda dapat menggunakan Tag LaTeX dalam dokumen PDF dengan Aspose.PDF untuk Java.
lastmod: "2022-01-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dukungan untuk Tag Latex

Alat ini digunakan secara keseluruhan untuk membuat makalah ilmiah, menulis buku, dan banyak bentuk publikasi lainnya. Ini tidak hanya memungkinkan untuk membuat dokumen yang didesain dengan indah, tetapi juga memungkinkan pengguna untuk dengan cepat mengimplementasikan elemen kompleks dari set cetak seperti ekspresi matematika, tabel, referensi, dan bibliografi, mendapatkan markup yang konsisten di semua bagian.

Mari kita lihat contoh latihan matematika dalam potongan kode menggunakan tag Latex.

Mulai dari versi Aspose.PDF untuk Java 19.9 API menyediakan dukungan untuk tag Latex \begin \end \qedhere. Ini mengharuskan Anda untuk memasukkan teks LaTeX ke dalam lingkungan dokumen seperti yang ditunjukkan dalam contoh kode berikut.

```java
String dataDir = Utils.getSharedDataDir(UseLatexScript3.class) + "Text/";





String s =
              "\\usepackage{amsmath,amsthm}" +
              "\\begin{document}" +
              "\\begin{proof} Bukti adalah sebagai berikut: " +
              "\\begin{align}" +
              "(x+y)^3&=(x+y)(x+y)^2" +
              "(x+y)(x^2+2xy+y^2)\\\\" +
              "&=x^3+3x^2y+3xy^3+x^3.\\qedhere" +
              "\\end{align}" +
              "\\end{proof}" +
              "\\end{document}";

Document doc = new Document();
Page page = doc.getPages().add();

LatexFragment latex = new LatexFragment(s);

page.getParagraphs().add(latex);
      
doc.save(dataDir + "Script_out.pdf");
```