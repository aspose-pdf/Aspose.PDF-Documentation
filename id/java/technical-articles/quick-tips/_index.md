---
title: Tips Cepat
type: docs
weight: 50
url: /id/java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini berisi beberapa tips cepat terkait Aspose.PDF untuk API Java

{{% /alert %}}

## Menambahkan JavaScript ke PDF

Cuplikan kode berikut dapat digunakan untuk menetapkan/menambahkan JavaScript ke file PDF.

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    //Menambahkan JavaScript pada Tingkat Dokumen
    //Instansiasi JavascriptAction dengan pernyataan JavaScript yang diinginkan
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    //Menugaskan objek JavascriptAction ke aksi yang diinginkan dari Dokumen
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    //Menambahkan JavaScript pada Tingkat Halaman
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('dokumen sedang ditutup')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('halaman 1 dibuka')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('halaman 2 dibuka')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('halaman 2 ditutup')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**Beberapa contoh lainnya**

```java

// setelah pencetakan
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('File was printed')"));

// setelah penyimpanan
document.getActions().setAfterSaving(new JavascriptAction("app.alert('File was Saved')"));

```

## Membebaskan Memori yang Digunakan

Jika Anda telah menyelesaikan pekerjaan dengan Aspose.PDF untuk Java dan ingin membersihkan memori dari berbagai instance statis,
untuk memaksimalkan memori untuk proses lain, Anda harus menjalankan baris kode berikut:

```java

 com.aspose.pdf.MemoryCleaner.clear();

```

## Memuat PDF dari ByteArrayInputStream

Cuplikan kode berikut menunjukkan langkah-langkah untuk memuat file PDF ke dalam ByteArray dan kemudian membuat objek Document dengan ByteArrayInputStream.

```java

 // file PDF sumber

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //tidak diragukan di sini adalah 0

        //Menulis len byte dari array byte tertentu mulai dari offset off ke output stream array byte ini.

        System.out.println("membaca " + readNum + " byte,");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// membuat objek Document dengan ByteArrayInputStream sambil melewatkan array byte sebagai argumen

com.aspose.pdf.Document doc = new 
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// mendapatkan jumlah halaman dari file PDF

 System.out.println(doc.getPages().size());

```


## Simpan PDF ke ByteArrayOutputStream

Cuplikan kode berikut menunjukkan langkah-langkah untuk menyimpan file PDF hasil ke dalam ByteArrayOutputStream.

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```