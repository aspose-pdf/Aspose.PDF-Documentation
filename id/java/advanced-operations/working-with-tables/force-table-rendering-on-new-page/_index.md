---
title: Memaksa Perenderan Tabel pada Halaman Baru
type: docs
weight: 20
url: /id/java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## Render Tabel pada Halaman Baru

Secara default, paragraf ditambahkan ke koleksi Paragraf objek Page. Namun, dimungkinkan untuk merender tabel pada halaman baru alih-alih langsung setelah objek tingkat paragraf yang ditambahkan sebelumnya pada halaman.

### Menambahkan Tabel

Untuk merender tabel pada halaman baru, gunakan metode [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) dalam kelas [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph). Cuplikan kode berikut menunjukkan caranya.

```java
public static void RenderTableOnNewPage(){
        Document doc = new Document();
        PageInfo pageInfo = doc.getPageInfo();
        MarginInfo marginInfo = pageInfo.getMargin();

        marginInfo.setLeft (37);
        marginInfo.setRight (37);
        marginInfo.setTop (37);
        marginInfo.setBottom (37);

        pageInfo.setLandscape(true);

        Table table = new Table();
        table.setColumnWidths ("50 100");
        // Halaman ditambahkan.
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("Konten 1"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("HHHHH"));
        }
        Paragraphs paragraphs = curPage.getParagraphs();
        paragraphs.add(table);
        /********************************************/
        Table table1 = new Table();
        table.setColumnWidths ("100 100");
        for (int i = 1; i <= 10; i++)
        {
            Row row = table1.getRows().add();
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("LAAAAAAA"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("LAAGGGGGG"));
        }
        table1.setInNewPage (true);
        // Saya ingin menjaga tabel 1 ke halaman berikutnya, tolong...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

Kelas com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) memungkinkan untuk membuat/menghasilkan tabel dalam dokumen PDF. Fitur serupa juga didukung oleh kelas aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) tetapi kami mendorong pelanggan kami untuk mencoba menggunakan Model Objek Dokumen (DOM) terbaru dari paket com.aspose.pdf, karena semua fitur baru dan penyelesaian masalah dilakukan dalam DOM baru. Namun, Aspose.PDF untuk Java yang lama (paket aspose.pdf) memiliki metode [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) dalam kelas paragraf, sehingga paragraf tersebut dirender di halaman baru. Untuk kompatibilitas mundur, metode [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) telah ditambahkan ke kelas [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph).

{{% /alert %}}