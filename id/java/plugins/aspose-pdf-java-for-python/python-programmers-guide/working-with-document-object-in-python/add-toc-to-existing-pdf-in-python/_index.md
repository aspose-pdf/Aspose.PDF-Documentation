---
title: Tambahkan TOC ke PDF yang Ada di Python
linktitle: Tambahkan TOC ke PDF yang Ada di Python
type: docs
weight: 20
url: /id/java/add-toc-to-existing-pdf-in-python/
description: Pelajari cara menambahkan Daftar Isi (TOC) ke dokumen PDF yang ada dalam Python dengan Aspose.PDF untuk navigasi yang mudah.
lastmod: "2026-09-29"
---
Untuk menambahkan TOC dalam dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **AddToc**.

```python

# Open a pdf document.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get access to first page of PDF file
toc_page = doc.getPages().insert(1)

# Create object to represent TOC information
toc_info = self.TocInfo()
title = self.TextFragment("Table Of Contents")
title.getTextState().setFontSize(20)

# Set the title for TOC
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Create string objects which will be used as TOC elements
titles = ["First page", "Second page"]

i = 0;
while (i < 2):

# Create Heading object
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Specify the destination page for heading object
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Destination page
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Destination coordinate
segment2.setText(titles[i])

# Add heading to page containing TOC
toc_page.getParagraphs().add(heading2)

i +=1;

# Save PDF Document
doc.save(self.dataDir + "TOC.pdf")

print "Added TOC Successfully, please check the output file."
```

**Unduh Kode yang Berjalan**

UnduhВ **Add TOC (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)
