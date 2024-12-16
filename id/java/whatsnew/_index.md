---
title: Apa yang baru
linktitle: Apa yang baru
type: docs
weight: 10
url: /id/java/whatsnew/
description: Halaman ini memperkenalkan fitur baru paling populer di Aspose.PDF untuk Java yang telah diperkenalkan dalam rilis terbaru.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## Apa yang baru di Aspose.PDF 24.8

Sejak 24.8, dukungan untuk format PDF/A-4:

```java

    Document document = new Document(inputPdf);
    // Hanya dokumen PDF-2.x yang dapat dikonversi ke PDF/A-4
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

Juga, adalah mungkin untuk menambahkan teks alternatif untuk Image Stamp:

Properti AlternativeText telah ditambahkan ke ImageStamp - jika sebuah nilai diberikan kepadanya, maka ketika menambahkan ImageStamp ke dokumen, ia memiliki Teks Alternatif.

```java

    String p1_Alt1 = "*** halaman 1, Teks alt 1 ***",
                    p1_Alt2 = "*** halaman 1, Teks alt 2 ***",
                    p2_Alt1 = "--- halaman 1, Teks alt 1 ---",
                    p2_Alt2 = "--- halaman 1, Teks alt 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // Ke halaman 1
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // Ke halaman 2
    document.getPages().add();
    imageStamp.setXIndent(400);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setAlternativeText(p2_Alt1);
    document.getPages().get_Item(2).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p2_Alt2);
    document.getPages().get_Item(2).addStamp(imageStamp);

    // Simpan dokumen
    document.save(outFile);
```


Juga, kode berikut menunjukkan cara menambahkan AlternativeText pada gambar yang ada di FigureElements.

```java

    String inFile = dataDir + "46040.pdf";
    String outFile = dataDir + "46040_1_out.pdf";

    Document document = new Document(inFile);

    ITaggedContent taggedContent = document.getTaggedContent();
    StructureElement rootElement = taggedContent.getRootElement();

    Iterator tmp0 = (rootElement.getChildElements()).iterator();
    while (tmp0.hasNext())
    {
        com.aspose.pdf.tagged.logicalstructure.elements.Element element = (com.aspose.pdf.tagged.logicalstructure.elements.Element)tmp0.next();
        if (element instanceof com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)
                {
            com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figureElement = (com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)element;

            // Atur Teks Alternatif
            figureElement.setAlternativeText("Teks alternatif gambar (teknik 1)");
        }
    }

    // Simpan dokumen
    document.save(outFile);
