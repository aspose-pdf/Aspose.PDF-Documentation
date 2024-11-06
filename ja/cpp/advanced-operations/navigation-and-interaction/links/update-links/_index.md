---
title: PDF のリンクを更新する
linktitle: リンクを更新する
type: docs
weight: 20
url: ja/cpp/update-links/
description: Aspose.PDF for C++ を使用してプログラムで PDF 内のリンクを更新します。このガイドは、PDF ファイル内のリンクを更新する方法について説明しています。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ファイル内のリンクを更新する

PDF ファイルにハイパーリンクを追加する際に説明したように、[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) クラスを使用すると、PDF ファイルにリンクを追加することが可能です。また、PDF ファイル内の既存のリンクを取得するための同様のクラスもあります。既存のリンクを更新する必要がある場合は、これを使用します。既存のリンクを更新するには：

1. PDF ファイルを読み込む。
1. PDF ファイルの特定のページに移動する。
1. [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action) オブジェクトの Destination プロパティを使用してリンク先を指定する。
1. 指定されたページは、[XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination) コンストラクターを使用して指定されます。

### 同じドキュメント内のページにリンクターゲットを設定する

次のコードスニペットは、PDFファイル内のリンクを更新し、そのターゲットをドキュメントの2ページ目に設定する方法を示しています。

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // リンクの変更: リンク先を変更
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // リンクオブジェクトの宛先を指定
    // 座標 (left, top) をウィンドウの左上隅に位置させ、ページの内容を拡大率 zoom で拡大表示する明示的な宛先を表す。
    // 第1パラメータは宛先ページ番号です。
    // 第2パラメータは左座標です。
    // 第3パラメータは上座標です。
    // 第4引数は、該当ページを表示する際のズーム倍率です。2 を使用すると、ページは 200% のズームで表示されます。
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // 更新されたリンクでドキュメントを保存
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### Webアドレスへのリンク先を設定する

ハイパーリンクを更新してWebアドレスを指すようにするには、[GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action)オブジェクトをインスタンス化し、それをLinkAnnotationのActionプロパティに渡します。次のコードスニペットは、PDFファイル内のリンクを更新し、そのターゲットをWebアドレスに設定する方法を示しています。

```cpp
void SetLinkDestinationToWebAddress() 
{
    // PDFファイルをロードする
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成する
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDFファイルのページコレクションにページを追加する
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // リンクの変更：リンクアクションを変更し、ターゲットをWebアドレスとして設定する
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // 更新されたリンクでドキュメントを保存する
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### 別のPDFファイルへのリンクターゲットを設定する

次のコードスニペットは、PDFファイル内のリンクを更新して、そのターゲットを別のPDFファイルに設定する方法を示しています。

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // PDFファイルを読み込む
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // リンクを修正: リンクアクションを変更し、ターゲットをウェブアドレスとして設定
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // 次の行は宛先を更新し、ファイルを更新しない
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // 次の行はファイルを更新
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // 更新されたリンクでドキュメントを保存
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### リンク注釈のテキストカラーを更新する

リンク注釈にはテキストが含まれていません。代わりに、テキストは注釈の下のページの内容に配置されます。したがって、テキストの色を変更するには、注釈の色を変更しようとするのではなく、ページテキストの色を置き換えます。次のコードスニペットは、PDFファイル内のリンク注釈の色を更新する方法を示しています。

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // PDFファイルをロードする
    String _dataDir("C:\\Samples\\");

    // Documentインスタンスを作成する
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // PDFファイルのページコレクションにページを追加する
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // 注釈の下のテキストを検索する
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // テキストの色を変更する。
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // 更新されたリンクでドキュメントを保存する
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```