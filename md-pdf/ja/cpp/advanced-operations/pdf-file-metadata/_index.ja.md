---
title: PDFファイルのメタデータ
type: docs
weight: 20
url: /cpp/pdf-file-metadata/
---

## PDFファイル情報の取得/設定

PDFファイルの特定の情報を取得するためには、まずDocumentクラスの**get_Info()**を呼び出す必要があります。DocumentInfoオブジェクトが取得されると、個々のプロパティの値を取得できます。さらに、DocumentInfoクラスのそれぞれのメソッドを使用してプロパティを設定することもできます。以下のコードスニペットは、Aspose.PDF for C++を使用してPDFファイル情報を取得/設定する方法を示しています。

{{% alert color="primary" %}}

**Application**および**Producer**フィールドに対して値を設定することはできませんのでご注意ください。これらのフィールドにはAspose Ltd.およびAspose.PDF for C++ x.x.xが表示されます。

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // ドキュメント情報を取得
    auto docInfo = pdfDocument->get_Info();
    // ドキュメント情報を表示
    Console::WriteLine(u"Author: {0}", docInfo->get_Author());
    Console::WriteLine(u"Creation Date: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Keywords: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Modify Date: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Subject: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Title: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // ドキュメント情報を指定
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"PDF Information");
    docInfo->set_Title (u"Setting PDF Document Information");

    // 出力ドキュメントを保存
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## PDF ファイルから XMP メタデータを取得/設定する

Aspose.PDF for C++ を使用すると、PDF ファイルの XMP メタデータにアクセスしたり、それを設定したりすることができます。PDF ファイルのメタデータを取得/設定するには、以下の手順を行います。

1. Document オブジェクトを作成し、入力 PDF ファイルを開きます。
2. それぞれのメソッドを使用してファイルのメタデータを取得/設定します。

次のコードスニペットは、PDF ファイルからメタデータを取得/設定する方法を示しています。

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // プロパティを取得
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // プロパティを設定
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // ドキュメントを保存
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // xmlns プレフィックスは削除されました
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // ドキュメントを保存
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```