```


## Apa yang baru di Aspose.PDF 24.7

Sejak rilis 24.7, sebagai bagian dari pengeditan PDF bertanda, metode ditambahkan pada **Aspose.Pdf.LogicalStructure.Element**:

- Tag (menambahkan tag ke operator spesifik seperti gambar, teks, dan tautan)
- InsertChild
- RemoveChild
- ClearChilds

Metode-metode ini memungkinkan Anda untuk mengedit tag file PDF, misalnya:

```java

    Document document = new Document(dataDir + "test.pdf");

    // Mengambil halaman pertama dari dokumen.
    Page page = document.getPages().get_Item(1);

    // Inisialisasi variabel untuk menampung elemen BDC (Begin Dictionary Context) untuk tujuan yang berbeda.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // Iterasi melalui konten halaman.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // Dapatkan operator saat ini dari konten halaman.
        Operator op = page.getContents().get_Item(i);

        // Periksa apakah operator adalah instance dari BDC.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // Cast operator ke tipe BDC.
        if (bdc != null)
        {
            // Periksa apakah MCID (Mark Content Identifier) dari BDC adalah 0.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // Simpan BDC untuk penggunaan selanjutnya.
            }
        }
    }

    // Periksa apakah operator adalah instance dari Do (Draw Object).
    if (op instanceof Do) {
        Do doXobj = (Do)op; // Cast operator ke tipe Do.
        if (doXobj != null)
        {
            // Buat BDC baru untuk gambar dan masukkan ke dalam konten halaman.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // Masukkan sebelum operator saat ini.
            i++; // Tingkatkan indeks untuk memperhitungkan BDC yang dimasukkan.
            page.getContents().insert(i + 1, new EMC()); // Masukkan EMC (End Mark Content).
            i++; // Tingkatkan indeks lagi.
        }
    }

    // Periksa apakah operator adalah instance dari TextShowOperator (untuk tampilan teks).
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // Cast operator ke tipe TextShowOperator.
        if (tx != null)
        {
            // Periksa konten teks tertentu dan masukkan BDC yang sesuai.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // Masukkan sebelum operator saat ini.
                i++; // Tingkatkan indeks.
                page.getContents().insert(i + 1, new EMC()); // Masukkan EMC.
                i++; // Tingkatkan indeks.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // Masukkan sebelum operator saat ini.
                i++; // Tingkatkan indeks.
                page.getContents().insert(i + 1, new EMC()); // Masukkan EMC.
                i++; // Tingkatkan indeks.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // Masukkan sebelum operator saat ini.
                i++; // Tingkatkan indeks.
                page.getContents().insert(i + 1, new EMC()); // Masukkan EMC.
                i++; // Tingkatkan indeks.
            }
        }
    }
}
 
    // Mengambil konten bertanda dari dokumen.
    ITaggedContent tagged = document.getTaggedContent();

    // Memproses konten bertanda untuk memodifikasi atribut struktur.
    // Dapatkan elemen anak pertama dari elemen root dalam konten bertanda.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // Hapus elemen anak yang ada.

    // Tag helloBdc dengan elemen struktur induk.
    MCRElement mcr = p.tag(helloBdc);

    // Buat dan atur atribut struktur untuk elemen bertanda.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // Atur atribut jarak setelah.
    attrs.setAttribute(attr); // Terapkan atribut ke struktur.

    // Buat elemen FigureElement baru dalam konten bertanda.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // Masukkan elemen figure pada posisi kedua.
    figure.setAlternativeText("A fly."); // Atur teks alternatif untuk gambar.

    // Tag imageBdc dengan elemen gambar.
    MCRElement mcr = figure.tag(imageBdc);

    // Mengambil elemen struktur induk dari MCR (Marked Content Reference) yang ditentukan
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Buat atribut struktur baru untuk jarak setelah elemen
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // Atur nilai jarak setelah menjadi 3.625 unit
    attrs.setAttribute(spaceAfter); // Berikan atribut jarak setelah ke atribut struktur

    // Buat atribut struktur baru untuk kotak batas (BBox)
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // Atur nilai kotak batas untuk atribut struktur
    attrs.setAttribute(bbox); // Berikan atribut kotak batas ke atribut struktur

    // Buat atribut struktur baru untuk penempatan
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // Atur tipe penempatan ke blok
    attrs.setAttribute(placement); // Berikan atribut penempatan ke atribut struktur

    // Mengambil elemen anak keempat dari elemen root dari struktur bertanda
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // Hapus elemen anak yang ada dari p2

    // Buat elemen SpanElement baru untuk ditambahkan ke p2
    SpanElement span1 = tagged.createSpanElement();

    // Buat atribut struktur untuk elemen span
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Buat atribut struktur baru untuk tipe dekorasi teks
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Atur dekorasi teks menjadi garis bawah
    attrs.setAttribute(textDecorationType); // Berikan atribut tipe dekorasi teks ke atribut struktur

    // Buat atribut struktur baru untuk ketebalan dekorasi teks
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // Atur ketebalan dekorasi teks menjadi 0
    attrs.setAttribute(textDecorationThickness); // Berikan atribut ketebalan dekorasi teks ke atribut struktur

    // Buat atribut struktur baru untuk warna dekorasi teks
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // Atur nilai warna RGB untuk dekorasi teks
    attrs.setAttribute(textDecorationColor); // Berikan atribut warna dekorasi teks ke atribut struktur

    p2.appendChild(span1); // Tambahkan elemen span1 ke p2


    // Buat elemen MCR baru dan tag dengan pBdc
    MCRElement mcr = p2.tag(pBdc);
    // Mengambil elemen struktur induk dari MCR dan buat atribut tata letak
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Buat atribut struktur baru untuk perataan teks
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // Atur perataan teks menjadi tengah
    attrs.setAttribute(textAlign); // Berikan atribut perataan teks ke atribut struktur

    // Buat atribut struktur baru untuk jarak setelah elemen
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // Atur nilai jarak setelah menjadi 21.75 unit
    attrs.setAttribute(spaceAfter); // Berikan atribut jarak setelah ke atribut struktur


    // Buat elemen SpanElement baru untuk ditambahkan ke p2
    SpanElement span2 = tagged.createSpanElement();

    // Buat atribut struktur untuk elemen span
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Buat atribut struktur baru untuk tipe dekorasi teks
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Atur dekorasi teks menjadi garis bawah
    attrs.setAttribute(textDecorationType); // Berikan atribut tipe dekorasi teks ke atribut struktur

    // Buat atribut struktur baru untuk warna dekorasi teks menggunakan kunci yang ditentukan.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // Atur nilai nomor array untuk atribut warna dekorasi teks.
    // Warna diwakili dalam array nilai RGB, di mana setiap nilai adalah Double.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // Komponen Merah
    new Double[] { (0.384308) },  // Komponen Hijau
    new Double[] { (0.756866) }   // Komponen Biru
    });

    // Atur atribut warna dekorasi teks ke objek attrs.
    attrs.setAttribute(textDecorationColor);

    // Tambahkan elemen span anak ke elemen induk p2.
    p2.appendChild(span2);

    // Buat instance LinkElement baru untuk tautan kedua.
    LinkElement link2 = tagged.createLinkElement();

    // Berikan ID unik untuk elemen tautan menggunakan UUID yang dihasilkan secara acak.
    link2.setId(UUID.randomUUID().toString());

    // Tambahkan elemen link2 sebagai anak dari span2.
    span2.appendChild(link2);

    // Tag elemen link2 dengan anotasi yang sesuai dari anotasi halaman.
    link2.tag(page.getAnnotations().get_Item(1));

    // Tag elemen link2 dengan metadata atau konteks tambahan (link2Bdc).
    link2.tag(link2Bdc);

    // Buat instance LinkElement lain untuk tautan pertama.
    LinkElement link1 = tagged.createLinkElement();

    // Berikan ID unik untuk elemen link1 menggunakan UUID yang dihasilkan secara acak.
    link1.setId(UUID.randomUUID().toString());

    // Tambahkan elemen link1 sebagai anak dari span1.
    span1.appendChild(link1);

    // Tag elemen link1 dengan anotasi yang sesuai dari anotasi halaman.
    link1.tag(page.getAnnotations().get_Item(2));

    // Tag elemen link1 dengan metadata atau konteks tambahan (link1Bdc).
    link1.tag(link1Bdc);

    // Hapus elemen anak pertama dari elemen root dari dokumen bertanda.
    tagged.getRootElement().removeChild(0);

    // Simpan dokumen ke direktori output yang ditentukan dengan nama file "_out.pdf".
    document.save(dataDir + "_out.pdf");

