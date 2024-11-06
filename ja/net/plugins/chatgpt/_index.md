---
title: ChatGPT
type: docs
weight: 30
url: ja/net/plugins/chatGPT/
description: AIパワードのChatGPTレスポンスを生成してPDFに保存する方法
lastmod: "2024-02-24"
---

## ChatGptプラグインを使用したAIパワードチャットレスポンスの生成

PDFドキュメントにAI生成のチャットレスポンスを追加したいと思ったことはありませんか？ これ以上探す必要はありません！ このガイドでは、C#アプリケーションに強力な[ChatGptプラグイン](https://products.aspose.org/pdf/net/chat-gpt/)を統合するプロセスを説明します。 数ステップで、魅力的なチャットレスポンスを簡単に生成できます。

## 前提条件

次のものが必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.1以降
* サンプルPDFファイル

## ステップ

### 1. オブジェクトの作成

まず、チャット生成タスクのオブジェクトを作成しましょう。 提供されたC#コードスニペットは、PdfChatGptプラグインのオプションを設定する方法を示しています。

```csharp
// ChatGPTプラグインのオプションを作成します。
var options = new PdfChatGptRequestOptions();
```
### 2. データソースの追加

次に、データソースを追加する必要があります。この場合、AI生成チャットレスポンスでテキストを強化したい入力PDFファイルです。

```csharp
// 入力PDFファイルをオプションに追加します。
options.AddInput(new FileDataSource("c:\\Samples\\sample.pdf"));

// 出力PDFファイルをオプションに追加します。
options.AddOutput(new FileDataSource("c:\\Samples\\chat_results.pdf"));
```

上記のコードスニペットでは、入力PDFファイルのパスと、チャットレスポンスで強化されたPDFが保存される出力パスを指定しています。

### 3. プロセスメソッドの実行

さあ、プロセスメソッドを実行して全てを動かしましょう。ここで魔法が起こります – AIパワードのChatGPTモデルが提供されたクエリとテキストに基づいてチャットレスポンスを生成します。

```csharp
// 認証のためAPIキーを設定します。
options.ApiKey = "sk-******";

// ChatGPTモデルの最大トークン数を設定します。
options.MaxTokens = 1000;

// ChatGPTモデルのクエリを設定します。
options.Query = "What are the best keywords for this text?";

// PdfChatGptプラグインのインスタンスを作成します。
var plugin = new PdfChatGpt();

// ChatGPTプラグインを使用してPDFドキュメントを処理します。
var result = await plugin.ProcessAsync(options);
```
これらのコード行を使用して、認証を設定し、ChatGPTモデルのパラメータを設定し、チャット生成プロセスを開始しています。
