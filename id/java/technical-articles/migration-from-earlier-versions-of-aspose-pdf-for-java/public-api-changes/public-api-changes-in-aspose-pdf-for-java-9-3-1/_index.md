---
title: Perubahan API Publik di Aspose.PDF untuk Java 9.3.1
type: docs
weight: 60
url: /id/java/public-api-changes-in-aspose-pdf-for-java-9-3-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan dalam **Aspose.PDF untuk Java 9.3.1.** Ini mencakup tidak hanya metode publik baru dan usang, tetapi juga deskripsi tentang perubahan perilaku di balik layar dalam Aspose.PDF untuk Java yang dapat mempengaruhi kode yang ada. Perilaku apa pun yang diperkenalkan yang dapat dilihat sebagai regresi dan memodifikasi perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

## Metode berikut telah diinternalisasi:

com.aspose.pdf.DocumentInfo.setCreator(String)<p>
com.aspose.pdf.DocumentInfo.setProducer(String)<p>
com.aspose.pdf.FileParams.getEngineDict()

## Konstanta usang berikut telah diinternalisasi, perlu menggunakan pengambil statis sebagai gantinya:

com.aspose.pdf.ImageFormatInternal.Bmp<p>
com.aspose.pdf.ImageFormatInternal.Emf<p>

com.aspose.pdf.ImageFormatInternal.Exif<p>

com.aspose.pdf.ImageFormatInternal.Gif<p>
com.aspose.pdf.ImageFormatInternal.Jpeg<p>
com.aspose.pdf.ImageFormatInternal.Icon<p>
com.aspose.pdf.ImageFormatInternal.MemoryBmp<p>
com.aspose.pdf.ImageFormatInternal.Png<p>
com.aspose.pdf.ImageFormatInternal.Tiff<p>
com.aspose.pdf.ImageFormatInternal.Wmf<p>
com.aspose.pdf.TextEncodingInternal.ASCII<p>
com.aspose.pdf.TextEncodingInternal.BigEndianUnicode<p>
com.aspose.pdf.TextEncodingInternal.Default<p>
com.aspose.pdf.TextEncodingInternal.Unicode<p>
com.aspose.pdf.TextEncodingInternal.UTF32<p>
com.aspose.pdf.TextEncodingInternal.UTF32BE<p>
com.aspose.pdf.TextEncodingInternal.UTF7<p>
com.aspose.pdf.TextEncodingInternal.UTF8<p>
com.aspose.pdf.TextEncodingInternal.UTF8Unmarked

## Bidang berikut ditambahkan:

public static Rectangle com.aspose.pdf.Rectangle.getEmpty() - mengembalikan persegi panjang kosong