---
title: Mengatur Properti Elemen Struktur dalam PDF Bertanda
linktitle: Mengatur Properti Elemen Struktur
type: docs
weight: 30
url: /id/java/set-tagged-pdfs-element-properties/
description: Dengan Aspose.PDF untuk Java, Anda dapat mengatur berbagai Properti Elemen Struktur. Ada pengaturan Elemen Struktur Blok Teks, pengaturan Elemen Struktur Inline, menambahkan Elemen Struktur ke dalam Elemen dan lain-lain.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mengatur Properti Elemen Struktur

Untuk mengatur properti elemen struktur dalam Dokumen PDF Bertanda, Aspose.PDF menawarkan metode **createSectElement()** dan **createHeaderElement()** dari Antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Cuplikan kode berikut menunjukkan cara mengatur properti elemen struktur dari Dokumen PDF Bertanda:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";
// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Atur Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen Pdf Bertanda");
taggedContent.setLanguage("en-US");

// Buat Elemen Struktur
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("The Header");

h1.setTitle("Judul");
h1.setLanguage("en-US");
h1.setAlternativeText("Teks Alternatif");
h1.setExpansionText("Teks Ekspansi");
h1.setActualText("Teks Aktual");

// Simpan Dokumen Pdf Bertanda
document.save(path + "StructureElementsProperties.pdf");
```


## Mengatur Elemen Struktur Teks

Untuk mengatur elemen struktur teks dari Dokumen PDF Berlabel, Aspose.PDF menawarkan Kelas [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Potongan kode berikut menunjukkan cara mengatur elemen struktur teks dari Dokumen PDF Berlabel:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";

// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Atur Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen Pdf Berlabel");
taggedContent.setLanguage("en-US");

// Dapatkan Elemen Struktur Akar
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// Atur Teks ke Elemen Struktur Teks
p.setText("Paragraf.");
rootElement.appendChild(p);

// Simpan Dokumen Pdf Berlabel
document.save(path + "TextStructureElement.pdf");
```


## Menyetel Elemen Struktur Blok Teks

