---
title: SharePoint で安全な PDF を作成する
linktitle: 安全な PDF の作成
type: docs
weight: 60
url: /ja/sharepoint/creating-a-secure-pdf/
lastmod: "2020-12-16"
description: Using the PDF SharePoint API, you may produce safe, encrypted PDFs and specify their passwords in SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint は、安全な PDF の作成をサポートしています。 Aspose.PDF for SharePoint をインストールすると、サイト設定に **PDF セキュリティ設定** オプションが追加されます。ここでは、出力 PDF を暗号化するために、ユーザー パスワード、所有者パスワード、およびアルゴリズム リストの任意の値を設定できます。アルゴリズム リストには、暗号化アルゴリズムとキー サイズのさまざまな組み合わせが示されています。選択した値を渡します。

この記事では、Aspose.PDF for SharePoint を使用して暗号化された PDF を生成する方法を説明します。

{{% /alert %}}

## 安全な PDF の作成

この機能をデモンストレーションするために、まず所有者とユーザーのパスワードと暗号化アルゴリズムの **PDF セキュリティ設定** オプションを構成します。次に、この例では、ドキュメント ライブラリから 2 つのドキュメントを結合します。

### PDF セキュア設定オプションの設定

Open **PDF Secure Settings** option from Site Settings and set algorithm, owner password and user password.

PDF ファイルを暗号化する際に、異なるユーザーと所有者のパスワードを指定します。

- ユーザー パスワードが設定されている場合、PDF を開くために入力する必要があります。 Acrobat Reader は、ユーザーにユーザーパスワードの入力を求めるプロンプトを表示します。間違っている場合、ドキュメントは開きません。
- The owner password, if set, controls permissions such as printing, editing, extracting, commenting, etc. Acrobat Reader disallows these features based on the permission settings. Acrobat requires this password if you want to set/change permissions.

![PDF Secure Settings](creating-a-secure-pdf_1.png)

### ドキュメントを結合する

**PDF に変換** オプションを使用して 2 つのドキュメントを結合します。この機能は、複数の非 PDF ファイル (HTML、テキスト、または画像) を 1 つの PDF ファイルに結合します。

1. ドキュメント ライブラリを開き、リストから目的のドキュメントを選択します。

![Merge Documents](creating-a-secure-pdf_2.png)

1. ライブラリ ツールの **PDF に結合** オプションを使用して、出力ファイルを保存します。出力ファイルをディスクに保存するように求められます。

![Merge to PDF](creating-a-secure-pdf_3.png)

### Output

出力ファイルは暗号化されます。

![Output](creating-a-secure-pdf_4.png)


