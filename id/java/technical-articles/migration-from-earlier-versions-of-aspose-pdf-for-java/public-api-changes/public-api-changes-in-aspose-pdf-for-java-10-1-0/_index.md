---
title: Perubahan API Publik di Aspose.PDF untuk Java 10.1.0
type: docs
weight: 100
url: /id/java/public-api-changes-in-aspose-pdf-for-java-10-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan dalam [Aspose.PDF untuk Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx). Ini tidak hanya mencakup metode publik baru dan usang, tetapi juga deskripsi perubahan dalam perilaku di balik layar di Aspose.PDF untuk Java yang mungkin mempengaruhi kode yang ada. Setiap perilaku yang diperkenalkan yang dapat dilihat sebagai regresi dan memodifikasi perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}


**Perubahan API Publik dan Ketidakcocokan ke Belakang**

## Menambahkan kelas pengecualian baru:

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**


Menambahkan metode:

- public boolean getUseIntermidiateImage()
- public void setUseIntermidiateImage(boolean value)

**com.aspose.pdf.XForm**

Metode yang ditambahkan:

- public void freeMemory()

**com.aspose.pdf.TextSearchOptions**

Metode yang ditambahkan:

- public boolean getUseFontEngineEncoding()
- public void setUseFontEngineEncoding(boolean value)

**com.aspose.pdf.TextEditOptions**

Metode yang ditambahkan:

- public TextEditOptions(boolean allowLanguageTransformation)
- public boolean getAllowLanguageTransformation()
- public void setAllowLanguageTransformation(boolean value)

**com.aspose.pdf.Page**

Metode yang ditambahkan:

- public void processParagraphs()
- public void dispose()

**com.aspose.pdf.IDocument**

Metode yang ditambahkan:

- public void processParagraphs();

**com.aspose.pdf.Document**

Metode yang ditambahkan:

- public void processParagraphs();

**com.aspose.pdf.DocSaveOptions**

Metode yang ditambahkan:

- public boolean getAddReturnToLineEnd()
- public void setAddReturnToLineEnd(boolean value)

**com.aspose.pdf.HtmlDocumentTypeInternal - dihapus.**