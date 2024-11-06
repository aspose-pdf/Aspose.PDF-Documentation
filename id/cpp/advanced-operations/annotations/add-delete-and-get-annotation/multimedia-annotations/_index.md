---

title: PDF Multimedia Annotation menggunakan C++

linktitle: Multimedia Annotation

type: docs

weight: 40

url: id/cpp/multimedia-annotation/

description: Aspose.PDF untuk C++ memungkinkan Anda menambahkan, mendapatkan, dan menghapus anotasi multimedia dari dokumen PDF Anda.

lastmod: "2021-11-24"

sitemap:

    changefreq: "weekly"

    priority: 0.7

---

Menambahkan video, audio, dan konten interaktif mengubah PDF menjadi alat komunikasi multidimensi yang meningkatkan minat dan keterlibatan dengan dokumen Anda. Konten semacam itu dalam file format PDF disebut Anotasi Multimedia.

Anotasi dalam dokumen PDF terdapat dalam koleksi Anotasi objek [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Koleksi ini hanya berisi semua anotasi untuk halaman tersebut saja: setiap halaman memiliki koleksi Anotasi tersendiri. Untuk menambahkan anotasi ke halaman tertentu, tambahkan ke koleksi Anotasi halaman tersebut menggunakan metode Add.

Gunakan kelas [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation) dalam namespace Aspose.PDF.InteractiveFeatures.Annotations untuk memasukkan file SWF sebagai anotasi dalam dokumen PDF. Sebuah anotasi layar menentukan sebuah wilayah di halaman di mana klip media dapat diputar.

Ketika Anda perlu menambahkan tautan video eksternal dalam dokumen PDF, Anda dapat menggunakan [MovieAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation). Anotasi Film mengandung grafik animasi dan suara untuk ditampilkan pada layar komputer dan melalui speaker.

Sebuah [Sound Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) harus analog dengan anotasi teks kecuali bahwa alih-alih catatan teks, ia berisi suara yang direkam dari mikrofon komputer atau diimpor dari file. Ketika anotasi diaktifkan, suara akan diputar. Anotasi harus berperilaku seperti anotasi teks dalam banyak hal, dengan ikon yang berbeda (secara default, speaker) untuk menunjukkan bahwa itu mewakili suara.

Namun, ketika ada kebutuhan untuk menyematkan media di dalam dokumen PDF, Anda perlu menggunakan [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation).
## Tambahkan Anotasi Layar

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Layar ke file PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // Buat Anotasi Layar
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## Tambahkan Anotasi Suara

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Suara ke file PDF:

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // Buat Anotasi Suara
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"Demo Anotasi Suara");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}

```

## Tambahkan RichMediaAnnotation

Cuplikan kode berikut menunjukkan cara menambahkan RichMediaAnnotation ke file PDF:

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // beri nama pada data video. Data ini akan disematkan ke dalam dokumen dengan nama ini
    // dan dirujuk dari variabel flash dengan nama ini.
    // videoName tidak boleh berisi path ke file; ini lebih merupakan "kunci" untuk mengakses
    // data di dalam dokumen PDF

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // kami juga menggunakan skin untuk pemutar video
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // di sini kita harus menentukan stream yang berisi kode dari pemutar video
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // susun baris variabel flash untuk pemutar. Harap dicatat bahwa pemutar yang berbeda
    // mungkin memiliki format baris variabel flash yang berbeda.
    // Lihat dokumentasi untuk pemutar Anda.
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // tambahkan kode skin.
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // atur poster untuk video
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // atur konten video
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // atur tipe konten (video)
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // aktifkan pemutar dengan klik
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // perbarui data anotasi. Metode ini harus dipanggil setelah semua
    // penugasan/pengaturan. Metode ini menginisialisasi struktur data anotasi
    // dan menyematkan data yang diperlukan.
    rma->Update();

    // tambahkan anotasi pada halaman.
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### Dapatkan MultimediaAnnotation

Silakan coba menggunakan potongan kode berikut untuk mendapatkan MultimediaAnnotation dari dokumen PDF.

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        Console::WriteLine(u"{0} {1}", ma->get_AnnotationType(), ma->get_Rect());
    }
}
```

### Hapus MultimediaAnnotation

