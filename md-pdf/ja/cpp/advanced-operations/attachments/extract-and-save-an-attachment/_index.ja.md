---
title: 添付ファイルを抽出して保存 
linktitle: 添付ファイルを抽出して保存
type: docs
weight: 20
url: /cpp/extract-and-save-an-attachment/
description: Aspose.PDF for C++を使用すると、PDFドキュメントからすべての添付ファイルを取得できます。また、ドキュメントから個別の添付ファイルを取得することもできます。
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## すべての添付ファイルを取得する

Aspose.PDFを使用すると、PDFドキュメントからすべての添付ファイルを取得することが可能です。これは、PDFから別々にドキュメントを保存したい場合、またはPDFの添付ファイルを削除する必要がある場合に便利です。

PDFファイルからすべての添付ファイルを取得するには:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトの [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) コレクションをループします。[EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) コレクションにはすべての添付ファイルが含まれています。このコレクションの各要素は [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) オブジェクトを表します。[EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) コレクションを介した foreach ループの各イテレーションは [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) オブジェクトを返します。
1. オブジェクトが利用可能になったら、すべての添付ファイルのプロパティまたはファイル自体を取得します。

以下のコードスニペットは、PDF ドキュメントからすべての添付ファイルを取得する方法を示しています。

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // ドキュメントを開く
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // 埋め込みファイルコレクションを取得
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // 埋め込みファイルの数を取得
 Console::WriteLine(u"Total files : {0}", embeddedFiles->get_Count());

 int count = 1;

 // コレクションをループしてすべての添付ファイルを取得
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

  // パラメータオブジェクトがパラメータを含んでいるか確認
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"CheckSum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Creation Date: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Modification Date: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Size: {0}", fileSpecification->get_Params()->get_Size());
  }

  // 添付ファイルを取得してファイルまたはストリームに書き込む
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## 個別の添付ファイルを取得する

個別の添付ファイルを取得するには、Document インスタンスの `EmbeddedFiles` オブジェクトで添付ファイルのインデックスを指定します。次のコードスニペットを使用してみてください。

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // 特定の埋め込みファイルを取得
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // ファイルプロパティを取得
    Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

    // パラメータオブジェクトがパラメータを含むかどうかを確認
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"CheckSum: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Creation Date: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Modification Date: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Size: {0}",
        fileSpecification->get_Params()->get_Size());
    }


    // 添付ファイルを取得してファイルまたはストリームに書き込む
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```