---
title: SharePoint でセキュア PDF を作成する
linktitle: セキュア PDF の作成
type: docs
weight: 60
url: /ja/sharepoint/creating-a-secure-pdf/
lastmod: "2026-06-18"
description: PDF SharePoint API を使用すると、安全で暗号化された PDF を作成し、SharePoint でパスワードを指定できます。
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint はセキュア PDF の作成に対応しています。Aspose.PDF for SharePoint をインストールすると、サイト設定に **PDF Secure Settings** オプションが追加されます。ここで、ユーザーパスワード、所有者パスワード、およびアルゴリズム リストから任意の値を設定して出力 PDF を暗号化できます。アルゴリズム リストは、暗号化アルゴリズムと鍵サイズのさまざまな組み合わせを提供します。希望の値を指定してください。

この記事では、Aspose.PDF for SharePoint を使用して暗号化された PDF を生成する方法を示します。

{{% /alert %}}

## **セキュア PDF の作成**

機能を実証するために、まず所有者パスワードとユーザーパスワード、および暗号化アルゴリズムの **PDF Secure Setting** オプションを設定します。次に、例としてドキュメント ライブラリから 2 つの文書をマージします。

### **PDF Secure Setting オプションの設定**

サイト設定から **PDF Secure Settings** オプションを開き、アルゴリズム、所有者パスワード、ユーザーパスワードを設定します。

PDF ファイルを暗号化する際に、異なるユーザーパスワードと所有者パスワードを指定します。

- ユーザーパスワードが設定されている場合、PDF を開くために入力する必要があるものです。Acrobat Reader はユーザーにユーザーパスワードの入力を求めます。パスワードが間違っていると、文書は開きません。
- 所有者パスワードが設定されている場合、印刷、編集、抽出、コメント付けなどの権限を制御します。Acrobat Reader は権限設定に基づきこれらの機能を無効にします。権限の設定/変更を行いたい場合、Acrobat はこのパスワードが必要です。

![todo:image_alt_text](creating-a-secure-pdf_1.png)

### **ドキュメントの結合**

**Convert to PDF**オプションを使用して2つのドキュメントを結合します。この機能は、複数の非PDFファイル（HTML、テキストまたは画像）をPDFファイルに結合します。

1. ドキュメント ライブラリを開き、リストから目的のドキュメントを選択します。

![todo:image_alt_text](creating-a-secure-pdf_2.png)


1. ライブラリ ツールの**Merge to PDF**オプションを使用して出力ファイルを保存します。出力ファイルをディスクに保存するように求められます。

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **出力**

出力ファイルは暗号化されています。

![todo:image_alt_text](creating-a-secure-pdf_4.png)