```


## Apa yang baru di Aspose.PDF 24.6

Sejak 24.6 Aspose.PDF untuk Java memungkinkan penandatanganan PDF dengan java.security.cert.X509Certificate, java.security.PrivateKey:

Kode ini mengambil sertifikat dan kunci pribadi dari toko sertifikat dan kemudian menggunakannya untuk menerapkan tanda tangan digital pada halaman pertama dokumen PDF.

```java

    KeyStore trustStore = KeyStore.getInstance("Windows");
    trustStore.load(null, null);
    java.security.cert.X509Certificate certificate = (java.security.cert.X509Certificate) trustStore.getCertificate("ProfMoriarty");
    PrivateKey key = (PrivateKey) trustStore.getKey("ProfMoriarty", null);

    PdfFileSignature pdfSign = new PdfFileSignature(getInputPdf());
    Signature signature = new ExternalSignature(certificate, key);
    pdfSign.sign(1, "reasonTest", "contactTest", "locationTest", true, new java.awt.Rectangle(1, 691, 100, 100), signature);

    pdfSign.save("PDFJAVA.pdf");
    pdfSign.close();
```

## Apa yang baru di Aspose.PDF 24.5

 Sejak rilis 24.5, Plugin Editor Form telah diimplementasikan.

**Cara Mengedit Formulir dalam PDF menggunakan Editor Formulir**

- Setel kunci lisensi Anda
- Buat instance dari kelas FormEditor, yang menyediakan metode untuk memanipulasi formulir PDF
- Buat instance dari kelas FormEditorAddOptions, yang menentukan opsi untuk menambahkan bidang formulir ke dokumen PDF
- Tambahkan sumber file input dan sumber file output ke objek FormEditorAddOptions, menggunakan kelas FileDataSource yang mewakili jalur file atau stream
- Panggil metode Process dari objek FormEditor, dengan melewatkan objek FormEditorAddOptions sebagai parameter
- Akses hasil menggunakan ResultContainer.resultCollection

```java

    // Tentukan jalur input dan output untuk file PDF.
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // Buat instance dari plugin FormEditor.
    FormEditor pdfFormPlugin = new FormEditor();

    // Buat opsi untuk menambahkan bidang formulir.
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // Buat bidang formulir kotak teks.
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // Buat bidang formulir kotak kombo.
    FormComboBoxFieldCreateOptions tmp2 = new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 800, 350, 815));

    tmp2.setColor(com.aspose.pdf.Color.getRed());
    tmp2.setEditable(new Boolean[]{true});
    tmp2.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    ArrayList<String> list1 = new ArrayList<String>();
    list1.add("p1");
    list1.add("p2");
    list1.add("p3");
    tmp2.setOptions(list1);
    tmp2.setSelected(new Integer[]{2});
    tmp2.setPartialName("ComboBoxField");
    options.add(tmp2);

    // Buat bidang formulir kotak centang.
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // Buat bidang formulir kotak centang.
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // Buat bidang formulir kotak centang.
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // Tambahkan file input dan output ke opsi.
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // Proses bidang formulir menggunakan plugin.
    ResultContainer results = pdfFormPlugin.process(opt);
```


Rilis ini memungkinkan kita untuk bekerja dengan lapisan PDF. Sebagai contoh:

- mengunci lapisan PDF
- mengekstrak elemen lapisan PDF
- meratakan PDF berlapis
- menggabungkan Semua Lapisan di dalam PDF menjadi satu

**Mengunci lapisan PDF**

Sejak rilis 24.5, Anda dapat membuka PDF, mengunci lapisan tertentu pada halaman pertama, dan menyimpan dokumen dengan perubahan tersebut. Ada dua metode baru dan satu properti yang ditambahkan:

Layer.Lock(); - Mengunci lapisan.
Layer.Unlock(); - Membuka kunci lapisan.
Layer.Locked; - Properti, menunjukkan keadaan terkunci lapisan.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**Mengekstrak elemen lapisan PDF**

Perpustakaan Aspose.PDF untuk Java memungkinkan ekstraksi setiap lapisan dari halaman pertama dan menyimpan setiap lapisan ke file terpisah.

Untuk membuat PDF baru dari lapisan, cuplikan kode berikut dapat digunakan:

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**Meratakan PDF Berlapis**

Aspose.PDF untuk pustaka Java membuka PDF, mengiterasi setiap lapisan pada halaman pertama, dan meratakan setiap lapisan, membuatnya permanen pada halaman.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

Metode Layer.flatten(boolean cleanupContentStream) menerima parameter boolean yang menentukan apakah akan menghapus penanda grup konten opsional dari aliran konten. Menyetel parameter cleanupContentStream ke false mempercepat proses perataan.

**Menggabungkan Semua Lapisan di dalam PDF menjadi satu**

Aspose.PDF untuk pustaka Java memungkinkan penggabungan baik semua lapisan PDF atau lapisan tertentu pada halaman pertama menjadi lapisan baru dan menyimpan dokumen yang diperbarui.

Dua metode ditambahkan untuk menggabungkan semua lapisan pada halaman:

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

Parameter kedua memungkinkan penamaan ulang penanda grup konten opsional. Nilai default adalah "oc1" (/OC /oc1 BDC).

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // Atau page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## Apa yang baru di Aspose.PDF 24.4

Rilis ini memperkenalkan plugin Java untuk PDF:

- Plugin Penghalus Formulir

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // Periksa hasil.
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- Pengekspor Formulir

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // Penggunaan plugin.
    FormExporter pdfFormPlugin = new FormExporter();
    SelectField selectField = new SelectField() {
      public boolean invoke(Field field) {
        return field instanceof TextBoxField && field.getPageIndex() == 2 && rect.isInclude(field.getRect(), 0);
      }
    };
    FormExporterValuesToCsvOptions opt = new FormExporterValuesToCsvOptions(selectField, ';');

    opt.addInput(new FileDataSource(inputFileNameWithFields));
    opt.addInput(new FileDataSource(getInputPath("document-1.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-2.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-3.pdf")));
    opt.addOutput(new FileDataSource(getOutputPath("out.csv")));
    ResultContainer result = pdfFormPlugin.process(opt);

    // Periksa hasil.
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- Plugin Penggabungan

```java

    String input1 = "sample.pdf";
    String input2 = "sample.pdf";

    String output = "TestMergeFileAndStream_ResultAsFile.pdf";

    Merger merger = new Merger();

    MergeOptions opt = new MergeOptions();
    opt.addInput(new FileDataSource(input1));
    opt.addInput(new StreamDataSource(new FileInputStream(input2)));

    opt.addOutput(new FileDataSource(output));

    ResultContainer results = merger.process(opt);

    System.out.println(results.getResultCollection().size());
    System.out.println(results.getResultCollection().get(0).isFile());
