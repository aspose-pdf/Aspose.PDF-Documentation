---
title: Ekstrak Teks Dari Stempel
type: docs
weight: 60
url: /java/extract-text-from-stamps/
---

## Ekstrak Teks dari Anotasi Stempel

Aspose.PDF untuk Java memungkinkan Anda mengekstrak teks dari anotasi stempel. Untuk mengekstrak teks dari Anotasi Stempel dalam PDF, langkah-langkah berikut dapat digunakan.

1. Buat objek kelas Document
1. Dapatkan Anotasi yang diinginkan dari daftar anotasi pada sebuah halaman
1. Definisikan objek baru dari kelas TextAbsorber
1. Gunakan metode visit dari TextAbsorber untuk mendapatkan Teks

```java
Document doc = new Document(dataDir+"test.pdf");
Annotation item = doc.getPages().get_Item(1).getAnnotations().get_Item(3);
if (item instanceof StampAnnotation ) {
   StampAnnotation annot = (StampAnnotation) item;
   TextAbsorber ta = new TextAbsorber();
   XForm ap = annot.getNormalAppearance();
   ta.visit(ap);
   System.out.println(ta.getText());
}
```