title: Dapatkan Properti Halaman dalam Python
type: docs
weight: 50
url: /python-java/get-page-properties-in-python/
---

Untuk mendapatkan properti halaman dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **GetPageProperties**.

**Kode Python**
```
doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# dapatkan koleksi halaman
page_collection = pdf_document.getPages();

# dapatkan halaman tertentu
pdf_page = page_collection.get_Item(1);

# dapatkan properti halaman
print "ArtBox : Height = " + pdf_page.getArtBox().getHeight() + ", Width = " + pdf_page.getArtBox().getWidth() + ", LLX = " + pdf_page.getArtBox().getLLX() + ", LLY = " + pdf_page.getArtBox().getLLY() + ", URX = " + pdf_page.getArtBox().getURX() + ", URY = " + pdf_page.getArtBox().getURY()
print "BleedBox : Height = " + pdf_page.getBleedBox().getHeight() + ", Width = " + pdf_page.getBleedBox().getWidth() + ", LLX = " + pdf_page.getBleedBox().getLLX() + ", LLY = " + pdf_page.getBleedBox().getLLY() + ", URX = " + pdf_page.getBleedBox().getURX() + ", URY = " .

 pdf_page.getBleedBox().getURY()
print "CropBox : Tinggi = " + pdf_page.getCropBox().getHeight() + ", Lebar = " + pdf_page.getCropBox().getWidth() + ", LLX = " + pdf_page.getCropBox().getLLX() + ", LLY = " + pdf_page.getCropBox().getLLY() + ", URX = " + pdf_page.getCropBox().getURX() + ", URY = " + pdf_page.getCropBox().getURY()
print "MediaBox : Tinggi = " + pdf_page.getMediaBox().getHeight() + ", Lebar = " + pdf_page.getMediaBox().getWidth() + ", LLX = " + pdf_page.getMediaBox().getLLX() + ", LLY = " + pdf_page.getMediaBox().getLLY() + ", URX = " + pdf_page.getMediaBox().getURX() + ", URY = " + pdf_page.getMediaBox().getURY()
print "TrimBox : Tinggi = " + pdf_page.getTrimBox().getHeight() + ", Lebar = " + pdf_page.getTrimBox().getWidth() + ", LLX = " + pdf_page.getTrimBox().getLLX() + ", LLY = " + pdf_page.getTrimBox().getLLY() + ", URX = " + pdf_page.getTrimBox().getURX() + ", URY = " + pdf_page.getTrimBox().getURY()

print "Rect : Tinggi = " + pdf_page.getRect().getHeight() + ", Lebar = " + pdf_page.getRect().getWidth() + ", LLX = " + pdf_page.getRect().getLLX() + ", LLY = " + pdf_page.getRect().getLLY() + ", URX = " + pdf_page.getRect().getURX() + ", URY = " + pdf_page.getRect().getURY() print "Nomor Halaman :- " + pdf_page.getNumber()
print "Rotasi :-" + pdf_page.getRotate()

```

**Unduh Kode Berjalan**

Unduh **Dapatkan Properti Halaman (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetPageProperties/GetPageProperties.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/GetPageProperties/GetPageProperties.py)