```

- Plugin Optimizer

Bagaimana cara mengurangi ukuran Dokumen PDF?

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

Bagaimana cara mengubah ukuran Dokumen PDF?

```java

    String input = "sample.pdf";
    String output = "ResizeMain.pdf";

    Optimizer organizer = new Optimizer();

    ResizeOptions opt = new ResizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    opt.setPageSize(PageSize.getA1());

    organizer.process(opt);
```


Bagaimana cara memutar Dokumen PDF?

```java

    String input = "sample.pdf";
    String output = "OptimizerRotateMain.pdf";

    Optimizer optimizer = new Optimizer();

    RotateOptions opt = new RotateOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));
    opt.setRotation(Rotation.on90);

    ResultContainer results = optimizer.process(opt);
```

## Apa yang baru di Aspose.PDF 24.3

Mulai dari 24.3 menerapkan pencarian melalui daftar frasa dalam TextFragmentAbsorber.

```java

    String[] expressions = new String[] {
      //mendeteksi nomor telepon
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      //mendeteksi nomor kartu
      "\\b(?:\\d[ -]*?){13,16}\\b"
    };
    Document document = new Document(input);

    TextFragmentCollection newTextFragmentCollection = new TextFragmentCollection();

    Pattern[] regexes = new Pattern[6];
    for (int i = 0; i < expressions.length; i++) {
      regexes[i] = Pattern.compile(expressions[i], Pattern.CASE_INSENSITIVE);
    }
    TextFragmentAbsorber newAbsorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
    document.getPages().accept(newAbsorber);
    HashMap < Pattern, TextFragmentCollection > map = newAbsorber.getRegexResults();
```


Fitur berikutnya adalah menambahkan kemampuan untuk mengonversi tabel untuk konverter PDF ke Markdown

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## Apa yang baru di Aspose.PDF 24.2

Mulai 24.2 dimungkinkan untuk menambahkan Watermark di PDF dengan AcroForms. TextStamp cocok digunakan dengan file AcroForm. Jika Anda menggunakan TextStamp untuk file XFA, teks akan digambar pada halaman seperti pada file PDF biasa (dapat dilihat pada penampil PDF yang tidak dapat membaca file XFA, misalnya pada browser Chrome). Untuk menambahkan teks ke file XFA, itu harus diubah dalam XML internal file XFA.

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Sample Stamp</text>\n" +
    "</value>" +
    "<font typeface=\"Arial\" size=\"14px\" weight=\"bold\" posture=\"italic\">" +
    "<fill>" +
    "<color value=\"0,128,0\"/>" +
    "</fill>" +
    "</font>" +
    "</draw>" +
    "</subform>";

    xfa.appendToTemplate("//tpl:pageArea", watermark);

    pdfDocument.save(targetName);
    pdfDocument.close();
```


Setel StateModel untuk Anotasi
Kita dapat menggunakan setReviewState dan setMarkedState dari kelas MarkupAnnotation untuk menetapkan status yang diperlukan. Semua anotasi markup memiliki opsi Set State yang tersedia.

