---
title: 複雑なPDFの作成
linktitle: 複雑なPDFの作成
type: docs
weight: 60
url: ja/cpp/complex-pdf-example/
description: Aspose.PDF for C++を使用すると、画像、テキストフラグメント、テーブルを1つのドキュメントに含む、より複雑なドキュメントを作成できます。
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

[Hello, World](/pdf/cpp/hello-world-example/) の例では、C++ と Aspose.PDF を使用して PDF ドキュメントを作成する簡単な手順を示しました。この記事では、C++ と Aspose.PDF for C++ を使用して、より複雑なドキュメントを作成する方法を見ていきます。例として、乗客フェリーサービスを運営する架空の会社のドキュメントを取り上げます。
私たちのドキュメントには、画像、2つのテキストフラグメント（ヘッダーと段落）、およびテーブルが含まれます。このようなドキュメントを構築するには、DOMベースのアプローチを使用します。[DOM APIの基本](/pdf/cpp/basics-of-dom-api/) セクションで詳細を読むことができます。

ドキュメントをゼロから作成する場合、特定の手順を踏む必要があります。

1. Create a [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) for path name and file name.  
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトをインスタンス化します。このステップでは、メタデータを含むがページを含まない空のPDFドキュメントを作成します。  
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)を追加します。これで、ドキュメントには1ページが含まれるようになります。  
1. ページに[Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image)を追加します。  
1. ヘッダー用に[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)を作成します。ヘッダーにはフォントサイズ24ptのArialフォントを使用し、中央揃えにします。  
1. ヘッダーをページの[Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170)に追加します。  
1. Create a [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) for 説明. For the 説明 we will use Arial font with font size 24pt and center alignment.
1. Add (説明) to the page Paragraphs.
1. Create a table, add table properties.
1. Add (テーブル) to the page [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170).
1. Save a document "Complex.pdf".

```cpp
void ExampleComplex()
{
    String outputFileName;

    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String filename("Complex.pdf");

    // Initialize document object
    auto document = MakeObject<Document>();
    // Add page
    auto page = document->get_Pages()->Add();

    // Add image
    String imageFileName = _dataDir + String(u"logo.png");

    // Add image to Images collection of Page Resources
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // Add Header
    auto header = MakeObject<TextFragment>(u"New ferry routes in Fall 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Add description
    String descriptionText(u"Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // Add table
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"Departs City");
    headerRow->get_Cells()->Add(u"Departs Island");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // Save updated PDF
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```