Potongan kode berikut menunjukkan cara menghapus MultimediaAnnotation dari file PDF.

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        page->get_Annotations()->Delete(ma);
    }
    document->Save(_dataDir + u"RichMediaAnnotation_del.pdf");
}
```

## Tambah Anotasi 3D

Saat ini, file PDF dapat berisi berbagai konten selain teks dan grafik sederhana, termasuk struktur logis, elemen interaktif seperti anotasi dan bidang formulir, lapisan, multimedia (termasuk konten video), dan objek 3D.

Konten 3D semacam itu dapat dilihat dalam file PDF menggunakan anotasi 3D.

Bagian ini menunjukkan langkah-langkah dasar untuk membuat anotasi 3D dalam dokumen PDF menggunakan pustaka C++ oleh Aspose.PDF.

Anotasi 3D ditambahkan menggunakan model yang dibuat dalam format U3D.

1. Buat [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) baru
1. Muat data model 3D yang diinginkan (dalam kasus kami "Ring.u3d") untuk membuat [PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/)
1. Buat objek [3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/) dan hubungkan ke dokumen dan 3DContent
1. Sesuaikan objek pdf3dArtWork:

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // Muat file PDF
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        //set gambar pratinjau jika diperlukan
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

Dokumen contoh kode ini menunjukkan kepada kita model seperti ini:

![Demo Anotasi 3D](3d_demo.png)


## Tambahkan Anotasi Widget

Anotasi Widget mewakili tampilan bidang formulir dalam formulir PDF interaktif.

Sejak PDF v 1.2 kita bisa menggunakan Anotasi Widget. Ini adalah elemen formulir interaktif yang bisa kita tambahkan ke PDF untuk memudahkan memasukkan, mengirimkan informasi, atau melakukan beberapa tindakan lainnya dengan pengguna. Meskipun widget adalah jenis anotasi khusus, kita tidak dapat membuatnya sebagai anotasi langsung, karena anotasi widget adalah representasi grafis dari bidang formulir pada halaman tertentu.

Setiap bidang formulir untuk setiap lokasi dalam dokumen mewakili satu Anotasi Widget. Data anotasi spesifik lokasi untuk widget ditambahkan ke halaman tertentu. Setiap bidang formulir memiliki beberapa opsi. Sebuah tombol dapat berupa toggle, checkbox, atau tombol. Widget seleksi bisa berupa kotak daftar atau kotak kombo.

Aspose.PDF untuk C++ memungkinkan Anda menambahkan anotasi ini menggunakan kelas [Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/).

Untuk menambahkan tombol ke halaman, kita perlu menggunakan potongan kode berikut:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;

void ExampleWidgetAnnotation::AddButton() {

    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(72, 748, 164, 768);

    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_AlternateName(u"Cetak dokumen saat ini");
    printButton->set_Color(Color::get_Black());
    printButton->set_PartialName(u"printBtn1");
    printButton->set_NormalCaption(u"Cetak Dokumen");

    auto border = MakeObject<Border>(printButton);
    border->set_Style(BorderStyle::Solid);
    border->set_Width(2);

    printButton->set_Border(border);
    printButton->get_Characteristics()->set_Border(System::Drawing::Color::FromArgb(255, 0, 0, 255));
    printButton->get_Characteristics()->set_Background(System::Drawing::Color::FromArgb(255, 0, 191, 255));
    auto wa = System::DynamicCast<Field>(printButton);
    document->get_Form()->Add(wa);

    document->Save(_dataDir + u"sample_widgetannot.pdf");
}
```

### Menggunakan aksi Navigasi-Dokumen

Contoh ini menunjukkan cara membuat 4 tombol:

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"Ke halaman pertama", u"Ke halaman sebelumnya", u"Ke halaman berikutnya", u"Ke halaman terakhir" });
    auto normalCaptions = MakeArray<String>({ u"Pertama", u"Sebelum", u"Berikutnya", u"Terakhir" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// Kita harus membuat tombol tanpa melampirkannya ke halaman.

    for (int i = 0; i < 4; i++) {
        buttons[i] = MakeObject<ButtonField>(document, MakeObject<Rectangle>(32 + i * 80, 28, 104 + i * 80, 68));
        buttons[i]->set_AlternateName(alternateNames[i]);
        buttons[i]->set_Color(Color::get_White());
        buttons[i]->set_NormalCaption(normalCaptions[i]);
        buttons[i]->set_OnActivated(new NamedAction(actions[i]));
        auto border = MakeObject<Border>(buttons[i]);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        buttons[i]->set_Border(border);
        buttons[i]->get_Characteristics()->set_Border(clrBorder);
        buttons[i]->get_Characteristics()->set_Background(clrBackGround);
    }

// Kita harus menduplikasi array tombol ini di setiap halaman dalam dokumen.

    for (int pageIndex = 1; pageIndex <= 4; pageIndex++)
        for (int i = 0; i < 4; i++)
            document->get_Form()->Add(buttons[i], String::Format(u"btn{0}_{1}", pageIndex,(i + 1)), pageIndex);

    document->get_Form()->idx_get(u"btn1_1")->set_ReadOnly(true);
    document->get_Form()->idx_get(u"btn1_2")->set_ReadOnly(true);

    document->get_Form()->idx_get(String::Format(u"btn{0}_3", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->get_Form()->idx_get(String::Format(u"btn{0}_4", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->Save(_dataDir + u"sample_widgetannot_2.pdf");
}
```

### Hapus Anotasi Widget

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // hapus anotasi
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```