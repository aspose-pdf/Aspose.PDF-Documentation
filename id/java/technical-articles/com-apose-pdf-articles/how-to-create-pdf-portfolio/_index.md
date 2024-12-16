---
title: Cara Membuat Portofolio PDF
type: docs
weight: 10
url: /id/java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Portofolio PDF memungkinkan Anda untuk menggabungkan konten dari berbagai sumber (misalnya, file PDF, Word, Excel, JPEG) ke dalam satu wadah terpadu. File asli mempertahankan identitas individual mereka tetapi dirakit menjadi file portofolio PDF. Pengguna dapat membuka, membaca, mengedit, dan memformat setiap file komponen secara independen dari file komponen lainnya.

Aspose.PDF untuk Java memungkinkan pembuatan dokumen Portofolio PDF menggunakan kelas Document. Muat file individual ke dalam objek FileSpecification dan tambahkan ke objek Document.Collection menggunakan metode add(...). Setelah file ditambahkan, gunakan metode save(..) kelas Document untuk menghasilkan dokumen portofolio.

{{% /alert %}}

## Contoh Kode

Contoh berikut menggunakan File Microsoft XPS, dokumen Word, PDF, dan file gambar untuk membuat Portofolio PDF.

**Portofolio PDF yang dibuat dengan Aspose.PDF**

![todo:image_alt_text](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "CreatePDFPortfolio.java" >}}