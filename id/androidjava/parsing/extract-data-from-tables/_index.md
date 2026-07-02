---
title: Ekstrak Data Tabel dari PDF
linktitle: Ekstrak Data Tabel
type: docs
weight: 40
url: /id/androidjava/extract-data-from-table-in-pdf/
description: Pelajari cara mengekstrak data tabel dari PDF menggunakan Aspose.PDF untuk Android via Java.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak Tabel dari PDF secara programatik

Mengekstrak tabel dari PDF bukanlah tugas yang sederhana karena tabel dapat dibuat dengan berbagai cara.

Aspose.PDF untuk Android via Java memiliki alat yang memudahkan pengambilan tabel. Untuk mengekstrak data tabel, Anda harus melakukan langkah-langkah berikut:

1. Buka dokumen - buat sebuah [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objek;
1. Buat sebuah [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber) objek.
1. Tentukan halaman mana yang akan dianalisis dan terapkan [kunjungi](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) ke halaman yang diinginkan. Data tabel akan dipindai, dan hasilnya akan disimpan dalam daftar [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Kami dapat memperoleh daftar ini melalui [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) metode.
1. Untuk mendapatkan data, lakukan iterasi melalui `TableList` dan menangani daftar [baris yang diserap](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) dan daftar sel yang diserap. Kami dapat mengakses daftar pertama dengan memanggil [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) metode dan ke yang kedua dengan memanggil [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).
1. Setiap [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) mengandung [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Anda dapat memprosesnya untuk keperluan Anda sendiri.

Contoh berikut menunjukkan ekstraksi tabel dari semua halaman:

```java
public void extractTable () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();

        File file=new File(fileStorage, "extracted-text.txt");
        FileOutputStream fileOutputStream;

        try {
            fileOutputStream=new FileOutputStream(file);

        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
        // Scan pages
        for (Page page : (Iterable<? extends Page>) document.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                try {
                    bw.write("Table");
                    bw.newLine();
                    // Iterate through list of rows
                    for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                        // Iterate through list of cell
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb=new StringBuilder();
                                for (TextSegment seg :
                                        (Iterable<? extends TextSegment>) fragment.getSegments())
                                    sb.append(seg.getText());
                                bw.write(sb.toString() + "|");
                            }
                        }
                        bw.newLine();
                    }
                } catch (IOException e) {
                    resultMessage.setText(e.getMessage());
                    return;
                }
            }
        }
        try {
            bw.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Ekstrak tabel di area spesifik halaman PDF

Setiap tabel abosorbed memiliki [Rectangle](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) properti yang menggambarkan posisi tabel pada halaman.

Jadi, jika Anda perlu mengekstrak tabel yang berada di wilayah tertentu, Anda harus bekerja dengan koordinat tertentu.

Contoh berikut menunjukkan cara mengekstrak tabel yang ditandai dengan Square Annotation:

```java
public void extractMarkedTable () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.Page page=document.getPages().get_Item(1);

        com.aspose.pdf.AnnotationSelector annotationSelector=
                new com.aspose.pdf.AnnotationSelector(
                        new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

        List list=annotationSelector.getSelected();
        if (list.size() == 0) {
            resultMessage.setText("Marked tables not found..");
            return;
        }

        com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();
        absorber.visit(page);

        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            {
                boolean isInRegion=(squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                        && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                        && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                        && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

                if (isInRegion) {
                    File file=new File(fileStorage, "extracted-text.txt");
                    FileOutputStream fileOutputStream;

                    try {
                        fileOutputStream=new FileOutputStream(file);

                    } catch (FileNotFoundException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }

                    BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
                    try {
                        //Parse table
                        for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                            {
                                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                                    for (com.aspose.pdf.TextFragment fragment :
                                            cell.getTextFragments()) {
                                        bw.write(fragment.getText());
                                    }
                                    bw.write("|");
                                }
                                bw.newLine();
                            }
                        }
                        bw.close();
                        // -------------
                    } catch (IOException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }
                    resultMessage.setText(R.string.success_message);
                }
            }
        }
    }
```

## Ekstrak Data Tabel dari PDF dan simpan ke dalam file CSV

Contoh berikut menunjukkan cara mengekstrak tabel dan menyimpannya sebagai file CSV.
Untuk melihat cara mengonversi PDF ke Spreadsheet Excel, silakan merujuk ke [Konversi PDF ke Excel](/pdf/id/java/convert-pdf-to-excel/) artikel.

```java
 public void extractTableSaveCSV () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "PDFToXLS_out.csv");
        // Instantiate ExcelSave Option object
        com.aspose.pdf.ExcelSaveOptions excelSave=new com.aspose.pdf.ExcelSaveOptions();
        excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);
        try {
            document.save(file.toString(), excelSave);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