Untuk menyetel elemen struktur blok teks dari Dokumen PDF Bertanda, Aspose.PDF menawarkan Kelas [HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) dan [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Anda dapat menambahkan objek dari kelas ini sebagai anak dari objek **StructureElement**. Kode berikut menunjukkan cara menyetel elemen struktur blok teks dari Dokumen PDF Bertanda:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";

// Membuat Dokumen Pdf
Document document = new Document();

// Mendapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Menyetel Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen Pdf Bertanda");
taggedContent.setLanguage("en-US");

// Mendapatkan Elemen Struktur Akar
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. Header Level 1");
h2.setText("H2. Header Level 2");
h3.setText("H3. Header Level 3");
h4.setText("H4. Header Level 4");
h5.setText("H5. Header Level 5");
h6.setText("H6. Header Level 6");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// Simpan Dokumen Pdf Bertanda
document.save(path + "TextBlockStructureElements.pdf");
```


## Mengatur Elemen Struktur Inline

Untuk mengatur elemen struktur inline dari Dokumen PDF Bertag, Aspose.PDF menawarkan Kelas [SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) dan [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Anda dapat menambahkan objek dari kelas ini sebagai anak dari objek **StructureElement**. Cuplikan kode berikut menunjukkan cara mengatur elemen struktur inline dari Dokumen PDF Bertag:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";
// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Atur Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen Pdf Bertag");
taggedContent.setLanguage("en-US");

// Dapatkan Elemen Struktur Root
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

SpanElement spanH11 = taggedContent.createSpanElement();
spanH11.setText("H1. ");
h1.appendChild(spanH11);
SpanElement spanH12 = taggedContent.createSpanElement();
spanH12.setText("Header Level 1");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("Header Level 2");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("Header Level 3");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("Header Level 4");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("Header Level 5");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("Header Level 6");
h6.appendChild(spanH62);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. ");
rootElement.appendChild(p);
SpanElement span1 = taggedContent.createSpanElement();
span1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.appendChild(span1);
SpanElement span2 = taggedContent.createSpanElement();
span2.setText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.appendChild(span2);
SpanElement span3 = taggedContent.createSpanElement();
span3.setText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.appendChild(span3);
SpanElement span4 = taggedContent.createSpanElement();
span4.setText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.appendChild(span4);
SpanElement span5 = taggedContent.createSpanElement();
span5.setText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.appendChild(span5);
SpanElement span6 = taggedContent.createSpanElement();
span6.setText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.appendChild(span6);
SpanElement span7 = taggedContent.createSpanElement();
span7.setText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.appendChild(span7);
SpanElement span8 = taggedContent.createSpanElement();
span8.setText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.appendChild(span8);
SpanElement span9 = taggedContent.createSpanElement();
span9.setText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.appendChild(span9);
SpanElement span10 = taggedContent.createSpanElement();
span10.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.appendChild(span10);

// Simpan Dokumen Pdf Bertag
document.save(path + "InlineStructureElements.pdf");
```


## Mengatur Nama Tag Kustom

Untuk mengatur nama tag kustom dari elemen-elemen dari Dokumen PDF Berlabel, Aspose.PDF menawarkan metode **setTag()** untuk elemen-elemen. Cuplikan kode berikut menunjukkan cara mengatur nama tag kustom:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";
// Buat Dokumen PDF
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Tetapkan Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen PDF Berlabel");
taggedContent.setLanguage("en-US");

// Buat Elemen Struktur Logis
SectElement sect = taggedContent.createSectElement();
taggedContent.getRootElement().appendChild(sect);

ParagraphElement p1 = taggedContent.createParagraphElement();
ParagraphElement p2 = taggedContent.createParagraphElement();
ParagraphElement p3 = taggedContent.createParagraphElement();
ParagraphElement p4 = taggedContent.createParagraphElement();

p1.setText("P1. ");
p2.setText("P2. ");
p3.setText("P3. ");
p4.setText("P4. ");

p1.setTag("P1");
p2.setTag("Para");
p3.setTag("Para");
p4.setTag("Paragraph");

sect.appendChild(p1);
sect.appendChild(p2);
sect.appendChild(p3);
sect.appendChild(p4);

SpanElement span1 = taggedContent.createSpanElement();
SpanElement span2 = taggedContent.createSpanElement();
SpanElement span3 = taggedContent.createSpanElement();
SpanElement span4 = taggedContent.createSpanElement();

span1.setText("Span 1.");
span2.setText("Span 2.");
span3.setText("Span 3.");
span4.setText("Span 4.");

span1.setTag("SPAN");
span2.setTag("Sp");
span3.setTag("Sp");
span4.setTag("TheSpan");

p1.appendChild(span1);
p2.appendChild(span2);
p3.appendChild(span3);
p4.appendChild(span4);

// Simpan Dokumen PDF Berlabel
document.save(path + "CustomTag.pdf");
```


## Menambahkan Elemen Struktur ke dalam Elemen

Untuk mengatur elemen struktur tautan dalam Dokumen PDF Bertanda, Aspose.PDF menawarkan metode **createLinkElement()** dari Antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Cuplikan kode berikut menunjukkan cara mengatur elemen struktur dalam paragraf dengan teks Dokumen PDF Bertanda:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// Pembuatan dokumen dan mendapatkan Konten Pdf Bertanda
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();


// Mengatur Judul dan Bahasa Alam untuk dokumen
taggedContent.setTitle("Contoh Elemen Teks");
taggedContent.setLanguage("en-US");

// Mendapatkan elemen struktur Akar (elemen struktur Dokumen)
StructureElement rootElement = taggedContent.getRootElement();


ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" dan Span_12.");
p1.setText("Paragraf dengan ");
p1.appendChild(span11);
p1.appendChild(span12);


ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22.");
p2.appendChild(span21);
p2.setText(" dan ");
p2.appendChild(span22);


ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" dan Span_32");
p3.appendChild(span31);
p3.appendChild(span32);
p3.setText(".");


ParagraphElement p4 = taggedContent.createParagraphElement();
rootElement.appendChild(p4);
SpanElement span41 = taggedContent.createSpanElement();
SpanElement span411 = taggedContent.createSpanElement();
span411.setText("Span_411, ");
span41.setText("Span_41, ");
span41.appendChild(span411);
SpanElement span42 = taggedContent.createSpanElement();
SpanElement span421 = taggedContent.createSpanElement();
span421.setText("Span 421 dan ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText(".");


// Simpan Dokumen Pdf Bertanda
document.save(outFile);
```


## Menetapkan Elemen Struktur Catatan

Aspose.PDF untuk Java API juga memungkinkan Anda untuk menambahkan **NoteElement** dalam dokumen PDF bertanda. Cuplikan kode berikut menunjukkan cara menambahkan elemen catatan dalam Dokumen PDF Bertanda:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// Buat Dokumen Pdf
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Contoh Elemen Catatan");
taggedContent.setLanguage("en-US");

// Tambahkan Elemen Paragraf
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// Tambahkan NoteElement
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("Catatan dengan ID yang dihasilkan secara otomatis. ");

// Tambahkan NoteElement
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("Catatan dengan ID = 'note_002'. ");
note2.setId("note_002");

// Tambahkan NoteElement
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("Catatan dengan ID = 'note_003'. ");
note3.setId("note_003");
// Simpan Dokumen Pdf Bertanda
document.save(outFile);
```