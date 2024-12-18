---
title: Menambahkan JavaScript dalam Python
type: docs
weight: 10
url: /id/java/adding-javascript-in-python/
lastmod: "2021-06-05"
---

Untuk menambahkan JavaScript menggunakan Aspose.PDF Java dalam Python, cukup panggil metode AddJavascript() dari kelas Document.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('halaman 2 dibuka')")

# Menambahkan JavaScript di Tingkat Halaman
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('halaman 2 ditutup')"))

# Simpan Dokumen PDF
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "JavaScript berhasil ditambahkan, silakan periksa file keluaran."

```

**Unduh Kode Berjalan**

Unduh **Tambahkan Javascript (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)