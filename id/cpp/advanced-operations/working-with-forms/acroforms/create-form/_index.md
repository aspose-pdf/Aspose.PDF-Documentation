---
title: Buat AcroForms menggunakan C++
linktitle: Buat AcroForms
type: docs
weight: 10
url: id/cpp/create-form/
description: Bagian ini menjelaskan cara membuat AcroForms dari awal dalam dokumen PDF Anda dengan Aspose.PDF untuk C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Bidang Formulir dalam Dokumen PDF

Kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) menyediakan koleksi bernama Form yang membantu mengelola bidang formulir dalam dokumen PDF.

Untuk menambahkan bidang formulir:

1. Buat bidang formulir yang ingin Anda tambahkan.
2. Panggil metode tambah koleksi [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms).

Contoh ini menunjukkan cara menambahkan [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field). Anda dapat menambahkan bidang formulir apa pun menggunakan pendekatan yang sama:

1. Pertama, buat objek bidang dan atur propertinya.
2. Kemudian, tambahkan bidang ke koleksi Form.

### Menambahkan TextBoxField

Bidang teks adalah elemen formulir yang memungkinkan penerima memasukkan teks ke dalam formulir Anda. Ini akan digunakan kapan saja Anda ingin memberikan kebebasan kepada pengguna untuk mengetik apa yang mereka inginkan.

Cuplikan kode berikut menunjukkan cara menambahkan TextBoxField ke dokumen PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // Buat sebuah field
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // Tambahkan field ke dokumen
    document->get_Form()->Add(textBoxField, 1);

    // Simpan PDF yang telah dimodifikasi
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## Menambahkan RadioButtonField

RadioButton paling sering digunakan untuk pertanyaan pilihan ganda, dalam skenario di mana hanya satu jawaban yang dapat dipilih.

Cuplikan kode berikut menunjukkan cara menambahkan [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) dalam dokumen PDF.

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke file PDF
    document->get_Pages()->Add();

    // Instansiasi objek RadioButtonField dengan nomor halaman sebagai argumen

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // Tambahkan opsi radio button pertama dan juga tentukan asalnya menggunakan objek Rectangle
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // Tambahkan opsi radio button kedua
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // Tambahkan radio button ke objek form dari objek Document
    document->get_Form()->Add(radio,1);

    // Simpan file PDF
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

Potongan kode berikut menunjukkan langkah-langkah untuk menambahkan [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) dengan tiga opsi dan menempatkannya di dalam sel Tabel.

```cpp
void AddRadioButtonFieldInsideTableCells()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto table = MakeObject<Aspose::Pdf::Table>();

    table->set_ColumnWidths(u"120 120 120");

    page->get_Paragraphs()->Add(table);

    auto r1 = table->get_Rows()->Add();
    auto c1 = r1->get_Cells()->Add();
    auto c2 = r1->get_Cells()->Add();
    auto c3 = r1->get_Cells()->Add();

    auto rf = MakeObject<RadioButtonField>(page);
    rf->set_PartialName(u"radio");
    document->get_Form()->Add(rf, 1);

    auto opt1 = MakeObject<RadioButtonOptionField>();
    auto opt2 = MakeObject<RadioButtonOptionField>();
    auto opt3 = MakeObject<RadioButtonOptionField>();

    opt1->set_OptionName(u"Item1");
    opt2->set_OptionName(u"Item2");
    opt3->set_OptionName(u"Item3");

    opt1->set_Width (15);
    opt1->set_Height(15);
    opt2->set_Width (15);
    opt2->set_Height(15);
    opt3->set_Width (15);
    opt3->set_Height(15);

    rf->Add(opt1);
    rf->Add(opt2);
    rf->Add(opt3);

    opt1->set_Border(MakeObject<Border>(opt1));
    opt1->get_Border()->set_Width(1);
    opt1->get_Border()->set_Style(BorderStyle::Solid);
    opt1->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt1->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt1->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item1"));
    opt2->set_Border(MakeObject<Border>(opt2));
    opt2->get_Border()->set_Width(1);
    opt2->get_Border()->set_Style(BorderStyle::Solid);
    opt2->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt2->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt2->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item2"));
    opt3->set_Border(MakeObject<Border>(opt3));
    opt3->get_Border()->set_Width(1);
    opt3->get_Border()->set_Style(BorderStyle::Solid);
    opt3->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt3->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt3->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item3"));
    c1->get_Paragraphs()->Add(opt1);
    c2->get_Paragraphs()->Add(opt2);
    c3->get_Paragraphs()->Add(opt3);

    // Simpan file PDF
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## Menambahkan Keterangan ke RadioButtonField

Cuplikan kode berikut menunjukkan cara menambahkan keterangan yang akan dikaitkan dengan [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field):

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // Memuat formulir PDF sumber
    auto form1 =
        MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"RadioButtonField.pdf");

    auto PDF_Template_PDF_HTML = MakeObject<Document>(_dataDir + u"RadioButtonField.pdf");

    for(auto item : form1->get_FieldNames())
    {
        System::Console::WriteLine(item);
        auto radioOptions = form1->GetButtonOptionValues(item);
        if (item.Contains(u"radio1"))
        {
            auto field0 = System::DynamicCast<RadioButtonField>(PDF_Template_PDF_HTML->get_Form()->idx_get(item));
            auto fieldoption = MakeObject<RadioButtonOptionField>();
            fieldoption->set_OptionName (u"Yes");
            fieldoption->set_PartialName (u"Yesname");

            auto updatedFragment = MakeObject<Aspose::Pdf::Text::TextFragment>(u"test123");
            updatedFragment->get_TextState()->set_Font (Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
            updatedFragment->get_TextState()->set_FontSize(10);
            updatedFragment->get_TextState()->set_LineSpacing(6.32f);

            // Membuat objek TextParagraph
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // Mengatur posisi paragraf
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // Menentukan mode pembungkusan kata
            par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // Menambahkan TextFragment baru ke paragraf
            par->AppendLine(updatedFragment);

            // Menambahkan TextParagraph menggunakan TextBuilder
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## Menambahkan field ComboBox

Combo Box adalah field formulir yang akan menambahkan menu dropdown ke dokumen Anda.

Cuplikan kode berikut menunjukkan cara menambahkan field [ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field) dalam dokumen PDF.

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Buat objek Dokumen
    auto document = MakeObject<Document>();
    // Tambahkan halaman ke objek dokumen
    document->get_Pages()->Add();
    // Memperkenalkan objek ComboBox Field
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // Tambahkan opsi ke ComboBox
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // Tambahkan objek combo box ke koleksi field formulir dari objek dokumen
    document->get_Form()->Add(combo);

    // Simpan dokumen PDF
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```

## Menambahkan Tooltip ke Formulir

The Document class menyediakan koleksi bernama Form yang mengelola bidang formulir dalam dokumen PDF. Untuk menambahkan tooltip ke bidang formulir, gunakan AlternateName dari kelas Field. Adobe Acrobat menggunakan 'nama alternatif' sebagai tooltip bidang.

Cuplikan kode berikut menunjukkan cara menambahkan tooltip ke bidang formulir dengan C++.

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // Muat formulir PDF sumber
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // Atur tooltip untuk textfield
    //(doc.Form["textbox1"] as Field).AlternateName = "Text box tool tip";

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```