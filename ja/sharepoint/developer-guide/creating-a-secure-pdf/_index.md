---
title: SharePoint でセキュアな PDF を作成する
linktitle: セキュアな PDF の作成
type: docs
weight: 60
url: /ja/sharepoint/creating-a-secure-pdf/
lastmod: "2026-08-10"
description: PDF SharePoint API を使用すると、安全な暗号化 PDF を作成し、SharePoint でそのパスワードを指定できます。
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint はセキュアな PDF の作成をサポートします。Aspose.PDF for SharePoint をインストールすると、Site Setting に **PDF Secure Settings** オプションが追加されます。ここで、ユーザーパスワード、所有者パスワード、およびアルゴリズム一覧から任意の値を設定して出力 PDF を暗号化できます。アルゴリズム一覧は、暗号化アルゴリズムと鍵サイズのさまざまな組み合わせを提供します。希望する値を指定してください。

この記事では、Aspose.PDF for SharePoint を使用して暗号化 PDF を生成する方法を示します。

{{% /alert %}}

## セキュアな PDF の作成

機能をデモンストレーションするために、まず所有者パスワードとユーザーパスワード、および暗号化アルゴリズムの **PDF Secure Setting** オプションを設定します。次に、例ではドキュメント ライブラリから 2 つのドキュメントを結合します。

### PDF Secure Setting オプションの設定

サイト設定から **PDF Secure Settings** オプションを開き、アルゴリズム、所有者パスワード、ユーザーパスワードを設定します。

PDF ファイルを暗号化する際に、異なるユーザーパスワードと所有者パスワードを指定します。

- ユーザーパスワードが設定されている場合、PDF を開くために提供しなければならないものです。Acrobat Reader はユーザーにユーザーパスワードの入力を求めます。パスワードが間違っていると、ドキュメントは開きません。
- 所有者パスワードが設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。Acrobat Reader は権限設定に基づいてこれらの機能を無効にします。権限を設定/変更したい場合、Acrobat はこのパスワードを必要とします。

![PDF セキュリティ設定](creating-a-secure-pdf_1.png)

### ドキュメントの結合

**Convert to PDF** オプションを使用して 2 つのドキュメントを結合します。この機能は、複数の非 PDF ファイル（HTML、テキスト、または画像）を PDF ファイルに結合します。

1. ドキュメント ライブラリを開き、一覧から目的のドキュメントを選択します。

![ドキュメントの結合](creating-a-secure-pdf_2.png)

1. Library Tools の **Merge to PDF** オプションを使用して出力ファイルを保存します。出力ファイルをディスクに保存するように求められます。

![PDF に結合](creating-a-secure-pdf_3.png)

### 出力

出力ファイルは暗号化されています。

![出力](creating-a-secure-pdf_4.png)

