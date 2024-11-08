---
title: Membuat PDF Bertag 
linktitle: Membuat PDF Bertag 
type: docs
weight: 10
lastmod: "2021-06-05"
url: /id/java/create-tagged-pdf-documents/
description: Artikel ini menjelaskan cara membuat elemen struktur untuk dokumen PDF bertag secara programatis menggunakan Aspose.PDF untuk Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Membuat Elemen Struktur

Untuk membuat elemen struktur dalam Dokumen PDF Bertag, Aspose.PDF menawarkan metode untuk membuat elemen struktur menggunakan Antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Cuplikan kode berikut menunjukkan cara membuat elemen struktur dari PDF Bertag:

```java
// Untuk contoh lengkap dan file data, silakan pergi ke https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";

// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Setel Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen Pdf Bertag");
taggedContent.setLanguage("en-US");

// Buat Elemen Pengelompokan
PartElement partElement = taggedContent.createPartElement();
ArtElement artElement = taggedContent.createArtElement();
SectElement sectElement = taggedContent.createSectElement();
DivElement divElement = taggedContent.createDivElement();
BlockQuoteElement blockQuoteElement = taggedContent.createBlockQuoteElement();
CaptionElement captionElement = taggedContent.createCaptionElement();
TOCElement tocElement = taggedContent.createTOCElement();
TOCIElement tociElement = taggedContent.createTOCIElement();
IndexElement indexElement = taggedContent.createIndexElement();
NonStructElement nonStructElement = taggedContent.createNonStructElement();
PrivateElement privateElement = taggedContent.createPrivateElement();

// Buat Elemen Struktur Tingkat Blok Teks
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// Buat Elemen Struktur Tingkat Garis Teks
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// Buat Elemen Struktur Ilustrasi
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// Metode sedang dalam pengembangan
ListElement listElement = taggedContent.createListElement();
TableElement tableElement = taggedContent.createTableElement();
ReferenceElement referenceElement = taggedContent.createReferenceElement();
BibEntryElement bibEntryElement = taggedContent.createBibEntryElement();
CodeElement codeElement = taggedContent.createCodeElement();
LinkElement linkElement = taggedContent.createLinkElement();
AnnotElement annotElement = taggedContent.createAnnotElement();
RubyElement rubyElement = taggedContent.createRubyElement();
WarichuElement warichuElement = taggedContent.createWarichuElement();
FormElement formElement = taggedContent.createFormElement();

// Simpan Dokumen Pdf Bertag
document.save(path + "StructureElements.pdf");
```


## Membuat Pohon Elemen Struktur

Untuk membuat pohon elemen struktur dalam Dokumen PDF Berlabel, Aspose.PDF menawarkan metode untuk membuat pohon elemen struktur menggunakan Antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Cuplikan kode berikut menunjukkan cara membuat pohon elemen struktur dari Dokumen PDF Berlabel:

```java
// Untuk contoh lengkap dan file data, silakan pergi ke https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";
// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Tetapkan Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen Pdf Berlabel");
taggedContent.setLanguage("en-US");

// Dapatkan elemen struktur akar (Dokumen)
StructureElement rootElement = taggedContent.getRootElement();

// Buat Struktur Logis
SectElement sect1 = taggedContent.createSectElement();
rootElement.appendChild(sect1);

SectElement sect2 = taggedContent.createSectElement();
rootElement.appendChild(sect2);

DivElement div11 = taggedContent.createDivElement();
sect1.appendChild(div11);

DivElement div12 = taggedContent.createDivElement();
sect1.appendChild(div12);

ArtElement art21 = taggedContent.createArtElement();
sect2.appendChild(art21);

ArtElement art22 = taggedContent.createArtElement();
sect2.appendChild(art22);

DivElement div211 = taggedContent.createDivElement();
art21.appendChild(div211);

DivElement div212 = taggedContent.createDivElement();
art21.appendChild(div212);

DivElement div221 = taggedContent.createDivElement();
art22.appendChild(div221);

DivElement div222 = taggedContent.createDivElement();
art22.appendChild(div222);

SectElement sect3 = taggedContent.createSectElement();
rootElement.appendChild(sect3);

DivElement div31 = taggedContent.createDivElement();
sect3.appendChild(div31);

// Simpan Dokumen Pdf Berlabel
document.save(path + "StructureElementsTree.pdf");
```


## Menata Struktur Teks

Untuk menata struktur teks dalam Dokumen PDF Bertanda, Aspose.PDF menawarkan properti **setFont()**, **setFontSize()**, **setFontStyle()**, dan **setForegroundColor()** dari Kelas [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState). Cuplikan kode berikut menunjukkan cara menata struktur teks dalam Dokumen PDF Bertanda:

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

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// Dalam Pengembangan
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("Teks merah miring.");

// Simpan Dokumen Pdf Bertanda
document.save(path + "StyleTextStructure.pdf");
```


## Mengilustrasikan Elemen Struktur

Untuk mengilustrasikan elemen struktur dalam Dokumen PDF Berlabel, Aspose.PDF menawarkan Kelas [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement). Cuplikan kode berikut menunjukkan cara mengilustrasikan elemen struktur dalam Dokumen PDF Berlabel:

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

// Sedang Dalam Pengembangan
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("Gambar Satu");
figure1.setTitle("Gambar 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// Simpan Dokumen Pdf Berlabel
document.save(path + "IllustrationStructureElements.pdf");
```


## **Membuat PDF dengan Gambar Berlabel**

Untuk membuat PDF dengan Gambar Berlabel, Aspose.PDF menawarkan metode [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) dari Antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Cuplikan kode berikut menunjukkan fungsionalitasnya.

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Logo Aspose");
figure1.setTitle("Gambar 1");
figure1.setTag("Fig");
// Tambahkan gambar dengan resolusi 300 DPI (secara default)
figure1.setImage("aspose-logo.jpg");
// Simpan Dokumen PDF
document.save("PDFwithTaggedImage.pdf");
```


## Membuat PDF dengan Teks Bertanda

Untuk membuat PDF dengan Teks Bertanda, Aspose.PDF menawarkan Antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Cuplikan kode berikut menunjukkan fungsionalitasnya.

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Tetapkan Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen Pdf Bertanda");
taggedContent.setLanguage("en-US");

// Buat Elemen Struktur Level-Blok Teks
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("Judul 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("uji 1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("uji 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("uji 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("uji 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("uji 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("uji 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("uji 7");

// Simpan Dokumen PDF
document.save(dataDir + "PDFwithTaggedText.pdf");
```