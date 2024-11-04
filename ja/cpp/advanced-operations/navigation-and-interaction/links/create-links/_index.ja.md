---
title: C++でPDFファイルにリンクを作成する
linktitle: リンクを作成
type: docs
weight: 10
url: /cpp/create-links/
description: このセクションでは、C++でPDFドキュメントにリンクを作成する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## リンクを作成する

ドキュメントにアプリケーションへのリンクを追加することで、ドキュメントからアプリケーションにリンクすることが可能になります。これは、たとえばチュートリアルの特定のポイントで読者に特定のアクションを取らせたい場合や、機能豊富なドキュメントを作成したい場合に役立ちます。アプリケーションリンクを作成するには:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトを作成します。
1. リンクを追加したい [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) を取得します。
1. Pageと[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle)オブジェクトを使用して[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)オブジェクトを作成します。
1. リンク属性を[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)オブジェクトを使用して設定します。  
1. また、[LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/)オブジェクトのActionプロパティを設定します。  
1. [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/)オブジェクトを作成するとき、起動したいアプリケーションを指定します。  
1. ページオブジェクトの[Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations)プロパティにリンクを追加します。  
1. 最後に、DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存します。  

次のコードスニペットは、PDFファイルにアプリケーションへのリンクを作成する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```
### PDFファイルにPDFドキュメントリンクを作成する

Aspose.PDF for C++を使用すると、外部のPDFファイルへのリンクを追加して、複数のドキュメントをリンクさせることができます。PDFドキュメントリンクを作成するには:

1. 最初に、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトを作成します。
1. 次に、リンクを追加したい特定の[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)を取得します。
1. [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)オブジェクトと[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle)オブジェクトを使用して、[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)オブジェクトを作成します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)オブジェクトを使用してリンク属性を設定します。
1. Actionプロパティを[GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/)オブジェクトに設定します。
1.  GoToRemoteActionオブジェクトを作成する際に、起動するPDFファイルと、それが開くべきページ番号を指定します。
1. リンクをPageオブジェクトのAnnotationsコレクションに追加します。
1. DocumentオブジェクトのSaveメソッドを使用して更新されたPDFを保存します。

以下のコードスニペットは、PDFファイル内にPDFドキュメントリンクを作成する方法を示しています。

 ```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // ページをPDFファイルのページコレクションに追加
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```