---
title: "Mengatur submit flag"
linktitle: "Mengatur submit flag"
type: docs
weight: 40
url: /id/java/set-submit-flag/
description: "Tinjau cakupan Java saat ini untuk mengatur submit flag pada tombol formulir PDF dengan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: Konfigurasi submit flag dalam contoh FormEditor Java
Abstract: Set contoh Java saat ini tidak menampilkan konfigurasi submit-flag sebagai metode contoh terpisah yang berdiri sendiri. Sebagai gantinya, konfigurasi tersebut ditunjukkan bersama dengan konfigurasi submit URL dalam `setSubmitUrl(...)`.
---
Java metode `FormEditorExamples.setSubmitUrl(...)` mencakup:

## Mengonfigurasi submit flag

1. Ikat PDF sumber ke fasad `FormEditor`.
2. Atur URL pengiriman untuk bidang tombol.
3. Atur flag pengiriman untuk format yang diperlukan.
4. Simpan dokumen yang diperbarui.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

Gunakan contoh gabungan itu sebagai alur kerja Java yang didukung sumber untuk mengonfigurasi bendera kirim dalam repositori ini.
