---
title: Menambahkan JavaScript di Python
linktitle: Menambahkan JavaScript di Python
type: docs
weight: 10
url: /id/java/adding-javascript-in-python/
description: Cari tahu cara menyematkan kode JavaScript dalam dokumen PDF menggunakan Python dan Aspose.PDF untuk meningkatkan interaktivitas.
lastmod: "2026-09-29"
---
Untuk menambahkan Add Javascript menggunakan Aspose.PDF Java di Python, cukup panggil metode AddJavascript() dari kelas Document.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# Adding JavaScript at Page Level
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Save PDF Document
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "Added JavaScript Successfully, please check the output file."

```

**Unduh Kode yang Berjalan**

Unduh **Add Javascript (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