```java

    // Buka dokumen PDF sumber
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // Buat anotasi
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    //Tetapkan judul anotasi
    textAnnotation.setTitle("Contoh Judul Anotasi");

    //Tetapkan subjek anotasi
    textAnnotation.setSubject("Contoh Subjek");
    //Tentukan isi anotasi
    textAnnotation.setContents("Contoh isi untuk anotasi");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    //Tambahkan anotasi dalam koleksi anotasi di halaman
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    //Simpan file keluaran
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


Dari 24.2 implementasi konversi OFD ke PDF:

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## Apa yang baru di Aspose.PDF 24.1

Dari rilis 24.1 implementasi konversi PDF ke Markdown:

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

Juga, di 24.1 interupsi thread menggunakan InterruptMonitor telah diimplementasikan.

```java

    final InterruptMonitor monitor = new InterruptMonitor();

    new Thread(new Runnable() {

      public void run() {

        InterruptMonitor.setThreadLocalInstance(monitor);
        Document document = new Document();

        try {
          Page page = document.getPages().insert(1);
          PageInfo pageInfo = page.getPageInfo();
          pageInfo.setLandscape(true);
          Table topicTable = new Table();
          topicTable.setBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setColumnWidths("5% 10% 5% 60% 10% 10%");
          topicTable.setRepeatingRowsCount(1);

          Row topicRow = topicTable.getRows().add();

          topicRow.getCells().add("teks");
          topicRow.getCells().add("teks");
          topicRow.getCells().add("teks");
          topicRow.getCells().add("teks");
          topicRow.getCells().add("teks");
          topicRow.getCells().add("teks");

          //konversi pernyataan foreach ke while
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("teks");
          row2.getCells().add("teks");
          row2.getCells().add("teks");
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
          row2.getCells().add(LongText);
          row2.getCells().add("teks");
          row2.getCells().add("teks");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("Menginterupsi thread simpan pada " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("Proses dimulai thread pada " + System.currentTimeMillis());

    // Timeout harus kurang dari waktu yang dibutuhkan untuk menyimpan dokumen sepenuhnya (tanpa interupsi).
    Thread.sleep(500);

    // Interupsi proses
    monitor.interrupt();

    System.out.println("Menginterupsi thread simpan pada " + System.currentTimeMillis());
```


## Apa yang baru di Aspose.PDF 23.12

Formulir dapat ditemukan dan teks dapat diganti menggunakan cuplikan kode berikut:

```java

    Document document = new Document(input);
    String expectedText = "Ini adalah teks yang ditambahkan saat membuat PDF baru di Kofx Power PDF Standard.";

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
      XForm form = (XForm) tmp0.next();
      if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(form);

        Iterator tmp1 = (absorber.getTextFragments()).iterator();
        while (tmp1.hasNext()) {
          TextFragment fragment = (TextFragment) tmp1.next();
          fragment.setText("");
        }
      }
    }

    document.save(output);
```            

Atau, formulir dapat dihapus sepenuhnya:

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    // konversi pernyataan foreach ke while
    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
        XForm form = (XForm) tmp0.next();
        if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
            String name = forms.getFormName(form);
            forms.delete(name);
        }
    }

    document.save(output);
```


Varian lain untuk menghapus formulir:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    for (int i = 1; i <= forms.size(); i++) {
        if ("Typewriter".equals(forms.get_Item(i).getIT()) && "Form".equals(forms.get_Item(i).getSubtype())) {
            forms.delete(forms.get_Item(i).getName());
        }
    }

    document.save(output);
``` 

- Semua formulir dapat dihapus menggunakan potongan kode berikut:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## Apa yang baru di Aspose.PDF 23.11

Mulai rilis ini dimungkinkan untuk menghapus teks tersembunyi dari file PDF:

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    //konversi pernyataan foreach ke while
    Iterator tmp0 = (textAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext()) {
            TextFragment fragment = (TextFragment) tmp0.next();
            if (fragment.getTextState().isInvisible()) {
                result.append(fragment.getText());
                fragment.setText("");
            }
        }

    document.save(outputFile);
```


## Apa Yang Baru di Aspose.PDF 23.10

Pembaruan saat ini menyajikan tiga versi Penghapusan tag dari PDF bertanda.

- Hapus beberapa elemen node dari documentElement (elemen pohon akar):

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // Anda juga dapat menghapus structElement itu sendiri
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- Hapus semua tag elemen yang ditandai dari dokumen, tetapi pertahankan elemen struktur:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root= structure.getChildren().get_Item(0);
    Queue<Element> queue = new ArrayDeque<Element>();
    queue.add(root);
    for (Element element : structure.getChildren() ) {
        queue.add(element);
        for (Element child : element.getChildren())
        {
            queue.add(child);
        }
    }
    for (Element element:queue ) {
        if (element instanceof TextElement  || element instanceof FigureElement)
            element.remove();
    }
    document.save(outputPath);
```


- Hapus tag sama sekali:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

Kami telah mengimplementasikan fitur baru untuk mengukur tinggi karakter. Gunakan kode berikut untuk mengukur tinggi karakter:

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

Perhatikan bahwa pengukuran didasarkan pada font yang tertanam dalam dokumen. Jika ada informasi untuk ukuran yang hilang, metode ini mengembalikan 0.

## Apa yang baru di Aspose.PDF 23.9

Dari 23.9 dukungan untuk menghapus anotasi anak dari bidang yang dapat diisi.

contoh 1:

```java

    String input = "55343_1.pdf";
    Document doc = new Document(input);
    final String fieldName = "1 Vehicle Identification Number";
    Field field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
    Rectangle rect = field.getRect();
    doc.getForm().addFieldAppearance(field, 2, rect);
    System.out.println(2 == field.size());

    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(2 == field.size());
    doc.getForm().removeFieldAppearance(field, 1);

    System.out.println(0 == field.size());
    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
```


example 2:

```java

    {
    String option1 = "opsi 1";
    String option2 = "opsi 2";
    String outputPdf = "output.pdf";

    final Document document = new Document();
    try /*JAVA: sedang menggunakan*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // Tetapkan nilai opsi grup kotak centang pertama
        checkbox.setExportValue(option1);
        checkbox.addOption(option2);
        document.getForm().add(checkbox);
        java.util.List < String > tmp0 = new ArrayList < String > ();
        tmp0.add("Off");
        tmp0.add(option1);
        tmp0.add(option2);
        System.out.println(collectionAssert_AreEqual(tmp0, checkbox.getAllowedStates()));
        checkbox.setValue(option2);

        WidgetAnnotation f = document.getForm().get_Item(1);
        document.getForm().removeFieldAppearance((Field) f, 2);

        checkbox = (CheckboxField) document.getForm().get_Item(1);
        java.util.List < String > tmp1 = new java.util.ArrayList < String > ();
        tmp1.add("Off");
        tmp1.add(option1);
        System.out.println(collectionAssert_AreEqual(tmp1, checkbox.getAllowedStates()));

        document.save(outputPdf);
    } finally {
        if (document != null)(document).close();
    }
    }
    public static boolean collectionAssert_AreEqual(java.util.List < String > value1,
    java.util.List < String > value2) {
    if (value1.size() == value2.size()) {
        for (int i = 0; i < value1.size(); i++) {
        if (!value1.get(i).equals(value2.get(i)))
            return false;
        }
    } else {
        return false;
    }
    return true;
    }
```


Menambahkan gambar dengan ImageFilterType.Flate tidak menjaga transparansi.

```java

    Document document = new Document();
    Page page = document.getPages().add();

    FileInputStream stream = new FileInputStream(("55037_1.png"));

    page.getResources().getImages().addWithImageFilterType(stream, ImageFilterType.Flate);
    page.getContents().add(new GSave());
    Rectangle rectangle = new Rectangle(413, 428, 548, 564);
    Matrix matrix = new Matrix(
      new double[] {
        rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY()
      });

    page.getContents().add(new ConcatenateMatrix(matrix));
    XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
    page.getContents().add(new Do(ximage.getName()));
    page.getContents().add(new GRestore());
    document.save(getOutputPath("55157.pdf"));
    stream.close();
```

## Apa yang baru di Aspose.PDF 23.8

Fungsi untuk mendeteksi Pembaruan Inkremental dalam dokumen PDF telah ditambahkan pada 23.8. Fungsi ini mengembalikan 'true' jika dokumen disimpan dengan pembaruan inkremental, jika tidak, fungsi ini mengembalikan 'false'.

```java

    Document doc = new Document(dataDir+"PDF_Support_Tech_Note.pdf");
    boolean not_updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(not_updatedIncrementally);

    doc.getPages().add();
    doc.saveIncrementally(dataDir+"PDF_updatedIncrementally.pdf");

    doc = new Document(dataDir+"PDF_updatedIncrementally.pdf");
    boolean updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(updatedIncrementally);
    doc.close();
```    

Satu fitur lagi adalah Menyalin OutputIntents dari PDF input ke PDF tujuan

Kami menambahkan properti publik baru Document.getOutputIntents() untuk memungkinkan akses ke output intents dalam sebuah dokumen. Untuk sementara waktu hanya penggunaan output intents yang sudah ada dalam beberapa dokumen yang didukung, pengguna tidak dapat membuat OutputIntent dari awal.

```java

    Document document1 = new Document(dataDir+"pdfa.pdf");
    Document resultDocument = new Document();
    resultDocument.getPages().add(document1.getPages());

    for (OutputIntent intent : document1.getOutputIntents())
    {
        resultDocument.getOutputIntents().addItem(intent);
    }

    resultDocument.save(dataDir+"resultpath.pdf");
```  


Dari dukungan Aspose.PDF 23.8 untuk menambahkan ekstraksi bentuk:

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    //konversi pernyataan foreach ke while
    Iterator tmp0 = ( tfAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext())
        {
            TextFragment textFragment = (TextFragment)tmp0.next();
            System.out.println(textFragment.getText());
            addTextImproved(destPage, textFragment);
        }

    ImagePlacementAbsorber imageAbsorber = new ImagePlacementAbsorber();
    imageAbsorber.visit(source);

    Iterator tmp1 = ( imageAbsorber.getImagePlacements()).iterator();
        while (tmp1.hasNext())
        {
            ImagePlacement image = (ImagePlacement)tmp1.next();
            destPage.addImage(image.getImage().toStream(), image.getRectangle());
        }

    GraphicsAbsorber vectorAbsorber = new GraphicsAbsorber();
    vectorAbsorber.visit(source.getPages().get_Item(1));
    Rectangle area = new Rectangle(90, 250, 300, 400);
    dest.getPages().get_Item(1).addGraphics(vectorAbsorber.getElements(), area);
    dest.save(getOutputPath("46298-out.pdf"));
    }

    private static void addTextImproved(Page page, TextFragment textFragment)
    {
        TextFragment local = new TextFragment();
        local.setPosition(textFragment.getPosition());

        // Hitung ulang posisi baru karena ukuran halaman berbeda dengan PDF asli
        local.getPosition().setXIndent(textFragment.getPosition().getXIndent());//2.5 * 72;
        double newPageHeight = page.getPageRect(true).getHeight();
        double oldPageHeight = textFragment.getPage().getPageRect(true).getHeight();
        local.getPosition().setYIndent(textFragment.getPosition().getYIndent());

        local.setText(textFragment.getText());
        local.getTextState().setFont(textFragment.getTextState().getFont());
        local.getTextState().setFontSize(textFragment.getTextState().getFontSize());

        local.getTextState().setFormattingOptions(textFragment.getTextState().getFormattingOptions());
        local.getTextState().setForegroundColor(textFragment.getTextState().getForegroundColor());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(local);
    }
```


Juga mendukung kemampuan untuk mendeteksi Overflow saat menambahkan teks:

```java

    Document doc = new Document();
    String paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    Rectangle rectangle = new Rectangle(100, 600, 500, 700, false);
    TextParagraph paragraph = new TextParagraph();
    TextFragment fragment = new TextFragment(paragraphContent);
    paragraph.setVerticalAlignment(VerticalAlignment.Top);
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    paragraph.setRectangle(rectangle);
    boolean isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.getTextState().setFontSize(fragment.getTextState().getFontSize() - 0.5f);
        isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    }
    paragraph.appendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.getPages().add());
    builder.appendParagraph(paragraph);
    doc.save(output);
```


## Apa yang baru di Aspose.PDF 23.7

Dari versi 23.7 mendukung Pengaturan Cetak Dialog Preset Skala Halaman:

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## Apa yang baru di Aspose.PDF 23.6

Dari versi 23.6 mendukung penambahan kemampuan untuk mengatur judul halaman HTML, Epub.

kode untuk HTML:

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>HALAMAN & JUDUL BARU</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


code untuk EPUB:

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>HALAMAN BARU & JUDUL</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

Dari dukungan 23.6 untuk menyediakan API untuk memposisikan grafik vektor:

```java

    Document document = new Document(input);
    VectorGraphicsAbsorber vectorAbsorber = new VectorGraphicsAbsorber();
    vectorAbsorber.visit(document.getPages().get_Item(1));

    SubPath subPath1 = vectorAbsorber.getSubPaths().get_Item(2);
    SubPath subPath2 = vectorAbsorber.getSubPaths().get_Item(3);
    SubPath subPath3 = vectorAbsorber.getSubPaths().get_Item(4);

    Point point1 = new Point(subPath1.getPosition().getX() + 200, subPath1.getPosition().getY() - 100);
    Point point2 = new Point(subPath2.getPosition().getX() + 200, subPath2.getPosition().getY() - 100);
    Point point3 = new Point(subPath3.getPosition().getX() + 200, subPath3.getPosition().getY() - 100);

    subPath1.setPosition(point1);
    subPath2.setPosition(point2);
    subPath3.setPosition(point3);

    document.save(output);
```

## Apa yang baru di Aspose.PDF 23.1

Dari versi 23.1 mendukung untuk membuat anotasi PrinterMark. Ditambahkan salah satu varian anotasi: ColorBarAnnotation.

```java

    Document doc = new Document();
    Page page = doc.getPages().add();
    page.setTrimBox(new com.aspose.pdf.Rectangle(20, 20, 580, 820));
    Rectangle rectBlack = new com.aspose.pdf.Rectangle(100, 300, 300, 320);
    Rectangle rectCyan = new com.aspose.pdf.Rectangle(200, 600, 260, 690);
    Rectangle rectMagenta = new com.aspose.pdf.Rectangle(10, 650, 140, 670);

    ColorBarAnnotation colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    ColorBarAnnotation colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    ColorBarAnnotation colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.setColorOfCMYK(ColorsOfCMYK.Magenta);
    ColorBarAnnotation colorBarYellow = new ColorBarAnnotation(page, new com.aspose.pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.getAnnotations().add(colorBarBlack);
    page.getAnnotations().add(colorBarCyan);
    page.getAnnotations().add(colorBaMagenta);
    page.getAnnotations().add(colorBarYellow);
    doc.save("outFile.pdf");
```


## Apa yang baru di Aspose.PDF 22.12

Dari rilis ini mendukung konversi PDF ke Gambar DICOM:

```java
    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## Apa yang baru di Aspose.PDF 22.9

Dari 22.09 mendukung penambahan properti untuk mengubah urutan rubrik subjek (E=, CN=, O=, OU=) ke dalam tanda tangan.

```java
    String inputPdf = getInputPath("input.pdf");
    String inputPfx = getInputPath("input.pfx");
    String outputPdf = getOutputPath("out.pdf");

    final PdfFileSignature fileSign = new PdfFileSignature();
    try 
    {
        fileSign.bindPdf(inputPdf);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 400, 100);
        PKCS7Detached signature = new PKCS7Detached(inputPfx, "123456789");
        signature.setDate(new Date());
        signature.setCustomAppearance(new SignatureCustomAppearance());
        signature.getCustomAppearance().setUseDigitalSubjectFormat(true);
        signature.getCustomAppearance().setDigitalSubjectFormat(new /*SubjectNameElements*/int[] { SubjectNameElements.CN, SubjectNameElements.O });

        fileSign.sign(1, true, rect, signature);
        fileSign.save(outputPdf);
    }
    finally { 
        if (fileSign != null) 
            fileSign.close(); 
    }
```

## Apa yang baru di Aspose.PDF 22.8

Dari Aspose.PDF 23.8 dukungan untuk menambahkan metode untuk membangun kembali tabel xref:

```java

    PdfFileSanitization sanitizer = new PdfFileSanitization();
    try {
        sanitizer.bindPdf(dataDir + "50528_1.pdf");
        sanitizer.rebuildXrefAndTrailer();
        sanitizer.save(dataDir + "50528_1" + version + ".pdf");
    } finally {
        if (sanitizer != null) ( sanitizer).close();
    }
```

## Apa yang baru di Aspose.PDF 22.6

PDF ke PDF_A_1A - menerapkan opsi untuk menghapus warna transparansi untuk menghindari ukuran file keluaran yang besar.

Dari versi 22.5 pelanggan dapat mengontrol kualitas transparansi yang dikonversi, dan ukuran file keluaran sebagai hasilnya:

```java
    opts.setTransparencyResolution(300);
```

## Apa yang baru di Aspose.PDF 22.5

Selama konversi PDF/A konten transparan dihapus dan diganti dengan gambar. Kami telah menerapkan fitur baru, dan sekarang pelanggan dapat mengontrol kualitas gambar dengan parameter TransparencyResolution:

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## Apa yang baru di Aspose.PDF 22.4

Rilis ini mencakup informasi untuk Aspose.PDF untuk Java:

- PDF ke ODS: Mengenali teks dalam subskrip dan superskrip;

**contoh**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF ke XMLSpreadSheet2003: Mengenali teks dalam subskrip dan superskrip;

- PDF ke Excel: Mengenali teks dalam subskrip dan superskrip;

## Apa yang baru di Aspose.PDF 22.3

PDF ke ODS: Dukungan untuk RTL tersedia dalam versi 22.3

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## Apa yang baru di Aspose.PDF 22.2

Rilis ini mencakup PDF ke XSLX: Dukungan untuk RTL (Ibrani, Arab).

## Apa yang baru di Aspose.PDF 22.1

Aspose.PDF untuk Java memungkinkan memuat dokumen Portable Document Format (PDF) versi 2.0.

## Apa yang baru di Aspose.PDF 21.10

### Bagaimana cara mendeteksi teks tersembunyi?

Silakan gunakan kode berikut:

```java

Document pdf = new Document(inFile);
        Page page = pdf.getPages().get_Item(1);
        TextFragmentAbsorber textFragmentAbsorber = new com.aspose.pdf.TextFragmentAbsorber();
        page.accept(textFragmentAbsorber);
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

        int fragmentsCount = textFragmentAbsorber.getTextFragments().size();
        int invisibleCount = 0;

        Iterator tmp0 = ( textFragmentCollection).iterator();
            while (tmp0.hasNext())
            {
                com.aspose.pdf.TextFragment fragment = (com.aspose.pdf.TextFragment)tmp0.next();
                System.out.println(fragment.getText());
                System.out.println(fragment.getTextState().isInvisible());
                if (fragment.getTextState().isInvisible())
                    invisibleCount++;
            }
```


## Apa yang baru di Aspose.PDF 21.8

### Bagaimana cara mengubah warna teks dalam Tanda Tangan Digital?

Dalam versi 21.8, setForegroundColor, memungkinkan mengubah warna teks dalam Tanda Tangan Digital:

```java
Silakan, gunakan kode berikut:

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    //buat persegi panjang untuk lokasi tanda tangan
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
//atur warna teks
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // menandatangani file PDF
                    pdfSign.sign(1, true, rect, pkcs);
                    //simpan file PDF output
                    pdfSign.save(outFile);
```

## Apa yang baru di Aspose.PDF 21.6

### Menyembunyikan gambar menggunakan ImagePlacementAbsorber dari dokumen

Dengan Aspose.PDF untuk Java, Anda dapat menyembunyikan gambar menggunakan ImagePlacementAbsorber dari dokumen:

```java
      Document doc = new Document("input.pdf");

        for (Page page : doc.getPages()) {
            ImagePlacementAbsorber ipa = new ImagePlacementAbsorber();
            ipa.visit(page);
            for (ImagePlacement ip : ipa.getImagePlacements()) {
                ip.hide();
            }
        }

        doc.save("out.pdf");
```

## Apa yang baru di Aspose.PDF 21.5

### Tambahkan API untuk menggabungkan gambar

Aspose.PDF 21.4 memungkinkan Anda untuk menggabungkan Gambar. Menggabungkan daftar aliran gambar sebagai satu aliran gambar. Format keluaran Png/jpg/tiff didukung, dalam kasus menggunakan format yang tidak didukung, aliran keluaran akan dienkode sebagai Jpeg secara default. Ikuti cuplikan kode berikut:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile300dpi = new FileInputStream("image1.jpg");
        try  {
            inputImagesStreams.add(inputFile300dpi);
            InputStream inputFile600dpi = new FileInputStream("image2.jpg");
            try {
                inputImagesStreams.add(inputFile600dpi);
                inputStream = PdfConverter.mergeImages(
                        inputImagesStreams,
                        com.aspose.pdf.ImageFormat.Jpeg,
                        ImageMergeMode.Vertical,
                        new Integer(1),
                        new Integer(1)
                );
            } finally {
                if (inputFile600dpi != null) (inputFile600dpi).close();
            }
        } finally {
            if (inputFile300dpi != null) (inputFile300dpi).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out.pdf");
        inputStream.close();
```


Juga Anda dapat menggabungkan gambar Anda sebagai format Tiff:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile1 = new FileInputStream("1.tif");
        try  {
            inputImagesStreams.add(inputFile1);
            InputStream inputFile2 = new FileInputStream("2.tif");
            try {
                inputImagesStreams.add(inputFile2);
                inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
            } finally {
                if (inputFile2 != null) (inputFile2).close();
            }
        } finally {
            if (inputFile1 != null) (inputFile1).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out2.pdf");
        inputStream.close();
```

## Apa yang baru di Aspose.PDF 21.02

Aspose.PDF v21.02 Tanda Tangani PDF dengan Tanda Tangan PAdES LTV

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //Tanda tangani PDF dengan Tanda Tangan PAdES LTV
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```