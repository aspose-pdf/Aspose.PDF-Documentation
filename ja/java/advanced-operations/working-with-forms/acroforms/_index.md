---
title: PDFでのAcroFormsの操作
linktitle: AcroForms
type: docs
weight: 10
url: /ja/java/acroforms/
description: Aspose.PDF for Javaを使用すると、ゼロからフォームを作成し、PDFドキュメントのフォームフィールドに入力し、フォームからデータを抽出し、既存のフォームにフィールドを追加または削除できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## AcroFormsの基本

**AcroForms**は、元々のPDFフォーム技術です。AcroFormsはページ指向のフォームです。それらは1998年に初めて導入されました。それらはForms Data FormatまたはFDFおよびXML Forms Data FormatまたはxFDFでの入力を受け付けます。サードパーティのベンダーはAcroFormsをサポートしています。AdobeがAcroFormsを導入したとき、彼らはそれらを「Adobe Acrobat Pro/Standardで作成されたPDFフォームであり、特定の種類の静的または動的XFAフォームではない」と称していました。Acroformsは移植可能であり、すべてのプラットフォームで動作します。

AcroFormsを使用して、PDFフォームドキュメントに追加のページを追加することができます。
 テンプレートの概念のおかげで、AcroFormsを使用して複数のデータベースレコードでフォームを埋めることができます。

PDF 1.7は、データとPDFフォームを統合するための2つの異なる方法をサポートしています。

*AcroForms（Acrobatフォームとしても知られています）*は、PDF 1.2フォーマット仕様で導入され、含まれています。

*Adobe XML Forms Architecture (XFA) forms*は、PDF 1.5フォーマット仕様でオプション機能として導入されました（XFA仕様はPDF仕様には含まれておらず、参照のみです）。

**Acroforms**と**XFA**フォームを理解するためには、まず基本を理解する必要があります。まず最初に、どちらも使用できるPDFフォームです。Acroformsは1998年に作成された古いもので、今でもクラシックなPDFフォームと呼ばれています。XFAフォームは、PDFとして保存できるウェブページで、2003年に登場しました。PDFがXFAフォームを受け入れ始めるまでには時間がかかりました。

AcroFormsにはXFAにはない機能があり、逆にXFAにはAcroFormsにはない機能があります。例えば：

- AcroFormsは「テンプレート」の概念をサポートしており、複数のデータベースレコードでフォームを埋めるためにPDFフォームドキュメントに追加ページを追加することができます。- XFAは、データに合わせてフィールドをリサイズできるようにするドキュメントリフローの概念をサポートしています。

したがって、PDFは、電子的に配布でき、ドキュメント内に情報を記入し、印刷や従来の郵便で送ることなく送信者に返送できるため、フォームに最適なファイル形式です。

フォーム操作の可能性を詳細に研究するには、以下のセクションの記事を参照してください：

-[AcroFormを作成する](/pdf/ja/java/create-form/) - Javaを使用して、RadioButtonField、TextBoxField、Caption Fieldを追加し、ゼロからフォームを作成します。

-[AcroFormを記入する](/pdf/ja/java/fill-form/) - フォームフィールドに記入するには、DocumentオブジェクトのFormコレクションからフィールドを取得します。

-[AcroFormデータを抽出する](/pdf/ja/java/extract-form/) - すべてのフィールド、および個別のフィールドから値を取得するなど。

-[AcroFormを変更する](/pdf/ja/java/modifing-form/) - FieldLimitの取得/設定、既存のフォームからフィールドを削除、Javaで14のCore PDFフォント以外のフォームフィールドフォントを設定します。