---
title: Tambahkan TOC ke PDF yang Ada di Python
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-python/
lastmod: "2021-06-05"
---

Untuk menambahkan TOC dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **AddToc**.

```python

# Buka dokumen pdf.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Dapatkan akses ke halaman pertama file PDF
toc_page = doc.getPages().insert(1)

# Buat objek untuk mewakili informasi TOC
toc_info = self.TocInfo()
title = self.TextFragment("Daftar Isi")
title.getTextState().setFontSize(20)

# Tetapkan judul untuk TOC
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Buat objek string yang akan digunakan sebagai elemen TOC
titles = ["Halaman pertama", "Halaman kedua"]

i = 0;
while (i < 2):

# Buat objek Heading
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Tentukan halaman tujuan untuk objek heading
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Halaman tujuan
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Koordinat tujuan
segment2.setText(titles[i])

# Tambahkan heading ke halaman yang mengandung TOC
toc_page.getParagraphs().add(heading2)

i +=1;

# Simpan Dokumen PDF
doc.save(self.dataDir + "TOC.pdf")

print "Berhasil menambahkan TOC, silakan periksa file output."
```


**Unduh Kode Berjalan**

Unduh **Tambahkan TOC (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)