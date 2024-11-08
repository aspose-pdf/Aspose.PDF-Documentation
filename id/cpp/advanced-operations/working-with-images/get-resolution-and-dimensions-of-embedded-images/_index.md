---
title: Dapatkan Resolusi dan Dimensi dari Gambar yang Tertanam menggunakan C++
linktitle: Dapatkan Resolusi dan Dimensi
type: docs
weight: 40
url: /id/cpp/get-resolution-and-dimensions-of-embedded-images/
description: Bagian ini menunjukkan detail dalam mendapatkan resolusi dan dimensi dari Gambar yang Tertanam
lastmod: "2021-12-18"
---

Topik ini menjelaskan bagaimana menggunakan kelas operator dalam namespace Aspose.PDF yang menyediakan kemampuan untuk mendapatkan informasi resolusi dan dimensi tentang gambar tanpa harus mengekstraknya.

Ada berbagai cara untuk mencapai ini. Artikel ini menjelaskan bagaimana menggunakan `arraylist` dan [kelas penempatan gambar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement).

1. Pertama, muat file PDF sumber (dengan gambar).
1. Kemudian buat objek ArrayList untuk menampung nama gambar apa pun dalam dokumen.
1. Dapatkan gambar menggunakan properti Page.Resources.Images.
1. Buat objek stack untuk menampung keadaan grafis gambar dan gunakan untuk melacak berbagai keadaan gambar.
1. Buat objek ConcatenateMatrix yang mendefinisikan transformasi saat ini. Ini juga mendukung penskalaan, pemutaran, dan pemiringan konten apa pun. Ini menggabungkan matriks baru dengan yang sebelumnya. Harap dicatat bahwa kita tidak dapat mendefinisikan transformasi dari awal tetapi hanya memodifikasi transformasi yang ada.
1. Karena kita dapat memodifikasi matriks dengan ConcatenateMatrix, kita mungkin juga perlu mengembalikan ke keadaan gambar asli. Gunakan [operator GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) dan [operator GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/). Operator ini dipasangkan sehingga harus dipanggil bersama. Misalnya, jika Anda melakukan pekerjaan grafis dengan transformasi kompleks dan akhirnya mengembalikan transformasi ke keadaan awal, pendekatannya akan seperti ini:

Cuplikan kode berikut menunjukkan kepada Anda cara mendapatkan dimensi dan resolusi gambar tanpa mengekstraksi gambar dari dokumen PDF.

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // Memuat file PDF sumber
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // Mendefinisikan resolusi default untuk gambar
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // Mendefinisikan objek daftar array yang akan menyimpan nama gambar
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // Memasukkan objek ke dalam stack
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // Mendapatkan semua operator pada halaman pertama dokumen
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // Gunakan operator GSave/GRestore untuk mengembalikan transformasi ke yang telah disetel sebelumnya
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // Memperkenalkan objek ConcatenateMatrix saat ini mendefinisikan matriks transformasi.
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // Membuat operator Do yang menggambar objek dari sumber daya. Ini menggambar objek Form dan objek Gambar
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // Simpan keadaan sebelumnya dan dorong keadaan saat ini ke atas stack
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // Buang keadaan saat ini dan kembalikan keadaan sebelumnya
            graphicsState->Pop();
        }
        else if (opCtm != nullptr)
        {
            auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
                (float)opCtm->get_Matrix()->get_A(),
                (float)opCtm->get_Matrix()->get_B(),
                (float)opCtm->get_Matrix()->get_C(),
                (float)opCtm->get_Matrix()->get_D(),
                (float)opCtm->get_Matrix()->get_E(),
                (float)opCtm->get_Matrix()->get_F());

            // Mengalikan matriks saat ini dengan matriks keadaan
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            continue;
        }
        else if (opDo != nullptr)
        {
            // Jika ini adalah operator gambar
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // Membuat objek XImage untuk menampung gambar halaman pertama pdf
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // Mendapatkan dimensi gambar
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // Mendapatkan informasi Tinggi dan Lebar dari gambar
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // Menghitung resolusi berdasarkan informasi di atas
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // Menampilkan informasi Dimensi dan Resolusi dari masing-masing gambar
                Console::Write(_dataDir);
                Console::Write(u" image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```